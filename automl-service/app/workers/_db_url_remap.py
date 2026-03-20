"""Remap sqlite database URLs across Domino cross-project mount points."""
import os

from app.core.domino_project_type import detect_project_type, DominoProjectType

_DB_MOUNT_ROOTS_DFS = [
    "/domino/datasets/local/",
    "/domino/datasets/",
    "/mnt/imported/data/",
    "/mnt/data/",
]

_DB_MOUNT_ROOTS_GIT = [
    "/mnt/imported/data/",
    "/mnt/data/",
    "/domino/datasets/local/",
    "/domino/datasets/",
]


def remap_database_url(url: str) -> str:
    """Remap a sqlite:// URL when the DB file isn't at the original mount path."""
    prefix = "sqlite:////"
    if not url.startswith(prefix):
        return url
    db_path = "/" + url[len(prefix):]
    if os.path.exists(db_path):
        return url

    project_type = detect_project_type()
    mount_roots = (
        _DB_MOUNT_ROOTS_DFS if project_type == DominoProjectType.DFS
        else _DB_MOUNT_ROOTS_GIT
    )

    for src_root in mount_roots:
        if not db_path.startswith(src_root):
            continue
        relative = db_path[len(src_root):]
        for candidate_root in mount_roots:
            if candidate_root == src_root:
                continue
            candidate = candidate_root + relative
            if os.path.exists(candidate):
                return f"sqlite:////{candidate.lstrip('/')}"
    return url
