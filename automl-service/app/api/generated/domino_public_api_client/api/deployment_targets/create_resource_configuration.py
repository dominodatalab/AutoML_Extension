from __future__ import annotations
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_resource_configuration_response_400 import CreateResourceConfigurationResponse400
from ...models.create_resource_configuration_response_404 import CreateResourceConfigurationResponse404
from ...models.create_resource_configuration_response_500 import CreateResourceConfigurationResponse500
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.new_resource_configuration import NewResourceConfiguration
from ...models.resource_configuration import ResourceConfiguration
from ...types import Response


def _get_kwargs(
    deployment_target_id: str,
    *,
    body: NewResourceConfiguration,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/admin/v1/deploymentTargets/{deployment_target_id}/resourceConfigurations".format(
            deployment_target_id=quote(str(deployment_target_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreateResourceConfigurationResponse400
    | CreateResourceConfigurationResponse404
    | CreateResourceConfigurationResponse500
    | FailureEnvelopeV1
    | ResourceConfiguration
    | None
):
    if response.status_code == 200:
        response_200 = ResourceConfiguration.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CreateResourceConfigurationResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CreateResourceConfigurationResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = CreateResourceConfigurationResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateResourceConfigurationResponse400
    | CreateResourceConfigurationResponse404
    | CreateResourceConfigurationResponse500
    | FailureEnvelopeV1
    | ResourceConfiguration
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    deployment_target_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: NewResourceConfiguration,
) -> Response[
    CreateResourceConfigurationResponse400
    | CreateResourceConfigurationResponse404
    | CreateResourceConfigurationResponse500
    | FailureEnvelopeV1
    | ResourceConfiguration
]:
    """Creates a new Resource Configuration

     Creates a new Resource Configuration.

    Args:
        deployment_target_id (str):
        body (NewResourceConfiguration): Resource Configuration creation request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateResourceConfigurationResponse400 | CreateResourceConfigurationResponse404 | CreateResourceConfigurationResponse500 | FailureEnvelopeV1 | ResourceConfiguration]
    """

    kwargs = _get_kwargs(
        deployment_target_id=deployment_target_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    deployment_target_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: NewResourceConfiguration,
) -> (
    CreateResourceConfigurationResponse400
    | CreateResourceConfigurationResponse404
    | CreateResourceConfigurationResponse500
    | FailureEnvelopeV1
    | ResourceConfiguration
    | None
):
    """Creates a new Resource Configuration

     Creates a new Resource Configuration.

    Args:
        deployment_target_id (str):
        body (NewResourceConfiguration): Resource Configuration creation request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateResourceConfigurationResponse400 | CreateResourceConfigurationResponse404 | CreateResourceConfigurationResponse500 | FailureEnvelopeV1 | ResourceConfiguration
    """

    return sync_detailed(
        deployment_target_id=deployment_target_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    deployment_target_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: NewResourceConfiguration,
) -> Response[
    CreateResourceConfigurationResponse400
    | CreateResourceConfigurationResponse404
    | CreateResourceConfigurationResponse500
    | FailureEnvelopeV1
    | ResourceConfiguration
]:
    """Creates a new Resource Configuration

     Creates a new Resource Configuration.

    Args:
        deployment_target_id (str):
        body (NewResourceConfiguration): Resource Configuration creation request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateResourceConfigurationResponse400 | CreateResourceConfigurationResponse404 | CreateResourceConfigurationResponse500 | FailureEnvelopeV1 | ResourceConfiguration]
    """

    kwargs = _get_kwargs(
        deployment_target_id=deployment_target_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    deployment_target_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: NewResourceConfiguration,
) -> (
    CreateResourceConfigurationResponse400
    | CreateResourceConfigurationResponse404
    | CreateResourceConfigurationResponse500
    | FailureEnvelopeV1
    | ResourceConfiguration
    | None
):
    """Creates a new Resource Configuration

     Creates a new Resource Configuration.

    Args:
        deployment_target_id (str):
        body (NewResourceConfiguration): Resource Configuration creation request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateResourceConfigurationResponse400 | CreateResourceConfigurationResponse404 | CreateResourceConfigurationResponse500 | FailureEnvelopeV1 | ResourceConfiguration
    """

    return (
        await asyncio_detailed(
            deployment_target_id=deployment_target_id,
            client=client,
            body=body,
        )
    ).parsed
