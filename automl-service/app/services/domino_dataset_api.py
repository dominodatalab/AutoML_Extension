"""Helpers for Domino Dataset RW listing APIs."""

import logging
from typing import Optional

from app.core.domino_http import domino_request, resolve_domino_nucleus_host

logger = logging.getLogger(__name__)

_DEFAULT_PAGE_SIZE = 50


def _preferred_dataset_api_base_url() -> Optional[str]:
    """Prefer the direct Domino host over the local proxy for dataset listing."""
    return resolve_domino_nucleus_host()


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


async def _list_project_datasets_v2(
    project_id: str,
    *,
    page_size: int = _DEFAULT_PAGE_SIZE,
) -> list[dict]:
    datasets: list[dict] = []
    offset = 0

    while True:
        resp = await domino_request(
            "GET",
            "/api/datasetrw/v2/datasets",
            params={
                "projectIdsToInclude": project_id,
                "offset": offset,
                "limit": page_size,
            },
            base_url=_preferred_dataset_api_base_url(),
            # Fail fast here so we can fall back to the public v1 endpoint.
            max_retries=0,
        )
        items = extract_dataset_list(resp.json())
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
        resp = await domino_request(
            "GET",
            "/api/datasetrw/v1/datasets",
            params={
                "projectId": project_id,
                "offset": offset,
                "limit": page_size,
            },
            base_url=_preferred_dataset_api_base_url(),
        )
        items = extract_dataset_list(resp.json())
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
