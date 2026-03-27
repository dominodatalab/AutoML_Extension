from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.display_admin_notifications_dir import DisplayAdminNotificationsDir
from ...models.display_admin_notifications_priority import DisplayAdminNotificationsPriority
from ...models.display_admin_notifications_sort import DisplayAdminNotificationsSort
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_notifications_list_admin_notifications_result import (
    DominoNotificationsListAdminNotificationsResult,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    priority: DisplayAdminNotificationsPriority | Unset = UNSET,
    expired: bool | None | Unset = UNSET,
    sort: DisplayAdminNotificationsSort | Unset = UNSET,
    dir_: DisplayAdminNotificationsDir | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_priority: str | Unset = UNSET
    if not isinstance(priority, Unset):
        json_priority = priority.value

    params["priority"] = json_priority

    json_expired: bool | None | Unset
    if isinstance(expired, Unset):
        json_expired = UNSET
    else:
        json_expired = expired
    params["expired"] = json_expired

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    json_dir_: str | Unset = UNSET
    if not isinstance(dir_, Unset):
        json_dir_ = dir_.value

    params["dir"] = json_dir_

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
        "url": "/admin/notifications",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoNotificationsListAdminNotificationsResult | None:
    if response.status_code == 200:
        response_200 = DominoNotificationsListAdminNotificationsResult.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = DominoApiErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DominoApiErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 500:
        response_500 = DominoApiErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DominoApiErrorResponse | DominoNotificationsListAdminNotificationsResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    priority: DisplayAdminNotificationsPriority | Unset = UNSET,
    expired: bool | None | Unset = UNSET,
    sort: DisplayAdminNotificationsSort | Unset = UNSET,
    dir_: DisplayAdminNotificationsDir | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoNotificationsListAdminNotificationsResult]:
    """Lists all current notificatons with paging.

    Args:
        priority (DisplayAdminNotificationsPriority | Unset):
        expired (bool | None | Unset):
        sort (DisplayAdminNotificationsSort | Unset):
        dir_ (DisplayAdminNotificationsDir | Unset):
        offset (int | None | Unset):
        limit (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoNotificationsListAdminNotificationsResult]
    """

    kwargs = _get_kwargs(
        priority=priority,
        expired=expired,
        sort=sort,
        dir_=dir_,
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
    priority: DisplayAdminNotificationsPriority | Unset = UNSET,
    expired: bool | None | Unset = UNSET,
    sort: DisplayAdminNotificationsSort | Unset = UNSET,
    dir_: DisplayAdminNotificationsDir | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
) -> DominoApiErrorResponse | DominoNotificationsListAdminNotificationsResult | None:
    """Lists all current notificatons with paging.

    Args:
        priority (DisplayAdminNotificationsPriority | Unset):
        expired (bool | None | Unset):
        sort (DisplayAdminNotificationsSort | Unset):
        dir_ (DisplayAdminNotificationsDir | Unset):
        offset (int | None | Unset):
        limit (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoNotificationsListAdminNotificationsResult
    """

    return sync_detailed(
        client=client,
        priority=priority,
        expired=expired,
        sort=sort,
        dir_=dir_,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    priority: DisplayAdminNotificationsPriority | Unset = UNSET,
    expired: bool | None | Unset = UNSET,
    sort: DisplayAdminNotificationsSort | Unset = UNSET,
    dir_: DisplayAdminNotificationsDir | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoNotificationsListAdminNotificationsResult]:
    """Lists all current notificatons with paging.

    Args:
        priority (DisplayAdminNotificationsPriority | Unset):
        expired (bool | None | Unset):
        sort (DisplayAdminNotificationsSort | Unset):
        dir_ (DisplayAdminNotificationsDir | Unset):
        offset (int | None | Unset):
        limit (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoNotificationsListAdminNotificationsResult]
    """

    kwargs = _get_kwargs(
        priority=priority,
        expired=expired,
        sort=sort,
        dir_=dir_,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    priority: DisplayAdminNotificationsPriority | Unset = UNSET,
    expired: bool | None | Unset = UNSET,
    sort: DisplayAdminNotificationsSort | Unset = UNSET,
    dir_: DisplayAdminNotificationsDir | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
) -> DominoApiErrorResponse | DominoNotificationsListAdminNotificationsResult | None:
    """Lists all current notificatons with paging.

    Args:
        priority (DisplayAdminNotificationsPriority | Unset):
        expired (bool | None | Unset):
        sort (DisplayAdminNotificationsSort | Unset):
        dir_ (DisplayAdminNotificationsDir | Unset):
        offset (int | None | Unset):
        limit (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoNotificationsListAdminNotificationsResult
    """

    return (
        await asyncio_detailed(
            client=client,
            priority=priority,
            expired=expired,
            sort=sort,
            dir_=dir_,
            offset=offset,
            limit=limit,
        )
    ).parsed
