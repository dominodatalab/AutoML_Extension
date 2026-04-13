"""Tests for export route helpers."""

from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from app.api.routes.export import _resolve_notebook_data_path


@pytest.mark.asyncio
async def test_resolve_notebook_data_path_builds_dataset_mount_path():
    job = SimpleNamespace(
        id="job-domino",
        data_source="domino_dataset",
        file_path="iris.csv",
        dataset_id="ds-123",
        project_id="proj-123",
    )
    dataset_manager = MagicMock()
    dataset_manager.get_dataset_path = AsyncMock(return_value="/domino/datasets/local/quick-start")

    with patch("app.api.routes.export.DominoDatasetManager", return_value=dataset_manager):
        result = await _resolve_notebook_data_path(job)

    assert result == "/domino/datasets/local/quick-start/iris.csv"
    dataset_manager.get_dataset_path.assert_awaited_once_with("ds-123")


@pytest.mark.asyncio
async def test_resolve_notebook_data_path_returns_none_without_dataset_id():
    job = SimpleNamespace(
        id="job-missing-dataset",
        data_source="uploaded_file",
        file_path="/tmp/train.csv",
        dataset_id=None,
        project_id="proj-123",
    )

    with patch("app.api.routes.export.DominoDatasetManager") as dataset_manager_cls:
        result = await _resolve_notebook_data_path(job)

    assert result is None
    dataset_manager_cls.assert_not_called()


@pytest.mark.asyncio
async def test_resolve_notebook_data_path_returns_none_without_file_path():
    job = SimpleNamespace(
        id="job-missing-file",
        data_source="domino_dataset",
        file_path=None,
        dataset_id="ds-123",
        project_id="proj-123",
    )

    with patch("app.api.routes.export.DominoDatasetManager") as dataset_manager_cls:
        result = await _resolve_notebook_data_path(job)

    assert result is None
    dataset_manager_cls.assert_not_called()


@pytest.mark.asyncio
async def test_resolve_notebook_data_path_returns_none_without_project_id():
    job = SimpleNamespace(
        id="job-missing-project",
        data_source="domino_dataset",
        file_path="iris.csv",
        dataset_id="ds-123",
        project_id=None,
    )

    with patch("app.api.routes.export.DominoDatasetManager") as dataset_manager_cls:
        result = await _resolve_notebook_data_path(job)

    assert result is None
    dataset_manager_cls.assert_not_called()
