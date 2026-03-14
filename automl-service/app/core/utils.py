"""Shared utility helpers."""

import hashlib
import logging
import os
import re
import time
from typing import Optional
from datetime import datetime, timezone

logger = logging.getLogger(__name__)

# Pattern: /domino/datasets/local/<dataset_name>/<relative_path>
_DATASET_MOUNT_RE = re.compile(
    r"^/domino/datasets/local/(?P<dataset_name>[^/]+)/(?P<relative>.+)$"
)


def cleanup_dataset_cache(cache_dir: str, max_age_hours: float = 24.0) -> int:
    """Delete cached dataset files older than *max_age_hours*. Returns count deleted."""
    if not os.path.isdir(cache_dir):
        return 0

    cutoff = time.time() - max_age_hours * 3600
    deleted = 0

    for dirpath, _, filenames in os.walk(cache_dir, topdown=False):
        for fname in filenames:
            fpath = os.path.join(dirpath, fname)
            try:
                if os.path.getmtime(fpath) < cutoff:
                    os.remove(fpath)
                    deleted += 1
            except OSError:
                pass
        # Remove empty directories
        try:
            if dirpath != cache_dir:
                os.rmdir(dirpath)  # only succeeds if empty
        except OSError:
            pass

    return deleted


def utc_now() -> datetime:
    """Return the current time as a timezone-aware UTC datetime."""
    return datetime.now(timezone.utc)


# Known Domino shared-dataset mount prefixes (order: most common first).
_MOUNT_ROOTS = [
    "/mnt/data/",
    "/domino/datasets/",
    "/domino/datasets/local/",
]


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

    relative_path = m.group("relative")

    from app.config import get_settings
    from app.services.storage_resolver import get_storage_resolver

    resolver = get_storage_resolver()
    info = await resolver.get_dataset_info(project_id)
    if not info:
        # Try resolve_or_create to ensure the dataset record exists
        try:
            info = await resolver._resolve_or_create(project_id)
        except Exception:
            logger.warning("Cannot resolve dataset for project %s", project_id)
            return file_path

    cache_key = hashlib.sha256(
        f"{info.dataset_id}:{relative_path}".encode()
    ).hexdigest()[:16]

    settings = get_settings()
    dest_path = os.path.join(settings.temp_path, "dataset_cache", cache_key, relative_path)

    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 0:
        logger.debug("Using cached download: %s", dest_path)
        return dest_path

    # Domino Dataset RW API has no file read/download endpoints.
    # Files should have been cached locally during upload.
    # If we reach here, the cache is missing — try download as last resort.
    logger.info(
        "File %s not found locally or in cache; attempting download from dataset %s",
        file_path, info.dataset_id,
    )
    try:
        await resolver.download_file(info.dataset_id, relative_path, dest_path)
        return dest_path
    except Exception:
        logger.warning(
            "Download failed (Domino has no file read API). "
            "File %s must be re-uploaded or accessed via dataset mount.",
            file_path,
        )
        return file_path
