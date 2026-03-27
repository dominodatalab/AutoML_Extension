from __future__ import annotations
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_model_deployment_response_400 import CreateModelDeploymentResponse400
from ...models.create_model_deployment_response_404 import CreateModelDeploymentResponse404
from ...models.create_model_deployment_response_500 import CreateModelDeploymentResponse500
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.model_deployment import ModelDeployment
from ...models.new_model_deployment import NewModelDeployment
from ...types import Response


def _get_kwargs(
    *,
    body: NewModelDeployment,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/modelServing/v1/modelDeployments",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreateModelDeploymentResponse400
    | CreateModelDeploymentResponse404
    | CreateModelDeploymentResponse500
    | FailureEnvelopeV1
    | ModelDeployment
    | None
):
    if response.status_code == 200:
        response_200 = ModelDeployment.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CreateModelDeploymentResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CreateModelDeploymentResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = CreateModelDeploymentResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateModelDeploymentResponse400
    | CreateModelDeploymentResponse404
    | CreateModelDeploymentResponse500
    | FailureEnvelopeV1
    | ModelDeployment
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
    body: NewModelDeployment,
) -> Response[
    CreateModelDeploymentResponse400
    | CreateModelDeploymentResponse404
    | CreateModelDeploymentResponse500
    | FailureEnvelopeV1
    | ModelDeployment
]:
    """Create a new Model Deployment

     Creates a new Model Deployment entity.

    Args:
        body (NewModelDeployment): Model Deployment

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateModelDeploymentResponse400 | CreateModelDeploymentResponse404 | CreateModelDeploymentResponse500 | FailureEnvelopeV1 | ModelDeployment]
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
    body: NewModelDeployment,
) -> (
    CreateModelDeploymentResponse400
    | CreateModelDeploymentResponse404
    | CreateModelDeploymentResponse500
    | FailureEnvelopeV1
    | ModelDeployment
    | None
):
    """Create a new Model Deployment

     Creates a new Model Deployment entity.

    Args:
        body (NewModelDeployment): Model Deployment

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateModelDeploymentResponse400 | CreateModelDeploymentResponse404 | CreateModelDeploymentResponse500 | FailureEnvelopeV1 | ModelDeployment
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: NewModelDeployment,
) -> Response[
    CreateModelDeploymentResponse400
    | CreateModelDeploymentResponse404
    | CreateModelDeploymentResponse500
    | FailureEnvelopeV1
    | ModelDeployment
]:
    """Create a new Model Deployment

     Creates a new Model Deployment entity.

    Args:
        body (NewModelDeployment): Model Deployment

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateModelDeploymentResponse400 | CreateModelDeploymentResponse404 | CreateModelDeploymentResponse500 | FailureEnvelopeV1 | ModelDeployment]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: NewModelDeployment,
) -> (
    CreateModelDeploymentResponse400
    | CreateModelDeploymentResponse404
    | CreateModelDeploymentResponse500
    | FailureEnvelopeV1
    | ModelDeployment
    | None
):
    """Create a new Model Deployment

     Creates a new Model Deployment entity.

    Args:
        body (NewModelDeployment): Model Deployment

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateModelDeploymentResponse400 | CreateModelDeploymentResponse404 | CreateModelDeploymentResponse500 | FailureEnvelopeV1 | ModelDeployment
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
