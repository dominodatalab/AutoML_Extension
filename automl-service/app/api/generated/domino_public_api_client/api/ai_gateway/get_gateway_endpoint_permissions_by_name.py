from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.endpoint_permissions_dto_v1 import EndpointPermissionsDtoV1
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_gateway_endpoint_permissions_by_name_response_400 import (
    GetGatewayEndpointPermissionsByNameResponse400,
)
from ...models.get_gateway_endpoint_permissions_by_name_response_404 import (
    GetGatewayEndpointPermissionsByNameResponse404,
)
from ...models.get_gateway_endpoint_permissions_by_name_response_500 import (
    GetGatewayEndpointPermissionsByNameResponse500,
)
from ...types import Response


def _get_kwargs(
    endpoint_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/aigateway/v1/endpoints/{endpoint_name}/permissions".format(
            endpoint_name=quote(str(endpoint_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    EndpointPermissionsDtoV1
    | FailureEnvelopeV1
    | GetGatewayEndpointPermissionsByNameResponse400
    | GetGatewayEndpointPermissionsByNameResponse404
    | GetGatewayEndpointPermissionsByNameResponse500
    | None
):
    if response.status_code == 200:
        response_200 = EndpointPermissionsDtoV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetGatewayEndpointPermissionsByNameResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetGatewayEndpointPermissionsByNameResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetGatewayEndpointPermissionsByNameResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    EndpointPermissionsDtoV1
    | FailureEnvelopeV1
    | GetGatewayEndpointPermissionsByNameResponse400
    | GetGatewayEndpointPermissionsByNameResponse404
    | GetGatewayEndpointPermissionsByNameResponse500
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
) -> Response[
    EndpointPermissionsDtoV1
    | FailureEnvelopeV1
    | GetGatewayEndpointPermissionsByNameResponse400
    | GetGatewayEndpointPermissionsByNameResponse404
    | GetGatewayEndpointPermissionsByNameResponse500
]:
    """Get permissions for a endpoint by name

     Get permissions for a endpoint by name

    Args:
        endpoint_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EndpointPermissionsDtoV1 | FailureEnvelopeV1 | GetGatewayEndpointPermissionsByNameResponse400 | GetGatewayEndpointPermissionsByNameResponse404 | GetGatewayEndpointPermissionsByNameResponse500]
    """

    kwargs = _get_kwargs(
        endpoint_name=endpoint_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    endpoint_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    EndpointPermissionsDtoV1
    | FailureEnvelopeV1
    | GetGatewayEndpointPermissionsByNameResponse400
    | GetGatewayEndpointPermissionsByNameResponse404
    | GetGatewayEndpointPermissionsByNameResponse500
    | None
):
    """Get permissions for a endpoint by name

     Get permissions for a endpoint by name

    Args:
        endpoint_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EndpointPermissionsDtoV1 | FailureEnvelopeV1 | GetGatewayEndpointPermissionsByNameResponse400 | GetGatewayEndpointPermissionsByNameResponse404 | GetGatewayEndpointPermissionsByNameResponse500
    """

    return sync_detailed(
        endpoint_name=endpoint_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    endpoint_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    EndpointPermissionsDtoV1
    | FailureEnvelopeV1
    | GetGatewayEndpointPermissionsByNameResponse400
    | GetGatewayEndpointPermissionsByNameResponse404
    | GetGatewayEndpointPermissionsByNameResponse500
]:
    """Get permissions for a endpoint by name

     Get permissions for a endpoint by name

    Args:
        endpoint_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EndpointPermissionsDtoV1 | FailureEnvelopeV1 | GetGatewayEndpointPermissionsByNameResponse400 | GetGatewayEndpointPermissionsByNameResponse404 | GetGatewayEndpointPermissionsByNameResponse500]
    """

    kwargs = _get_kwargs(
        endpoint_name=endpoint_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    endpoint_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    EndpointPermissionsDtoV1
    | FailureEnvelopeV1
    | GetGatewayEndpointPermissionsByNameResponse400
    | GetGatewayEndpointPermissionsByNameResponse404
    | GetGatewayEndpointPermissionsByNameResponse500
    | None
):
    """Get permissions for a endpoint by name

     Get permissions for a endpoint by name

    Args:
        endpoint_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EndpointPermissionsDtoV1 | FailureEnvelopeV1 | GetGatewayEndpointPermissionsByNameResponse400 | GetGatewayEndpointPermissionsByNameResponse404 | GetGatewayEndpointPermissionsByNameResponse500
    """

    return (
        await asyncio_detailed(
            endpoint_name=endpoint_name,
            client=client,
        )
    ).parsed
