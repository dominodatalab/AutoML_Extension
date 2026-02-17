"""Helpers for resolving Domino dataset mount paths."""

import os
from typing import Optional

DATASET_MOUNT_PATH_ENV = "DOMINO_DATASET_MOUNT_PATH"
DATASET_MOUNT_PATHS_ENV = "DOMINO_MOUNT_PATHS"

# Domino docs list these mount locations:
# - DFS projects: /domino/datasets/local
# - Git-based projects: /mnt/data (local) and /mnt/imported/data (shared)
DEFAULT_DOMINO_DATASET_ROOTS = (
    "/domino/datasets/local",
    "/mnt/data",
    "/mnt/imported/data",
)


def _split_mount_env(value: str) -> list[str]:
    """Split env-provided mount paths into normalized path strings."""
    if not value:
        return []

    normalized = value.replace("\n", ",").replace(";", ",")
    tokens: list[str] = []
    for chunk in normalized.split(","):
        chunk = chunk.strip()
        if not chunk:
            continue
        if os.pathsep in chunk:
            tokens.extend(part.strip() for part in chunk.split(os.pathsep) if part.strip())
        else:
            tokens.append(chunk)
    return tokens


def resolve_dataset_mount_paths(fallback_path: Optional[str] = None) -> list[str]:
    """Resolve existing dataset mount roots in precedence order."""
    candidates: list[str] = []
    explicit_paths: list[str] = []

    env_override = os.environ.get(DATASET_MOUNT_PATH_ENV)
    if env_override:
        explicit_paths.extend(_split_mount_env(env_override))

    env_mount_paths = os.environ.get(DATASET_MOUNT_PATHS_ENV)
    if env_mount_paths:
        explicit_paths.extend(_split_mount_env(env_mount_paths))

    if explicit_paths:
        candidates.extend(explicit_paths)
    else:
        candidates.extend(DEFAULT_DOMINO_DATASET_ROOTS)
        if fallback_path:
            candidates.append(fallback_path)

    # If explicit env paths were provided but none exist yet, still return
    # the raw explicit paths so callers can log/diagnose the configuration.
    if explicit_paths and not any(os.path.exists(path) for path in explicit_paths):
        return [os.path.abspath(path) for path in explicit_paths if path]

    resolved: list[str] = []
    seen: set[str] = set()
    for raw_path in candidates:
        if not raw_path:
            continue
        abs_path = os.path.abspath(raw_path)
        if abs_path in seen:
            continue
        if not os.path.exists(abs_path):
            continue
        resolved.append(abs_path)
        seen.add(abs_path)

    return resolved
