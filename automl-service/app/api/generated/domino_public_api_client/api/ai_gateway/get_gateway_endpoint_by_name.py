from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.endpoint_envelope_v1 import EndpointEnvelopeV1
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_gateway_endpoint_by_name_response_400 import GetGatewayEndpointByNameResponse400
from ...models.get_gateway_endpoint_by_name_response_404 import GetGatewayEndpointByNameResponse404
from ...models.get_gateway_endpoint_by_name_response_500 import GetGatewayEndpointByNameResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    endpoint_name: str,
    *,
    num_input_tokens: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["numInputTokens"] = num_input_tokens

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/aigateway/v1/endpoints/{endpoint_name}".format(
            endpoint_name=quote(str(endpoint_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    EndpointEnvelopeV1
    | FailureEnvelopeV1
    | GetGatewayEndpointByNameResponse400
    | GetGatewayEndpointByNameResponse404
    | GetGatewayEndpointByNameResponse500
    | None
):
    if response.status_code == 200:
        response_200 = EndpointEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetGatewayEndpointByNameResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetGatewayEndpointByNameResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetGatewayEndpointByNameResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    EndpointEnvelopeV1
    | FailureEnvelopeV1
    | GetGatewayEndpointByNameResponse400
    | GetGatewayEndpointByNameResponse404
    | GetGatewayEndpointByNameResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    endpoint_name: str,
    *,
    client: AuthenticatedClient | Client,
    num_input_tokens: str | Unset = UNSET,
) -> Response[
    EndpointEnvelopeV1
    | FailureEnvelopeV1
    | GetGatewayEndpointByNameResponse400
    | GetGatewayEndpointByNameResponse404
    | GetGatewayEndpointByNameResponse500
]:
    """Get a endpoint by name

     Get a endpoint by name (returns endpoint if user has access and endpoint is active)

    Args:
        endpoint_name (str):
        num_input_tokens (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EndpointEnvelopeV1 | FailureEnvelopeV1 | GetGatewayEndpointByNameResponse400 | GetGatewayEndpointByNameResponse404 | GetGatewayEndpointByNameResponse500]
    """

    kwargs = _get_kwargs(
        endpoint_name=endpoint_name,
        num_input_tokens=num_input_tokens,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    endpoint_name: str,
    *,
    client: AuthenticatedClient | Client,
    num_input_tokens: str | Unset = UNSET,
) -> (
    EndpointEnvelopeV1
    | FailureEnvelopeV1
    | GetGatewayEndpointByNameResponse400
    | GetGatewayEndpointByNameResponse404
    | GetGatewayEndpointByNameResponse500
    | None
):
    """Get a endpoint by name

     Get a endpoint by name (returns endpoint if user has access and endpoint is active)

    Args:
        endpoint_name (str):
        num_input_tokens (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EndpointEnvelopeV1 | FailureEnvelopeV1 | GetGatewayEndpointByNameResponse400 | GetGatewayEndpointByNameResponse404 | GetGatewayEndpointByNameResponse500
    """

    return sync_detailed(
        endpoint_name=endpoint_name,
        client=client,
        num_input_tokens=num_input_tokens,
    ).parsed


async def asyncio_detailed(
    endpoint_name: str,
    *,
    client: AuthenticatedClient | Client,
    num_input_tokens: str | Unset = UNSET,
) -> Response[
    EndpointEnvelopeV1
    | FailureEnvelopeV1
    | GetGatewayEndpointByNameResponse400
    | GetGatewayEndpointByNameResponse404
    | GetGatewayEndpointByNameResponse500
]:
    """Get a endpoint by name

     Get a endpoint by name (returns endpoint if user has access and endpoint is active)

    Args:
        endpoint_name (str):
        num_input_tokens (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EndpointEnvelopeV1 | FailureEnvelopeV1 | GetGatewayEndpointByNameResponse400 | GetGatewayEndpointByNameResponse404 | GetGatewayEndpointByNameResponse500]
    """

    kwargs = _get_kwargs(
        endpoint_name=endpoint_name,
        num_input_tokens=num_input_tokens,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    endpoint_name: str,
    *,
    client: AuthenticatedClient | Client,
    num_input_tokens: str | Unset = UNSET,
) -> (
    EndpointEnvelopeV1
    | FailureEnvelopeV1
    | GetGatewayEndpointByNameResponse400
    | GetGatewayEndpointByNameResponse404
    | GetGatewayEndpointByNameResponse500
    | None
):
    """Get a endpoint by name

     Get a endpoint by name (returns endpoint if user has access and endpoint is active)

    Args:
        endpoint_name (str):
        num_input_tokens (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EndpointEnvelopeV1 | FailureEnvelopeV1 | GetGatewayEndpointByNameResponse400 | GetGatewayEndpointByNameResponse404 | GetGatewayEndpointByNameResponse500
    """

    return (
        await asyncio_detailed(
            endpoint_name=endpoint_name,
            client=client,
            num_input_tokens=num_input_tokens,
        )
    ).parsed
