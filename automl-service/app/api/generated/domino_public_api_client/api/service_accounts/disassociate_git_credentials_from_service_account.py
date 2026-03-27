from __future__ import annotations
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.disassociate_git_credentials_from_service_account_response_400 import (
    DisassociateGitCredentialsFromServiceAccountResponse400,
)
from ...models.disassociate_git_credentials_from_service_account_response_404 import (
    DisassociateGitCredentialsFromServiceAccountResponse404,
)
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...types import Response


def _get_kwargs(
    service_account_idp_id: str,
    credential_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/serviceAccounts/v1/serviceAccounts/{service_account_idp_id}/gitcredentials/{credential_id}".format(
            service_account_idp_id=quote(str(service_account_idp_id), safe=""),
            credential_id=quote(str(credential_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DisassociateGitCredentialsFromServiceAccountResponse400
    | DisassociateGitCredentialsFromServiceAccountResponse404
    | FailureEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = DisassociateGitCredentialsFromServiceAccountResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DisassociateGitCredentialsFromServiceAccountResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DisassociateGitCredentialsFromServiceAccountResponse400
    | DisassociateGitCredentialsFromServiceAccountResponse404
    | FailureEnvelopeV1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_account_idp_id: str,
    credential_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DisassociateGitCredentialsFromServiceAccountResponse400
    | DisassociateGitCredentialsFromServiceAccountResponse404
    | FailureEnvelopeV1
]:
    """
    Args:
        service_account_idp_id (str):
        credential_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DisassociateGitCredentialsFromServiceAccountResponse400 | DisassociateGitCredentialsFromServiceAccountResponse404 | FailureEnvelopeV1]
    """

    kwargs = _get_kwargs(
        service_account_idp_id=service_account_idp_id,
        credential_id=credential_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_account_idp_id: str,
    credential_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DisassociateGitCredentialsFromServiceAccountResponse400
    | DisassociateGitCredentialsFromServiceAccountResponse404
    | FailureEnvelopeV1
    | None
):
    """
    Args:
        service_account_idp_id (str):
        credential_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DisassociateGitCredentialsFromServiceAccountResponse400 | DisassociateGitCredentialsFromServiceAccountResponse404 | FailureEnvelopeV1
    """

    return sync_detailed(
        service_account_idp_id=service_account_idp_id,
        credential_id=credential_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    service_account_idp_id: str,
    credential_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DisassociateGitCredentialsFromServiceAccountResponse400
    | DisassociateGitCredentialsFromServiceAccountResponse404
    | FailureEnvelopeV1
]:
    """
    Args:
        service_account_idp_id (str):
        credential_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DisassociateGitCredentialsFromServiceAccountResponse400 | DisassociateGitCredentialsFromServiceAccountResponse404 | FailureEnvelopeV1]
    """

    kwargs = _get_kwargs(
        service_account_idp_id=service_account_idp_id,
        credential_id=credential_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_account_idp_id: str,
    credential_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DisassociateGitCredentialsFromServiceAccountResponse400
    | DisassociateGitCredentialsFromServiceAccountResponse404
    | FailureEnvelopeV1
    | None
):
    """
    Args:
        service_account_idp_id (str):
        credential_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DisassociateGitCredentialsFromServiceAccountResponse400 | DisassociateGitCredentialsFromServiceAccountResponse404 | FailureEnvelopeV1
    """

    return (
        await asyncio_detailed(
            service_account_idp_id=service_account_idp_id,
            credential_id=credential_id,
            client=client,
        )
    ).parsed
