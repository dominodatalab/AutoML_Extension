"""Resolve project-scoped storage via Domino Datasets.

Provides dataset discovery, snapshot management, and file listing for
the ``automl-extension`` dataset in a target project.

Usage::

    resolver = get_storage_resolver()
    rw_id = await resolver.get_rw_snapshot_id(dataset_id)
    files = await resolver.list_snapshot_files(rw_id)
"""

import logging
import os
from dataclasses import dataclass, field
from functools import lru_cache
from typing import Optional

from app.api.generated.domino_public_api_client.api.dataset_rw import (
    get_dataset_snapshots,
)
from app.api.generated.domino_public_api_client.models.paginated_snapshot_envelope_v1 import (
    PaginatedSnapshotEnvelopeV1,
)
from app.api.generated.domino_public_api_client.models.snapshot_details_v1 import (
    SnapshotDetailsV1,
)
from app.api.generated.domino_public_api_client.models.snapshot_details_v1_status import (
    SnapshotDetailsV1Status,
)
from app.core.domino_http import (
    domino_request,
    get_domino_public_api_client_sync,
)
from app.services.domino_dataset_api import (
    extract_dataset_list as _extract_project_dataset_list,
    list_project_datasets,
)

logger = logging.getLogger(__name__)

DATASET_NAME = "automl-extension"

# Ordered list of mount path templates to probe after dataset creation.
_MOUNT_TEMPLATES = [
    "/domino/datasets/local/{name}",
    "/domino/datasets/{name}",
    "/mnt/data/{name}",
    "/mnt/imported/data/{name}",
]


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
    """Dataset discovery, snapshot management, and file listing.

    Provides read-only access to per-project ``automl-extension`` datasets.
    Results are cached in-memory so repeated calls for the same project
    hit the API at most once.
    """

    # project_id → DatasetInfo
    _cache: dict[str, DatasetInfo] = field(default_factory=dict)
    # dataset_id → rw_snapshot_id (dedicated cache so lookups don't
    # depend on the dataset having been resolved via ensure_dataset_exists)
    _rw_cache: dict[str, str] = field(default_factory=dict)

    # ------------------------------------------------------------------
    # Snapshot management
    # ------------------------------------------------------------------

    @staticmethod
    def _list_snapshots_typed(
        dataset_id: str,
        *,
        limit: Optional[int] = None,
    ) -> list[SnapshotDetailsV1]:
        """List snapshots for a dataset using the generated API client.

        Returns typed ``SnapshotDetailsV1`` objects.  Returns an empty list
        on any error so callers can fall through gracefully.
        """
        client = get_domino_public_api_client_sync()
        kwargs: dict = {}
        if limit is not None:
            kwargs["limit"] = limit
        result = get_dataset_snapshots.sync(dataset_id, client=client, **kwargs)
        if isinstance(result, PaginatedSnapshotEnvelopeV1):
            return list(result.snapshots)
        return []

    async def get_latest_snapshot_status(self, dataset_id: str) -> Optional[str]:
        """Return the status of the latest snapshot for a dataset.

        Returns the status string (``"active"``, ``"pending"``, ``"copying"``,
        ``"failed"``, etc.) or ``None`` if no snapshot exists.
        """
        try:
            snapshots = self._list_snapshots_typed(dataset_id, limit=1)
            if snapshots:
                return str(snapshots[0].status.value)
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

        # Fallback: retry the v1 snapshots endpoint (same generated client).
        try:
            snapshots = self._list_snapshots_typed(dataset_id)
            for s in snapshots:
                if s.status == SnapshotDetailsV1Status.ACTIVE:
                    self._backfill_rw_cache(dataset_id, s.id)
                    return s.id
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
            snapshots = self._list_snapshots_typed(dataset_id)
            for s in snapshots:
                if s.status == SnapshotDetailsV1Status.ACTIVE:
                    logger.debug(
                        "Resolved RW snapshot %s for dataset %s via v1 API",
                        s.id, dataset_id,
                    )
                    return s.id
        except Exception:
            logger.debug(
                "Failed to resolve RW snapshot via v1 for dataset %s",
                dataset_id,
                exc_info=True,
            )
        return None

    # ------------------------------------------------------------------
    # File listing
    # ------------------------------------------------------------------

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

    # ------------------------------------------------------------------
    # Dataset discovery
    # ------------------------------------------------------------------

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

    # ------------------------------------------------------------------
    # Utilities
    # ------------------------------------------------------------------

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
    """Normalize the Dataset RW API list response into a list of dicts."""
    return _extract_project_dataset_list(data)


@lru_cache()
def get_storage_resolver() -> ProjectStorageResolver:
    """Singleton ``ProjectStorageResolver`` instance."""
    return ProjectStorageResolver()
