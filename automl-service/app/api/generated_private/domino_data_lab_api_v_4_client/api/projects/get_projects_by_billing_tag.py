from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_projects_api_paginated_project_summary_results import (
    DominoProjectsApiPaginatedProjectSummaryResults,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    billing_tag: None | str | Unset = UNSET,
    offset: float | None | Unset = UNSET,
    page_size: float | None | Unset = UNSET,
    checkpoint_project_id: str | Unset = UNSET,
    name_filter: None | str | Unset = UNSET,
    sort_by: Any | Unset = UNSET,
    sort_order: Any | Unset = UNSET,
    missing_billing_tag_only: bool | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_billing_tag: None | str | Unset
    if isinstance(billing_tag, Unset):
        json_billing_tag = UNSET
    else:
        json_billing_tag = billing_tag
    params["billingTag"] = json_billing_tag

    json_offset: float | None | Unset
    if isinstance(offset, Unset):
        json_offset = UNSET
    else:
        json_offset = offset
    params["offset"] = json_offset

    json_page_size: float | None | Unset
    if isinstance(page_size, Unset):
        json_page_size = UNSET
    else:
        json_page_size = page_size
    params["pageSize"] = json_page_size

    params["checkpointProjectId"] = checkpoint_project_id

    json_name_filter: None | str | Unset
    if isinstance(name_filter, Unset):
        json_name_filter = UNSET
    else:
        json_name_filter = name_filter
    params["nameFilter"] = json_name_filter

    params["sortBy"] = sort_by

    params["sortOrder"] = sort_order

    json_missing_billing_tag_only: bool | None | Unset
    if isinstance(missing_billing_tag_only, Unset):
        json_missing_billing_tag_only = UNSET
    else:
        json_missing_billing_tag_only = missing_billing_tag_only
    params["missingBillingTagOnly"] = json_missing_billing_tag_only

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/billingtags/projects",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoProjectsApiPaginatedProjectSummaryResults | None:
    if response.status_code == 200:
        response_200 = DominoProjectsApiPaginatedProjectSummaryResults.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = DominoApiErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DominoApiErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = DominoApiErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DominoApiErrorResponse | DominoProjectsApiPaginatedProjectSummaryResults]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    billing_tag: None | str | Unset = UNSET,
    offset: float | None | Unset = UNSET,
    page_size: float | None | Unset = UNSET,
    checkpoint_project_id: str | Unset = UNSET,
    name_filter: None | str | Unset = UNSET,
    sort_by: Any | Unset = UNSET,
    sort_order: Any | Unset = UNSET,
    missing_billing_tag_only: bool | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoProjectsApiPaginatedProjectSummaryResults]:
    """get list of projects that are assigned a particular tag

    Args:
        billing_tag (None | str | Unset):
        offset (float | None | Unset):
        page_size (float | None | Unset):
        checkpoint_project_id (str | Unset):
        name_filter (None | str | Unset):
        sort_by (Any | Unset):
        sort_order (Any | Unset):
        missing_billing_tag_only (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectsApiPaginatedProjectSummaryResults]
    """

    kwargs = _get_kwargs(
        billing_tag=billing_tag,
        offset=offset,
        page_size=page_size,
        checkpoint_project_id=checkpoint_project_id,
        name_filter=name_filter,
        sort_by=sort_by,
        sort_order=sort_order,
        missing_billing_tag_only=missing_billing_tag_only,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    billing_tag: None | str | Unset = UNSET,
    offset: float | None | Unset = UNSET,
    page_size: float | None | Unset = UNSET,
    checkpoint_project_id: str | Unset = UNSET,
    name_filter: None | str | Unset = UNSET,
    sort_by: Any | Unset = UNSET,
    sort_order: Any | Unset = UNSET,
    missing_billing_tag_only: bool | None | Unset = UNSET,
) -> DominoApiErrorResponse | DominoProjectsApiPaginatedProjectSummaryResults | None:
    """get list of projects that are assigned a particular tag

    Args:
        billing_tag (None | str | Unset):
        offset (float | None | Unset):
        page_size (float | None | Unset):
        checkpoint_project_id (str | Unset):
        name_filter (None | str | Unset):
        sort_by (Any | Unset):
        sort_order (Any | Unset):
        missing_billing_tag_only (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectsApiPaginatedProjectSummaryResults
    """

    return sync_detailed(
        client=client,
        billing_tag=billing_tag,
        offset=offset,
        page_size=page_size,
        checkpoint_project_id=checkpoint_project_id,
        name_filter=name_filter,
        sort_by=sort_by,
        sort_order=sort_order,
        missing_billing_tag_only=missing_billing_tag_only,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    billing_tag: None | str | Unset = UNSET,
    offset: float | None | Unset = UNSET,
    page_size: float | None | Unset = UNSET,
    checkpoint_project_id: str | Unset = UNSET,
    name_filter: None | str | Unset = UNSET,
    sort_by: Any | Unset = UNSET,
    sort_order: Any | Unset = UNSET,
    missing_billing_tag_only: bool | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoProjectsApiPaginatedProjectSummaryResults]:
    """get list of projects that are assigned a particular tag

    Args:
        billing_tag (None | str | Unset):
        offset (float | None | Unset):
        page_size (float | None | Unset):
        checkpoint_project_id (str | Unset):
        name_filter (None | str | Unset):
        sort_by (Any | Unset):
        sort_order (Any | Unset):
        missing_billing_tag_only (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectsApiPaginatedProjectSummaryResults]
    """

    kwargs = _get_kwargs(
        billing_tag=billing_tag,
        offset=offset,
        page_size=page_size,
        checkpoint_project_id=checkpoint_project_id,
        name_filter=name_filter,
        sort_by=sort_by,
        sort_order=sort_order,
        missing_billing_tag_only=missing_billing_tag_only,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    billing_tag: None | str | Unset = UNSET,
    offset: float | None | Unset = UNSET,
    page_size: float | None | Unset = UNSET,
    checkpoint_project_id: str | Unset = UNSET,
    name_filter: None | str | Unset = UNSET,
    sort_by: Any | Unset = UNSET,
    sort_order: Any | Unset = UNSET,
    missing_billing_tag_only: bool | None | Unset = UNSET,
) -> DominoApiErrorResponse | DominoProjectsApiPaginatedProjectSummaryResults | None:
    """get list of projects that are assigned a particular tag

    Args:
        billing_tag (None | str | Unset):
        offset (float | None | Unset):
        page_size (float | None | Unset):
        checkpoint_project_id (str | Unset):
        name_filter (None | str | Unset):
        sort_by (Any | Unset):
        sort_order (Any | Unset):
        missing_billing_tag_only (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectsApiPaginatedProjectSummaryResults
    """

    return (
        await asyncio_detailed(
            client=client,
            billing_tag=billing_tag,
            offset=offset,
            page_size=page_size,
            checkpoint_project_id=checkpoint_project_id,
            name_filter=name_filter,
            sort_by=sort_by,
            sort_order=sort_order,
            missing_billing_tag_only=missing_billing_tag_only,
        )
    ).parsed
