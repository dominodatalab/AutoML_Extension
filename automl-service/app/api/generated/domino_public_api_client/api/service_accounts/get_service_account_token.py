from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_service_account_token_response_404 import GetServiceAccountTokenResponse404
from ...models.service_account_token_envelope import ServiceAccountTokenEnvelope
from ...types import Response


def _get_kwargs(
    service_account_idp_id: str,
    token_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/serviceAccounts/v1/serviceAccounts/{service_account_idp_id}/tokens/{token_name}".format(
            service_account_idp_id=quote(str(service_account_idp_id), safe=""),
            token_name=quote(str(token_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FailureEnvelopeV1 | GetServiceAccountTokenResponse404 | ServiceAccountTokenEnvelope | None:
    if response.status_code == 200:
        response_200 = ServiceAccountTokenEnvelope.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetServiceAccountTokenResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FailureEnvelopeV1 | GetServiceAccountTokenResponse404 | ServiceAccountTokenEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_account_idp_id: str,
    token_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[FailureEnvelopeV1 | GetServiceAccountTokenResponse404 | ServiceAccountTokenEnvelope]:
    """
    Args:
        service_account_idp_id (str):
        token_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetServiceAccountTokenResponse404 | ServiceAccountTokenEnvelope]
    """

    kwargs = _get_kwargs(
        service_account_idp_id=service_account_idp_id,
        token_name=token_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_account_idp_id: str,
    token_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> FailureEnvelopeV1 | GetServiceAccountTokenResponse404 | ServiceAccountTokenEnvelope | None:
    """
    Args:
        service_account_idp_id (str):
        token_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetServiceAccountTokenResponse404 | ServiceAccountTokenEnvelope
    """

    return sync_detailed(
        service_account_idp_id=service_account_idp_id,
        token_name=token_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    service_account_idp_id: str,
    token_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[FailureEnvelopeV1 | GetServiceAccountTokenResponse404 | ServiceAccountTokenEnvelope]:
    """
    Args:
        service_account_idp_id (str):
        token_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetServiceAccountTokenResponse404 | ServiceAccountTokenEnvelope]
    """

    kwargs = _get_kwargs(
        service_account_idp_id=service_account_idp_id,
        token_name=token_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_account_idp_id: str,
    token_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> FailureEnvelopeV1 | GetServiceAccountTokenResponse404 | ServiceAccountTokenEnvelope | None:
    """
    Args:
        service_account_idp_id (str):
        token_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetServiceAccountTokenResponse404 | ServiceAccountTokenEnvelope
    """

    return (
        await asyncio_detailed(
            service_account_idp_id=service_account_idp_id,
            token_name=token_name,
            client=client,
        )
    ).parsed
