"""Tests for export route helpers."""

from types import SimpleNamespace
from contextlib import contextmanager
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from app.api.routes.export import _resolve_notebook_data_path
from app.core.context.auth import set_request_auth_header
from app.db.models import JobStatus

@contextmanager
def _mock_infra():
    """Patch Domino-dependent services so job API tests run without a live Domino environment."""
    set_request_auth_header("Bearer test-token")
    try:
            yield
    finally:
        set_request_auth_header(None)

@pytest.mark.asyncio
async def test_export_notebook(app_client, db_session, make_job):
    dataset_id = "dataset_id"
    job = make_job(
        status=JobStatus.COMPLETED,
        dataset_id=dataset_id,
        domino_job_id="domino-run-123",
        project_id="proj-123",
        file_path="iris.csv",
        model_path=None,
    )
    db_session.add(job)
    await db_session.commit()

    fake_ds_manager = SimpleNamespace(get_dataset_path=AsyncMock(return_value="myfakepath"))
    expected_notebook = {"cells": []}

    with (
        _mock_infra(),
        patch("app.api.routes.export.get_job_or_404", new=AsyncMock(return_value=job)),
        patch("app.api.routes.export.DominoDatasetManager", return_value=fake_ds_manager),
        patch("app.api.routes.export.generate_tabular_notebook", return_value=expected_notebook) as generate_notebook,
    ):
        response = await app_client.post(
            "/svc/v1/export/notebook",
            json={"job_id": job.id},
        )

    assert response.status_code == 200
    assert response.json() == {
        "success": True,
        "filename": "test-job_automl.ipynb",
        "notebook": expected_notebook,
    }
    fake_ds_manager.get_dataset_path.assert_awaited_once_with(dataset_id)
    generate_notebook.assert_called_once_with(job, data_path="myfakepath/iris.csv")

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
