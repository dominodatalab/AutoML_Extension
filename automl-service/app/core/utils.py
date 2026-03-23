"""Shared utility helpers."""

import logging
import os
import time
from datetime import datetime, timezone

logger = logging.getLogger(__name__)


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
