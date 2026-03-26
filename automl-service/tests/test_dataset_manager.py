"""Tests for app.core.dataset_manager."""

from unittest.mock import AsyncMock, PropertyMock, patch

import pytest

from app.api.schemas.dataset import DatasetFileResponse
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
            DominoDatasetManager,
            "_fetch_dataset_details",
        ) as fetch_details, patch.object(
            manager,
            "_list_files_via_snapshot_api",
            new_callable=AsyncMock,
            return_value=([], 0),
        ):
            response = await manager.get_dataset("ds-123", include_files=True)

        assert response is not None
        assert response.id == "ds-123"
        fetch_details.assert_not_called()

    @pytest.mark.asyncio
    async def test_get_dataset_fetches_via_generated_client(self):
        manager = DominoDatasetManager()

        with patch.object(
            type(manager.settings),
            "is_domino_environment",
            new_callable=PropertyMock,
            return_value=True,
        ), patch.object(
            DominoDatasetManager,
            "_fetch_dataset_details",
            return_value={
                "id": "ds-123",
                "name": "sales-data",
                "description": "Quarterly sales",
                "fileCount": 7,
                "sizeInBytes": 4096,
                "projectId": "proj-1",
                "readWriteSnapshotId": "snap-1",
            },
        ):
            response = await manager.get_dataset("ds-123", include_files=False)

        assert response is not None
        assert response.id == "ds-123"
        assert response.file_count == 7
        assert response.size_bytes == 4096

    @pytest.mark.asyncio
    async def test_detail_listing_backfills_summary_cache(self):
        manager = DominoDatasetManager()
        item = {
            "datasetId": "ds-123",
            "datasetName": "sales-data",
            "description": "Quarterly sales",
            "projectId": "proj-1",
            "readWriteSnapshotId": "snap-1",
        }

        with patch.object(
            manager,
            "_list_files_via_snapshot_api",
            new_callable=AsyncMock,
            return_value=(
                [
                    DatasetFileResponse(
                        name="uploads/file.csv",
                        path="/tmp/uploads/file.csv",
                        size=11,
                    )
                ],
                11,
            ),
        ):
            response = await manager._api_item_to_dataset_response(
                item,
                include_files=True,
            )

        assert response is not None
        assert response.file_count == 1
        assert response.size_bytes == 11
        assert manager._dataset_item_cache["ds-123"]["fileCount"] == 1
        assert manager._dataset_item_cache["ds-123"]["sizeInBytes"] == 11


class TestSnapshotTraversal:
    """Verify recursive snapshot traversal across multiple directories."""

    @pytest.mark.asyncio
    async def test_list_files_via_snapshot_api_recurses_all_directories(self):
        manager = DominoDatasetManager()

        def _entries_for(snapshot_id: str, path: str = ""):
            assert snapshot_id == "snap-123"
            return {
                "": [
                    {"fileName": "uploads", "isDirectory": True, "sizeInBytes": 0},
                    {"fileName": "temp", "isDirectory": True, "sizeInBytes": 0},
                ],
                "uploads": [
                    {"fileName": "uploads/top.csv", "isDirectory": False, "sizeInBytes": 11},
                    {"fileName": "uploads/nested", "isDirectory": True, "sizeInBytes": 0},
                ],
                "uploads/nested": [
                    {
                        "fileName": "uploads/nested/model.parquet",
                        "isDirectory": False,
                        "sizeInBytes": 22,
                    },
                ],
                "temp": [
                    {"fileName": "temp/dataset_cache", "isDirectory": True, "sizeInBytes": 0},
                ],
                "temp/dataset_cache": [
                    {
                        "fileName": "temp/dataset_cache/panel.csv",
                        "isDirectory": False,
                        "sizeInBytes": 33,
                    },
                    {
                        "fileName": "temp/dataset_cache/notes.txt",
                        "isDirectory": False,
                        "sizeInBytes": 44,
                    },
                ],
            }[path]

        mock_resolver = AsyncMock()
        mock_resolver.list_snapshot_files.side_effect = _entries_for

        with patch(
            "app.services.storage_resolver.get_storage_resolver",
            return_value=mock_resolver,
        ), patch(
            "app.core.domino_project_type.detect_project_type",
        ) as detect_project_type:
            from app.core.domino_project_type import DominoProjectType

            detect_project_type.return_value = DominoProjectType.DFS
            files, total_size = await manager._list_files_via_snapshot_api(
                "snap-123",
                "automl_shared_db",
            )

        assert [f.name for f in files] == [
            "uploads/top.csv",
            "uploads/nested/model.parquet",
            "temp/dataset_cache/panel.csv",
        ]
        assert total_size == 66
        assert all(
            f.path.startswith("/domino/datasets/local/automl_shared_db/")
            for f in files
        )


class TestProjectScopedFallbacks:
    """Protect against showing app-project files for target-project requests."""

    @pytest.mark.asyncio
    async def test_cross_project_api_failure_does_not_fallback_to_local_scan(self, monkeypatch):
        manager = DominoDatasetManager()
        monkeypatch.setenv("DOMINO_PROJECT_ID", "app-project")

        with patch.object(
            type(manager.settings),
            "is_domino_environment",
            new_callable=PropertyMock,
            return_value=True,
        ), patch(
            "app.core.dataset_manager.list_project_datasets",
            new_callable=AsyncMock,
            side_effect=RuntimeError("boom"),
        ), patch.object(
            manager,
            "_list_local_datasets",
            new_callable=AsyncMock,
        ) as list_local:
            with pytest.raises(RuntimeError, match="target project target-project"):
                await manager.list_datasets(project_id="target-project", include_files=False)

        list_local.assert_not_called()

    @pytest.mark.asyncio
    async def test_app_project_api_failure_can_fallback_to_local_scan(self, monkeypatch):
        manager = DominoDatasetManager()
        monkeypatch.setenv("DOMINO_PROJECT_ID", "app-project")

        local_dataset = object()

        with patch.object(
            type(manager.settings),
            "is_domino_environment",
            new_callable=PropertyMock,
            return_value=True,
        ), patch(
            "app.core.dataset_manager.list_project_datasets",
            new_callable=AsyncMock,
            side_effect=RuntimeError("boom"),
        ), patch.object(
            manager,
            "_list_local_datasets",
            new_callable=AsyncMock,
            return_value=[local_dataset],
        ) as list_local:
            datasets = await manager.list_datasets(project_id="app-project", include_files=False)

        assert datasets == [local_dataset]
        list_local.assert_awaited_once()
