from __future__ import annotations
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_service_account import CreateServiceAccount
from ...models.create_service_account_response_400 import CreateServiceAccountResponse400
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.service_account_envelope import ServiceAccountEnvelope
from ...types import Response


def _get_kwargs(
    *,
    body: CreateServiceAccount,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/serviceAccounts/v1/serviceAccounts",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateServiceAccountResponse400 | FailureEnvelopeV1 | ServiceAccountEnvelope | None:
    if response.status_code == 200:
        response_200 = ServiceAccountEnvelope.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CreateServiceAccountResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateServiceAccountResponse400 | FailureEnvelopeV1 | ServiceAccountEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateServiceAccount,
) -> Response[CreateServiceAccountResponse400 | FailureEnvelopeV1 | ServiceAccountEnvelope]:
    """
    Args:
        body (CreateServiceAccount):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateServiceAccountResponse400 | FailureEnvelopeV1 | ServiceAccountEnvelope]
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
    body: CreateServiceAccount,
) -> CreateServiceAccountResponse400 | FailureEnvelopeV1 | ServiceAccountEnvelope | None:
    """
    Args:
        body (CreateServiceAccount):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateServiceAccountResponse400 | FailureEnvelopeV1 | ServiceAccountEnvelope
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateServiceAccount,
) -> Response[CreateServiceAccountResponse400 | FailureEnvelopeV1 | ServiceAccountEnvelope]:
    """
    Args:
        body (CreateServiceAccount):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateServiceAccountResponse400 | FailureEnvelopeV1 | ServiceAccountEnvelope]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateServiceAccount,
) -> CreateServiceAccountResponse400 | FailureEnvelopeV1 | ServiceAccountEnvelope | None:
    """
    Args:
        body (CreateServiceAccount):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateServiceAccountResponse400 | FailureEnvelopeV1 | ServiceAccountEnvelope
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
