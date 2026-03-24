"""Shared utility helpers."""

import hashlib
import logging
import os
import re
import time
from typing import Optional
from datetime import datetime, timezone

logger = logging.getLogger(__name__)

# Patterns for dataset mount paths across Domino project types:
#   DFS projects:      /domino/datasets/local/<name>/...
#   Git-based projects: /mnt/data/<name>/... or /mnt/imported/data/<name>/...
#   Alternative:       /domino/datasets/<name>/...
_DATASET_MOUNT_RE = re.compile(
    r"^(?:/domino/datasets/local|/domino/datasets|/mnt/data|/mnt/imported/data)"
    r"/(?P<dataset_name>[^/]+)/(?P<relative>.+)$"
)


def cleanup_dataset_cache(cache_dir: str, max_age_hours: int = 24) -> int:
    """Remove cached dataset files older than *max_age_hours*.

    Called at startup and can be called periodically for long-running pods.
    Returns the number of files deleted.
    """
    if not os.path.isdir(cache_dir):
        return 0

    cutoff = time.time() - (max_age_hours * 3600)
    deleted = 0

    for dirpath, _, filenames in os.walk(cache_dir, topdown=False):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            try:
                if os.path.getmtime(filepath) < cutoff:
                    os.remove(filepath)
                    deleted += 1
            except OSError:
                pass
        # Remove empty directories
        try:
            if dirpath != cache_dir and not os.listdir(dirpath):
                os.rmdir(dirpath)
        except OSError:
            pass

    return deleted


def utc_now() -> datetime:
    """Return the current time as a timezone-aware UTC datetime."""
    return datetime.now(timezone.utc)


# Known Domino shared-dataset mount prefixes (order: most common first).
_MOUNT_ROOTS = [
    "/mnt/data/",
    "/mnt/imported/data/",
    "/domino/datasets/",
    "/domino/datasets/local/",
]

# TODO I am not sure if this is necessary if the correct environment variables are set
# I personally wouldn't want some code to guess a file path for me
# It could cause code to write to the wrong location and cause annoying bugs
def remap_shared_path(path: str) -> str:
    """Remap an absolute file path when running in a different Domino project.

    The DB may store paths from the App's mount point (e.g.
    ``/mnt/data/automl_shared_db/uploads/file.csv``) but a child job in
    another project sees the same shared dataset at a different mount
    (e.g. ``/domino/datasets/automl_shared_db/uploads/file.csv``).

    Checks known shared-dataset mount prefixes and returns the first
    alternative that exists on disk.  If the original path already
    exists it is returned unchanged.
    """
    if not path or os.path.exists(path):
        return path

    for src_root in _MOUNT_ROOTS:
        if not path.startswith(src_root):
            continue
        relative = path[len(src_root):]
        for candidate_root in _MOUNT_ROOTS:
            if candidate_root == src_root:
                continue
            candidate = candidate_root + relative

            if os.path.exists(candidate):
                logger.info(
                    "Remapped path %s -> %s (cross-project mount)",
                    path, candidate,
                )
                return candidate

    return path


def extract_dataset_relative_path(file_path: Optional[str]) -> Optional[str]:
    """Return the relative path inside a Domino dataset mount, if present."""
    if not file_path:
        return None

    match = _DATASET_MOUNT_RE.match(file_path)
    if not match:
        return None

    return match.group("relative")


async def ensure_local_file(file_path: str, project_id: Optional[str] = None) -> str:
    """Return a local path to *file_path*, downloading from the dataset API if needed.

    If the file already exists locally (directly or via ``remap_shared_path``),
    it is returned as-is.  Otherwise, if the path looks like a Domino dataset
    mount path, the file is downloaded via the Dataset RW API into a local
    cache directory.
    """
    if os.path.exists(file_path):
        return file_path

    remapped = remap_shared_path(file_path)
    if os.path.exists(remapped):
        return remapped

    m = _DATASET_MOUNT_RE.match(file_path)
    if not m or not project_id:
        return file_path  # can't resolve — return original, will fail downstream

    dataset_name = m.group("dataset_name")
    relative_path = m.group("relative")

    from app.config import get_settings
    from app.services.storage_resolver import get_storage_resolver

    resolver = get_storage_resolver()

    # Resolve the dataset_id — first try the automl-extension dataset,
    # then look up by name across all project datasets.
    dataset_id: Optional[str] = None
    info = await resolver.get_dataset_info(project_id)
    if info and info.name == dataset_name:
        dataset_id = info.dataset_id
    else:
        # Dataset is not the automl-extension one — look it up by name
        # via the dataset manager (which queries the Domino API).
        dataset_id = await _resolve_dataset_id_by_name(
            project_id, dataset_name
        )

    if not dataset_id:
        logger.warning(
            "Cannot resolve dataset '%s' in project %s",
            dataset_name, project_id,
        )
        return file_path

    cache_key = hashlib.sha256(
        f"{dataset_id}:{relative_path}".encode()
    ).hexdigest()[:16]

    settings = get_settings()
    dest_path = os.path.join(settings.temp_path, "dataset_cache", cache_key, relative_path)

    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 0:
        logger.debug("Using cached download: %s", dest_path)
        return dest_path

    logger.info(
        "File %s not found locally or in cache; attempting download from dataset %s (%s)",
        file_path, dataset_name, dataset_id,
    )
    try:
        await resolver.download_file(dataset_id, relative_path, dest_path)
        return dest_path
    except Exception:
        logger.warning(
            "Download failed for '%s' from dataset %s (%s). "
            "File must be re-uploaded or the dataset mounted to this app.",
            relative_path, dataset_name, dataset_id,
        )
        return file_path


async def _resolve_dataset_id_by_name(
    project_id: str, dataset_name: str
) -> Optional[str]:
    """Look up a dataset ID by name within a project via the Domino API."""
    from app.services.domino_dataset_api import list_project_datasets

    try:
        items = await list_project_datasets(project_id)
        for item in items:
            name = item.get("datasetName") or item.get("name") or ""
            if name == dataset_name:
                return str(item.get("datasetId") or item.get("id") or "")
    except Exception:
        logger.debug(
            "Failed to resolve dataset '%s' in project %s",
            dataset_name, project_id, exc_info=True,
        )
    return None
