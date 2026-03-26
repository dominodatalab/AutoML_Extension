from __future__ import annotations
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.async_prediction_envelope_v1 import AsyncPredictionEnvelopeV1
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.retrieve_async_prediction_result_response_400 import RetrieveAsyncPredictionResultResponse400
from ...models.retrieve_async_prediction_result_response_404 import RetrieveAsyncPredictionResultResponse404
from ...models.retrieve_async_prediction_result_response_500 import RetrieveAsyncPredictionResultResponse500
from ...types import Response


def _get_kwargs(
    async_model_id: str,
    async_prediction_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/modelApis/async/v1/{async_model_id}/{async_prediction_id}".format(
            async_model_id=quote(str(async_model_id), safe=""),
            async_prediction_id=quote(str(async_prediction_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AsyncPredictionEnvelopeV1
    | FailureEnvelopeV1
    | RetrieveAsyncPredictionResultResponse400
    | RetrieveAsyncPredictionResultResponse404
    | RetrieveAsyncPredictionResultResponse500
    | None
):
    if response.status_code == 200:
        response_200 = AsyncPredictionEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RetrieveAsyncPredictionResultResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = RetrieveAsyncPredictionResultResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = RetrieveAsyncPredictionResultResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AsyncPredictionEnvelopeV1
    | FailureEnvelopeV1
    | RetrieveAsyncPredictionResultResponse400
    | RetrieveAsyncPredictionResultResponse404
    | RetrieveAsyncPredictionResultResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    async_model_id: str,
    async_prediction_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    AsyncPredictionEnvelopeV1
    | FailureEnvelopeV1
    | RetrieveAsyncPredictionResultResponse400
    | RetrieveAsyncPredictionResultResponse404
    | RetrieveAsyncPredictionResultResponse500
]:
    """Retrieve the result of an Async Model prediction

     Retrieve the result of an Async Model prediction

    Args:
        async_model_id (str):
        async_prediction_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncPredictionEnvelopeV1 | FailureEnvelopeV1 | RetrieveAsyncPredictionResultResponse400 | RetrieveAsyncPredictionResultResponse404 | RetrieveAsyncPredictionResultResponse500]
    """

    kwargs = _get_kwargs(
        async_model_id=async_model_id,
        async_prediction_id=async_prediction_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    async_model_id: str,
    async_prediction_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    AsyncPredictionEnvelopeV1
    | FailureEnvelopeV1
    | RetrieveAsyncPredictionResultResponse400
    | RetrieveAsyncPredictionResultResponse404
    | RetrieveAsyncPredictionResultResponse500
    | None
):
    """Retrieve the result of an Async Model prediction

     Retrieve the result of an Async Model prediction

    Args:
        async_model_id (str):
        async_prediction_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncPredictionEnvelopeV1 | FailureEnvelopeV1 | RetrieveAsyncPredictionResultResponse400 | RetrieveAsyncPredictionResultResponse404 | RetrieveAsyncPredictionResultResponse500
    """

    return sync_detailed(
        async_model_id=async_model_id,
        async_prediction_id=async_prediction_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    async_model_id: str,
    async_prediction_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    AsyncPredictionEnvelopeV1
    | FailureEnvelopeV1
    | RetrieveAsyncPredictionResultResponse400
    | RetrieveAsyncPredictionResultResponse404
    | RetrieveAsyncPredictionResultResponse500
]:
    """Retrieve the result of an Async Model prediction

     Retrieve the result of an Async Model prediction

    Args:
        async_model_id (str):
        async_prediction_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncPredictionEnvelopeV1 | FailureEnvelopeV1 | RetrieveAsyncPredictionResultResponse400 | RetrieveAsyncPredictionResultResponse404 | RetrieveAsyncPredictionResultResponse500]
    """

    kwargs = _get_kwargs(
        async_model_id=async_model_id,
        async_prediction_id=async_prediction_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    async_model_id: str,
    async_prediction_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    AsyncPredictionEnvelopeV1
    | FailureEnvelopeV1
    | RetrieveAsyncPredictionResultResponse400
    | RetrieveAsyncPredictionResultResponse404
    | RetrieveAsyncPredictionResultResponse500
    | None
):
    """Retrieve the result of an Async Model prediction

     Retrieve the result of an Async Model prediction

    Args:
        async_model_id (str):
        async_prediction_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncPredictionEnvelopeV1 | FailureEnvelopeV1 | RetrieveAsyncPredictionResultResponse400 | RetrieveAsyncPredictionResultResponse404 | RetrieveAsyncPredictionResultResponse500
    """

    return (
        await asyncio_detailed(
            async_model_id=async_model_id,
            async_prediction_id=async_prediction_id,
            client=client,
        )
    ).parsed
