from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_extension_response_400 import CreateExtensionResponse400
from ...models.create_extension_response_404 import CreateExtensionResponse404
from ...models.create_extension_response_500 import CreateExtensionResponse500
from ...models.extension_creation_request import ExtensionCreationRequest
from ...models.extension_response import ExtensionResponse
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...types import Response


def _get_kwargs(
    *,
    body: ExtensionCreationRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/extensions/beta/extensions",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreateExtensionResponse400
    | CreateExtensionResponse404
    | CreateExtensionResponse500
    | ExtensionResponse
    | FailureEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = ExtensionResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CreateExtensionResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CreateExtensionResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = CreateExtensionResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateExtensionResponse400
    | CreateExtensionResponse404
    | CreateExtensionResponse500
    | ExtensionResponse
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
    body: ExtensionCreationRequest,
) -> Response[
    CreateExtensionResponse400
    | CreateExtensionResponse404
    | CreateExtensionResponse500
    | ExtensionResponse
    | FailureEnvelopeV1
]:
    """Create an Extension

     Create an Extension given an App reference

    Args:
        body (ExtensionCreationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateExtensionResponse400 | CreateExtensionResponse404 | CreateExtensionResponse500 | ExtensionResponse | FailureEnvelopeV1]
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
    body: ExtensionCreationRequest,
) -> (
    CreateExtensionResponse400
    | CreateExtensionResponse404
    | CreateExtensionResponse500
    | ExtensionResponse
    | FailureEnvelopeV1
    | None
):
    """Create an Extension

     Create an Extension given an App reference

    Args:
        body (ExtensionCreationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateExtensionResponse400 | CreateExtensionResponse404 | CreateExtensionResponse500 | ExtensionResponse | FailureEnvelopeV1
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ExtensionCreationRequest,
) -> Response[
    CreateExtensionResponse400
    | CreateExtensionResponse404
    | CreateExtensionResponse500
    | ExtensionResponse
    | FailureEnvelopeV1
]:
    """Create an Extension

     Create an Extension given an App reference

    Args:
        body (ExtensionCreationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateExtensionResponse400 | CreateExtensionResponse404 | CreateExtensionResponse500 | ExtensionResponse | FailureEnvelopeV1]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ExtensionCreationRequest,
) -> (
    CreateExtensionResponse400
    | CreateExtensionResponse404
    | CreateExtensionResponse500
    | ExtensionResponse
    | FailureEnvelopeV1
    | None
):
    """Create an Extension

     Create an Extension given an App reference

    Args:
        body (ExtensionCreationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateExtensionResponse400 | CreateExtensionResponse404 | CreateExtensionResponse500 | ExtensionResponse | FailureEnvelopeV1
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
