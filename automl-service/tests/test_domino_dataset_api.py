"""Tests for Dataset RW list API fallbacks."""

from unittest.mock import AsyncMock, MagicMock, patch

import httpx
import pytest

from app.services.domino_dataset_api import extract_dataset_list, list_project_datasets


class TestExtractDatasetList:
    def test_unwraps_v2_items(self):
        result = extract_dataset_list(
            {
                "items": [
                    {"dataset": {"datasetId": "ds-1", "datasetName": "wrapped"}},
                ]
            }
        )

        assert result == [{"datasetId": "ds-1", "datasetName": "wrapped"}]


@pytest.mark.asyncio
async def test_list_project_datasets_falls_back_to_v1_when_v2_fails():
    v2_error = httpx.RemoteProtocolError("Server disconnected without sending a response.")
    v1_response = MagicMock()
    v1_response.json.return_value = {
        "datasets": [
            {"datasetId": "ds-1", "datasetName": "automl_shared_db"},
        ]
    }

    with patch(
        "app.services.domino_dataset_api.domino_request",
        new_callable=AsyncMock,
        side_effect=[v2_error, v1_response],
    ) as mock_request:
        datasets = await list_project_datasets("proj-123")

    assert datasets == [{"datasetId": "ds-1", "datasetName": "automl_shared_db"}]
    assert mock_request.await_count == 2
    # v2 attempt
    first = mock_request.await_args_list[0]
    assert first.args == ("GET", "/api/datasetrw/v2/datasets")
    # v1 fallback
    second = mock_request.await_args_list[1]
    assert second.args == ("GET", "/api/datasetrw/v1/datasets")


@pytest.mark.asyncio
async def test_list_project_datasets_returns_v2_results():
    response = MagicMock()
    response.json.return_value = {"datasets": []}

    with patch(
        "app.services.domino_dataset_api.domino_request",
        new_callable=AsyncMock,
        return_value=response,
    ) as mock_request:
        await list_project_datasets("proj-123")

    # Should use proxy (no base_url override)
    first = mock_request.await_args_list[0]
    assert first.args == ("GET", "/api/datasetrw/v2/datasets")
    assert "base_url" not in first.kwargs
