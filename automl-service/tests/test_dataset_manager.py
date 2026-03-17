"""Tests for app.core.dataset_manager."""

from unittest.mock import patch

import pytest

from app.core.dataset_manager import DominoDatasetManager


class TestGetDatasetFilePath:
    """Exercise file selection behavior for mounted Domino datasets."""

    @pytest.mark.asyncio
    async def test_returns_requested_file_when_present(self, tmp_path):
        dataset_dir = tmp_path / "sales-data"
        dataset_dir.mkdir()
        first_file = dataset_dir / "first.csv"
        requested_file = dataset_dir / "selected.csv"
        first_file.write_text("a,b\n1,2\n")
        requested_file.write_text("target,feature\n1,2\n")

        manager = DominoDatasetManager()

        with patch.object(manager, "_resolve_dataset_mount_paths", return_value=[str(tmp_path)]):
            resolved = await manager.get_dataset_file_path(
                "domino:sales-data",
                file_name="selected.csv",
            )

        assert resolved == str(requested_file)

    @pytest.mark.asyncio
    async def test_does_not_fallback_to_other_file_when_requested_file_missing(self, tmp_path):
        dataset_dir = tmp_path / "sales-data"
        dataset_dir.mkdir()
        (dataset_dir / "first.csv").write_text("a,b\n1,2\n")

        manager = DominoDatasetManager()

        with patch.object(manager, "_resolve_dataset_mount_paths", return_value=[str(tmp_path)]):
            with pytest.raises(FileNotFoundError) as exc_info:
                await manager.get_dataset_file_path(
                    "domino:sales-data",
                    file_name="selected.csv",
                )

        assert "selected.csv" in str(exc_info.value)
