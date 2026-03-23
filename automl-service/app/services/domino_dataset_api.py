"""Helpers for Domino Dataset RW listing APIs.

Uses the generated Domino Public API client for typed, structured access
to the Dataset RW v1/v2 endpoints.
"""

from __future__ import annotations

import logging

from app.api.generated.domino_public_api_client.api.dataset_rw import (
    get_datasets as get_datasets_v1,
    get_datasets_v2,
)
from app.api.generated.domino_public_api_client.models.paginated_dataset_rw_envelope_v1 import (
    PaginatedDatasetRwEnvelopeV1,
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
    envelope: PaginatedDatasetRwEnvelopeV1 | PaginatedDatasetRwEnvelopeV2,
) -> list[dict]:
    """Convert a typed paginated envelope into a flat list of dataset dicts.

    For v2 envelopes, each item is a ``DatasetRwInfoDtoV1`` that wraps the
    actual dataset under a ``dataset`` attribute.  We unwrap it so callers
    always receive flat dataset dicts (matching ``extract_dataset_list``
    semantics).
    """
    result: list[dict] = []
    for ds in envelope.datasets:
        d = ds.to_dict()
        # v2 items wrap the dataset inside a "dataset" key — unwrap it.
        if "dataset" in d and isinstance(d["dataset"], dict):
            result.append(d["dataset"])
        else:
            result.append(d)
    return result


async def _list_project_datasets_v2(
    project_id: str,
    *,
    page_size: int = _DEFAULT_PAGE_SIZE,
) -> list[dict]:
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


async def _list_project_datasets_v1(
    project_id: str,
    *,
    page_size: int = _DEFAULT_PAGE_SIZE,
) -> list[dict]:
    datasets: list[dict] = []
    offset = 0

    while True:
        client = get_domino_public_api_client_sync()
        result = get_datasets_v1.sync(
            client=client,
            project_id=project_id,
            offset=offset,
            limit=page_size,
        )

        if not isinstance(result, PaginatedDatasetRwEnvelopeV1):
            raise RuntimeError(
                f"Unexpected v1 dataset list response: {type(result).__name__}"
            )

        items = _envelope_to_dataset_dicts(result)
        if not items:
            break

        datasets.extend(items)
        if len(items) < page_size:
            break
        offset += page_size

    return datasets


async def list_project_datasets(
    project_id: str,
    *,
    page_size: int = _DEFAULT_PAGE_SIZE,
) -> list[dict]:
    """List datasets for a project, falling back from v2 to v1 when needed."""
    try:
        return await _list_project_datasets_v2(project_id, page_size=page_size)
    except Exception:
        logger.warning(
            "Domino Dataset RW v2 listing failed for project %s; falling back to v1",
            project_id,
            exc_info=True,
        )
        return await _list_project_datasets_v1(project_id, page_size=page_size)
