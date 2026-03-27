from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_server_account_api_git_credential_accessor_dto import (
    DominoServerAccountApiGitCredentialAccessorDto,
)
from ...types import Response


def _get_kwargs(
    service_account_idp_id: str,
    credential_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/serviceAccounts/{service_account_idp_id}/gitcredentials/{credential_id}".format(
            service_account_idp_id=quote(str(service_account_idp_id), safe=""),
            credential_id=quote(str(credential_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoServerAccountApiGitCredentialAccessorDto | None:
    if response.status_code == 200:
        response_200 = DominoServerAccountApiGitCredentialAccessorDto.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = DominoApiErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DominoApiErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DominoApiErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DominoApiErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = DominoApiErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DominoApiErrorResponse | DominoServerAccountApiGitCredentialAccessorDto]:
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
) -> Response[DominoApiErrorResponse | DominoServerAccountApiGitCredentialAccessorDto]:
    """Remove Git credentials from a service account

    Args:
        service_account_idp_id (str):
        credential_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoServerAccountApiGitCredentialAccessorDto]
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
) -> DominoApiErrorResponse | DominoServerAccountApiGitCredentialAccessorDto | None:
    """Remove Git credentials from a service account

    Args:
        service_account_idp_id (str):
        credential_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoServerAccountApiGitCredentialAccessorDto
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
) -> Response[DominoApiErrorResponse | DominoServerAccountApiGitCredentialAccessorDto]:
    """Remove Git credentials from a service account

    Args:
        service_account_idp_id (str):
        credential_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoServerAccountApiGitCredentialAccessorDto]
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
) -> DominoApiErrorResponse | DominoServerAccountApiGitCredentialAccessorDto | None:
    """Remove Git credentials from a service account

    Args:
        service_account_idp_id (str):
        credential_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoServerAccountApiGitCredentialAccessorDto
    """

    return (
        await asyncio_detailed(
            service_account_idp_id=service_account_idp_id,
            credential_id=credential_id,
            client=client,
        )
    ).parsed
