from __future__ import annotations
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.async_prediction_request_envelope_v1 import AsyncPredictionRequestEnvelopeV1
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.new_async_prediction_v1 import NewAsyncPredictionV1
from ...models.request_async_prediction_response_400 import RequestAsyncPredictionResponse400
from ...models.request_async_prediction_response_404 import RequestAsyncPredictionResponse404
from ...models.request_async_prediction_response_500 import RequestAsyncPredictionResponse500
from ...types import Response


def _get_kwargs(
    async_model_id: str,
    *,
    body: NewAsyncPredictionV1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/modelApis/async/v1/{async_model_id}".format(
            async_model_id=quote(str(async_model_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AsyncPredictionRequestEnvelopeV1
    | FailureEnvelopeV1
    | RequestAsyncPredictionResponse400
    | RequestAsyncPredictionResponse404
    | RequestAsyncPredictionResponse500
    | None
):
    if response.status_code == 200:
        response_200 = AsyncPredictionRequestEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RequestAsyncPredictionResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = RequestAsyncPredictionResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 413:
        response_413 = FailureEnvelopeV1.from_dict(response.json())

        return response_413

    if response.status_code == 422:
        response_422 = FailureEnvelopeV1.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = FailureEnvelopeV1.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RequestAsyncPredictionResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AsyncPredictionRequestEnvelopeV1
    | FailureEnvelopeV1
    | RequestAsyncPredictionResponse400
    | RequestAsyncPredictionResponse404
    | RequestAsyncPredictionResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    async_model_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: NewAsyncPredictionV1,
) -> Response[
    AsyncPredictionRequestEnvelopeV1
    | FailureEnvelopeV1
    | RequestAsyncPredictionResponse400
    | RequestAsyncPredictionResponse404
    | RequestAsyncPredictionResponse500
]:
    """Request a prediction from an Async model

     Request a prediction from an Async Model

    Args:
        async_model_id (str):
        body (NewAsyncPredictionV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncPredictionRequestEnvelopeV1 | FailureEnvelopeV1 | RequestAsyncPredictionResponse400 | RequestAsyncPredictionResponse404 | RequestAsyncPredictionResponse500]
    """

    kwargs = _get_kwargs(
        async_model_id=async_model_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    async_model_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: NewAsyncPredictionV1,
) -> (
    AsyncPredictionRequestEnvelopeV1
    | FailureEnvelopeV1
    | RequestAsyncPredictionResponse400
    | RequestAsyncPredictionResponse404
    | RequestAsyncPredictionResponse500
    | None
):
    """Request a prediction from an Async model

     Request a prediction from an Async Model

    Args:
        async_model_id (str):
        body (NewAsyncPredictionV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncPredictionRequestEnvelopeV1 | FailureEnvelopeV1 | RequestAsyncPredictionResponse400 | RequestAsyncPredictionResponse404 | RequestAsyncPredictionResponse500
    """

    return sync_detailed(
        async_model_id=async_model_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    async_model_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: NewAsyncPredictionV1,
) -> Response[
    AsyncPredictionRequestEnvelopeV1
    | FailureEnvelopeV1
    | RequestAsyncPredictionResponse400
    | RequestAsyncPredictionResponse404
    | RequestAsyncPredictionResponse500
]:
    """Request a prediction from an Async model

     Request a prediction from an Async Model

    Args:
        async_model_id (str):
        body (NewAsyncPredictionV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncPredictionRequestEnvelopeV1 | FailureEnvelopeV1 | RequestAsyncPredictionResponse400 | RequestAsyncPredictionResponse404 | RequestAsyncPredictionResponse500]
    """

    kwargs = _get_kwargs(
        async_model_id=async_model_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    async_model_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: NewAsyncPredictionV1,
) -> (
    AsyncPredictionRequestEnvelopeV1
    | FailureEnvelopeV1
    | RequestAsyncPredictionResponse400
    | RequestAsyncPredictionResponse404
    | RequestAsyncPredictionResponse500
    | None
):
    """Request a prediction from an Async model

     Request a prediction from an Async Model

    Args:
        async_model_id (str):
        body (NewAsyncPredictionV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncPredictionRequestEnvelopeV1 | FailureEnvelopeV1 | RequestAsyncPredictionResponse400 | RequestAsyncPredictionResponse404 | RequestAsyncPredictionResponse500
    """

    return (
        await asyncio_detailed(
            async_model_id=async_model_id,
            client=client,
            body=body,
        )
    ).parsed
