from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.endpoint_permissions_dto_v1 import EndpointPermissionsDtoV1
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.update_gateway_endpoint_permissions_by_name_response_400 import (
    UpdateGatewayEndpointPermissionsByNameResponse400,
)
from ...models.update_gateway_endpoint_permissions_by_name_response_404 import (
    UpdateGatewayEndpointPermissionsByNameResponse404,
)
from ...models.update_gateway_endpoint_permissions_by_name_response_500 import (
    UpdateGatewayEndpointPermissionsByNameResponse500,
)
from ...models.updated_endpoint_permissions_v1 import UpdatedEndpointPermissionsV1
from ...types import Response


def _get_kwargs(
    endpoint_name: str,
    *,
    body: UpdatedEndpointPermissionsV1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/aigateway/v1/endpoints/{endpoint_name}/permissions".format(
            endpoint_name=quote(str(endpoint_name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    EndpointPermissionsDtoV1
    | FailureEnvelopeV1
    | UpdateGatewayEndpointPermissionsByNameResponse400
    | UpdateGatewayEndpointPermissionsByNameResponse404
    | UpdateGatewayEndpointPermissionsByNameResponse500
    | None
):
    if response.status_code == 200:
        response_200 = EndpointPermissionsDtoV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateGatewayEndpointPermissionsByNameResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UpdateGatewayEndpointPermissionsByNameResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = UpdateGatewayEndpointPermissionsByNameResponse500.from_dict(response.json())

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
    | UpdateGatewayEndpointPermissionsByNameResponse400
    | UpdateGatewayEndpointPermissionsByNameResponse404
    | UpdateGatewayEndpointPermissionsByNameResponse500
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
    body: UpdatedEndpointPermissionsV1,
) -> Response[
    EndpointPermissionsDtoV1
    | FailureEnvelopeV1
    | UpdateGatewayEndpointPermissionsByNameResponse400
    | UpdateGatewayEndpointPermissionsByNameResponse404
    | UpdateGatewayEndpointPermissionsByNameResponse500
]:
    """Update permissions for a endpoint by name

     Update permissions for a endpoint by name (add or remove user IDs, or change isEveryoneAllowed)

    Args:
        endpoint_name (str):
        body (UpdatedEndpointPermissionsV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EndpointPermissionsDtoV1 | FailureEnvelopeV1 | UpdateGatewayEndpointPermissionsByNameResponse400 | UpdateGatewayEndpointPermissionsByNameResponse404 | UpdateGatewayEndpointPermissionsByNameResponse500]
    """

    kwargs = _get_kwargs(
        endpoint_name=endpoint_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    endpoint_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatedEndpointPermissionsV1,
) -> (
    EndpointPermissionsDtoV1
    | FailureEnvelopeV1
    | UpdateGatewayEndpointPermissionsByNameResponse400
    | UpdateGatewayEndpointPermissionsByNameResponse404
    | UpdateGatewayEndpointPermissionsByNameResponse500
    | None
):
    """Update permissions for a endpoint by name

     Update permissions for a endpoint by name (add or remove user IDs, or change isEveryoneAllowed)

    Args:
        endpoint_name (str):
        body (UpdatedEndpointPermissionsV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EndpointPermissionsDtoV1 | FailureEnvelopeV1 | UpdateGatewayEndpointPermissionsByNameResponse400 | UpdateGatewayEndpointPermissionsByNameResponse404 | UpdateGatewayEndpointPermissionsByNameResponse500
    """

    return sync_detailed(
        endpoint_name=endpoint_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    endpoint_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatedEndpointPermissionsV1,
) -> Response[
    EndpointPermissionsDtoV1
    | FailureEnvelopeV1
    | UpdateGatewayEndpointPermissionsByNameResponse400
    | UpdateGatewayEndpointPermissionsByNameResponse404
    | UpdateGatewayEndpointPermissionsByNameResponse500
]:
    """Update permissions for a endpoint by name

     Update permissions for a endpoint by name (add or remove user IDs, or change isEveryoneAllowed)

    Args:
        endpoint_name (str):
        body (UpdatedEndpointPermissionsV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EndpointPermissionsDtoV1 | FailureEnvelopeV1 | UpdateGatewayEndpointPermissionsByNameResponse400 | UpdateGatewayEndpointPermissionsByNameResponse404 | UpdateGatewayEndpointPermissionsByNameResponse500]
    """

    kwargs = _get_kwargs(
        endpoint_name=endpoint_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    endpoint_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatedEndpointPermissionsV1,
) -> (
    EndpointPermissionsDtoV1
    | FailureEnvelopeV1
    | UpdateGatewayEndpointPermissionsByNameResponse400
    | UpdateGatewayEndpointPermissionsByNameResponse404
    | UpdateGatewayEndpointPermissionsByNameResponse500
    | None
):
    """Update permissions for a endpoint by name

     Update permissions for a endpoint by name (add or remove user IDs, or change isEveryoneAllowed)

    Args:
        endpoint_name (str):
        body (UpdatedEndpointPermissionsV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EndpointPermissionsDtoV1 | FailureEnvelopeV1 | UpdateGatewayEndpointPermissionsByNameResponse400 | UpdateGatewayEndpointPermissionsByNameResponse404 | UpdateGatewayEndpointPermissionsByNameResponse500
    """

    return (
        await asyncio_detailed(
            endpoint_name=endpoint_name,
            client=client,
            body=body,
        )
    ).parsed
