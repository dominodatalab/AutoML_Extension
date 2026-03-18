"""Tests for Dataset RW list API fallbacks."""

from unittest.mock import AsyncMock, MagicMock, call, patch

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
    ) as domino_request:
        datasets = await list_project_datasets("proj-123")

    assert datasets == [{"datasetId": "ds-1", "datasetName": "automl_shared_db"}]
    assert domino_request.await_args_list == [
        call(
            "GET",
            "/api/datasetrw/v2/datasets",
            params={"projectIdsToInclude": "proj-123", "offset": 0, "limit": 50},
            base_url=None,
            max_retries=0,
        ),
        call(
            "GET",
            "/api/datasetrw/v1/datasets",
            params={"projectId": "proj-123", "offset": 0, "limit": 50},
            base_url=None,
        ),
    ]


@pytest.mark.asyncio
async def test_list_project_datasets_prefers_direct_domino_host():
    response = MagicMock()
    response.json.return_value = {"datasets": []}

    with patch(
        "app.services.domino_dataset_api.resolve_domino_nucleus_host",
        return_value="https://extensions-dev.engineering-sandbox.domino.tech",
    ), patch(
        "app.services.domino_dataset_api.domino_request",
        new_callable=AsyncMock,
        return_value=response,
    ) as domino_request:
        await list_project_datasets("proj-123")

    first_call = domino_request.await_args_list[0]
    assert first_call.kwargs["base_url"] == "https://extensions-dev.engineering-sandbox.domino.tech"
