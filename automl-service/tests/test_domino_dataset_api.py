"""Tests for Dataset RW list API fallbacks using generated client."""

from unittest.mock import MagicMock, patch

import pytest

from app.api.generated.domino_public_api_client.models.paginated_dataset_rw_envelope_v1 import (
    PaginatedDatasetRwEnvelopeV1,
)
from app.api.generated.domino_public_api_client.models.paginated_dataset_rw_envelope_v2 import (
    PaginatedDatasetRwEnvelopeV2,
)
from app.services.domino_dataset_api import extract_dataset_list, list_project_datasets


def _make_v1_envelope(datasets_dicts: list[dict]) -> PaginatedDatasetRwEnvelopeV1:
    """Build a PaginatedDatasetRwEnvelopeV1 from raw dataset dicts."""
    return PaginatedDatasetRwEnvelopeV1.from_dict(
        {
            "datasets": datasets_dicts,
            "metadata": {
                "offset": 0,
                "limit": 50,
                "totalCount": len(datasets_dicts),
                "notices": [],
                "requestId": "test-req",
            },
        }
    )


def _make_v2_envelope(datasets_dicts: list[dict]) -> PaginatedDatasetRwEnvelopeV2:
    """Build a PaginatedDatasetRwEnvelopeV2 from raw v2 item dicts.

    Each item should be a ``{"dataset": {...}}`` wrapper.
    """
    return PaginatedDatasetRwEnvelopeV2.from_dict(
        {
            "datasets": datasets_dicts,
            "metadata": {
                "offset": 0,
                "limit": 50,
                "totalCount": len(datasets_dicts),
                "notices": [],
                "requestId": "test-req",
            },
        }
    )


def _minimal_v1_dataset(*, id: str = "ds-1", name: str = "test") -> dict:
    """Return a minimal v1 dataset dict with all required fields."""
    return {
        "id": id,
        "name": name,
        "createdAt": "2024-01-01T00:00:00Z",
        "snapshotIds": [],
        "tags": {},
    }


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
    v1_envelope = _make_v1_envelope(
        [_minimal_v1_dataset(id="ds-1", name="automl_shared_db")]
    )

    mock_client = MagicMock()

    with (
        patch(
            "app.services.domino_dataset_api.get_domino_public_api_client_sync",
            return_value=mock_client,
        ),
        patch(
            "app.services.domino_dataset_api.get_datasets_v2.sync",
            side_effect=RuntimeError("v2 unavailable"),
        ) as mock_v2,
        patch(
            "app.services.domino_dataset_api.get_datasets_v1.sync",
            return_value=v1_envelope,
        ) as mock_v1,
    ):
        datasets = await list_project_datasets("proj-123")

    # v2 was attempted
    mock_v2.assert_called_once()
    # v1 fallback succeeded
    mock_v1.assert_called_once()
    assert mock_v1.call_args.kwargs["client"] is mock_client
    assert mock_v1.call_args.kwargs["project_id"] == "proj-123"

    assert len(datasets) == 1
    assert datasets[0]["id"] == "ds-1"
    assert datasets[0]["name"] == "automl_shared_db"


@pytest.mark.asyncio
async def test_list_project_datasets_returns_v2_results():
    v2_envelope = _make_v2_envelope(
        [{"dataset": _minimal_v1_dataset(id="ds-2", name="my_dataset")}]
    )

    mock_client = MagicMock()

    with (
        patch(
            "app.services.domino_dataset_api.get_domino_public_api_client_sync",
            return_value=mock_client,
        ),
        patch(
            "app.services.domino_dataset_api.get_datasets_v2.sync",
            return_value=v2_envelope,
        ) as mock_v2,
        patch(
            "app.services.domino_dataset_api.get_datasets_v1.sync",
        ) as mock_v1,
    ):
        datasets = await list_project_datasets("proj-123")

    mock_v2.assert_called_once()
    assert mock_v2.call_args.kwargs["client"] is mock_client
    assert mock_v2.call_args.kwargs["project_ids_to_include"] == ["proj-123"]

    # v1 should NOT have been called
    mock_v1.assert_not_called()

    # v2 items are unwrapped from the "dataset" wrapper
    assert len(datasets) == 1
    assert datasets[0]["id"] == "ds-2"
    assert datasets[0]["name"] == "my_dataset"


@pytest.mark.asyncio
async def test_list_project_datasets_paginates_v2():
    """Verify pagination loops until a short page is returned."""
    page1 = _make_v2_envelope(
        [{"dataset": _minimal_v1_dataset(id=f"ds-{i}")} for i in range(50)]
    )
    page2 = _make_v2_envelope(
        [{"dataset": _minimal_v1_dataset(id=f"ds-{i}")} for i in range(50, 60)]
    )

    mock_client = MagicMock()
    call_count = 0

    def v2_side_effect(**kwargs):
        nonlocal call_count
        call_count += 1
        if kwargs.get("offset", 0) == 0:
            return page1
        return page2

    with (
        patch(
            "app.services.domino_dataset_api.get_domino_public_api_client_sync",
            return_value=mock_client,
        ),
        patch(
            "app.services.domino_dataset_api.get_datasets_v2.sync",
            side_effect=v2_side_effect,
        ),
    ):
        datasets = await list_project_datasets("proj-123")

    assert len(datasets) == 60
    assert call_count == 2


@pytest.mark.asyncio
async def test_list_project_datasets_v2_non_success_raises():
    """Non-envelope v2 response (e.g. error model) triggers v1 fallback."""
    mock_client = MagicMock()
    error_model = MagicMock()  # Simulates a FailureEnvelopeV1 or 400 response

    v1_envelope = _make_v1_envelope(
        [_minimal_v1_dataset(id="ds-fallback")]
    )

    with (
        patch(
            "app.services.domino_dataset_api.get_domino_public_api_client_sync",
            return_value=mock_client,
        ),
        patch(
            "app.services.domino_dataset_api.get_datasets_v2.sync",
            return_value=error_model,
        ),
        patch(
            "app.services.domino_dataset_api.get_datasets_v1.sync",
            return_value=v1_envelope,
        ) as mock_v1,
    ):
        datasets = await list_project_datasets("proj-123")

    mock_v1.assert_called_once()
    assert len(datasets) == 1
    assert datasets[0]["id"] == "ds-fallback"
