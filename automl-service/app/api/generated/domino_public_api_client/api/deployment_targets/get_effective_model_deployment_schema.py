from __future__ import annotations
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.effective_model_deployment_schema import EffectiveModelDeploymentSchema
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_effective_model_deployment_schema_response_400 import GetEffectiveModelDeploymentSchemaResponse400
from ...models.get_effective_model_deployment_schema_response_404 import GetEffectiveModelDeploymentSchemaResponse404
from ...models.get_effective_model_deployment_schema_response_500 import GetEffectiveModelDeploymentSchemaResponse500
from ...types import Response


def _get_kwargs(
    deployment_target_id: str,
    resource_configuration_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/admin/v1/deploymentTargets/{deployment_target_id}/resourceConfigurations/{resource_configuration_id}/effectiveModelDeploymentSchema".format(
            deployment_target_id=quote(str(deployment_target_id), safe=""),
            resource_configuration_id=quote(str(resource_configuration_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    EffectiveModelDeploymentSchema
    | FailureEnvelopeV1
    | GetEffectiveModelDeploymentSchemaResponse400
    | GetEffectiveModelDeploymentSchemaResponse404
    | GetEffectiveModelDeploymentSchemaResponse500
    | None
):
    if response.status_code == 200:
        response_200 = EffectiveModelDeploymentSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetEffectiveModelDeploymentSchemaResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetEffectiveModelDeploymentSchemaResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetEffectiveModelDeploymentSchemaResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    EffectiveModelDeploymentSchema
    | FailureEnvelopeV1
    | GetEffectiveModelDeploymentSchemaResponse400
    | GetEffectiveModelDeploymentSchemaResponse404
    | GetEffectiveModelDeploymentSchemaResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    deployment_target_id: str,
    resource_configuration_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    EffectiveModelDeploymentSchema
    | FailureEnvelopeV1
    | GetEffectiveModelDeploymentSchemaResponse400
    | GetEffectiveModelDeploymentSchemaResponse404
    | GetEffectiveModelDeploymentSchemaResponse500
]:
    """Gets the effective configuration for model deployments using the resource configuration

     Gets the effective configuration for model deployments using the resource configuration.

    Args:
        deployment_target_id (str):
        resource_configuration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EffectiveModelDeploymentSchema | FailureEnvelopeV1 | GetEffectiveModelDeploymentSchemaResponse400 | GetEffectiveModelDeploymentSchemaResponse404 | GetEffectiveModelDeploymentSchemaResponse500]
    """

    kwargs = _get_kwargs(
        deployment_target_id=deployment_target_id,
        resource_configuration_id=resource_configuration_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    deployment_target_id: str,
    resource_configuration_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    EffectiveModelDeploymentSchema
    | FailureEnvelopeV1
    | GetEffectiveModelDeploymentSchemaResponse400
    | GetEffectiveModelDeploymentSchemaResponse404
    | GetEffectiveModelDeploymentSchemaResponse500
    | None
):
    """Gets the effective configuration for model deployments using the resource configuration

     Gets the effective configuration for model deployments using the resource configuration.

    Args:
        deployment_target_id (str):
        resource_configuration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EffectiveModelDeploymentSchema | FailureEnvelopeV1 | GetEffectiveModelDeploymentSchemaResponse400 | GetEffectiveModelDeploymentSchemaResponse404 | GetEffectiveModelDeploymentSchemaResponse500
    """

    return sync_detailed(
        deployment_target_id=deployment_target_id,
        resource_configuration_id=resource_configuration_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    deployment_target_id: str,
    resource_configuration_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    EffectiveModelDeploymentSchema
    | FailureEnvelopeV1
    | GetEffectiveModelDeploymentSchemaResponse400
    | GetEffectiveModelDeploymentSchemaResponse404
    | GetEffectiveModelDeploymentSchemaResponse500
]:
    """Gets the effective configuration for model deployments using the resource configuration

     Gets the effective configuration for model deployments using the resource configuration.

    Args:
        deployment_target_id (str):
        resource_configuration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EffectiveModelDeploymentSchema | FailureEnvelopeV1 | GetEffectiveModelDeploymentSchemaResponse400 | GetEffectiveModelDeploymentSchemaResponse404 | GetEffectiveModelDeploymentSchemaResponse500]
    """

    kwargs = _get_kwargs(
        deployment_target_id=deployment_target_id,
        resource_configuration_id=resource_configuration_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    deployment_target_id: str,
    resource_configuration_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    EffectiveModelDeploymentSchema
    | FailureEnvelopeV1
    | GetEffectiveModelDeploymentSchemaResponse400
    | GetEffectiveModelDeploymentSchemaResponse404
    | GetEffectiveModelDeploymentSchemaResponse500
    | None
):
    """Gets the effective configuration for model deployments using the resource configuration

     Gets the effective configuration for model deployments using the resource configuration.

    Args:
        deployment_target_id (str):
        resource_configuration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EffectiveModelDeploymentSchema | FailureEnvelopeV1 | GetEffectiveModelDeploymentSchemaResponse400 | GetEffectiveModelDeploymentSchemaResponse404 | GetEffectiveModelDeploymentSchemaResponse500
    """

    return (
        await asyncio_detailed(
            deployment_target_id=deployment_target_id,
            resource_configuration_id=resource_configuration_id,
            client=client,
        )
    ).parsed
