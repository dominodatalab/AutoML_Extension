from __future__ import annotations
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_service_accounts_response_400 import GetServiceAccountsResponse400
from ...models.paginated_service_account_envelope import PaginatedServiceAccountEnvelope
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include_deactivated: bool | Unset = False,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["includeDeactivated"] = include_deactivated

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/serviceAccounts/v1/serviceAccounts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FailureEnvelopeV1 | GetServiceAccountsResponse400 | PaginatedServiceAccountEnvelope | None:
    if response.status_code == 200:
        response_200 = PaginatedServiceAccountEnvelope.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetServiceAccountsResponse400.from_dict(response.json())

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
) -> Response[FailureEnvelopeV1 | GetServiceAccountsResponse400 | PaginatedServiceAccountEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    include_deactivated: bool | Unset = False,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[FailureEnvelopeV1 | GetServiceAccountsResponse400 | PaginatedServiceAccountEnvelope]:
    """
    Args:
        include_deactivated (bool | Unset):  Default: False.
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetServiceAccountsResponse400 | PaginatedServiceAccountEnvelope]
    """

    kwargs = _get_kwargs(
        include_deactivated=include_deactivated,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    include_deactivated: bool | Unset = False,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> FailureEnvelopeV1 | GetServiceAccountsResponse400 | PaginatedServiceAccountEnvelope | None:
    """
    Args:
        include_deactivated (bool | Unset):  Default: False.
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetServiceAccountsResponse400 | PaginatedServiceAccountEnvelope
    """

    return sync_detailed(
        client=client,
        include_deactivated=include_deactivated,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    include_deactivated: bool | Unset = False,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[FailureEnvelopeV1 | GetServiceAccountsResponse400 | PaginatedServiceAccountEnvelope]:
    """
    Args:
        include_deactivated (bool | Unset):  Default: False.
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetServiceAccountsResponse400 | PaginatedServiceAccountEnvelope]
    """

    kwargs = _get_kwargs(
        include_deactivated=include_deactivated,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    include_deactivated: bool | Unset = False,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> FailureEnvelopeV1 | GetServiceAccountsResponse400 | PaginatedServiceAccountEnvelope | None:
    """
    Args:
        include_deactivated (bool | Unset):  Default: False.
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetServiceAccountsResponse400 | PaginatedServiceAccountEnvelope
    """

    return (
        await asyncio_detailed(
            client=client,
            include_deactivated=include_deactivated,
            offset=offset,
            limit=limit,
        )
    ).parsed
