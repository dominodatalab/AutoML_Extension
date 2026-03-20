from __future__ import annotations
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_model_deployment_credentials_response_400 import GetModelDeploymentCredentialsResponse400
from ...models.get_model_deployment_credentials_response_404 import GetModelDeploymentCredentialsResponse404
from ...models.get_model_deployment_credentials_response_500 import GetModelDeploymentCredentialsResponse500
from ...models.model_deployment_credentials_list import ModelDeploymentCredentialsList
from ...types import Response


def _get_kwargs(
    model_deployment_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/modelServing/v1/modelDeployments/{model_deployment_id}/credentials".format(
            model_deployment_id=quote(str(model_deployment_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GetModelDeploymentCredentialsResponse400
    | GetModelDeploymentCredentialsResponse404
    | GetModelDeploymentCredentialsResponse500
    | ModelDeploymentCredentialsList
    | None
):
    if response.status_code == 200:
        response_200 = ModelDeploymentCredentialsList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetModelDeploymentCredentialsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetModelDeploymentCredentialsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetModelDeploymentCredentialsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | GetModelDeploymentCredentialsResponse400
    | GetModelDeploymentCredentialsResponse404
    | GetModelDeploymentCredentialsResponse500
    | ModelDeploymentCredentialsList
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    model_deployment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    FailureEnvelopeV1
    | GetModelDeploymentCredentialsResponse400
    | GetModelDeploymentCredentialsResponse404
    | GetModelDeploymentCredentialsResponse500
    | ModelDeploymentCredentialsList
]:
    """Retrieve all temporary credentials for a specific Model Deployment

     Retrieves summary information for all available temporary credentials of a Model Deployment.

    Args:
        model_deployment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetModelDeploymentCredentialsResponse400 | GetModelDeploymentCredentialsResponse404 | GetModelDeploymentCredentialsResponse500 | ModelDeploymentCredentialsList]
    """

    kwargs = _get_kwargs(
        model_deployment_id=model_deployment_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    model_deployment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    FailureEnvelopeV1
    | GetModelDeploymentCredentialsResponse400
    | GetModelDeploymentCredentialsResponse404
    | GetModelDeploymentCredentialsResponse500
    | ModelDeploymentCredentialsList
    | None
):
    """Retrieve all temporary credentials for a specific Model Deployment

     Retrieves summary information for all available temporary credentials of a Model Deployment.

    Args:
        model_deployment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetModelDeploymentCredentialsResponse400 | GetModelDeploymentCredentialsResponse404 | GetModelDeploymentCredentialsResponse500 | ModelDeploymentCredentialsList
    """

    return sync_detailed(
        model_deployment_id=model_deployment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    model_deployment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    FailureEnvelopeV1
    | GetModelDeploymentCredentialsResponse400
    | GetModelDeploymentCredentialsResponse404
    | GetModelDeploymentCredentialsResponse500
    | ModelDeploymentCredentialsList
]:
    """Retrieve all temporary credentials for a specific Model Deployment

     Retrieves summary information for all available temporary credentials of a Model Deployment.

    Args:
        model_deployment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetModelDeploymentCredentialsResponse400 | GetModelDeploymentCredentialsResponse404 | GetModelDeploymentCredentialsResponse500 | ModelDeploymentCredentialsList]
    """

    kwargs = _get_kwargs(
        model_deployment_id=model_deployment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    model_deployment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    FailureEnvelopeV1
    | GetModelDeploymentCredentialsResponse400
    | GetModelDeploymentCredentialsResponse404
    | GetModelDeploymentCredentialsResponse500
    | ModelDeploymentCredentialsList
    | None
):
    """Retrieve all temporary credentials for a specific Model Deployment

     Retrieves summary information for all available temporary credentials of a Model Deployment.

    Args:
        model_deployment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetModelDeploymentCredentialsResponse400 | GetModelDeploymentCredentialsResponse404 | GetModelDeploymentCredentialsResponse500 | ModelDeploymentCredentialsList
    """

    return (
        await asyncio_detailed(
            model_deployment_id=model_deployment_id,
            client=client,
        )
    ).parsed
