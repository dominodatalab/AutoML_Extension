from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_environment_response_400 import CreateEnvironmentResponse400
from ...models.create_environment_response_404 import CreateEnvironmentResponse404
from ...models.create_environment_response_500 import CreateEnvironmentResponse500
from ...models.environment_envelope_v1 import EnvironmentEnvelopeV1
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.new_environment_v1 import NewEnvironmentV1
from ...types import Response


def _get_kwargs(
    *,
    body: NewEnvironmentV1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/environments/beta/environments",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreateEnvironmentResponse400
    | CreateEnvironmentResponse404
    | CreateEnvironmentResponse500
    | EnvironmentEnvelopeV1
    | FailureEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = EnvironmentEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CreateEnvironmentResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CreateEnvironmentResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = CreateEnvironmentResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateEnvironmentResponse400
    | CreateEnvironmentResponse404
    | CreateEnvironmentResponse500
    | EnvironmentEnvelopeV1
    | FailureEnvelopeV1
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
    body: NewEnvironmentV1,
) -> Response[
    CreateEnvironmentResponse400
    | CreateEnvironmentResponse404
    | CreateEnvironmentResponse500
    | EnvironmentEnvelopeV1
    | FailureEnvelopeV1
]:
    """Create an environment

     Create an environment. Required permissions: `CreateEnvironment, EditEnvironment, UseFileStorage`.
    *Note:* This is a beta endpoint with known limitations.

    Args:
        body (NewEnvironmentV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateEnvironmentResponse400 | CreateEnvironmentResponse404 | CreateEnvironmentResponse500 | EnvironmentEnvelopeV1 | FailureEnvelopeV1]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: NewEnvironmentV1,
) -> (
    CreateEnvironmentResponse400
    | CreateEnvironmentResponse404
    | CreateEnvironmentResponse500
    | EnvironmentEnvelopeV1
    | FailureEnvelopeV1
    | None
):
    """Create an environment

     Create an environment. Required permissions: `CreateEnvironment, EditEnvironment, UseFileStorage`.
    *Note:* This is a beta endpoint with known limitations.

    Args:
        body (NewEnvironmentV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateEnvironmentResponse400 | CreateEnvironmentResponse404 | CreateEnvironmentResponse500 | EnvironmentEnvelopeV1 | FailureEnvelopeV1
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: NewEnvironmentV1,
) -> Response[
    CreateEnvironmentResponse400
    | CreateEnvironmentResponse404
    | CreateEnvironmentResponse500
    | EnvironmentEnvelopeV1
    | FailureEnvelopeV1
]:
    """Create an environment

     Create an environment. Required permissions: `CreateEnvironment, EditEnvironment, UseFileStorage`.
    *Note:* This is a beta endpoint with known limitations.

    Args:
        body (NewEnvironmentV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateEnvironmentResponse400 | CreateEnvironmentResponse404 | CreateEnvironmentResponse500 | EnvironmentEnvelopeV1 | FailureEnvelopeV1]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: NewEnvironmentV1,
) -> (
    CreateEnvironmentResponse400
    | CreateEnvironmentResponse404
    | CreateEnvironmentResponse500
    | EnvironmentEnvelopeV1
    | FailureEnvelopeV1
    | None
):
    """Create an environment

     Create an environment. Required permissions: `CreateEnvironment, EditEnvironment, UseFileStorage`.
    *Note:* This is a beta endpoint with known limitations.

    Args:
        body (NewEnvironmentV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateEnvironmentResponse400 | CreateEnvironmentResponse404 | CreateEnvironmentResponse500 | EnvironmentEnvelopeV1 | FailureEnvelopeV1
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
