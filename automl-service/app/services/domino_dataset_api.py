"""Helpers for Domino Dataset RW listing APIs.

Uses the generated Domino Public API client for typed, structured access
to the Dataset RW v2 endpoint.
"""

from __future__ import annotations

import logging

from app.api.generated.domino_public_api_client.api.dataset_rw import (
    get_datasets_v2,
)
from app.api.generated.domino_public_api_client.models.paginated_dataset_rw_envelope_v2 import (
    PaginatedDatasetRwEnvelopeV2,
)
from app.core.domino_http import get_domino_public_api_client_sync

logger = logging.getLogger(__name__)

_DEFAULT_PAGE_SIZE = 50


def extract_dataset_list(data: object) -> list[dict]:
    """Normalize Dataset RW list responses into a flat list of datasets."""
    if isinstance(data, list):
        items = data
    elif isinstance(data, dict):
        items = (
            data.get("items")
            or data.get("datasets")
            or data.get("data")
            or []
        )
    else:
        return []

    return [
        item.get("dataset", item) if isinstance(item, dict) and "dataset" in item else item
        for item in items
        if isinstance(item, dict)
    ]


def _envelope_to_dataset_dicts(
    envelope: PaginatedDatasetRwEnvelopeV2,
) -> list[dict]:
    """Convert a typed paginated envelope into a flat list of dataset dicts.

    V2 items wrap the actual dataset under a ``dataset`` key — unwrap it
    so callers always receive flat dataset dicts.
    """
    result: list[dict] = []
    for ds in envelope.datasets:
        d = ds.to_dict()
        if "dataset" in d and isinstance(d["dataset"], dict):
            result.append(d["dataset"])
        else:
            result.append(d)
    return result


async def list_project_datasets(
    project_id: str,
    *,
    page_size: int = _DEFAULT_PAGE_SIZE,
) -> list[dict]:
    """List datasets for a project using the v2 Dataset RW API."""
    datasets: list[dict] = []
    offset = 0

    while True:
        client = get_domino_public_api_client_sync()
        result = get_datasets_v2.sync(
            client=client,
            project_ids_to_include=[project_id],
            offset=offset,
            limit=page_size,
        )

        if not isinstance(result, PaginatedDatasetRwEnvelopeV2):
            raise RuntimeError(
                f"Unexpected v2 dataset list response: {type(result).__name__}"
            )

        items = _envelope_to_dataset_dicts(result)
        if not items:
            break

        datasets.extend(items)
        if len(items) < page_size:
            break
        offset += page_size

    return datasets
