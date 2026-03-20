from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.associate_token_git_credentials_with_service_account_response_400 import (
    AssociateTokenGitCredentialsWithServiceAccountResponse400,
)
from ...models.associate_token_git_credentials_with_service_account_response_404 import (
    AssociateTokenGitCredentialsWithServiceAccountResponse404,
)
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.git_credentials_accessor_envelope_v1 import GitCredentialsAccessorEnvelopeV1
from ...models.token_git_credential import TokenGitCredential
from ...types import Response


def _get_kwargs(
    service_account_idp_id: str,
    *,
    body: TokenGitCredential,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/serviceAccounts/v1/serviceAccounts/{service_account_idp_id}/tokengitcredentials".format(
            service_account_idp_id=quote(str(service_account_idp_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AssociateTokenGitCredentialsWithServiceAccountResponse400
    | AssociateTokenGitCredentialsWithServiceAccountResponse404
    | FailureEnvelopeV1
    | GitCredentialsAccessorEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = GitCredentialsAccessorEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AssociateTokenGitCredentialsWithServiceAccountResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = AssociateTokenGitCredentialsWithServiceAccountResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AssociateTokenGitCredentialsWithServiceAccountResponse400
    | AssociateTokenGitCredentialsWithServiceAccountResponse404
    | FailureEnvelopeV1
    | GitCredentialsAccessorEnvelopeV1
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
    body: TokenGitCredential,
) -> Response[
    AssociateTokenGitCredentialsWithServiceAccountResponse400
    | AssociateTokenGitCredentialsWithServiceAccountResponse404
    | FailureEnvelopeV1
    | GitCredentialsAccessorEnvelopeV1
]:
    """
    Args:
        service_account_idp_id (str):
        body (TokenGitCredential):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssociateTokenGitCredentialsWithServiceAccountResponse400 | AssociateTokenGitCredentialsWithServiceAccountResponse404 | FailureEnvelopeV1 | GitCredentialsAccessorEnvelopeV1]
    """

    kwargs = _get_kwargs(
        service_account_idp_id=service_account_idp_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_account_idp_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TokenGitCredential,
) -> (
    AssociateTokenGitCredentialsWithServiceAccountResponse400
    | AssociateTokenGitCredentialsWithServiceAccountResponse404
    | FailureEnvelopeV1
    | GitCredentialsAccessorEnvelopeV1
    | None
):
    """
    Args:
        service_account_idp_id (str):
        body (TokenGitCredential):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssociateTokenGitCredentialsWithServiceAccountResponse400 | AssociateTokenGitCredentialsWithServiceAccountResponse404 | FailureEnvelopeV1 | GitCredentialsAccessorEnvelopeV1
    """

    return sync_detailed(
        service_account_idp_id=service_account_idp_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    service_account_idp_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TokenGitCredential,
) -> Response[
    AssociateTokenGitCredentialsWithServiceAccountResponse400
    | AssociateTokenGitCredentialsWithServiceAccountResponse404
    | FailureEnvelopeV1
    | GitCredentialsAccessorEnvelopeV1
]:
    """
    Args:
        service_account_idp_id (str):
        body (TokenGitCredential):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssociateTokenGitCredentialsWithServiceAccountResponse400 | AssociateTokenGitCredentialsWithServiceAccountResponse404 | FailureEnvelopeV1 | GitCredentialsAccessorEnvelopeV1]
    """

    kwargs = _get_kwargs(
        service_account_idp_id=service_account_idp_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_account_idp_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TokenGitCredential,
) -> (
    AssociateTokenGitCredentialsWithServiceAccountResponse400
    | AssociateTokenGitCredentialsWithServiceAccountResponse404
    | FailureEnvelopeV1
    | GitCredentialsAccessorEnvelopeV1
    | None
):
    """
    Args:
        service_account_idp_id (str):
        body (TokenGitCredential):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssociateTokenGitCredentialsWithServiceAccountResponse400 | AssociateTokenGitCredentialsWithServiceAccountResponse404 | FailureEnvelopeV1 | GitCredentialsAccessorEnvelopeV1
    """

    return (
        await asyncio_detailed(
            service_account_idp_id=service_account_idp_id,
            client=client,
            body=body,
        )
    ).parsed
