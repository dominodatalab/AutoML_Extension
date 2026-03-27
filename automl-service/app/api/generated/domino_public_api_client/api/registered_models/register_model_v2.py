from __future__ import annotations
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.new_registered_model_v2 import NewRegisteredModelV2
from ...models.register_model_response_v2 import RegisterModelResponseV2
from ...models.register_model_v2_response_400 import RegisterModelV2Response400
from ...models.register_model_v2_response_404 import RegisterModelV2Response404
from ...models.register_model_v2_response_500 import RegisterModelV2Response500
from ...types import Response


def _get_kwargs(
    *,
    body: NewRegisteredModelV2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/registeredmodels/v2",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | RegisterModelResponseV2
    | RegisterModelV2Response400
    | RegisterModelV2Response404
    | RegisterModelV2Response500
    | None
):
    if response.status_code == 200:
        response_200 = RegisterModelResponseV2.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RegisterModelV2Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = RegisterModelV2Response404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = RegisterModelV2Response500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | RegisterModelResponseV2
    | RegisterModelV2Response400
    | RegisterModelV2Response404
    | RegisterModelV2Response500
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
    body: NewRegisteredModelV2,
) -> Response[
    FailureEnvelopeV1
    | RegisterModelResponseV2
    | RegisterModelV2Response400
    | RegisterModelV2Response404
    | RegisterModelV2Response500
]:
    """Register a model from various sources

     Register a model from various sources using a unified API

    Args:
        body (NewRegisteredModelV2):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | RegisterModelResponseV2 | RegisterModelV2Response400 | RegisterModelV2Response404 | RegisterModelV2Response500]
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
    body: NewRegisteredModelV2,
) -> (
    FailureEnvelopeV1
    | RegisterModelResponseV2
    | RegisterModelV2Response400
    | RegisterModelV2Response404
    | RegisterModelV2Response500
    | None
):
    """Register a model from various sources

     Register a model from various sources using a unified API

    Args:
        body (NewRegisteredModelV2):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | RegisterModelResponseV2 | RegisterModelV2Response400 | RegisterModelV2Response404 | RegisterModelV2Response500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: NewRegisteredModelV2,
) -> Response[
    FailureEnvelopeV1
    | RegisterModelResponseV2
    | RegisterModelV2Response400
    | RegisterModelV2Response404
    | RegisterModelV2Response500
]:
    """Register a model from various sources

     Register a model from various sources using a unified API

    Args:
        body (NewRegisteredModelV2):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | RegisterModelResponseV2 | RegisterModelV2Response400 | RegisterModelV2Response404 | RegisterModelV2Response500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: NewRegisteredModelV2,
) -> (
    FailureEnvelopeV1
    | RegisterModelResponseV2
    | RegisterModelV2Response400
    | RegisterModelV2Response404
    | RegisterModelV2Response500
    | None
):
    """Register a model from various sources

     Register a model from various sources using a unified API

    Args:
        body (NewRegisteredModelV2):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | RegisterModelResponseV2 | RegisterModelV2Response400 | RegisterModelV2Response404 | RegisterModelV2Response500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
