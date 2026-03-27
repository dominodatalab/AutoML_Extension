from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.display_user_notifications_dir import DisplayUserNotificationsDir
from ...models.display_user_notifications_priority import DisplayUserNotificationsPriority
from ...models.display_user_notifications_sort import DisplayUserNotificationsSort
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_notifications_list_notifications_result import DominoNotificationsListNotificationsResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    priority: DisplayUserNotificationsPriority | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    sort: DisplayUserNotificationsSort | Unset = DisplayUserNotificationsSort.CREATED,
    dir_: DisplayUserNotificationsDir | Unset = DisplayUserNotificationsDir.DESC,
    default_sort: bool | None | Unset = False,
    expired: bool | None | Unset = UNSET,
    read: bool | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_priority: str | Unset = UNSET
    if not isinstance(priority, Unset):
        json_priority = priority.value

    params["priority"] = json_priority

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

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    json_dir_: str | Unset = UNSET
    if not isinstance(dir_, Unset):
        json_dir_ = dir_.value

    params["dir"] = json_dir_

    json_default_sort: bool | None | Unset
    if isinstance(default_sort, Unset):
        json_default_sort = UNSET
    else:
        json_default_sort = default_sort
    params["defaultSort"] = json_default_sort

    json_expired: bool | None | Unset
    if isinstance(expired, Unset):
        json_expired = UNSET
    else:
        json_expired = expired
    params["expired"] = json_expired

    json_read: bool | None | Unset
    if isinstance(read, Unset):
        json_read = UNSET
    else:
        json_read = read
    params["read"] = json_read

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users/notifications",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoNotificationsListNotificationsResult | None:
    if response.status_code == 200:
        response_200 = DominoNotificationsListNotificationsResult.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoNotificationsListNotificationsResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    priority: DisplayUserNotificationsPriority | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    sort: DisplayUserNotificationsSort | Unset = DisplayUserNotificationsSort.CREATED,
    dir_: DisplayUserNotificationsDir | Unset = DisplayUserNotificationsDir.DESC,
    default_sort: bool | None | Unset = False,
    expired: bool | None | Unset = UNSET,
    read: bool | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoNotificationsListNotificationsResult]:
    """Display all notifications for the current user.

    Args:
        priority (DisplayUserNotificationsPriority | Unset):
        offset (int | None | Unset):
        limit (int | None | Unset):
        sort (DisplayUserNotificationsSort | Unset):  Default:
            DisplayUserNotificationsSort.CREATED.
        dir_ (DisplayUserNotificationsDir | Unset):  Default: DisplayUserNotificationsDir.DESC.
        default_sort (bool | None | Unset):  Default: False.
        expired (bool | None | Unset):
        read (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoNotificationsListNotificationsResult]
    """

    kwargs = _get_kwargs(
        priority=priority,
        offset=offset,
        limit=limit,
        sort=sort,
        dir_=dir_,
        default_sort=default_sort,
        expired=expired,
        read=read,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    priority: DisplayUserNotificationsPriority | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    sort: DisplayUserNotificationsSort | Unset = DisplayUserNotificationsSort.CREATED,
    dir_: DisplayUserNotificationsDir | Unset = DisplayUserNotificationsDir.DESC,
    default_sort: bool | None | Unset = False,
    expired: bool | None | Unset = UNSET,
    read: bool | None | Unset = UNSET,
) -> DominoApiErrorResponse | DominoNotificationsListNotificationsResult | None:
    """Display all notifications for the current user.

    Args:
        priority (DisplayUserNotificationsPriority | Unset):
        offset (int | None | Unset):
        limit (int | None | Unset):
        sort (DisplayUserNotificationsSort | Unset):  Default:
            DisplayUserNotificationsSort.CREATED.
        dir_ (DisplayUserNotificationsDir | Unset):  Default: DisplayUserNotificationsDir.DESC.
        default_sort (bool | None | Unset):  Default: False.
        expired (bool | None | Unset):
        read (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoNotificationsListNotificationsResult
    """

    return sync_detailed(
        client=client,
        priority=priority,
        offset=offset,
        limit=limit,
        sort=sort,
        dir_=dir_,
        default_sort=default_sort,
        expired=expired,
        read=read,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    priority: DisplayUserNotificationsPriority | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    sort: DisplayUserNotificationsSort | Unset = DisplayUserNotificationsSort.CREATED,
    dir_: DisplayUserNotificationsDir | Unset = DisplayUserNotificationsDir.DESC,
    default_sort: bool | None | Unset = False,
    expired: bool | None | Unset = UNSET,
    read: bool | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoNotificationsListNotificationsResult]:
    """Display all notifications for the current user.

    Args:
        priority (DisplayUserNotificationsPriority | Unset):
        offset (int | None | Unset):
        limit (int | None | Unset):
        sort (DisplayUserNotificationsSort | Unset):  Default:
            DisplayUserNotificationsSort.CREATED.
        dir_ (DisplayUserNotificationsDir | Unset):  Default: DisplayUserNotificationsDir.DESC.
        default_sort (bool | None | Unset):  Default: False.
        expired (bool | None | Unset):
        read (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoNotificationsListNotificationsResult]
    """

    kwargs = _get_kwargs(
        priority=priority,
        offset=offset,
        limit=limit,
        sort=sort,
        dir_=dir_,
        default_sort=default_sort,
        expired=expired,
        read=read,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    priority: DisplayUserNotificationsPriority | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    sort: DisplayUserNotificationsSort | Unset = DisplayUserNotificationsSort.CREATED,
    dir_: DisplayUserNotificationsDir | Unset = DisplayUserNotificationsDir.DESC,
    default_sort: bool | None | Unset = False,
    expired: bool | None | Unset = UNSET,
    read: bool | None | Unset = UNSET,
) -> DominoApiErrorResponse | DominoNotificationsListNotificationsResult | None:
    """Display all notifications for the current user.

    Args:
        priority (DisplayUserNotificationsPriority | Unset):
        offset (int | None | Unset):
        limit (int | None | Unset):
        sort (DisplayUserNotificationsSort | Unset):  Default:
            DisplayUserNotificationsSort.CREATED.
        dir_ (DisplayUserNotificationsDir | Unset):  Default: DisplayUserNotificationsDir.DESC.
        default_sort (bool | None | Unset):  Default: False.
        expired (bool | None | Unset):
        read (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoNotificationsListNotificationsResult
    """

    return (
        await asyncio_detailed(
            client=client,
            priority=priority,
            offset=offset,
            limit=limit,
            sort=sort,
            dir_=dir_,
            default_sort=default_sort,
            expired=expired,
            read=read,
        )
    ).parsed
