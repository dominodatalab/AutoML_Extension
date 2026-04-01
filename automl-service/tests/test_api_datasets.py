"""Tests for dataset API endpoints."""

import pytest


@pytest.mark.asyncio
async def test_preview_dataset_file_happy_path(app_client, monkeypatch):
    """POST /svc/v1/datasets/preview returns a preview for a dataset file."""
    calls = []

    async def fake_fetch(dataset_id: str, file_path: str) -> bytes:
        calls.append((dataset_id, file_path))
        return b"id,target\n1,0\n"

    monkeypatch.setattr(
        "app.services.dataset_service.dataset_file_bytes.fetch",
        fake_fetch,
    )

    response = await app_client.post(
        "/svc/v1/datasets/preview",
        json={
            "dataset_id": "ds-123",
            "file_path": "folder/train.csv",
            "limit": 25,
            "offset": 0,
        },
    )

    assert response.status_code == 200
    assert calls == [("ds-123", "folder/train.csv")]
    assert response.json() == {
        "dataset_id": "ds-123",
        "file_path": "folder/train.csv",
        "file_name": "train.csv",
        "columns": ["id", "target"],
        "rows": [{"id": 1, "target": 0}],
        "total_rows": 1,
        "preview_rows": 1,
        "dtypes": {"id": "int64", "target": "int64"},
    }
