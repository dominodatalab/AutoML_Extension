from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_gateway_endpoint_response_400 import CreateGatewayEndpointResponse400
from ...models.create_gateway_endpoint_response_404 import CreateGatewayEndpointResponse404
from ...models.create_gateway_endpoint_response_500 import CreateGatewayEndpointResponse500
from ...models.endpoint_envelope_v1 import EndpointEnvelopeV1
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.new_endpoint_v1 import NewEndpointV1
from ...types import Response


def _get_kwargs(
    *,
    body: NewEndpointV1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/aigateway/v1/endpoints",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreateGatewayEndpointResponse400
    | CreateGatewayEndpointResponse404
    | CreateGatewayEndpointResponse500
    | EndpointEnvelopeV1
    | FailureEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = EndpointEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CreateGatewayEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CreateGatewayEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = CreateGatewayEndpointResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateGatewayEndpointResponse400
    | CreateGatewayEndpointResponse404
    | CreateGatewayEndpointResponse500
    | EndpointEnvelopeV1
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
    body: NewEndpointV1,
) -> Response[
    CreateGatewayEndpointResponse400
    | CreateGatewayEndpointResponse404
    | CreateGatewayEndpointResponse500
    | EndpointEnvelopeV1
    | FailureEnvelopeV1
]:
    """Create a new endpoint

     Create a new a endpoint

    Args:
        body (NewEndpointV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateGatewayEndpointResponse400 | CreateGatewayEndpointResponse404 | CreateGatewayEndpointResponse500 | EndpointEnvelopeV1 | FailureEnvelopeV1]
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
    body: NewEndpointV1,
) -> (
    CreateGatewayEndpointResponse400
    | CreateGatewayEndpointResponse404
    | CreateGatewayEndpointResponse500
    | EndpointEnvelopeV1
    | FailureEnvelopeV1
    | None
):
    """Create a new endpoint

     Create a new a endpoint

    Args:
        body (NewEndpointV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateGatewayEndpointResponse400 | CreateGatewayEndpointResponse404 | CreateGatewayEndpointResponse500 | EndpointEnvelopeV1 | FailureEnvelopeV1
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: NewEndpointV1,
) -> Response[
    CreateGatewayEndpointResponse400
    | CreateGatewayEndpointResponse404
    | CreateGatewayEndpointResponse500
    | EndpointEnvelopeV1
    | FailureEnvelopeV1
]:
    """Create a new endpoint

     Create a new a endpoint

    Args:
        body (NewEndpointV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateGatewayEndpointResponse400 | CreateGatewayEndpointResponse404 | CreateGatewayEndpointResponse500 | EndpointEnvelopeV1 | FailureEnvelopeV1]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: NewEndpointV1,
) -> (
    CreateGatewayEndpointResponse400
    | CreateGatewayEndpointResponse404
    | CreateGatewayEndpointResponse500
    | EndpointEnvelopeV1
    | FailureEnvelopeV1
    | None
):
    """Create a new endpoint

     Create a new a endpoint

    Args:
        body (NewEndpointV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateGatewayEndpointResponse400 | CreateGatewayEndpointResponse404 | CreateGatewayEndpointResponse500 | EndpointEnvelopeV1 | FailureEnvelopeV1
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
