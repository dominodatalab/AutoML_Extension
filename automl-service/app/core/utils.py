"""Shared utility helpers."""

import logging
import os
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

            logger.info(f"CANDIDATE PATH IS {candidate}")
            if os.path.exists(candidate):
                logger.info(
                    "Remapped path %s -> %s (cross-project mount)",
                    path, candidate,
                )
                return candidate

    return path
