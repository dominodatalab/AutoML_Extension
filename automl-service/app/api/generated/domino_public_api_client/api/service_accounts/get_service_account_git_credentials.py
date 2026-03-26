from __future__ import annotations
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_service_account_git_credentials_response_404 import GetServiceAccountGitCredentialsResponse404
from ...models.paginated_service_account_git_credentials_accessor_envelope_v1 import (
    PaginatedServiceAccountGitCredentialsAccessorEnvelopeV1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_account_idp_id: str,
    *,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/serviceAccounts/v1/serviceAccounts/{service_account_idp_id}/gitcredentials".format(
            service_account_idp_id=quote(str(service_account_idp_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GetServiceAccountGitCredentialsResponse404
    | PaginatedServiceAccountGitCredentialsAccessorEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedServiceAccountGitCredentialsAccessorEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetServiceAccountGitCredentialsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | GetServiceAccountGitCredentialsResponse404
    | PaginatedServiceAccountGitCredentialsAccessorEnvelopeV1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_account_idp_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1
    | GetServiceAccountGitCredentialsResponse404
    | PaginatedServiceAccountGitCredentialsAccessorEnvelopeV1
]:
    """
    Args:
        service_account_idp_id (str):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetServiceAccountGitCredentialsResponse404 | PaginatedServiceAccountGitCredentialsAccessorEnvelopeV1]
    """

    kwargs = _get_kwargs(
        service_account_idp_id=service_account_idp_id,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_account_idp_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> (
    FailureEnvelopeV1
    | GetServiceAccountGitCredentialsResponse404
    | PaginatedServiceAccountGitCredentialsAccessorEnvelopeV1
    | None
):
    """
    Args:
        service_account_idp_id (str):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetServiceAccountGitCredentialsResponse404 | PaginatedServiceAccountGitCredentialsAccessorEnvelopeV1
    """

    return sync_detailed(
        service_account_idp_id=service_account_idp_id,
        client=client,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    service_account_idp_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1
    | GetServiceAccountGitCredentialsResponse404
    | PaginatedServiceAccountGitCredentialsAccessorEnvelopeV1
]:
    """
    Args:
        service_account_idp_id (str):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetServiceAccountGitCredentialsResponse404 | PaginatedServiceAccountGitCredentialsAccessorEnvelopeV1]
    """

    kwargs = _get_kwargs(
        service_account_idp_id=service_account_idp_id,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_account_idp_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> (
    FailureEnvelopeV1
    | GetServiceAccountGitCredentialsResponse404
    | PaginatedServiceAccountGitCredentialsAccessorEnvelopeV1
    | None
):
    """
    Args:
        service_account_idp_id (str):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetServiceAccountGitCredentialsResponse404 | PaginatedServiceAccountGitCredentialsAccessorEnvelopeV1
    """

    return (
        await asyncio_detailed(
            service_account_idp_id=service_account_idp_id,
            client=client,
            offset=offset,
            limit=limit,
        )
    ).parsed
