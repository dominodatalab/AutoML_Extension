from __future__ import annotations
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.environment_envelope_v1 import EnvironmentEnvelopeV1
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_environment_response_400 import GetEnvironmentResponse400
from ...models.get_environment_response_404 import GetEnvironmentResponse404
from ...models.get_environment_response_500 import GetEnvironmentResponse500
from ...types import Response


def _get_kwargs(
    environment_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/environments/v1/environments/{environment_id}".format(
            environment_id=quote(str(environment_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    EnvironmentEnvelopeV1
    | FailureEnvelopeV1
    | GetEnvironmentResponse400
    | GetEnvironmentResponse404
    | GetEnvironmentResponse500
    | None
):
    if response.status_code == 200:
        response_200 = EnvironmentEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetEnvironmentResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetEnvironmentResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetEnvironmentResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    EnvironmentEnvelopeV1
    | FailureEnvelopeV1
    | GetEnvironmentResponse400
    | GetEnvironmentResponse404
    | GetEnvironmentResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    environment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    EnvironmentEnvelopeV1
    | FailureEnvelopeV1
    | GetEnvironmentResponse400
    | GetEnvironmentResponse404
    | GetEnvironmentResponse500
]:
    """Get an environment

     Get an Environment by its Id. Required permissions: `ViewEnvironment`

    Args:
        environment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnvironmentEnvelopeV1 | FailureEnvelopeV1 | GetEnvironmentResponse400 | GetEnvironmentResponse404 | GetEnvironmentResponse500]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    EnvironmentEnvelopeV1
    | FailureEnvelopeV1
    | GetEnvironmentResponse400
    | GetEnvironmentResponse404
    | GetEnvironmentResponse500
    | None
):
    """Get an environment

     Get an Environment by its Id. Required permissions: `ViewEnvironment`

    Args:
        environment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnvironmentEnvelopeV1 | FailureEnvelopeV1 | GetEnvironmentResponse400 | GetEnvironmentResponse404 | GetEnvironmentResponse500
    """

    return sync_detailed(
        environment_id=environment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    EnvironmentEnvelopeV1
    | FailureEnvelopeV1
    | GetEnvironmentResponse400
    | GetEnvironmentResponse404
    | GetEnvironmentResponse500
]:
    """Get an environment

     Get an Environment by its Id. Required permissions: `ViewEnvironment`

    Args:
        environment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnvironmentEnvelopeV1 | FailureEnvelopeV1 | GetEnvironmentResponse400 | GetEnvironmentResponse404 | GetEnvironmentResponse500]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    EnvironmentEnvelopeV1
    | FailureEnvelopeV1
    | GetEnvironmentResponse400
    | GetEnvironmentResponse404
    | GetEnvironmentResponse500
    | None
):
    """Get an environment

     Get an Environment by its Id. Required permissions: `ViewEnvironment`

    Args:
        environment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnvironmentEnvelopeV1 | FailureEnvelopeV1 | GetEnvironmentResponse400 | GetEnvironmentResponse404 | GetEnvironmentResponse500
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            client=client,
        )
    ).parsed
