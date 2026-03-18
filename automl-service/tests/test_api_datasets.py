"""Tests for dataset API route project scoping."""

import pytest


@pytest.mark.asyncio
async def test_svcdatasets_uses_project_id_from_query_param(app_client, monkeypatch):
    captured: dict[str, object] = {}

    async def fake_list_datasets_response(dataset_manager, project_id=None, include_files=True):
        captured["dataset_manager"] = dataset_manager
        captured["project_id"] = project_id
        captured["include_files"] = include_files
        return {"datasets": [], "total": 0}

    sentinel_manager = object()
    monkeypatch.setenv("DOMINO_PROJECT_ID", "app-project")
    monkeypatch.setattr(
        "app.api.compat.custom_datasets.get_dataset_manager",
        lambda: sentinel_manager,
    )
    monkeypatch.setattr(
        "app.api.compat.custom_datasets.list_datasets_response",
        fake_list_datasets_response,
    )

    response = await app_client.get(
        "/svcdatasets",
        params={"projectId": "target-project", "include_files": "false"},
    )

    assert response.status_code == 200, response.text
    assert response.json() == {"datasets": [], "total": 0}
    assert captured == {
        "dataset_manager": sentinel_manager,
        "project_id": "target-project",
        "include_files": False,
    }
