"""Resolve project-scoped storage via Domino Datasets (auto-created).

Ensures a writable ``automl-extension`` dataset exists for a given target
project and returns the local mount path.  The dataset is created via the
Domino Dataset RW v2 API if it does not already exist.

Usage::

    resolver = get_storage_resolver()
    mount_path = await resolver.ensure_project_storage(project_id)
    # mount_path == "/domino/datasets/local/automl-extension" (or similar)
"""

import logging
import os
from dataclasses import dataclass, field
from functools import lru_cache
from typing import Optional

from app.core.domino_http import domino_request, resolve_domino_api_host

logger = logging.getLogger(__name__)

DATASET_NAME = "automl-extension"
DATASET_DESCRIPTION = "AutoML Extension storage — auto-created by the AutoML App"

# Ordered list of mount path templates to probe after dataset creation.
_MOUNT_TEMPLATES = [
    "/domino/datasets/local/{name}",
    "/domino/datasets/{name}",
    "/mnt/data/{name}",
    "/mnt/imported/data/{name}",
]


@dataclass
class DatasetInfo:
    """Lightweight handle for a resolved dataset."""

    dataset_id: str
    name: str
    project_id: str
    mount_path: Optional[str] = None


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

    async def get_dataset_info(self, project_id: str) -> Optional[DatasetInfo]:
        """Return cached dataset info for a project, or None."""
        if project_id in self._cache:
            return self._cache[project_id]
        return await self._find_existing(project_id)

    def invalidate(self, project_id: Optional[str] = None) -> None:
        """Clear cached info for one or all projects."""
        if project_id:
            self._cache.pop(project_id, None)
        else:
            self._cache.clear()

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    async def _resolve_or_create(self, project_id: str) -> DatasetInfo:
        """Find or create the automl-extension dataset for *project_id*."""
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

        logger.info("Creating dataset '%s' in project %s", DATASET_NAME, project_id)
        created = await self._create_dataset(project_id)
        self._cache[project_id] = created
        return created

    async def _find_existing(self, project_id: str) -> Optional[DatasetInfo]:
        """List datasets for *project_id* and return ours if it exists."""
        try:
            resp = await domino_request(
                "GET",
                "/api/datasetrw/v2/datasets",
                params={"projectIdsToInclude": project_id},
            )
        except Exception:
            logger.exception("Failed to list datasets for project %s", project_id)
            return None

        data = resp.json()
        datasets = _extract_dataset_list(data)

        for ds in datasets:
            name = ds.get("datasetName") or ds.get("name") or ""
            if name == DATASET_NAME:
                ds_id = str(ds.get("datasetId") or ds.get("id") or "")
                mount = self._probe_mount(name)
                info = DatasetInfo(
                    dataset_id=ds_id,
                    name=name,
                    project_id=project_id,
                    mount_path=mount,
                )
                return info

        return None

    async def _create_dataset(self, project_id: str) -> DatasetInfo:
        """POST to create the dataset.  Tries common payload shapes."""
        payloads = [
            # Most likely Domino v2 shape
            {
                "datasetName": DATASET_NAME,
                "projectId": project_id,
                "description": DATASET_DESCRIPTION,
            },
            # Alternate field names
            {
                "name": DATASET_NAME,
                "projectId": project_id,
                "description": DATASET_DESCRIPTION,
            },
        ]

        last_error: Optional[str] = None
        for payload in payloads:
            try:
                resp = await domino_request(
                    "POST",
                    "/api/datasetrw/v2/datasets",
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
                    "Created dataset '%s' (id=%s) in project %s",
                    ds_name,
                    ds_id,
                    project_id,
                )
                mount = self._probe_mount(ds_name)
                return DatasetInfo(
                    dataset_id=ds_id,
                    name=ds_name,
                    project_id=project_id,
                    mount_path=mount,
                )
            except Exception as exc:
                last_error = str(exc)
                logger.debug(
                    "Create attempt failed with payload %s: %s",
                    list(payload.keys()),
                    exc,
                )
                continue

        raise RuntimeError(
            f"Failed to create dataset '{DATASET_NAME}' in project {project_id}. "
            f"Last error: {last_error}"
        )

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
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        return (
            data.get("items")
            or data.get("datasets")
            or data.get("data")
            or []
        )
    return []


@lru_cache()
def get_storage_resolver() -> ProjectStorageResolver:
    """Singleton ``ProjectStorageResolver`` instance."""
    return ProjectStorageResolver()
