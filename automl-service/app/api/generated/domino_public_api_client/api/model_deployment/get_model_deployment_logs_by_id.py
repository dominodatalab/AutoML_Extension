from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_model_deployment_logs_by_id_response_400 import GetModelDeploymentLogsByIdResponse400
from ...models.get_model_deployment_logs_by_id_response_404 import GetModelDeploymentLogsByIdResponse404
from ...models.get_model_deployment_logs_by_id_response_500 import GetModelDeploymentLogsByIdResponse500
from ...models.model_deployment_log_line import ModelDeploymentLogLine
from ...types import Response


def _get_kwargs(
    model_deployment_id: str,
    log_suffix: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/modelServing/v1/modelDeployments/{model_deployment_id}/logs/{log_suffix}".format(
            model_deployment_id=quote(str(model_deployment_id), safe=""),
            log_suffix=quote(str(log_suffix), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GetModelDeploymentLogsByIdResponse400
    | GetModelDeploymentLogsByIdResponse404
    | GetModelDeploymentLogsByIdResponse500
    | list[ModelDeploymentLogLine]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ModelDeploymentLogLine.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = GetModelDeploymentLogsByIdResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetModelDeploymentLogsByIdResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetModelDeploymentLogsByIdResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | GetModelDeploymentLogsByIdResponse400
    | GetModelDeploymentLogsByIdResponse404
    | GetModelDeploymentLogsByIdResponse500
    | list[ModelDeploymentLogLine]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    model_deployment_id: str,
    log_suffix: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    FailureEnvelopeV1
    | GetModelDeploymentLogsByIdResponse400
    | GetModelDeploymentLogsByIdResponse404
    | GetModelDeploymentLogsByIdResponse500
    | list[ModelDeploymentLogLine]
]:
    """Retrieve the logs for a specific Model Deployment

     Retrieves the logs for a specific Model Deployment entity by id.

    Args:
        model_deployment_id (str):
        log_suffix (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetModelDeploymentLogsByIdResponse400 | GetModelDeploymentLogsByIdResponse404 | GetModelDeploymentLogsByIdResponse500 | list[ModelDeploymentLogLine]]
    """

    kwargs = _get_kwargs(
        model_deployment_id=model_deployment_id,
        log_suffix=log_suffix,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    model_deployment_id: str,
    log_suffix: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    FailureEnvelopeV1
    | GetModelDeploymentLogsByIdResponse400
    | GetModelDeploymentLogsByIdResponse404
    | GetModelDeploymentLogsByIdResponse500
    | list[ModelDeploymentLogLine]
    | None
):
    """Retrieve the logs for a specific Model Deployment

     Retrieves the logs for a specific Model Deployment entity by id.

    Args:
        model_deployment_id (str):
        log_suffix (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetModelDeploymentLogsByIdResponse400 | GetModelDeploymentLogsByIdResponse404 | GetModelDeploymentLogsByIdResponse500 | list[ModelDeploymentLogLine]
    """

    return sync_detailed(
        model_deployment_id=model_deployment_id,
        log_suffix=log_suffix,
        client=client,
    ).parsed


async def asyncio_detailed(
    model_deployment_id: str,
    log_suffix: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    FailureEnvelopeV1
    | GetModelDeploymentLogsByIdResponse400
    | GetModelDeploymentLogsByIdResponse404
    | GetModelDeploymentLogsByIdResponse500
    | list[ModelDeploymentLogLine]
]:
    """Retrieve the logs for a specific Model Deployment

     Retrieves the logs for a specific Model Deployment entity by id.

    Args:
        model_deployment_id (str):
        log_suffix (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetModelDeploymentLogsByIdResponse400 | GetModelDeploymentLogsByIdResponse404 | GetModelDeploymentLogsByIdResponse500 | list[ModelDeploymentLogLine]]
    """

    kwargs = _get_kwargs(
        model_deployment_id=model_deployment_id,
        log_suffix=log_suffix,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    model_deployment_id: str,
    log_suffix: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    FailureEnvelopeV1
    | GetModelDeploymentLogsByIdResponse400
    | GetModelDeploymentLogsByIdResponse404
    | GetModelDeploymentLogsByIdResponse500
    | list[ModelDeploymentLogLine]
    | None
):
    """Retrieve the logs for a specific Model Deployment

     Retrieves the logs for a specific Model Deployment entity by id.

    Args:
        model_deployment_id (str):
        log_suffix (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetModelDeploymentLogsByIdResponse400 | GetModelDeploymentLogsByIdResponse404 | GetModelDeploymentLogsByIdResponse500 | list[ModelDeploymentLogLine]
    """

    return (
        await asyncio_detailed(
            model_deployment_id=model_deployment_id,
            log_suffix=log_suffix,
            client=client,
        )
    ).parsed
