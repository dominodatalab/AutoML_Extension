"""Tests for app.core.dataset_manager."""

from unittest.mock import AsyncMock, PropertyMock, patch

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


class TestApiDatasetSummaries:
    """Exercise lightweight dataset list behavior for Domino API datasets."""

    @pytest.mark.asyncio
    async def test_summary_mode_skips_snapshot_file_listing(self):
        manager = DominoDatasetManager()
        item = {
            "datasetId": "ds-123",
            "datasetName": "sales-data",
            "description": "Quarterly sales",
            "fileCount": 7,
            "sizeInBytes": 4096,
            "projectId": "proj-1",
            "readWriteSnapshotId": "snap-1",
        }

        with patch.object(
            manager,
            "_list_files_via_snapshot_api",
            new_callable=AsyncMock,
        ) as list_files:
            response = await manager._api_item_to_dataset_response(
                item,
                include_files=False,
            )

        assert response is not None
        assert response.id == "ds-123"
        assert response.file_count == 7
        assert response.size_bytes == 4096
        assert response.files == []
        list_files.assert_not_called()

    @pytest.mark.asyncio
    async def test_get_dataset_reuses_cached_summary_item(self):
        manager = DominoDatasetManager()
        manager._dataset_item_cache["ds-123"] = {
            "datasetId": "ds-123",
            "datasetName": "sales-data",
            "description": "Quarterly sales",
            "fileCount": 7,
            "sizeInBytes": 4096,
            "projectId": "proj-1",
            "readWriteSnapshotId": "snap-1",
        }

        with patch.object(
            type(manager.settings),
            "is_domino_environment",
            new_callable=PropertyMock,
            return_value=True,
        ), patch.object(
            manager,
            "_api_request",
            new_callable=AsyncMock,
        ) as api_request, patch.object(
            manager,
            "_list_files_via_snapshot_api",
            new_callable=AsyncMock,
            return_value=([], 0),
        ):
            response = await manager.get_dataset("ds-123", include_files=True)

        assert response is not None
        assert response.id == "ds-123"
        api_request.assert_not_called()
