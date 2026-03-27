from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_admin_usermanagement_api_users_with_usage_response import (
    DominoAdminUsermanagementApiUsersWithUsageResponse,
)
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    offset: int | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/admin/user-management/users-with-usage",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoAdminUsermanagementApiUsersWithUsageResponse | DominoApiErrorResponse | None:
    if response.status_code == 200:
        response_200 = DominoAdminUsermanagementApiUsersWithUsageResponse.from_dict(response.json())

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
) -> Response[DominoAdminUsermanagementApiUsersWithUsageResponse | DominoApiErrorResponse]:
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
) -> Response[DominoAdminUsermanagementApiUsersWithUsageResponse | DominoApiErrorResponse]:
    """Gets users and their user usage reports.

    Args:
        offset (int | None | Unset):
        limit (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoAdminUsermanagementApiUsersWithUsageResponse | DominoApiErrorResponse]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
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
) -> DominoAdminUsermanagementApiUsersWithUsageResponse | DominoApiErrorResponse | None:
    """Gets users and their user usage reports.

    Args:
        offset (int | None | Unset):
        limit (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoAdminUsermanagementApiUsersWithUsageResponse | DominoApiErrorResponse
    """

    return sync_detailed(
        client=client,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    offset: int | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
) -> Response[DominoAdminUsermanagementApiUsersWithUsageResponse | DominoApiErrorResponse]:
    """Gets users and their user usage reports.

    Args:
        offset (int | None | Unset):
        limit (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoAdminUsermanagementApiUsersWithUsageResponse | DominoApiErrorResponse]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    offset: int | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
) -> DominoAdminUsermanagementApiUsersWithUsageResponse | DominoApiErrorResponse | None:
    """Gets users and their user usage reports.

    Args:
        offset (int | None | Unset):
        limit (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoAdminUsermanagementApiUsersWithUsageResponse | DominoApiErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            limit=limit,
        )
    ).parsed
