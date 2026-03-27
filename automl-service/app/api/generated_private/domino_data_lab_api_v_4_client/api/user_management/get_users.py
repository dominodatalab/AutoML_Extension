from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_admin_usermanagement_api_users_response import DominoAdminUsermanagementApiUsersResponse
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.get_users_sortby import GetUsersSortby
from ...models.get_users_sortdir import GetUsersSortdir
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    offset: int | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    query: None | str | Unset = UNSET,
    sortby: GetUsersSortby | Unset = UNSET,
    sortdir: GetUsersSortdir | Unset = UNSET,
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

    json_query: None | str | Unset
    if isinstance(query, Unset):
        json_query = UNSET
    else:
        json_query = query
    params["query"] = json_query

    json_sortby: str | Unset = UNSET
    if not isinstance(sortby, Unset):
        json_sortby = sortby.value

    params["sortby"] = json_sortby

    json_sortdir: str | Unset = UNSET
    if not isinstance(sortdir, Unset):
        json_sortdir = sortdir.value

    params["sortdir"] = json_sortdir

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/admin/user-management/users",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoAdminUsermanagementApiUsersResponse | DominoApiErrorResponse | None:
    if response.status_code == 200:
        response_200 = DominoAdminUsermanagementApiUsersResponse.from_dict(response.json())

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
) -> Response[DominoAdminUsermanagementApiUsersResponse | DominoApiErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    offset: int | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    query: None | str | Unset = UNSET,
    sortby: GetUsersSortby | Unset = UNSET,
    sortdir: GetUsersSortdir | Unset = UNSET,
) -> Response[DominoAdminUsermanagementApiUsersResponse | DominoApiErrorResponse]:
    """Get users.

    Args:
        offset (int | None | Unset):
        limit (int | None | Unset):
        query (None | str | Unset):
        sortby (GetUsersSortby | Unset):
        sortdir (GetUsersSortdir | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoAdminUsermanagementApiUsersResponse | DominoApiErrorResponse]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        query=query,
        sortby=sortby,
        sortdir=sortdir,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    offset: int | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    query: None | str | Unset = UNSET,
    sortby: GetUsersSortby | Unset = UNSET,
    sortdir: GetUsersSortdir | Unset = UNSET,
) -> DominoAdminUsermanagementApiUsersResponse | DominoApiErrorResponse | None:
    """Get users.

    Args:
        offset (int | None | Unset):
        limit (int | None | Unset):
        query (None | str | Unset):
        sortby (GetUsersSortby | Unset):
        sortdir (GetUsersSortdir | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoAdminUsermanagementApiUsersResponse | DominoApiErrorResponse
    """

    return sync_detailed(
        client=client,
        offset=offset,
        limit=limit,
        query=query,
        sortby=sortby,
        sortdir=sortdir,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    offset: int | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    query: None | str | Unset = UNSET,
    sortby: GetUsersSortby | Unset = UNSET,
    sortdir: GetUsersSortdir | Unset = UNSET,
) -> Response[DominoAdminUsermanagementApiUsersResponse | DominoApiErrorResponse]:
    """Get users.

    Args:
        offset (int | None | Unset):
        limit (int | None | Unset):
        query (None | str | Unset):
        sortby (GetUsersSortby | Unset):
        sortdir (GetUsersSortdir | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoAdminUsermanagementApiUsersResponse | DominoApiErrorResponse]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        query=query,
        sortby=sortby,
        sortdir=sortdir,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    offset: int | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    query: None | str | Unset = UNSET,
    sortby: GetUsersSortby | Unset = UNSET,
    sortdir: GetUsersSortdir | Unset = UNSET,
) -> DominoAdminUsermanagementApiUsersResponse | DominoApiErrorResponse | None:
    """Get users.

    Args:
        offset (int | None | Unset):
        limit (int | None | Unset):
        query (None | str | Unset):
        sortby (GetUsersSortby | Unset):
        sortdir (GetUsersSortdir | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoAdminUsermanagementApiUsersResponse | DominoApiErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            limit=limit,
            query=query,
            sortby=sortby,
            sortdir=sortdir,
        )
    ).parsed
