from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_admin_interface_project_search_results_dto import DominoAdminInterfaceProjectSearchResultsDto
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.get_dashboard_entries_sort_by import GetDashboardEntriesSortBy
from ...models.get_dashboard_entries_sort_order import GetDashboardEntriesSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    offset: int | None | Unset = 0,
    page_size: int | None | Unset = 50,
    checkpoint_project_id: str | Unset = UNSET,
    search_string: None | str | Unset = UNSET,
    sort_by: GetDashboardEntriesSortBy | Unset = UNSET,
    sort_order: GetDashboardEntriesSortOrder | Unset = UNSET,
    include_archived: bool | None | Unset = UNSET,
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

    params["checkpointProjectId"] = checkpoint_project_id

    json_search_string: None | str | Unset
    if isinstance(search_string, Unset):
        json_search_string = UNSET
    else:
        json_search_string = search_string
    params["searchString"] = json_search_string

    json_sort_by: str | Unset = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value

    params["sortBy"] = json_sort_by

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sortOrder"] = json_sort_order

    json_include_archived: bool | None | Unset
    if isinstance(include_archived, Unset):
        json_include_archived = UNSET
    else:
        json_include_archived = include_archived
    params["includeArchived"] = json_include_archived

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/admin/dashboardEntries",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoAdminInterfaceProjectSearchResultsDto | DominoApiErrorResponse | None:
    if response.status_code == 200:
        response_200 = DominoAdminInterfaceProjectSearchResultsDto.from_dict(response.json())

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
) -> Response[DominoAdminInterfaceProjectSearchResultsDto | DominoApiErrorResponse]:
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
    checkpoint_project_id: str | Unset = UNSET,
    search_string: None | str | Unset = UNSET,
    sort_by: GetDashboardEntriesSortBy | Unset = UNSET,
    sort_order: GetDashboardEntriesSortOrder | Unset = UNSET,
    include_archived: bool | None | Unset = UNSET,
) -> Response[DominoAdminInterfaceProjectSearchResultsDto | DominoApiErrorResponse]:
    """Gets all dashboard entries

    Args:
        offset (int | None | Unset):  Default: 0.
        page_size (int | None | Unset):  Default: 50.
        checkpoint_project_id (str | Unset):
        search_string (None | str | Unset):
        sort_by (GetDashboardEntriesSortBy | Unset):
        sort_order (GetDashboardEntriesSortOrder | Unset):
        include_archived (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoAdminInterfaceProjectSearchResultsDto | DominoApiErrorResponse]
    """

    kwargs = _get_kwargs(
        offset=offset,
        page_size=page_size,
        checkpoint_project_id=checkpoint_project_id,
        search_string=search_string,
        sort_by=sort_by,
        sort_order=sort_order,
        include_archived=include_archived,
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
    checkpoint_project_id: str | Unset = UNSET,
    search_string: None | str | Unset = UNSET,
    sort_by: GetDashboardEntriesSortBy | Unset = UNSET,
    sort_order: GetDashboardEntriesSortOrder | Unset = UNSET,
    include_archived: bool | None | Unset = UNSET,
) -> DominoAdminInterfaceProjectSearchResultsDto | DominoApiErrorResponse | None:
    """Gets all dashboard entries

    Args:
        offset (int | None | Unset):  Default: 0.
        page_size (int | None | Unset):  Default: 50.
        checkpoint_project_id (str | Unset):
        search_string (None | str | Unset):
        sort_by (GetDashboardEntriesSortBy | Unset):
        sort_order (GetDashboardEntriesSortOrder | Unset):
        include_archived (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoAdminInterfaceProjectSearchResultsDto | DominoApiErrorResponse
    """

    return sync_detailed(
        client=client,
        offset=offset,
        page_size=page_size,
        checkpoint_project_id=checkpoint_project_id,
        search_string=search_string,
        sort_by=sort_by,
        sort_order=sort_order,
        include_archived=include_archived,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    offset: int | None | Unset = 0,
    page_size: int | None | Unset = 50,
    checkpoint_project_id: str | Unset = UNSET,
    search_string: None | str | Unset = UNSET,
    sort_by: GetDashboardEntriesSortBy | Unset = UNSET,
    sort_order: GetDashboardEntriesSortOrder | Unset = UNSET,
    include_archived: bool | None | Unset = UNSET,
) -> Response[DominoAdminInterfaceProjectSearchResultsDto | DominoApiErrorResponse]:
    """Gets all dashboard entries

    Args:
        offset (int | None | Unset):  Default: 0.
        page_size (int | None | Unset):  Default: 50.
        checkpoint_project_id (str | Unset):
        search_string (None | str | Unset):
        sort_by (GetDashboardEntriesSortBy | Unset):
        sort_order (GetDashboardEntriesSortOrder | Unset):
        include_archived (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoAdminInterfaceProjectSearchResultsDto | DominoApiErrorResponse]
    """

    kwargs = _get_kwargs(
        offset=offset,
        page_size=page_size,
        checkpoint_project_id=checkpoint_project_id,
        search_string=search_string,
        sort_by=sort_by,
        sort_order=sort_order,
        include_archived=include_archived,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    offset: int | None | Unset = 0,
    page_size: int | None | Unset = 50,
    checkpoint_project_id: str | Unset = UNSET,
    search_string: None | str | Unset = UNSET,
    sort_by: GetDashboardEntriesSortBy | Unset = UNSET,
    sort_order: GetDashboardEntriesSortOrder | Unset = UNSET,
    include_archived: bool | None | Unset = UNSET,
) -> DominoAdminInterfaceProjectSearchResultsDto | DominoApiErrorResponse | None:
    """Gets all dashboard entries

    Args:
        offset (int | None | Unset):  Default: 0.
        page_size (int | None | Unset):  Default: 50.
        checkpoint_project_id (str | Unset):
        search_string (None | str | Unset):
        sort_by (GetDashboardEntriesSortBy | Unset):
        sort_order (GetDashboardEntriesSortOrder | Unset):
        include_archived (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoAdminInterfaceProjectSearchResultsDto | DominoApiErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            page_size=page_size,
            checkpoint_project_id=checkpoint_project_id,
            search_string=search_string,
            sort_by=sort_by,
            sort_order=sort_order,
            include_archived=include_archived,
        )
    ).parsed
