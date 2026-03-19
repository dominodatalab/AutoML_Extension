from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.model_deployment import ModelDeployment
from ...models.update_model_deployment_response_400 import UpdateModelDeploymentResponse400
from ...models.update_model_deployment_response_404 import UpdateModelDeploymentResponse404
from ...models.update_model_deployment_response_500 import UpdateModelDeploymentResponse500
from ...models.updated_model_deployment import UpdatedModelDeployment
from ...types import Response


def _get_kwargs(
    model_deployment_id: str,
    *,
    body: UpdatedModelDeployment,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/modelServing/v1/modelDeployments/{model_deployment_id}".format(
            model_deployment_id=quote(str(model_deployment_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | ModelDeployment
    | UpdateModelDeploymentResponse400
    | UpdateModelDeploymentResponse404
    | UpdateModelDeploymentResponse500
    | None
):
    if response.status_code == 200:
        response_200 = ModelDeployment.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateModelDeploymentResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UpdateModelDeploymentResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = UpdateModelDeploymentResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | ModelDeployment
    | UpdateModelDeploymentResponse400
    | UpdateModelDeploymentResponse404
    | UpdateModelDeploymentResponse500
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
    body: UpdatedModelDeployment,
) -> Response[
    FailureEnvelopeV1
    | ModelDeployment
    | UpdateModelDeploymentResponse400
    | UpdateModelDeploymentResponse404
    | UpdateModelDeploymentResponse500
]:
    """Update a Model Deployment

     Update fields of a Model Deployment entity by id.

    Args:
        model_deployment_id (str):
        body (UpdatedModelDeployment): Model Deployment

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | ModelDeployment | UpdateModelDeploymentResponse400 | UpdateModelDeploymentResponse404 | UpdateModelDeploymentResponse500]
    """

    kwargs = _get_kwargs(
        model_deployment_id=model_deployment_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    model_deployment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatedModelDeployment,
) -> (
    FailureEnvelopeV1
    | ModelDeployment
    | UpdateModelDeploymentResponse400
    | UpdateModelDeploymentResponse404
    | UpdateModelDeploymentResponse500
    | None
):
    """Update a Model Deployment

     Update fields of a Model Deployment entity by id.

    Args:
        model_deployment_id (str):
        body (UpdatedModelDeployment): Model Deployment

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | ModelDeployment | UpdateModelDeploymentResponse400 | UpdateModelDeploymentResponse404 | UpdateModelDeploymentResponse500
    """

    return sync_detailed(
        model_deployment_id=model_deployment_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    model_deployment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatedModelDeployment,
) -> Response[
    FailureEnvelopeV1
    | ModelDeployment
    | UpdateModelDeploymentResponse400
    | UpdateModelDeploymentResponse404
    | UpdateModelDeploymentResponse500
]:
    """Update a Model Deployment

     Update fields of a Model Deployment entity by id.

    Args:
        model_deployment_id (str):
        body (UpdatedModelDeployment): Model Deployment

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | ModelDeployment | UpdateModelDeploymentResponse400 | UpdateModelDeploymentResponse404 | UpdateModelDeploymentResponse500]
    """

    kwargs = _get_kwargs(
        model_deployment_id=model_deployment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    model_deployment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatedModelDeployment,
) -> (
    FailureEnvelopeV1
    | ModelDeployment
    | UpdateModelDeploymentResponse400
    | UpdateModelDeploymentResponse404
    | UpdateModelDeploymentResponse500
    | None
):
    """Update a Model Deployment

     Update fields of a Model Deployment entity by id.

    Args:
        model_deployment_id (str):
        body (UpdatedModelDeployment): Model Deployment

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | ModelDeployment | UpdateModelDeploymentResponse400 | UpdateModelDeploymentResponse404 | UpdateModelDeploymentResponse500
    """

    return (
        await asyncio_detailed(
            model_deployment_id=model_deployment_id,
            client=client,
            body=body,
        )
    ).parsed
