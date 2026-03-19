from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_visible_users_response_400 import GetVisibleUsersResponse400
from ...models.get_visible_users_response_404 import GetVisibleUsersResponse404
from ...models.get_visible_users_response_500 import GetVisibleUsersResponse500
from ...models.paginated_user_envelope_v1 import PaginatedUserEnvelopeV1
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/users/v1/users",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GetVisibleUsersResponse400
    | GetVisibleUsersResponse404
    | GetVisibleUsersResponse500
    | PaginatedUserEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedUserEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetVisibleUsersResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetVisibleUsersResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetVisibleUsersResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | GetVisibleUsersResponse400
    | GetVisibleUsersResponse404
    | GetVisibleUsersResponse500
    | PaginatedUserEnvelopeV1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1
    | GetVisibleUsersResponse400
    | GetVisibleUsersResponse404
    | GetVisibleUsersResponse500
    | PaginatedUserEnvelopeV1
]:
    """Get all users visible to the current user

     Retrieves all users visible to the current user. Required permissions: `None`

    Args:
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetVisibleUsersResponse400 | GetVisibleUsersResponse404 | GetVisibleUsersResponse500 | PaginatedUserEnvelopeV1]
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
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> (
    FailureEnvelopeV1
    | GetVisibleUsersResponse400
    | GetVisibleUsersResponse404
    | GetVisibleUsersResponse500
    | PaginatedUserEnvelopeV1
    | None
):
    """Get all users visible to the current user

     Retrieves all users visible to the current user. Required permissions: `None`

    Args:
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetVisibleUsersResponse400 | GetVisibleUsersResponse404 | GetVisibleUsersResponse500 | PaginatedUserEnvelopeV1
    """

    return sync_detailed(
        client=client,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1
    | GetVisibleUsersResponse400
    | GetVisibleUsersResponse404
    | GetVisibleUsersResponse500
    | PaginatedUserEnvelopeV1
]:
    """Get all users visible to the current user

     Retrieves all users visible to the current user. Required permissions: `None`

    Args:
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetVisibleUsersResponse400 | GetVisibleUsersResponse404 | GetVisibleUsersResponse500 | PaginatedUserEnvelopeV1]
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
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> (
    FailureEnvelopeV1
    | GetVisibleUsersResponse400
    | GetVisibleUsersResponse404
    | GetVisibleUsersResponse500
    | PaginatedUserEnvelopeV1
    | None
):
    """Get all users visible to the current user

     Retrieves all users visible to the current user. Required permissions: `None`

    Args:
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetVisibleUsersResponse400 | GetVisibleUsersResponse404 | GetVisibleUsersResponse500 | PaginatedUserEnvelopeV1
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            limit=limit,
        )
    ).parsed
