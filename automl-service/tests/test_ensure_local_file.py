"""Tests for app.core.utils.ensure_local_file.

Covers:
- File exists locally — returned as-is
- File found via remap_shared_path — remapped path returned
- Dataset mount path pattern — downloads via API and caches
- Cache hit — skips re-download
- No project_id — returns original path
- Non-matching path pattern — returns original path
"""

import os
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from app.core.utils import ensure_local_file, _DATASET_MOUNT_RE


# ---------------------------------------------------------------------------
# Regex pattern tests
# ---------------------------------------------------------------------------


class TestDatasetMountRegex:

    def test_matches_standard_path(self):
        m = _DATASET_MOUNT_RE.match("/domino/datasets/local/automl-extension/uploads/file.csv")
        assert m is not None
        assert m.group("dataset_name") == "automl-extension"
        assert m.group("relative") == "uploads/file.csv"

    def test_matches_nested_path(self):
        m = _DATASET_MOUNT_RE.match("/domino/datasets/local/my-dataset/a/b/c/file.parquet")
        assert m is not None
        assert m.group("dataset_name") == "my-dataset"
        assert m.group("relative") == "a/b/c/file.parquet"

    def test_no_match_for_other_paths(self):
        assert _DATASET_MOUNT_RE.match("/mnt/data/automl-extension/uploads/file.csv") is None

    def test_no_match_without_relative(self):
        assert _DATASET_MOUNT_RE.match("/domino/datasets/local/automl-extension/") is None
        # Must have content after dataset_name/
        m = _DATASET_MOUNT_RE.match("/domino/datasets/local/automl-extension/f")
        assert m is not None


# ---------------------------------------------------------------------------
# ensure_local_file — file exists locally
# ---------------------------------------------------------------------------


class TestEnsureLocalFileExists:

    @pytest.mark.asyncio
    async def test_returns_existing_file_as_is(self, tmp_path):
        f = tmp_path / "data.csv"
        f.write_text("a,b\n1,2\n")
        result = await ensure_local_file(str(f))
        assert result == str(f)

    @pytest.mark.asyncio
    async def test_returns_existing_file_without_project_id(self, tmp_path):
        f = tmp_path / "data.csv"
        f.write_text("a,b\n1,2\n")
        result = await ensure_local_file(str(f), project_id=None)
        assert result == str(f)


# ---------------------------------------------------------------------------
# ensure_local_file — remap_shared_path
# ---------------------------------------------------------------------------


class TestEnsureLocalFileRemap:

    @pytest.mark.asyncio
    async def test_uses_remapped_path_when_original_missing(self, tmp_path):
        """When original path doesn't exist but remap finds an alternative."""
        remapped = str(tmp_path / "remapped.csv")
        with open(remapped, "w") as f:
            f.write("a,b\n1,2\n")

        with patch("app.core.utils.remap_shared_path", return_value=remapped):
            result = await ensure_local_file("/nonexistent/path.csv")

        assert result == remapped


# ---------------------------------------------------------------------------
# ensure_local_file — downloads from dataset API
# ---------------------------------------------------------------------------


class TestEnsureLocalFileDownload:

    @pytest.mark.asyncio
    async def test_downloads_when_mount_path_missing(self, tmp_path, monkeypatch):
        """When path matches dataset pattern and file doesn't exist, downloads it."""
        file_path = "/domino/datasets/local/automl-extension/uploads/train.csv"

        mock_info = MagicMock()
        mock_info.dataset_id = "ds-abc-123"

        mock_resolver = MagicMock()
        mock_resolver.get_dataset_info = AsyncMock(return_value=mock_info)
        mock_resolver.download_file = AsyncMock(return_value=str(tmp_path / "cached.csv"))

        # Mock settings to use tmp_path as temp_path
        mock_settings = MagicMock()
        mock_settings.temp_path = str(tmp_path)

        with patch("app.core.utils.remap_shared_path", return_value=file_path), \
             patch("app.services.storage_resolver.get_storage_resolver", return_value=mock_resolver), \
             patch("app.config.get_settings", return_value=mock_settings):
            result = await ensure_local_file(file_path, project_id="proj-1")

        mock_resolver.download_file.assert_called_once()
        call_args = mock_resolver.download_file.call_args
        assert call_args[0][0] == "ds-abc-123"
        assert call_args[0][1] == "uploads/train.csv"

    @pytest.mark.asyncio
    async def test_uses_cache_when_file_already_downloaded(self, tmp_path, monkeypatch):
        """When cached file exists with non-zero size, skip download."""
        file_path = "/domino/datasets/local/automl-extension/uploads/train.csv"

        mock_info = MagicMock()
        mock_info.dataset_id = "ds-abc-123"

        mock_resolver = MagicMock()
        mock_resolver.get_dataset_info = AsyncMock(return_value=mock_info)
        mock_resolver.download_file = AsyncMock()

        mock_settings = MagicMock()
        mock_settings.temp_path = str(tmp_path)

        with patch("app.core.utils.remap_shared_path", return_value=file_path), \
             patch("app.services.storage_resolver.get_storage_resolver", return_value=mock_resolver), \
             patch("app.config.get_settings", return_value=mock_settings):

            # First call — will attempt download (mock returns the dest path)
            # We need to create the cached file to simulate previous download
            # Run once to figure out where the cache path would be
            result1 = await ensure_local_file(file_path, project_id="proj-1")

            # Create the file at the expected cache location
            os.makedirs(os.path.dirname(result1), exist_ok=True)
            with open(result1, "w") as f:
                f.write("cached data")

            mock_resolver.download_file.reset_mock()

            # Second call — should use cache
            result2 = await ensure_local_file(file_path, project_id="proj-1")

        assert result2 == result1
        mock_resolver.download_file.assert_not_called()

    @pytest.mark.asyncio
    async def test_returns_original_when_no_project_id(self):
        """Without project_id, cannot download — returns original path."""
        file_path = "/domino/datasets/local/automl-extension/uploads/train.csv"
        result = await ensure_local_file(file_path, project_id=None)
        assert result == file_path

    @pytest.mark.asyncio
    async def test_returns_original_for_non_dataset_path(self):
        """Non-matching paths are returned as-is."""
        file_path = "/some/random/path/data.csv"
        result = await ensure_local_file(file_path, project_id="proj-1")
        assert result == file_path

    @pytest.mark.asyncio
    async def test_falls_back_to_resolve_or_create(self, tmp_path):
        """When get_dataset_info returns None, tries _resolve_or_create."""
        file_path = "/domino/datasets/local/automl-extension/uploads/train.csv"

        mock_info = MagicMock()
        mock_info.dataset_id = "ds-new-123"

        mock_resolver = MagicMock()
        mock_resolver.get_dataset_info = AsyncMock(return_value=None)
        mock_resolver._resolve_or_create = AsyncMock(return_value=mock_info)
        mock_resolver.download_file = AsyncMock(return_value=str(tmp_path / "cached.csv"))

        mock_settings = MagicMock()
        mock_settings.temp_path = str(tmp_path)

        with patch("app.core.utils.remap_shared_path", return_value=file_path), \
             patch("app.services.storage_resolver.get_storage_resolver", return_value=mock_resolver), \
             patch("app.config.get_settings", return_value=mock_settings):
            result = await ensure_local_file(file_path, project_id="proj-1")

        mock_resolver._resolve_or_create.assert_called_once_with("proj-1")
        mock_resolver.download_file.assert_called_once()

    @pytest.mark.asyncio
    async def test_returns_original_when_resolve_fails(self):
        """When both get_dataset_info and _resolve_or_create fail, returns original."""
        file_path = "/domino/datasets/local/automl-extension/uploads/train.csv"

        mock_resolver = MagicMock()
        mock_resolver.get_dataset_info = AsyncMock(return_value=None)
        mock_resolver._resolve_or_create = AsyncMock(side_effect=RuntimeError("fail"))

        with patch("app.core.utils.remap_shared_path", return_value=file_path), \
             patch("app.services.storage_resolver.get_storage_resolver", return_value=mock_resolver):
            result = await ensure_local_file(file_path, project_id="proj-1")

        assert result == file_path

    @pytest.mark.asyncio
    async def test_returns_original_when_download_fails(self, tmp_path):
        """When download_file raises (no read API), returns original path."""
        file_path = "/domino/datasets/local/automl-extension/uploads/train.csv"

        mock_info = MagicMock()
        mock_info.dataset_id = "ds-abc-123"

        mock_resolver = MagicMock()
        mock_resolver.get_dataset_info = AsyncMock(return_value=mock_info)
        mock_resolver.download_file = AsyncMock(
            side_effect=RuntimeError("No download API")
        )

        mock_settings = MagicMock()
        mock_settings.temp_path = str(tmp_path)

        with patch("app.core.utils.remap_shared_path", return_value=file_path), \
             patch("app.services.storage_resolver.get_storage_resolver", return_value=mock_resolver), \
             patch("app.config.get_settings", return_value=mock_settings):
            result = await ensure_local_file(file_path, project_id="proj-1")

        assert result == file_path
