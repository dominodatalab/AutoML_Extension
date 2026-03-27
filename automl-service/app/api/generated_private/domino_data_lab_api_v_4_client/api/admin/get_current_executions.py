from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_admin_interface_execution_overviews_with_total_count import (
    DominoAdminInterfaceExecutionOverviewsWithTotalCount,
)
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.get_current_executions_sort_by import GetCurrentExecutionsSortBy
from ...models.get_current_executions_sort_order import GetCurrentExecutionsSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    offset: int | None | Unset = 0,
    page_size: int | None | Unset = 50,
    sort_by: GetCurrentExecutionsSortBy | Unset = GetCurrentExecutionsSortBy.EXECUTIONID,
    sort_order: GetCurrentExecutionsSortOrder | Unset = GetCurrentExecutionsSortOrder.ASC,
    search_query: None | str | Unset = UNSET,
    search_columns: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_offset: int | None | Unset
    if isinstance(offset, Unset):
        json_offset = UNSET
    else:
        json_offset = offset
    params["offset"] = json_offset

    json_page_size: int | None | Unset
    if isinstance(page_size, Unset):
        json_page_size = UNSET
    else:
        json_page_size = page_size
    params["pageSize"] = json_page_size

    json_sort_by: str | Unset = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value

    params["sortBy"] = json_sort_by

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sortOrder"] = json_sort_order

    json_search_query: None | str | Unset
    if isinstance(search_query, Unset):
        json_search_query = UNSET
    else:
        json_search_query = search_query
    params["searchQuery"] = json_search_query

    json_search_columns: None | str | Unset
    if isinstance(search_columns, Unset):
        json_search_columns = UNSET
    else:
        json_search_columns = search_columns
    params["searchColumns"] = json_search_columns

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/admin/executions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoAdminInterfaceExecutionOverviewsWithTotalCount | DominoApiErrorResponse | None:
    if response.status_code == 200:
        response_200 = DominoAdminInterfaceExecutionOverviewsWithTotalCount.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = DominoApiErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DominoApiErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DominoApiErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = DominoApiErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DominoAdminInterfaceExecutionOverviewsWithTotalCount | DominoApiErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    offset: int | None | Unset = 0,
    page_size: int | None | Unset = 50,
    sort_by: GetCurrentExecutionsSortBy | Unset = GetCurrentExecutionsSortBy.EXECUTIONID,
    sort_order: GetCurrentExecutionsSortOrder | Unset = GetCurrentExecutionsSortOrder.ASC,
    search_query: None | str | Unset = UNSET,
    search_columns: None | str | Unset = UNSET,
) -> Response[DominoAdminInterfaceExecutionOverviewsWithTotalCount | DominoApiErrorResponse]:
    """Gets all non-completed executions (running on the Kubernetes Compute Grid, for now)

    Args:
        offset (int | None | Unset):  Default: 0.
        page_size (int | None | Unset):  Default: 50.
        sort_by (GetCurrentExecutionsSortBy | Unset):  Default:
            GetCurrentExecutionsSortBy.EXECUTIONID.
        sort_order (GetCurrentExecutionsSortOrder | Unset):  Default:
            GetCurrentExecutionsSortOrder.ASC.
        search_query (None | str | Unset):
        search_columns (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoAdminInterfaceExecutionOverviewsWithTotalCount | DominoApiErrorResponse]
    """

    kwargs = _get_kwargs(
        offset=offset,
        page_size=page_size,
        sort_by=sort_by,
        sort_order=sort_order,
        search_query=search_query,
        search_columns=search_columns,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    offset: int | None | Unset = 0,
    page_size: int | None | Unset = 50,
    sort_by: GetCurrentExecutionsSortBy | Unset = GetCurrentExecutionsSortBy.EXECUTIONID,
    sort_order: GetCurrentExecutionsSortOrder | Unset = GetCurrentExecutionsSortOrder.ASC,
    search_query: None | str | Unset = UNSET,
    search_columns: None | str | Unset = UNSET,
) -> DominoAdminInterfaceExecutionOverviewsWithTotalCount | DominoApiErrorResponse | None:
    """Gets all non-completed executions (running on the Kubernetes Compute Grid, for now)

    Args:
        offset (int | None | Unset):  Default: 0.
        page_size (int | None | Unset):  Default: 50.
        sort_by (GetCurrentExecutionsSortBy | Unset):  Default:
            GetCurrentExecutionsSortBy.EXECUTIONID.
        sort_order (GetCurrentExecutionsSortOrder | Unset):  Default:
            GetCurrentExecutionsSortOrder.ASC.
        search_query (None | str | Unset):
        search_columns (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoAdminInterfaceExecutionOverviewsWithTotalCount | DominoApiErrorResponse
    """

    return sync_detailed(
        client=client,
        offset=offset,
        page_size=page_size,
        sort_by=sort_by,
        sort_order=sort_order,
        search_query=search_query,
        search_columns=search_columns,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    offset: int | None | Unset = 0,
    page_size: int | None | Unset = 50,
    sort_by: GetCurrentExecutionsSortBy | Unset = GetCurrentExecutionsSortBy.EXECUTIONID,
    sort_order: GetCurrentExecutionsSortOrder | Unset = GetCurrentExecutionsSortOrder.ASC,
    search_query: None | str | Unset = UNSET,
    search_columns: None | str | Unset = UNSET,
) -> Response[DominoAdminInterfaceExecutionOverviewsWithTotalCount | DominoApiErrorResponse]:
    """Gets all non-completed executions (running on the Kubernetes Compute Grid, for now)

    Args:
        offset (int | None | Unset):  Default: 0.
        page_size (int | None | Unset):  Default: 50.
        sort_by (GetCurrentExecutionsSortBy | Unset):  Default:
            GetCurrentExecutionsSortBy.EXECUTIONID.
        sort_order (GetCurrentExecutionsSortOrder | Unset):  Default:
            GetCurrentExecutionsSortOrder.ASC.
        search_query (None | str | Unset):
        search_columns (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoAdminInterfaceExecutionOverviewsWithTotalCount | DominoApiErrorResponse]
    """

    kwargs = _get_kwargs(
        offset=offset,
        page_size=page_size,
        sort_by=sort_by,
        sort_order=sort_order,
        search_query=search_query,
        search_columns=search_columns,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    offset: int | None | Unset = 0,
    page_size: int | None | Unset = 50,
    sort_by: GetCurrentExecutionsSortBy | Unset = GetCurrentExecutionsSortBy.EXECUTIONID,
    sort_order: GetCurrentExecutionsSortOrder | Unset = GetCurrentExecutionsSortOrder.ASC,
    search_query: None | str | Unset = UNSET,
    search_columns: None | str | Unset = UNSET,
) -> DominoAdminInterfaceExecutionOverviewsWithTotalCount | DominoApiErrorResponse | None:
    """Gets all non-completed executions (running on the Kubernetes Compute Grid, for now)

    Args:
        offset (int | None | Unset):  Default: 0.
        page_size (int | None | Unset):  Default: 50.
        sort_by (GetCurrentExecutionsSortBy | Unset):  Default:
            GetCurrentExecutionsSortBy.EXECUTIONID.
        sort_order (GetCurrentExecutionsSortOrder | Unset):  Default:
            GetCurrentExecutionsSortOrder.ASC.
        search_query (None | str | Unset):
        search_columns (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoAdminInterfaceExecutionOverviewsWithTotalCount | DominoApiErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            page_size=page_size,
            sort_by=sort_by,
            sort_order=sort_order,
            search_query=search_query,
            search_columns=search_columns,
        )
    ).parsed
