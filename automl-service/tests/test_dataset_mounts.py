"""Tests for app.core.dataset_mounts.

Covers:
- _split_mount_env — comma, semicolon, newline separated, empty values
- resolve_dataset_mount_paths — env override, default paths, fallback_path, deduplication
"""

import os

import pytest

from app.core.dataset_mounts import (
    DATASET_MOUNT_PATH_ENV,
    DATASET_MOUNT_PATHS_ENV,
    DEFAULT_DOMINO_DATASET_ROOTS,
    _split_mount_env,
    resolve_dataset_mount_paths,
)


# ---------------------------------------------------------------------------
# _split_mount_env
# ---------------------------------------------------------------------------


class TestSplitMountEnv:
    """Test the _split_mount_env helper for parsing mount path strings."""

    def test_comma_separated(self):
        result = _split_mount_env("/mnt/a,/mnt/b,/mnt/c")
        assert result == ["/mnt/a", "/mnt/b", "/mnt/c"]

    def test_semicolon_separated(self):
        result = _split_mount_env("/mnt/a;/mnt/b;/mnt/c")
        assert result == ["/mnt/a", "/mnt/b", "/mnt/c"]

    def test_newline_separated(self):
        result = _split_mount_env("/mnt/a\n/mnt/b\n/mnt/c")
        assert result == ["/mnt/a", "/mnt/b", "/mnt/c"]

    def test_mixed_separators(self):
        result = _split_mount_env("/mnt/a,/mnt/b;/mnt/c\n/mnt/d")
        assert result == ["/mnt/a", "/mnt/b", "/mnt/c", "/mnt/d"]

    def test_empty_string(self):
        assert _split_mount_env("") == []

    def test_whitespace_only(self):
        """Whitespace-only chunks are skipped."""
        result = _split_mount_env("  , , ")
        assert result == []

    def test_strips_whitespace(self):
        result = _split_mount_env("  /mnt/a , /mnt/b  ")
        assert result == ["/mnt/a", "/mnt/b"]

    def test_trailing_separator(self):
        result = _split_mount_env("/mnt/a,/mnt/b,")
        assert result == ["/mnt/a", "/mnt/b"]

    def test_leading_separator(self):
        result = _split_mount_env(",/mnt/a,/mnt/b")
        assert result == ["/mnt/a", "/mnt/b"]

    def test_consecutive_separators(self):
        result = _split_mount_env("/mnt/a,,/mnt/b;;;/mnt/c")
        assert result == ["/mnt/a", "/mnt/b", "/mnt/c"]

    def test_single_path(self):
        result = _split_mount_env("/mnt/data")
        assert result == ["/mnt/data"]


# ---------------------------------------------------------------------------
# resolve_dataset_mount_paths — env override
# ---------------------------------------------------------------------------


class TestResolveDatasetMountPathsEnvOverride:
    """Test resolve_dataset_mount_paths when env vars override defaults."""

    def test_env_override_with_existing_dir(self, tmp_path, monkeypatch):
        """DOMINO_DATASET_MOUNT_PATH pointing to an existing directory."""
        mount_dir = tmp_path / "datasets"
        mount_dir.mkdir()

        monkeypatch.setenv(DATASET_MOUNT_PATH_ENV, str(mount_dir))
        monkeypatch.delenv(DATASET_MOUNT_PATHS_ENV, raising=False)

        result = resolve_dataset_mount_paths()
        assert os.path.abspath(str(mount_dir)) in result

    def test_env_override_nonexistent_returns_abs_paths(self, monkeypatch):
        """When env paths don't exist, the function still returns their abs paths."""
        monkeypatch.setenv(DATASET_MOUNT_PATH_ENV, "/nonexistent/mount/path")
        monkeypatch.delenv(DATASET_MOUNT_PATHS_ENV, raising=False)

        result = resolve_dataset_mount_paths()
        assert len(result) >= 1
        assert all(os.path.isabs(p) for p in result)

    def test_env_mount_paths_with_existing_dirs(self, tmp_path, monkeypatch):
        """DOMINO_MOUNT_PATHS with multiple existing directories."""
        dir_a = tmp_path / "a"
        dir_b = tmp_path / "b"
        dir_a.mkdir()
        dir_b.mkdir()

        monkeypatch.delenv(DATASET_MOUNT_PATH_ENV, raising=False)
        monkeypatch.setenv(DATASET_MOUNT_PATHS_ENV, f"{dir_a},{dir_b}")

        result = resolve_dataset_mount_paths()
        assert os.path.abspath(str(dir_a)) in result
        assert os.path.abspath(str(dir_b)) in result

    def test_both_env_vars_combined(self, tmp_path, monkeypatch):
        """Both DOMINO_DATASET_MOUNT_PATH and DOMINO_MOUNT_PATHS are used."""
        dir_primary = tmp_path / "primary"
        dir_secondary = tmp_path / "secondary"
        dir_primary.mkdir()
        dir_secondary.mkdir()

        monkeypatch.setenv(DATASET_MOUNT_PATH_ENV, str(dir_primary))
        monkeypatch.setenv(DATASET_MOUNT_PATHS_ENV, str(dir_secondary))

        result = resolve_dataset_mount_paths()
        assert os.path.abspath(str(dir_primary)) in result
        assert os.path.abspath(str(dir_secondary)) in result


# ---------------------------------------------------------------------------
# resolve_dataset_mount_paths — default paths and fallback
# ---------------------------------------------------------------------------


class TestResolveDatasetMountPathsDefaults:
    """Test resolve_dataset_mount_paths without env vars (uses defaults)."""

    def test_uses_default_roots_when_no_env(self, monkeypatch):
        """Without env vars, DEFAULT_DOMINO_DATASET_ROOTS are used as candidates."""
        monkeypatch.delenv(DATASET_MOUNT_PATH_ENV, raising=False)
        monkeypatch.delenv(DATASET_MOUNT_PATHS_ENV, raising=False)

        # On a dev machine none of the Domino defaults exist, so result
        # should be empty (no existing dirs found and no fallback).
        result = resolve_dataset_mount_paths()
        # Each result, if any, must be one of the default roots
        for p in result:
            assert p in [os.path.abspath(d) for d in DEFAULT_DOMINO_DATASET_ROOTS]

    def test_fallback_path_used_when_no_env(self, tmp_path, monkeypatch):
        """When no env var is set and defaults don't exist, fallback_path is used."""
        monkeypatch.delenv(DATASET_MOUNT_PATH_ENV, raising=False)
        monkeypatch.delenv(DATASET_MOUNT_PATHS_ENV, raising=False)

        fallback = tmp_path / "fallback_datasets"
        fallback.mkdir()

        result = resolve_dataset_mount_paths(fallback_path=str(fallback))
        assert os.path.abspath(str(fallback)) in result

    def test_fallback_path_ignored_when_env_set(self, tmp_path, monkeypatch):
        """When env vars are set, fallback_path is NOT added to candidates."""
        env_dir = tmp_path / "env_mount"
        fallback_dir = tmp_path / "fallback"
        env_dir.mkdir()
        fallback_dir.mkdir()

        monkeypatch.setenv(DATASET_MOUNT_PATH_ENV, str(env_dir))
        monkeypatch.delenv(DATASET_MOUNT_PATHS_ENV, raising=False)

        result = resolve_dataset_mount_paths(fallback_path=str(fallback_dir))
        assert os.path.abspath(str(env_dir)) in result
        assert os.path.abspath(str(fallback_dir)) not in result


# ---------------------------------------------------------------------------
# resolve_dataset_mount_paths — deduplication
# ---------------------------------------------------------------------------


class TestResolveDatasetMountPathsDeduplication:
    """Test that resolve_dataset_mount_paths deduplicates paths."""

    def test_duplicate_paths_deduplicated(self, tmp_path, monkeypatch):
        mount_dir = tmp_path / "shared"
        mount_dir.mkdir()

        monkeypatch.setenv(
            DATASET_MOUNT_PATH_ENV, f"{mount_dir},{mount_dir}"
        )
        monkeypatch.delenv(DATASET_MOUNT_PATHS_ENV, raising=False)

        result = resolve_dataset_mount_paths()
        abs_mount = os.path.abspath(str(mount_dir))
        assert result.count(abs_mount) == 1

    def test_duplicate_across_env_vars(self, tmp_path, monkeypatch):
        """Same path in both env vars should only appear once."""
        mount_dir = tmp_path / "dup"
        mount_dir.mkdir()

        monkeypatch.setenv(DATASET_MOUNT_PATH_ENV, str(mount_dir))
        monkeypatch.setenv(DATASET_MOUNT_PATHS_ENV, str(mount_dir))

        result = resolve_dataset_mount_paths()
        abs_mount = os.path.abspath(str(mount_dir))
        assert result.count(abs_mount) == 1

    def test_relative_and_absolute_same_dir_deduplicated(self, tmp_path, monkeypatch):
        """A relative path that resolves to the same absolute path is deduplicated."""
        mount_dir = tmp_path / "rel_test"
        mount_dir.mkdir()
        abs_path = os.path.abspath(str(mount_dir))

        monkeypatch.setenv(
            DATASET_MOUNT_PATH_ENV, f"{mount_dir},{abs_path}"
        )
        monkeypatch.delenv(DATASET_MOUNT_PATHS_ENV, raising=False)

        result = resolve_dataset_mount_paths()
        assert result.count(abs_path) == 1


# ---------------------------------------------------------------------------
# resolve_dataset_mount_paths — result ordering and abs paths
# ---------------------------------------------------------------------------


class TestResolveDatasetMountPathsMisc:
    """Miscellaneous edge cases."""

    def test_results_are_absolute_paths(self, tmp_path, monkeypatch):
        mount_dir = tmp_path / "abs_check"
        mount_dir.mkdir()

        monkeypatch.setenv(DATASET_MOUNT_PATH_ENV, str(mount_dir))
        monkeypatch.delenv(DATASET_MOUNT_PATHS_ENV, raising=False)

        result = resolve_dataset_mount_paths()
        for p in result:
            assert os.path.isabs(p), f"Expected absolute path, got: {p}"

    def test_empty_env_var_ignored(self, monkeypatch):
        """An empty DOMINO_DATASET_MOUNT_PATH should behave as if unset."""
        monkeypatch.setenv(DATASET_MOUNT_PATH_ENV, "")
        monkeypatch.delenv(DATASET_MOUNT_PATHS_ENV, raising=False)

        # Empty string from env should not produce explicit_paths,
        # so function falls back to defaults.
        result = resolve_dataset_mount_paths()
        # The result should come from defaults (or be empty if defaults don't exist)
        # Either way, it should not crash.
        assert isinstance(result, list)

    def test_preserves_order_of_env_paths(self, tmp_path, monkeypatch):
        """Paths should appear in the order they were specified."""
        dir_a = tmp_path / "first"
        dir_b = tmp_path / "second"
        dir_c = tmp_path / "third"
        dir_a.mkdir()
        dir_b.mkdir()
        dir_c.mkdir()

        monkeypatch.setenv(DATASET_MOUNT_PATH_ENV, f"{dir_a},{dir_b},{dir_c}")
        monkeypatch.delenv(DATASET_MOUNT_PATHS_ENV, raising=False)

        result = resolve_dataset_mount_paths()
        assert result == [
            os.path.abspath(str(dir_a)),
            os.path.abspath(str(dir_b)),
            os.path.abspath(str(dir_c)),
        ]
