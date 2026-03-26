"""Service helpers for dataset route orchestration."""

import logging
import os
from functools import lru_cache
from typing import Any, Optional, Sequence

from fastapi import HTTPException

from app.api.schemas.dataset import (
    DatasetListResponse,
    DatasetResponse,
)
from app.config import get_settings
from app.core.dataset_mounts import resolve_dataset_mount_paths
from app.core.dataset_manager import DominoDatasetManager

logger = logging.getLogger(__name__)


@lru_cache()
def get_dataset_manager() -> DominoDatasetManager:
    """Get dataset manager instance (cached)."""
    return DominoDatasetManager()


def get_dataset_mount_root() -> str:
    """Resolve dataset mount root for current runtime."""
    mount_paths = resolve_dataset_mount_paths(fallback_path=get_settings().datasets_path)
    if mount_paths:
        return mount_paths[0]
    return get_settings().datasets_path


def get_dataset_mount_roots() -> list[str]:
    """Resolve all candidate dataset mount roots for the active runtime."""
    return resolve_dataset_mount_paths(fallback_path=get_settings().datasets_path)


def _extract_file_path(file_entry: Any) -> Optional[str]:
    if isinstance(file_entry, dict):
        path = file_entry.get("path")
        return str(path) if path else None
    if hasattr(file_entry, "path"):
        path = getattr(file_entry, "path")
        return str(path) if path else None
    return None


def filter_local_datasets(
    datasets: Sequence[Any],
    local_path: Optional[str] = None,
    local_paths: Optional[Sequence[str]] = None,
) -> list[Any]:
    """Return only datasets that are mounted in the active dataset path."""
    filtered_datasets: list[Any] = []
    resolved_paths = list(local_paths) if local_paths else []
    if local_path:
        resolved_paths.append(local_path)
    if not resolved_paths:
        resolved_paths = get_dataset_mount_roots()

    for ds in datasets:
        ds_name = getattr(ds, "name", None)
        ds_id = str(getattr(ds, "id", ""))
        ds_files = getattr(ds, "files", []) or []

        if not ds_name or ds_name.startswith("/") or ds_id.startswith("/"):
            continue

        found_on_mount = False
        for root in resolved_paths:
            if os.path.exists(os.path.join(root, ds_name)):
                found_on_mount = True
                break

        if not found_on_mount:
            for file_entry in ds_files:
                file_path = _extract_file_path(file_entry)
                if file_path and os.path.exists(file_path):
                    found_on_mount = True
                    break

        if found_on_mount or ds_id.startswith("domino:"):
            filtered_datasets.append(ds)

    return filtered_datasets


async def list_datasets_response(
    dataset_manager: DominoDatasetManager,
    project_id: Optional[str] = None,
    include_files: bool = True,
) -> DatasetListResponse:
    """List available datasets in API response shape."""
    datasets = await dataset_manager.list_datasets(
        project_id=project_id,
        include_files=include_files,
    )

    if project_id:
        filtered_datasets = datasets
    else:
        dataset_mount_roots = get_dataset_mount_roots()
        filtered_datasets = filter_local_datasets(datasets, local_paths=dataset_mount_roots)

    logger.info(
        "Returning %s datasets (from %s total, project_id=%s)",
        len(filtered_datasets),
        len(datasets),
        project_id or "(none)",
    )
    return DatasetListResponse(datasets=filtered_datasets, total=len(filtered_datasets))


async def get_dataset_or_404(
    dataset_manager: DominoDatasetManager,
    dataset_id: str,
    include_files: bool = True,
) -> DatasetResponse:
    """Get dataset details or raise a 404."""
    dataset = await dataset_manager.get_dataset(dataset_id, include_files=include_files)
    if not dataset:
        raise HTTPException(status_code=404, detail="Dataset not found")
    return dataset
