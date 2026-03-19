from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_current_user_response_400 import GetCurrentUserResponse400
from ...models.get_current_user_response_404 import GetCurrentUserResponse404
from ...models.get_current_user_response_500 import GetCurrentUserResponse500
from ...models.user_envelope_v1 import UserEnvelopeV1
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/users/v1/self",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GetCurrentUserResponse400
    | GetCurrentUserResponse404
    | GetCurrentUserResponse500
    | UserEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = UserEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetCurrentUserResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetCurrentUserResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetCurrentUserResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | GetCurrentUserResponse400
    | GetCurrentUserResponse404
    | GetCurrentUserResponse500
    | UserEnvelopeV1
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
) -> Response[
    FailureEnvelopeV1
    | GetCurrentUserResponse400
    | GetCurrentUserResponse404
    | GetCurrentUserResponse500
    | UserEnvelopeV1
]:
    """Get the current user

     Retrieve the current user. Required permissions: `None`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetCurrentUserResponse400 | GetCurrentUserResponse404 | GetCurrentUserResponse500 | UserEnvelopeV1]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> (
    FailureEnvelopeV1
    | GetCurrentUserResponse400
    | GetCurrentUserResponse404
    | GetCurrentUserResponse500
    | UserEnvelopeV1
    | None
):
    """Get the current user

     Retrieve the current user. Required permissions: `None`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetCurrentUserResponse400 | GetCurrentUserResponse404 | GetCurrentUserResponse500 | UserEnvelopeV1
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    FailureEnvelopeV1
    | GetCurrentUserResponse400
    | GetCurrentUserResponse404
    | GetCurrentUserResponse500
    | UserEnvelopeV1
]:
    """Get the current user

     Retrieve the current user. Required permissions: `None`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetCurrentUserResponse400 | GetCurrentUserResponse404 | GetCurrentUserResponse500 | UserEnvelopeV1]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    FailureEnvelopeV1
    | GetCurrentUserResponse400
    | GetCurrentUserResponse404
    | GetCurrentUserResponse500
    | UserEnvelopeV1
    | None
):
    """Get the current user

     Retrieve the current user. Required permissions: `None`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetCurrentUserResponse400 | GetCurrentUserResponse404 | GetCurrentUserResponse500 | UserEnvelopeV1
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
