from __future__ import annotations
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_model_deployments_response_400 import GetModelDeploymentsResponse400
from ...models.get_model_deployments_response_404 import GetModelDeploymentsResponse404
from ...models.get_model_deployments_response_500 import GetModelDeploymentsResponse500
from ...models.model_deployment_paginated_list import ModelDeploymentPaginatedList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    name: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    deployment_target_id: str | Unset = UNSET,
    resource_configuration_id: str | Unset = UNSET,
    registered_model_name: str | Unset = UNSET,
    registered_model_version: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = 25,
    order_by: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["name"] = name

    params["projectId"] = project_id

    params["deploymentTargetId"] = deployment_target_id

    params["resourceConfigurationId"] = resource_configuration_id

    params["registeredModelName"] = registered_model_name

    params["registeredModelVersion"] = registered_model_version

    params["limit"] = limit

    params["offset"] = offset

    params["orderBy"] = order_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/modelServing/v1/modelDeployments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GetModelDeploymentsResponse400
    | GetModelDeploymentsResponse404
    | GetModelDeploymentsResponse500
    | ModelDeploymentPaginatedList
    | None
):
    if response.status_code == 200:
        response_200 = ModelDeploymentPaginatedList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetModelDeploymentsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetModelDeploymentsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetModelDeploymentsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | GetModelDeploymentsResponse400
    | GetModelDeploymentsResponse404
    | GetModelDeploymentsResponse500
    | ModelDeploymentPaginatedList
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
    name: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    deployment_target_id: str | Unset = UNSET,
    resource_configuration_id: str | Unset = UNSET,
    registered_model_name: str | Unset = UNSET,
    registered_model_version: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = 25,
    order_by: str | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1
    | GetModelDeploymentsResponse400
    | GetModelDeploymentsResponse404
    | GetModelDeploymentsResponse500
    | ModelDeploymentPaginatedList
]:
    """Retrieve all Model Deployments

     Retrieves all Model Deployments filtered by optional query arguments.

    Args:
        name (str | Unset):
        project_id (str | Unset):
        deployment_target_id (str | Unset):
        resource_configuration_id (str | Unset):
        registered_model_name (str | Unset):
        registered_model_version (int | Unset):
        limit (int | Unset):
        offset (int | Unset):  Default: 25.
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetModelDeploymentsResponse400 | GetModelDeploymentsResponse404 | GetModelDeploymentsResponse500 | ModelDeploymentPaginatedList]
    """

    kwargs = _get_kwargs(
        name=name,
        project_id=project_id,
        deployment_target_id=deployment_target_id,
        resource_configuration_id=resource_configuration_id,
        registered_model_name=registered_model_name,
        registered_model_version=registered_model_version,
        limit=limit,
        offset=offset,
        order_by=order_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    deployment_target_id: str | Unset = UNSET,
    resource_configuration_id: str | Unset = UNSET,
    registered_model_name: str | Unset = UNSET,
    registered_model_version: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = 25,
    order_by: str | Unset = UNSET,
) -> (
    FailureEnvelopeV1
    | GetModelDeploymentsResponse400
    | GetModelDeploymentsResponse404
    | GetModelDeploymentsResponse500
    | ModelDeploymentPaginatedList
    | None
):
    """Retrieve all Model Deployments

     Retrieves all Model Deployments filtered by optional query arguments.

    Args:
        name (str | Unset):
        project_id (str | Unset):
        deployment_target_id (str | Unset):
        resource_configuration_id (str | Unset):
        registered_model_name (str | Unset):
        registered_model_version (int | Unset):
        limit (int | Unset):
        offset (int | Unset):  Default: 25.
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetModelDeploymentsResponse400 | GetModelDeploymentsResponse404 | GetModelDeploymentsResponse500 | ModelDeploymentPaginatedList
    """

    return sync_detailed(
        client=client,
        name=name,
        project_id=project_id,
        deployment_target_id=deployment_target_id,
        resource_configuration_id=resource_configuration_id,
        registered_model_name=registered_model_name,
        registered_model_version=registered_model_version,
        limit=limit,
        offset=offset,
        order_by=order_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    deployment_target_id: str | Unset = UNSET,
    resource_configuration_id: str | Unset = UNSET,
    registered_model_name: str | Unset = UNSET,
    registered_model_version: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = 25,
    order_by: str | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1
    | GetModelDeploymentsResponse400
    | GetModelDeploymentsResponse404
    | GetModelDeploymentsResponse500
    | ModelDeploymentPaginatedList
]:
    """Retrieve all Model Deployments

     Retrieves all Model Deployments filtered by optional query arguments.

    Args:
        name (str | Unset):
        project_id (str | Unset):
        deployment_target_id (str | Unset):
        resource_configuration_id (str | Unset):
        registered_model_name (str | Unset):
        registered_model_version (int | Unset):
        limit (int | Unset):
        offset (int | Unset):  Default: 25.
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetModelDeploymentsResponse400 | GetModelDeploymentsResponse404 | GetModelDeploymentsResponse500 | ModelDeploymentPaginatedList]
    """

    kwargs = _get_kwargs(
        name=name,
        project_id=project_id,
        deployment_target_id=deployment_target_id,
        resource_configuration_id=resource_configuration_id,
        registered_model_name=registered_model_name,
        registered_model_version=registered_model_version,
        limit=limit,
        offset=offset,
        order_by=order_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    deployment_target_id: str | Unset = UNSET,
    resource_configuration_id: str | Unset = UNSET,
    registered_model_name: str | Unset = UNSET,
    registered_model_version: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = 25,
    order_by: str | Unset = UNSET,
) -> (
    FailureEnvelopeV1
    | GetModelDeploymentsResponse400
    | GetModelDeploymentsResponse404
    | GetModelDeploymentsResponse500
    | ModelDeploymentPaginatedList
    | None
):
    """Retrieve all Model Deployments

     Retrieves all Model Deployments filtered by optional query arguments.

    Args:
        name (str | Unset):
        project_id (str | Unset):
        deployment_target_id (str | Unset):
        resource_configuration_id (str | Unset):
        registered_model_name (str | Unset):
        registered_model_version (int | Unset):
        limit (int | Unset):
        offset (int | Unset):  Default: 25.
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetModelDeploymentsResponse400 | GetModelDeploymentsResponse404 | GetModelDeploymentsResponse500 | ModelDeploymentPaginatedList
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            project_id=project_id,
            deployment_target_id=deployment_target_id,
            resource_configuration_id=resource_configuration_id,
            registered_model_name=registered_model_name,
            registered_model_version=registered_model_version,
            limit=limit,
            offset=offset,
            order_by=order_by,
        )
    ).parsed
