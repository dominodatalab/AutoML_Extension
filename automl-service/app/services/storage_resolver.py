"""Resolve project-scoped storage via Domino Datasets (auto-created).

Ensures a writable ``automl-extension`` dataset exists for a given target
project and returns the local mount path. The dataset is created via the
Domino Dataset RW API (v1 for create, v2 with v1 fallback for listing) if it
does not already exist.

Usage::

    resolver = get_storage_resolver()
    mount_path = await resolver.ensure_project_storage(project_id)
    # mount_path == "/domino/datasets/local/automl-extension" (or similar)
"""

import asyncio
import hashlib
import io
import logging
import os
from dataclasses import dataclass, field
from functools import lru_cache
from typing import Optional

import httpx
from fastapi import HTTPException

from app.core.domino_http import (
    domino_download,
    domino_request,
    resolve_domino_api_host,
    resolve_domino_nucleus_host,
)
from app.services.domino_dataset_api import (
    extract_dataset_list as _extract_project_dataset_list,
    list_project_datasets,
)

logger = logging.getLogger(__name__)

DATASET_NAME = "automl-extension"
DATASET_DESCRIPTION = "AutoML Extension storage - auto-created by the AutoML App"

# Upload settings (matching python-domino SDK defaults)
_UPLOAD_CHUNK_SIZE = 8 * 1024 * 1024  # 8 MB
_UPLOAD_MAX_RETRIES = 10

# Ordered list of mount path templates to probe after dataset creation.
_MOUNT_TEMPLATES = [
    "/domino/datasets/local/{name}",
    "/domino/datasets/{name}",
    "/mnt/data/{name}",
    "/mnt/imported/data/{name}",
]


def _preferred_snapshot_api_base_url() -> Optional[str]:
    """Prefer the direct Domino host for Dataset RW snapshot APIs."""
    return resolve_domino_nucleus_host()


@dataclass
class ProjectPaths:
    """Resolved storage paths for a specific target project."""

    project_id: str
    mount_path: str          # e.g. /domino/datasets/local/automl-extension
    models_path: str         # {mount}/models
    uploads_path: str        # {mount}/uploads
    eda_results_path: str    # {mount}/eda_results
    temp_path: str           # {mount}/temp


@dataclass
class DatasetInfo:
    """Lightweight handle for a resolved dataset."""

    dataset_id: str
    name: str
    project_id: str
    mount_path: Optional[str] = None
    rw_snapshot_id: Optional[str] = None


@dataclass
class ProjectStorageResolver:
    """Manages per-project ``automl-extension`` dataset lifecycle.

    * ``ensure_project_storage(project_id)`` — idempotent: list → create
      → probe mount → return path.
    * Results are cached in-memory so repeated calls for the same project
      hit the API at most once.
    """

    # project_id → DatasetInfo
    _cache: dict[str, DatasetInfo] = field(default_factory=dict)
    # dataset_id → rw_snapshot_id (dedicated cache so lookups don't
    # depend on the dataset having been resolved via ensure_dataset_exists)
    _rw_cache: dict[str, str] = field(default_factory=dict)

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    async def ensure_project_storage(self, project_id: str) -> str:
        """Return a writable mount path for the project's automl-extension dataset.

        Creates the dataset if it does not exist.  Raises ``RuntimeError``
        if creation fails or the mount cannot be located.
        """
        if project_id in self._cache and self._cache[project_id].mount_path:
            return self._cache[project_id].mount_path  # type: ignore[return-value]

        info = await self._resolve_or_create(project_id)
        mount = self._probe_mount(info.name)
        if mount:
            info.mount_path = mount
            self._cache[project_id] = info
            return mount

        raise RuntimeError(
            f"Dataset '{info.name}' (id={info.dataset_id}) exists in project "
            f"{project_id} but no local mount was found.  The App may need to "
            f"be restarted with the dataset attached, or sharing may be required."
        )

    async def resolve_project_paths(self, project_id: str) -> ProjectPaths:
        """Resolve storage paths for a target project.

        Raises ``HTTPException(503)`` if the dataset exists but is not
        mounted (a restart is required to pick up the new mount).
        """
        from app.config import get_settings

        settings = get_settings()
        if settings.standalone_mode:
            return ProjectPaths(
                project_id=project_id,
                mount_path=settings.models_path.rsplit("/", 1)[0],  # parent of models/
                models_path=settings.models_path,
                uploads_path=settings.uploads_path,
                eda_results_path=settings.eda_results_path,
                temp_path=os.path.join(
                    settings.models_path.rsplit("/", 1)[0], "temp"
                ),
            )

        info = await self._resolve_or_create(project_id)
        mount = self._probe_mount(info.name)
        if not mount:
            raise HTTPException(
                status_code=503,
                detail=f"Dataset '{info.name}' exists but is not mounted. "
                       f"Please restart the app.",
            )
        return ProjectPaths(
            project_id=project_id,
            mount_path=mount,
            models_path=os.path.join(mount, "models"),
            uploads_path=os.path.join(mount, "uploads"),
            eda_results_path=os.path.join(mount, "eda_results"),
            temp_path=os.path.join(mount, "temp"),
        )

    async def check_project_storage(
        self, project_id: str
    ) -> tuple[bool, Optional[str]]:
        """Check mount status without raising.

        Returns ``(mounted, mount_path_or_none)``.
        """
        try:
            info = await self._resolve_or_create(project_id)
        except Exception:
            return False, None
        mount = self._probe_mount(info.name)
        return (mount is not None), mount

    async def ensure_dataset_exists(self, project_id: str) -> Optional[DatasetInfo]:
        """Pre-create the automl-extension dataset in a project (best-effort).

        Unlike ``ensure_project_storage``, this does NOT probe for a local
        mount — the mount only appears inside a Domino Job that boots
        *after* the dataset exists.  Call this before launching a Job so
        the dataset mount is available when the Job starts.

        Returns ``DatasetInfo`` on success, ``None`` on failure (never raises).
        """
        try:
            info = await self._resolve_or_create(project_id)
            logger.info(
                "Pre-launch dataset ready: '%s' (id=%s) in project %s",
                info.name,
                info.dataset_id,
                project_id,
            )
            return info
        except Exception:
            logger.warning(
                "Pre-launch dataset creation failed for project %s; "
                "job will proceed without pre-created dataset",
                project_id,
                exc_info=True,
            )
            return None

    async def get_dataset_info(self, project_id: str) -> Optional[DatasetInfo]:
        """Return cached dataset info for a project, or None."""
        if project_id in self._cache:
            return self._cache[project_id]
        return await self._find_existing(project_id)

    async def delete_dataset(self, dataset_id: str) -> None:
        """Delete a dataset via the v1 API and remove it from the cache."""
        await self._dataset_rw_write_request(
            "DELETE",
            f"/api/datasetrw/v1/datasets/{dataset_id}",
        )
        self._cache = {k: v for k, v in self._cache.items() if v.dataset_id != dataset_id}
        self._rw_cache.pop(dataset_id, None)
        logger.info("Deleted dataset %s", dataset_id)

    async def _dataset_rw_write_request(
        self,
        method: str,
        path: str,
        **kwargs,
    ):
        """Call Dataset RW write endpoints, preferring the direct host first."""
        last_exc: Optional[Exception] = None
        base_urls: list[Optional[str]] = []
        nucleus = _preferred_snapshot_api_base_url()
        if nucleus:
            base_urls.append(nucleus)
        base_urls.append(None)

        for index, base_url in enumerate(base_urls):
            request_kwargs = dict(kwargs)
            if base_url is not None:
                request_kwargs.setdefault("max_retries", 0)
            is_last = index == len(base_urls) - 1
            try:
                return await domino_request(
                    method,
                    path,
                    base_url=base_url,
                    **request_kwargs,
                )
            except httpx.HTTPStatusError as exc:
                last_exc = exc
                resp_body = ""
                try:
                    resp_body = exc.response.text[:300]
                except Exception:
                    pass
                if is_last:
                    raise
                logger.warning(
                    "Domino Dataset RW %s %s returned HTTP %s via direct host; "
                    "falling back to the default host. Body: %s",
                    method,
                    path,
                    exc.response.status_code,
                    resp_body,
                )
            except Exception as exc:
                last_exc = exc
                if is_last:
                    raise
                logger.warning(
                    "Domino Dataset RW %s %s failed via direct host (%s); "
                    "falling back to the default host",
                    method,
                    path,
                    exc,
                )

        raise last_exc or RuntimeError(f"Domino Dataset RW {method} {path} failed")

    async def download_file(
        self,
        dataset_id: str,
        file_path: str,
        dest_path: str,
    ) -> str:
        """Download a single file from a dataset to *dest_path*.

        Tries snapshot-based and direct download endpoints in order.
        The v4 raw endpoint with API key auth is tried first as it is the
        most reliable for cross-project dataset downloads.
        Returns *dest_path* on success, raises on failure.
        """
        snapshot_id = await self._get_latest_snapshot_id(dataset_id)
        rw_snapshot_id = await self.get_rw_snapshot_id(dataset_id)

        from urllib.parse import quote

        # Each entry is (endpoint_path, use_api_key).
        # The v4 raw endpoint requires X-Domino-Api-Key auth.
        endpoints: list[tuple[str, bool]] = []

        if rw_snapshot_id:
            encoded_path = quote(file_path, safe="")
            # v4 endpoint works on both proxy and nucleus; try with both
            # API key auth and Bearer token auth.
            endpoints.append((
                f"/v4/datasetrw/snapshot/{rw_snapshot_id}/file/raw"
                f"?path={encoded_path}&download=true",
                True,
            ))
            endpoints.append((
                f"/v4/datasetrw/snapshot/{rw_snapshot_id}/file/raw"
                f"?path={encoded_path}&download=true",
                False,
            ))

        # Try each endpoint via the default host (proxy), then fall back
        # to the nucleus-frontend host directly (proxy may 404 for
        # cross-project dataset file downloads).
        base_urls = [None]  # None = default (proxy-first)
        nucleus = resolve_domino_nucleus_host()
        if nucleus:
            base_urls.append(nucleus)

        last_error: Optional[Exception] = None
        for base_url in base_urls:
            for endpoint, use_api_key in endpoints:
                try:
                    await domino_download(
                        endpoint, dest_path,
                        base_url=base_url, use_api_key=use_api_key,
                    )
                    logger.info(
                        "Downloaded '%s' from dataset %s via %s (host=%s, api_key=%s)",
                        file_path, dataset_id, endpoint,
                        base_url or "default", use_api_key,
                    )
                    return dest_path
                except Exception as exc:
                    last_error = exc
                    logger.debug(
                        "Download failed on %s (host=%s): %s",
                        endpoint, base_url or "default", exc,
                    )
                    continue

        raise RuntimeError(
            f"Failed to download '{file_path}' from dataset {dataset_id}: {last_error}"
        )

    async def get_latest_snapshot_status(self, dataset_id: str) -> Optional[str]:
        """Return the status of the latest snapshot for a dataset.

        Uses ``GET /api/datasetrw/v1/datasets/{id}/snapshots`` which returns
        ``{"snapshots": [{"id": ..., "status": "active"|"pending"|...}]}``.

        Returns the status string (``"active"``, ``"pending"``, ``"copying"``,
        ``"failed"``, etc.) or ``None`` if no snapshot exists.
        """
        try:
            resp = await domino_request(
                "GET",
                f"/api/datasetrw/v1/datasets/{dataset_id}/snapshots",
                params={"limit": 1},
            )
            data = resp.json()
            snapshots = data.get("snapshots") or []
            if snapshots:
                snapshot = snapshots[0]
                # The v1 response wraps as {"snapshot": {...}} — unwrap if needed
                if "snapshot" in snapshot and isinstance(snapshot["snapshot"], dict):
                    snapshot = snapshot["snapshot"]
                return snapshot.get("status")
        except Exception:
            logger.debug("Failed to get snapshot status for dataset %s", dataset_id, exc_info=True)
        return None

    async def get_rw_snapshot_id(self, dataset_id: str) -> Optional[str]:
        """Return the read-write (mutable head) snapshot ID for a dataset.

        Checks the in-memory cache first, then calls the dataset details API.
        """
        # Fast path: dedicated RW cache
        if dataset_id in self._rw_cache:
            return self._rw_cache[dataset_id]

        # Check project cache
        for info in self._cache.values():
            if info.dataset_id == dataset_id and info.rw_snapshot_id:
                self._rw_cache[dataset_id] = info.rw_snapshot_id
                return info.rw_snapshot_id

        # Preferred path: the v1 snapshots endpoint is the most reliable and
        # already gives us the active RW head without an extra detail lookup.
        rw_sid = await self._resolve_rw_snapshot_v1(dataset_id)
        if rw_sid:
            return rw_sid

        # Fallback: retry the v1 snapshots endpoint via the default host
        # (proxy).  The non-versioned /api/datasetrw/datasets/{id} and
        # /api/datasetrw/snapshots/{id} endpoints are 404 on this Domino
        # version, so we skip them.
        try:
            resp = await domino_request(
                "GET",
                f"/api/datasetrw/v1/datasets/{dataset_id}/snapshots",
            )
            data = resp.json()
            snapshots = data.get("snapshots") or []
            for s in snapshots:
                if "snapshot" in s and isinstance(s["snapshot"], dict):
                    s = s["snapshot"]
                if s.get("isReadWrite") or s.get("status") == "active":
                    rw_sid = str(s.get("id") or s.get("snapshotId") or "")
                    if rw_sid:
                        self._backfill_rw_cache(dataset_id, rw_sid)
                        return rw_sid
        except Exception:
            logger.debug(
                "Failed to list v1 snapshots for dataset %s",
                dataset_id,
                exc_info=True,
            )

        return None

    def _backfill_rw_cache(self, dataset_id: str, rw_sid: str) -> None:
        """Store a discovered RW snapshot ID in both caches."""
        self._rw_cache[dataset_id] = rw_sid
        for info in self._cache.values():
            if info.dataset_id == dataset_id:
                info.rw_snapshot_id = rw_sid
                return

    async def _resolve_rw_snapshot_v1(self, dataset_id: str) -> Optional[str]:
        """Try the v1 snapshots endpoint to find the RW snapshot ID."""
        try:
            resp = await domino_request(
                "GET",
                f"/api/datasetrw/v1/datasets/{dataset_id}/snapshots",
            )
            data = resp.json()
            snapshots = data.get("snapshots") or []
            for s in snapshots:
                if "snapshot" in s and isinstance(s["snapshot"], dict):
                    s = s["snapshot"]
                if s.get("isReadWrite") or s.get("status") == "active":
                    rw_sid = str(s.get("id") or s.get("snapshotId") or "")
                    if rw_sid:
                        logger.debug(
                            "Resolved RW snapshot %s for dataset %s via v1 API",
                            rw_sid, dataset_id,
                        )
                        return rw_sid
        except Exception:
            logger.debug(
                "Failed to resolve RW snapshot via v1 for dataset %s",
                dataset_id,
                exc_info=True,
            )
        return None

    async def list_snapshot_files(
        self,
        snapshot_id: str,
        path: str = "",
    ) -> list[dict]:
        """List files in a dataset snapshot via the v4 files API.

        Returns a flat list of dicts with keys: ``fileName``, ``isDirectory``,
        ``sizeInBytes``, ``lastModified``.
        """
        try:
            resp = await domino_request(
                "GET",
                f"/v4/datasetrw/files/{snapshot_id}",
                params={"path": path},
            )
            data = resp.json()
            rows = data.get("rows", [])
            # Flatten the nested structure
            result: list[dict] = []
            for row in rows:
                name_info = row.get("name", {})
                size_info = row.get("size", {})
                result.append({
                    "fileName": name_info.get("fileName") or name_info.get("label", ""),
                    "isDirectory": name_info.get("isDirectory", False),
                    "sizeInBytes": (
                        size_info.get("sizeInBytes")
                        or name_info.get("sizeInBytes")
                        or 0
                    ),
                    "lastModified": row.get("lastModified"),
                    "url": name_info.get("url"),
                })
            return result
        except Exception:
            logger.debug(
                "Failed to list files for snapshot %s at path '%s'",
                snapshot_id,
                path,
                exc_info=True,
            )
            return []

    async def download_directory(
        self,
        dataset_id: str,
        remote_path: str,
        dest_dir: str,
    ) -> str:
        """Download an entire directory tree from a dataset to *dest_dir*.

        Recursively lists files in the snapshot and downloads each one.
        Returns *dest_dir* on success, raises on failure.
        """
        rw_id = await self.get_rw_snapshot_id(dataset_id)
        if not rw_id:
            raise RuntimeError(
                f"No RW snapshot found for dataset {dataset_id}"
            )

        await self._download_dir_recursive(
            dataset_id, rw_id, remote_path, dest_dir
        )
        return dest_dir

    async def _download_dir_recursive(
        self,
        dataset_id: str,
        snapshot_id: str,
        remote_path: str,
        local_dir: str,
    ) -> None:
        """Recursively list and download files from a snapshot directory.

        Uses the already-resolved *snapshot_id* (the RW snapshot) to
        download each file directly via the v4 raw endpoint, avoiding
        the per-file ``get_rw_snapshot_id`` resolution overhead.
        """
        from urllib.parse import quote

        os.makedirs(local_dir, exist_ok=True)
        entries = await self.list_snapshot_files(snapshot_id, path=remote_path)

        prefix_slash = (remote_path + "/") if remote_path else ""

        for entry in entries:
            name = entry.get("fileName", "")
            if not name:
                continue

            # The v4 files API may return full paths (e.g. "models/job_xxx/
            # learner.pkl") or just basenames ("learner.pkl").  Normalise to
            # an absolute remote path and a local basename.
            if name.startswith(prefix_slash):
                remote_child = name
                basename = name[len(prefix_slash):]
            elif "/" not in name:
                remote_child = f"{prefix_slash}{name}"
                basename = name
            else:
                remote_child = name
                basename = name.rsplit("/", 1)[-1]

            local_child = os.path.join(local_dir, basename)

            if entry.get("isDirectory"):
                await self._download_dir_recursive(
                    dataset_id, snapshot_id, remote_child, local_child
                )
            else:
                # Download directly via the v4 raw endpoint using the
                # already-known snapshot_id — no per-file API resolution.
                encoded = quote(remote_child, safe="")
                endpoint = (
                    f"/v4/datasetrw/snapshot/{snapshot_id}/file/raw"
                    f"?path={encoded}&download=true"
                )
                try:
                    await domino_download(
                        endpoint, local_child, use_api_key=True,
                    )
                    logger.debug(
                        "Downloaded '%s' via v4 raw endpoint", remote_child,
                    )
                except Exception:
                    # Fall back to the full download_file with endpoint
                    # cascade (handles edge cases like missing snapshots).
                    logger.debug(
                        "v4 raw download failed for '%s', falling back",
                        remote_child, exc_info=True,
                    )
                    await self.download_file(
                        dataset_id, remote_child, local_child
                    )

    async def delete_snapshot_files(
        self,
        snapshot_id: str,
        relative_paths: list[str],
    ) -> bool:
        """Delete files from a dataset snapshot (best-effort).

        Returns True on success, False on failure.
        """
        if not relative_paths:
            return True
        try:
            await self._dataset_rw_write_request(
                "DELETE",
                f"/v4/datasetrw/snapshot/{snapshot_id}/files",
                json={"relativePaths": relative_paths},
            )
            logger.info(
                "Deleted %d file(s) from snapshot %s: %s",
                len(relative_paths),
                snapshot_id,
                relative_paths,
            )
            return True
        except Exception:
            logger.warning(
                "Failed to delete files from snapshot %s: %s",
                snapshot_id,
                relative_paths,
                exc_info=True,
            )
            return False

    async def _get_latest_snapshot_id(self, dataset_id: str) -> Optional[str]:
        """Return the latest snapshot ID for a dataset, or None."""
        try:
            resp = await domino_request(
                "GET",
                f"/api/datasetrw/v1/datasets/{dataset_id}/snapshots",
                params={"limit": 1},
            )
            data = resp.json()
            snapshots = data.get("snapshots") or []
            if snapshots:
                s = snapshots[0]
                # Unwrap v1 envelope if present
                if "snapshot" in s and isinstance(s["snapshot"], dict):
                    s = s["snapshot"]
                return str(s.get("id") or s.get("snapshotId") or "")
        except Exception:
            logger.debug("Failed to get snapshot ID for dataset %s", dataset_id, exc_info=True)
        return None

    def invalidate(self, project_id: Optional[str] = None) -> None:
        """Clear cached info for one or all projects."""
        if project_id:
            self._cache.pop(project_id, None)
        else:
            self._cache.clear()

    async def upload_file(
        self,
        dataset_id: str,
        file_path: str,
        file_content: bytes,
        collision_setting: str = "Overwrite",
        chunk_size: int = _UPLOAD_CHUNK_SIZE,
    ) -> None:
        """Upload a file to a dataset via the v4 chunked upload API.

        Supports files of any size by splitting into chunks (default 8 MB).
        This follows the same workflow as the python-domino SDK:
          1. POST .../snapshot/file/start → get upload_key
          2. POST .../snapshot/file (multipart chunk) → upload data (repeated per chunk)
          3. GET  .../snapshot/file/end/{key} → finalize

        Upload requests go through the proxy (``domino_request`` default)
        rather than the nucleus-first wrapper because the Domino app proxy
        injects auth headers that the v4 multipart endpoints require.
        """
        # Step 1: Start upload session
        resp = await domino_request(
            "POST",
            f"/v4/datasetrw/datasets/{dataset_id}/snapshot/file/start",
            json={
                "filePaths": [file_path],
                "fileCollisionSetting": collision_setting,
            },
        )
        upload_key = resp.json()
        if not isinstance(upload_key, str):
            upload_key = upload_key.get("upload_key") or upload_key.get("uploadKey") or upload_key.get("key")
        if not upload_key:
            raise RuntimeError(f"Failed to start upload session for dataset {dataset_id}")

        logger.debug("Upload session started for dataset %s, key=%s", dataset_id, upload_key)

        try:
            await self._upload_chunks(
                dataset_id, upload_key, file_path, file_content, chunk_size
            )

            # Step 3: Finalize
            await domino_request(
                "GET",
                f"/v4/datasetrw/datasets/{dataset_id}/snapshot/file/end/{upload_key}",
            )
            logger.info(
                "Uploaded '%s' (%d bytes, %d chunk(s)) to dataset %s",
                file_path,
                len(file_content),
                max(1, (len(file_content) + chunk_size - 1) // chunk_size),
                dataset_id,
            )

        except Exception:
            # Cancel on failure
            try:
                await domino_request(
                    "GET",
                    f"/v4/datasetrw/datasets/{dataset_id}/snapshot/file/cancel/{upload_key}",
                )
            except Exception:
                pass
            raise

    async def _upload_chunks(
        self,
        dataset_id: str,
        upload_key: str,
        file_path: str,
        file_content: bytes,
        chunk_size: int,
    ) -> None:
        """Split *file_content* into chunks and upload each sequentially."""
        total_size = len(file_content)
        total_chunks = max(1, (total_size + chunk_size - 1) // chunk_size)
        identifier = file_path.replace(".", "-").replace("/", "-")

        for chunk_num in range(1, total_chunks + 1):
            start = (chunk_num - 1) * chunk_size
            end = min(start + chunk_size, total_size)
            chunk_data = file_content[start:end]
            chunk_checksum = hashlib.md5(chunk_data).hexdigest()

            chunk_params = {
                "key": upload_key,
                "resumableChunkNumber": chunk_num,
                "resumableChunkSize": chunk_size,
                "resumableCurrentChunkSize": len(chunk_data),
                "resumableTotalChunks": total_chunks,
                "resumableIdentifier": identifier,
                "resumableRelativePath": file_path,
                "checksum": chunk_checksum,
            }

            for attempt in range(_UPLOAD_MAX_RETRIES):
                try:
                    await domino_request(
                        "POST",
                        f"/v4/datasetrw/datasets/{dataset_id}/snapshot/file",
                        params=chunk_params,
                        files={file_path: (file_path, io.BytesIO(chunk_data), "application/octet-stream")},
                        headers={"Csrf-Token": "nocheck"},
                        max_retries=0,  # we handle retries here
                    )
                    break
                except Exception:
                    if attempt == _UPLOAD_MAX_RETRIES - 1:
                        raise
                    backoff = 2 ** attempt
                    logger.warning(
                        "Chunk %d/%d upload failed, retrying in %ds (attempt %d/%d)",
                        chunk_num, total_chunks, backoff, attempt + 1, _UPLOAD_MAX_RETRIES,
                    )
                    await asyncio.sleep(backoff)

            if total_chunks > 1:
                logger.debug(
                    "Uploaded chunk %d/%d (%d bytes) for '%s'",
                    chunk_num, total_chunks, len(chunk_data), file_path,
                )

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    async def _resolve_or_create(self, project_id: str) -> DatasetInfo:
        """Find or create the automl-extension dataset for *project_id*.

        Tries to create first (``POST /dataset``) which is a single fast
        call through the proxy.  If the dataset already exists (HTTP 400),
        falls back to listing to resolve the existing ID.  This avoids the
        listing step entirely for new datasets and works in App environments
        where the proxy disconnects on GET listing requests.
        """
        logger.info("Ensuring dataset '%s' exists in project %s", DATASET_NAME, project_id)
        try:
            created = await self._create_dataset(project_id)
            self._cache[project_id] = created
            return created
        except Exception:
            # Creation failed — dataset likely already exists.
            logger.debug(
                "Create failed for project %s, looking up existing dataset",
                project_id,
                exc_info=True,
            )

        existing = await self._find_existing(project_id)
        if existing:
            logger.info(
                "Dataset '%s' already exists for project %s (id=%s)",
                DATASET_NAME,
                project_id,
                existing.dataset_id,
            )
            self._cache[project_id] = existing
            return existing

        raise RuntimeError(
            f"Failed to create or find dataset '{DATASET_NAME}' in project {project_id}"
        )

    async def _find_existing(self, project_id: str) -> Optional[DatasetInfo]:
        """List datasets for *project_id* and return ours if it exists."""
        try:
            datasets = await list_project_datasets(project_id)
        except Exception:
            logger.exception("Failed to list datasets for project %s", project_id)
            return None

        for ds in datasets:
            name = ds.get("datasetName") or ds.get("name") or ""
            if name == DATASET_NAME:
                ds_id = str(ds.get("datasetId") or ds.get("id") or "")
                rw_sid = ds.get("readWriteSnapshotId") or None
                mount = self._probe_mount(name)
                logger.debug(
                    "Found dataset '%s' (id=%s) rw_snapshot=%s mount=%s",
                    name, ds_id, rw_sid, mount,
                )
                # If the v2 listing didn't include the RW snapshot ID,
                # resolve it eagerly via the v1 snapshots endpoint.
                if not rw_sid and ds_id:
                    rw_sid = await self._resolve_rw_snapshot_v1(ds_id)
                info = DatasetInfo(
                    dataset_id=ds_id,
                    name=name,
                    project_id=project_id,
                    mount_path=mount,
                    rw_snapshot_id=rw_sid,
                )
                return info

        return None

    async def _create_dataset(self, project_id: str) -> DatasetInfo:
        """POST to create the dataset, trying known endpoints in order.

        Uses ``domino_request`` directly (through the proxy) rather than
        the nucleus-first wrapper.  The Domino app proxy handles auth
        injection for cross-project dataset creation.  This matches the
        original pre-refactor behaviour that worked reliably.
        """
        # Each entry is (endpoint, payload).
        # /dataset + datasetName is the canonical SDK endpoint.
        # /api/datasetrw/v1/datasets + name also works via proxy.
        # v2 is 404 everywhere — skipped.
        attempts: list[tuple[str, dict]] = [
            (
                "/dataset",
                {
                    "datasetName": DATASET_NAME,
                    "projectId": project_id,
                    "description": DATASET_DESCRIPTION,
                },
            ),
            (
                "/dataset",
                {
                    "datasetName": DATASET_NAME,
                    "projectId": project_id,
                },
            ),
            (
                "/api/datasetrw/v1/datasets",
                {
                    "name": DATASET_NAME,
                    "projectId": project_id,
                    "description": DATASET_DESCRIPTION,
                },
            ),
            (
                "/api/datasetrw/v1/datasets",
                {
                    "name": DATASET_NAME,
                    "projectId": project_id,
                },
            ),
        ]

        last_error: Optional[str] = None
        for endpoint, payload in attempts:
            try:
                resp = await domino_request(
                    "POST",
                    endpoint,
                    json=payload,
                )
                body = resp.json()
                ds_id = str(
                    body.get("datasetId")
                    or body.get("id")
                    or body.get("dataset", {}).get("id")
                    or ""
                )
                ds_name = (
                    body.get("datasetName")
                    or body.get("name")
                    or body.get("dataset", {}).get("name")
                    or DATASET_NAME
                )
                logger.info(
                    "Created dataset '%s' (id=%s) in project %s via %s",
                    ds_name,
                    ds_id,
                    project_id,
                    endpoint,
                )
                mount = self._probe_mount(ds_name)
                return DatasetInfo(
                    dataset_id=ds_id,
                    name=ds_name,
                    project_id=project_id,
                    mount_path=mount,
                )
            except httpx.HTTPStatusError as exc:
                last_error = self._format_http_error(exc)
            except Exception as exc:
                last_error = str(exc)

            logger.warning(
                "Create attempt failed on %s with payload keys %s: %s",
                endpoint,
                list(payload.keys()),
                last_error,
            )

        raise RuntimeError(
            f"Failed to create dataset '{DATASET_NAME}' in project {project_id}. "
            f"Last error: {last_error}"
        )

    @staticmethod
    def _format_http_error(exc: httpx.HTTPStatusError) -> str:
        """Return a compact error string including response text when present."""
        response = exc.response
        if response is None:
            return str(exc)
        try:
            detail = response.text.strip()
        except Exception:
            detail = ""
        if detail:
            detail = " ".join(detail.split())
            if len(detail) > 300:
                detail = f"{detail[:297]}..."
            return f"{exc} body={detail}"
        return str(exc)

    @staticmethod
    def _probe_mount(dataset_name: str) -> Optional[str]:
        """Check known mount locations for a writable directory."""
        for template in _MOUNT_TEMPLATES:
            path = template.format(name=dataset_name)
            if os.path.isdir(path) and os.access(path, os.W_OK):
                return path
        # Also check env-provided mount roots
        for env_key in ("DOMINO_DATASET_MOUNT_PATH", "DOMINO_MOUNT_PATHS"):
            val = os.environ.get(env_key)
            if not val:
                continue
            for part in val.replace(",", ":").replace(";", ":").split(":"):
                part = part.strip()
                if not part:
                    continue
                candidate = os.path.join(part, dataset_name)
                if os.path.isdir(candidate) and os.access(candidate, os.W_OK):
                    return candidate
        return None


def _extract_dataset_list(data: object) -> list[dict]:
    """Normalize the Dataset RW API list response into a list of dicts.

    The v2 response wraps each item as ``{"dataset": {...}}``; this helper
    unwraps to the inner dict so callers can access fields directly.
    """
    return _extract_project_dataset_list(data)


@lru_cache()
def get_storage_resolver() -> ProjectStorageResolver:
    """Singleton ``ProjectStorageResolver`` instance."""
    return ProjectStorageResolver()
