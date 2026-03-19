from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.deployment_target_type import DeploymentTargetType
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_deployment_target_types_response_400 import GetDeploymentTargetTypesResponse400
from ...models.get_deployment_target_types_response_404 import GetDeploymentTargetTypesResponse404
from ...models.get_deployment_target_types_response_500 import GetDeploymentTargetTypesResponse500
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/admin/v1/deploymentTargetTypes",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GetDeploymentTargetTypesResponse400
    | GetDeploymentTargetTypesResponse404
    | GetDeploymentTargetTypesResponse500
    | list[DeploymentTargetType]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DeploymentTargetType.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = GetDeploymentTargetTypesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetDeploymentTargetTypesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetDeploymentTargetTypesResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | GetDeploymentTargetTypesResponse400
    | GetDeploymentTargetTypesResponse404
    | GetDeploymentTargetTypesResponse500
    | list[DeploymentTargetType]
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
    | GetDeploymentTargetTypesResponse400
    | GetDeploymentTargetTypesResponse404
    | GetDeploymentTargetTypesResponse500
    | list[DeploymentTargetType]
]:
    """Gets all Deployment Target Types

     Gets all Deployment Target Types.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetDeploymentTargetTypesResponse400 | GetDeploymentTargetTypesResponse404 | GetDeploymentTargetTypesResponse500 | list[DeploymentTargetType]]
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
    | GetDeploymentTargetTypesResponse400
    | GetDeploymentTargetTypesResponse404
    | GetDeploymentTargetTypesResponse500
    | list[DeploymentTargetType]
    | None
):
    """Gets all Deployment Target Types

     Gets all Deployment Target Types.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetDeploymentTargetTypesResponse400 | GetDeploymentTargetTypesResponse404 | GetDeploymentTargetTypesResponse500 | list[DeploymentTargetType]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    FailureEnvelopeV1
    | GetDeploymentTargetTypesResponse400
    | GetDeploymentTargetTypesResponse404
    | GetDeploymentTargetTypesResponse500
    | list[DeploymentTargetType]
]:
    """Gets all Deployment Target Types

     Gets all Deployment Target Types.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetDeploymentTargetTypesResponse400 | GetDeploymentTargetTypesResponse404 | GetDeploymentTargetTypesResponse500 | list[DeploymentTargetType]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    FailureEnvelopeV1
    | GetDeploymentTargetTypesResponse400
    | GetDeploymentTargetTypesResponse404
    | GetDeploymentTargetTypesResponse500
    | list[DeploymentTargetType]
    | None
):
    """Gets all Deployment Target Types

     Gets all Deployment Target Types.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetDeploymentTargetTypesResponse400 | GetDeploymentTargetTypesResponse404 | GetDeploymentTargetTypesResponse500 | list[DeploymentTargetType]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
