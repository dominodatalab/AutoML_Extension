from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_workspace_api_workspace_admin_page_data_dto import DominoWorkspaceApiWorkspaceAdminPageDataDto
from ...models.get_admin_dashboard_row_data_sort_order import GetAdminDashboardRowDataSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    offset: int | None | Unset = 0,
    limit: int | None | Unset = 50,
    search_string: None | str | Unset = UNSET,
    sort_by: Any | Unset = UNSET,
    sort_order: GetAdminDashboardRowDataSortOrder | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_offset: int | None | Unset
    if isinstance(offset, Unset):
        json_offset = UNSET
    else:
        json_offset = offset
    params["offset"] = json_offset

    json_limit: int | None | Unset
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["limit"] = json_limit

    json_search_string: None | str | Unset
    if isinstance(search_string, Unset):
        json_search_string = UNSET
    else:
        json_search_string = search_string
    params["searchString"] = json_search_string

    params["sortBy"] = sort_by

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sortOrder"] = json_sort_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspace/adminDashboardRowData",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoWorkspaceApiWorkspaceAdminPageDataDto | None:
    if response.status_code == 200:
        response_200 = DominoWorkspaceApiWorkspaceAdminPageDataDto.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoWorkspaceApiWorkspaceAdminPageDataDto]:
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
    limit: int | None | Unset = 50,
    search_string: None | str | Unset = UNSET,
    sort_by: Any | Unset = UNSET,
    sort_order: GetAdminDashboardRowDataSortOrder | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoWorkspaceApiWorkspaceAdminPageDataDto]:
    """Get all workspace admin dashboard entries

    Args:
        offset (int | None | Unset):  Default: 0.
        limit (int | None | Unset):  Default: 50.
        search_string (None | str | Unset):
        sort_by (Any | Unset):
        sort_order (GetAdminDashboardRowDataSortOrder | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoWorkspaceApiWorkspaceAdminPageDataDto]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        search_string=search_string,
        sort_by=sort_by,
        sort_order=sort_order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    offset: int | None | Unset = 0,
    limit: int | None | Unset = 50,
    search_string: None | str | Unset = UNSET,
    sort_by: Any | Unset = UNSET,
    sort_order: GetAdminDashboardRowDataSortOrder | Unset = UNSET,
) -> DominoApiErrorResponse | DominoWorkspaceApiWorkspaceAdminPageDataDto | None:
    """Get all workspace admin dashboard entries

    Args:
        offset (int | None | Unset):  Default: 0.
        limit (int | None | Unset):  Default: 50.
        search_string (None | str | Unset):
        sort_by (Any | Unset):
        sort_order (GetAdminDashboardRowDataSortOrder | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoWorkspaceApiWorkspaceAdminPageDataDto
    """

    return sync_detailed(
        client=client,
        offset=offset,
        limit=limit,
        search_string=search_string,
        sort_by=sort_by,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    offset: int | None | Unset = 0,
    limit: int | None | Unset = 50,
    search_string: None | str | Unset = UNSET,
    sort_by: Any | Unset = UNSET,
    sort_order: GetAdminDashboardRowDataSortOrder | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoWorkspaceApiWorkspaceAdminPageDataDto]:
    """Get all workspace admin dashboard entries

    Args:
        offset (int | None | Unset):  Default: 0.
        limit (int | None | Unset):  Default: 50.
        search_string (None | str | Unset):
        sort_by (Any | Unset):
        sort_order (GetAdminDashboardRowDataSortOrder | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoWorkspaceApiWorkspaceAdminPageDataDto]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        search_string=search_string,
        sort_by=sort_by,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    offset: int | None | Unset = 0,
    limit: int | None | Unset = 50,
    search_string: None | str | Unset = UNSET,
    sort_by: Any | Unset = UNSET,
    sort_order: GetAdminDashboardRowDataSortOrder | Unset = UNSET,
) -> DominoApiErrorResponse | DominoWorkspaceApiWorkspaceAdminPageDataDto | None:
    """Get all workspace admin dashboard entries

    Args:
        offset (int | None | Unset):  Default: 0.
        limit (int | None | Unset):  Default: 50.
        search_string (None | str | Unset):
        sort_by (Any | Unset):
        sort_order (GetAdminDashboardRowDataSortOrder | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoWorkspaceApiWorkspaceAdminPageDataDto
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            limit=limit,
            search_string=search_string,
            sort_by=sort_by,
            sort_order=sort_order,
        )
    ).parsed
