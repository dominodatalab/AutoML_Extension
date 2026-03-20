"""Detect Domino project storage type (DFS vs git-based) via filesystem probe."""
import os
from enum import Enum


class DominoProjectType(Enum):
    DFS = "dfs"
    GIT = "git"
    UNKNOWN = "unknown"


def detect_project_type() -> DominoProjectType:
    """Detect current project type from filesystem signals.

    DFS projects mount datasets at /domino/datasets/local/.
    Git-based projects use /mnt/imported/data/ for shared datasets
    and /mnt/data/ for project workspace.
    """
    if os.path.isdir("/domino/datasets/local"):
        return DominoProjectType.DFS
    if os.path.isdir("/mnt/imported/data") or os.path.isdir("/mnt/data"):
        return DominoProjectType.GIT
    return DominoProjectType.UNKNOWN
