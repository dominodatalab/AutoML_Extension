"""Tracking and garbage collection for staged Model API source bundles."""

import asyncio
import logging
import os
import shutil
from datetime import datetime
from functools import lru_cache
from pathlib import Path
from typing import Optional

from app.core.domino_model_api import get_domino_model_api
from app.db import crud
from app.dependencies import get_db_session

logger = logging.getLogger(__name__)


def _parse_int_env(name: str, default: int, minimum: int = 0) -> int:
    """Parse integer env vars with safe fallback and lower bound."""
    raw = os.environ.get(name)
    if raw is None:
        return max(default, minimum)
    try:
        value = int(raw)
    except ValueError:
        logger.warning("Invalid %s='%s', using default=%s", name, raw, default)
        return max(default, minimum)
    return max(value, minimum)


def _dir_size_bytes(path: Path) -> int:
    """Best-effort directory size computation."""
    total = 0
    if not path.exists():
        return total
    for root, _, files in os.walk(path):
        for filename in files:
            file_path = Path(root) / filename
            try:
                total += file_path.stat().st_size
            except OSError:
                continue
    return total


class ModelApiSourceBundleGC:
    """Tracks staged bundles and garbage-collects stale source directories."""

    def __init__(self):
        self.interval_seconds = _parse_int_env(
            "MODEL_API_BUNDLE_GC_INTERVAL_SECONDS",
            default=6 * 60 * 60,
            minimum=300,
        )
        self.miss_threshold = _parse_int_env(
            "MODEL_API_BUNDLE_GC_MISS_THRESHOLD",
            default=2,
            minimum=1,
        )
        self.fresh_grace_seconds = _parse_int_env(
            "MODEL_API_BUNDLE_GC_FRESH_GRACE_SECONDS",
            default=60 * 60,
            minimum=0,
        )
        self.orphan_ttl_seconds = _parse_int_env(
            "MODEL_API_BUNDLE_ORPHAN_TTL_SECONDS",
            default=7 * 24 * 60 * 60,
            minimum=60 * 60,
        )
        self._task: Optional[asyncio.Task] = None
        self._stop_event = asyncio.Event()
        self._run_lock = asyncio.Lock()

    @staticmethod
    def bundle_root() -> Path:
        """Return absolute root directory for staged model-api source bundles."""
        service_root = Path(__file__).resolve().parents[2]
        return (service_root / "automl_model_api_sources").resolve()

    @staticmethod
    def legacy_bundle_root() -> Path:
        """Return legacy hidden root used by earlier bundle staging logic."""
        service_root = Path(__file__).resolve().parents[2]
        return (service_root / ".automl_model_api_sources").resolve()

    def _allowed_bundle_roots(self) -> tuple[Path, ...]:
        """Return allowed bundle roots for path normalization and cleanup."""
        current = self.bundle_root()
        legacy = self.legacy_bundle_root()
        if legacy == current:
            return (current,)
        return (current, legacy)

    def bundle_dir_for_job(self, job_id: str) -> Path:
        """Return absolute bundle directory path for a training job id."""
        return (self.bundle_root() / f"job_{job_id}").resolve()

    def _normalize_bundle_dir(self, bundle_dir: str) -> Optional[Path]:
        """Return resolved path only when it is under bundle_root."""
        try:
            resolved = Path(bundle_dir).resolve()
        except Exception:
            return None

        for root in self._allowed_bundle_roots():
            if resolved == root or root in resolved.parents:
                return resolved
        return None

    async def startup(self) -> None:
        """Start periodic GC loop."""
        if self._task is not None and not self._task.done():
            return

        self.bundle_root().mkdir(parents=True, exist_ok=True)
        self._stop_event.clear()
        self._task = asyncio.create_task(self._run_loop(), name="model-api-source-bundle-gc")
        logger.info(
            "Model API bundle GC started (interval=%ss, miss_threshold=%s, fresh_grace=%ss, orphan_ttl=%ss)",
            self.interval_seconds,
            self.miss_threshold,
            self.fresh_grace_seconds,
            self.orphan_ttl_seconds,
        )

    async def shutdown(self, timeout_seconds: int = 10) -> None:
        """Stop periodic GC loop."""
        if self._task is None:
            return

        self._stop_event.set()
        try:
            await asyncio.wait_for(self._task, timeout=float(timeout_seconds))
        except asyncio.TimeoutError:
            logger.warning("Timed out stopping Model API bundle GC task; cancelling")
            self._task.cancel()
        finally:
            self._task = None
            logger.info("Model API bundle GC stopped")

    async def track_model_api_source_bundle(
        self,
        model_api_id: str,
        job_id: str,
        bundle_dir: str,
        source_file: str,
    ) -> None:
        """Persist bundle tracking for a successfully published model API."""
        async with get_db_session() as db:
            await crud.upsert_model_api_source_bundle(
                db,
                model_api_id=model_api_id,
                job_id=job_id,
                bundle_dir=bundle_dir,
                source_file=source_file,
            )
        logger.info(
            "Tracked Model API source bundle: model_api_id=%s job_id=%s bundle_dir=%s",
            model_api_id,
            job_id,
            bundle_dir,
        )

    async def on_model_api_deleted(self, model_api_id: str) -> None:
        """Handle cleanup when model API deletion is initiated from this app."""
        async with get_db_session() as db:
            row = await crud.get_model_api_source_bundle(db, model_api_id)
            if row is None:
                return

            bundle_dir = row.bundle_dir
            await crud.delete_model_api_source_bundle(db, model_api_id)
            remaining_refs = await crud.count_model_api_source_bundles_by_bundle_dir(db, bundle_dir)

        if remaining_refs > 0:
            return

        normalized = self._normalize_bundle_dir(bundle_dir)
        if normalized is None:
            logger.warning(
                "Skipping filesystem delete for untrusted bundle path after model_api delete: %s",
                bundle_dir,
            )
            return

        if normalized.exists():
            try:
                shutil.rmtree(normalized)
                logger.info(
                    "Deleted unreferenced source bundle after model_api delete: model_api_id=%s bundle_dir=%s",
                    model_api_id,
                    normalized,
                )
            except Exception as exc:
                logger.warning(
                    "Failed deleting source bundle after model_api delete (model_api_id=%s, dir=%s): %s",
                    model_api_id,
                    normalized,
                    exc,
                )

    async def run_once(self) -> None:
        """Run one reconciliation/GC pass."""
        if self._run_lock.locked():
            logger.info("Skipping Model API bundle GC pass; previous run still in progress")
            return

        async with self._run_lock:
            await self._run_once_locked()

    async def _run_loop(self) -> None:
        """Periodic loop for reconciler GC."""
        await self.run_once()
        while not self._stop_event.is_set():
            try:
                await asyncio.wait_for(self._stop_event.wait(), timeout=float(self.interval_seconds))
            except asyncio.TimeoutError:
                pass

            if self._stop_event.is_set():
                break

            await self.run_once()

    async def _run_once_locked(self) -> None:
        """Reconcile tracking rows against Domino and clean stale/orphan bundles."""
        now = datetime.utcnow()
        root = self.bundle_root()
        root.mkdir(parents=True, exist_ok=True)

        stale_rows_deleted = 0
        bundle_dirs_deleted = 0
        bytes_freed = 0

        async with get_db_session() as db:
            tracked = list(await crud.list_model_api_source_bundles(db))
            domino_model_apis: Optional[set[str]] = None
            if tracked:
                domino_model_apis = await self._fetch_active_model_api_ids()

            if domino_model_apis is not None:
                # Update heartbeat/miss_count state from current Domino truth.
                for row in tracked:
                    row.last_checked_at = now
                    row.updated_at = now
                    if row.model_api_id in domino_model_apis:
                        row.miss_count = 0
                        row.last_seen_at = now
                    else:
                        row.miss_count = int(row.miss_count or 0) + 1
                await db.commit()

                # Group rows by normalized bundle path.
                bundle_rows: dict[Path, list] = {}
                for row in tracked:
                    normalized = self._normalize_bundle_dir(row.bundle_dir)
                    if normalized is None:
                        continue
                    bundle_rows.setdefault(normalized, []).append(row)

                active_bundle_paths = {
                    path
                    for path, rows in bundle_rows.items()
                    if any(r.model_api_id in domino_model_apis for r in rows)
                }

                for bundle_path, rows in bundle_rows.items():
                    stale_candidates = []
                    for row in rows:
                        if row.model_api_id in domino_model_apis:
                            continue
                        age_seconds = (now - (row.created_at or now)).total_seconds()
                        if row.miss_count >= self.miss_threshold and age_seconds >= self.fresh_grace_seconds:
                            stale_candidates.append(row)

                    if not stale_candidates:
                        continue

                    if bundle_path in active_bundle_paths:
                        # Another model_api_id still references this bundle and exists in Domino.
                        for row in stale_candidates:
                            await db.delete(row)
                            stale_rows_deleted += 1
                        continue

                    # Delete bundle only when all tracking rows for this bundle are stale.
                    if len(stale_candidates) < len(rows):
                        for row in stale_candidates:
                            await db.delete(row)
                            stale_rows_deleted += 1
                        continue

                    if bundle_path.exists():
                        bytes_freed += _dir_size_bytes(bundle_path)
                        try:
                            shutil.rmtree(bundle_path)
                            bundle_dirs_deleted += 1
                        except Exception as exc:
                            logger.warning("Failed deleting stale bundle dir %s: %s", bundle_path, exc)
                            continue

                    for row in rows:
                        await db.delete(row)
                        stale_rows_deleted += 1

                await db.commit()

            # Orphan bundle cleanup: local folders not tracked in DB, after TTL.
            fresh_rows = list(await crud.list_model_api_source_bundles(db))
            tracked_bundle_paths = set()
            for row in fresh_rows:
                normalized = self._normalize_bundle_dir(row.bundle_dir)
                if normalized is not None:
                    tracked_bundle_paths.add(normalized)

        for cleanup_root in self._allowed_bundle_roots():
            orphan_dirs_deleted, orphan_bytes_freed = self._delete_orphan_bundle_dirs(
                root=cleanup_root,
                tracked_bundle_paths=tracked_bundle_paths,
                now=now,
            )
            bundle_dirs_deleted += orphan_dirs_deleted
            bytes_freed += orphan_bytes_freed

        logger.info(
            "Model API bundle GC pass complete: stale_rows_deleted=%s bundle_dirs_deleted=%s bytes_freed=%s domino_reconciled=%s",
            stale_rows_deleted,
            bundle_dirs_deleted,
            bytes_freed,
            bool(tracked) and domino_model_apis is not None,
        )

    async def _fetch_active_model_api_ids(self) -> Optional[set[str]]:
        """Fetch active model API IDs from Domino, or None on failure."""
        api = get_domino_model_api()
        result = await api.list_model_apis()
        if not result.get("success"):
            logger.warning(
                "Skipping Domino model_api reconciliation this pass; list_model_apis failed: %s",
                result.get("error"),
            )
            return None

        data = result.get("data", [])
        if isinstance(data, dict):
            data = data.get("items", [])
        if not isinstance(data, list):
            return set()

        ids = set()
        for item in data:
            if isinstance(item, dict) and item.get("id"):
                ids.add(str(item["id"]))
        return ids

    def _delete_orphan_bundle_dirs(
        self,
        *,
        root: Path,
        tracked_bundle_paths: set[Path],
        now: datetime,
    ) -> tuple[int, int]:
        """Delete unmanaged bundle directories older than TTL."""
        deleted_dirs = 0
        freed_bytes = 0

        if not root.exists():
            return deleted_dirs, freed_bytes

        for entry in root.iterdir():
            if not entry.is_dir():
                continue
            resolved = entry.resolve()
            if resolved in tracked_bundle_paths:
                continue

            try:
                age_seconds = (now.timestamp() - entry.stat().st_mtime)
            except OSError:
                continue

            if age_seconds < self.orphan_ttl_seconds:
                continue

            freed_bytes += _dir_size_bytes(resolved)
            try:
                shutil.rmtree(resolved)
                deleted_dirs += 1
            except Exception as exc:
                logger.warning("Failed deleting orphan Model API bundle dir %s: %s", resolved, exc)

        return deleted_dirs, freed_bytes


@lru_cache()
def get_model_api_source_bundle_gc() -> ModelApiSourceBundleGC:
    """Singleton accessor for source-bundle GC service."""
    return ModelApiSourceBundleGC()
