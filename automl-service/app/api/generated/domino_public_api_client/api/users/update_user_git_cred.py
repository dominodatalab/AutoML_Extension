from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.git_credential_accessor_envelope_v1 import GitCredentialAccessorEnvelopeV1
from ...models.token_git_credential_v1 import TokenGitCredentialV1
from ...models.update_user_git_cred_response_400 import UpdateUserGitCredResponse400
from ...models.update_user_git_cred_response_404 import UpdateUserGitCredResponse404
from ...models.update_user_git_cred_response_500 import UpdateUserGitCredResponse500
from ...types import Response


def _get_kwargs(
    user_id: str,
    credential_id: str,
    *,
    body: TokenGitCredentialV1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/users/v1/user/{user_id}/tokenCredentials/{credential_id}".format(
            user_id=quote(str(user_id), safe=""),
            credential_id=quote(str(credential_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GitCredentialAccessorEnvelopeV1
    | UpdateUserGitCredResponse400
    | UpdateUserGitCredResponse404
    | UpdateUserGitCredResponse500
    | None
):
    if response.status_code == 200:
        response_200 = GitCredentialAccessorEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateUserGitCredResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UpdateUserGitCredResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = UpdateUserGitCredResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | GitCredentialAccessorEnvelopeV1
    | UpdateUserGitCredResponse400
    | UpdateUserGitCredResponse404
    | UpdateUserGitCredResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    credential_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TokenGitCredentialV1,
) -> Response[
    FailureEnvelopeV1
    | GitCredentialAccessorEnvelopeV1
    | UpdateUserGitCredResponse400
    | UpdateUserGitCredResponse404
    | UpdateUserGitCredResponse500
]:
    """Update git credential accessor for a User

     Update a user's git credential. Required permissions: `UpdateUser`. *Note:* This only supports
    updating GitHub and GitHub Enterprise PATs.

    Args:
        user_id (str):
        credential_id (str):
        body (TokenGitCredentialV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GitCredentialAccessorEnvelopeV1 | UpdateUserGitCredResponse400 | UpdateUserGitCredResponse404 | UpdateUserGitCredResponse500]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        credential_id=credential_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    credential_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TokenGitCredentialV1,
) -> (
    FailureEnvelopeV1
    | GitCredentialAccessorEnvelopeV1
    | UpdateUserGitCredResponse400
    | UpdateUserGitCredResponse404
    | UpdateUserGitCredResponse500
    | None
):
    """Update git credential accessor for a User

     Update a user's git credential. Required permissions: `UpdateUser`. *Note:* This only supports
    updating GitHub and GitHub Enterprise PATs.

    Args:
        user_id (str):
        credential_id (str):
        body (TokenGitCredentialV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GitCredentialAccessorEnvelopeV1 | UpdateUserGitCredResponse400 | UpdateUserGitCredResponse404 | UpdateUserGitCredResponse500
    """

    return sync_detailed(
        user_id=user_id,
        credential_id=credential_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    credential_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TokenGitCredentialV1,
) -> Response[
    FailureEnvelopeV1
    | GitCredentialAccessorEnvelopeV1
    | UpdateUserGitCredResponse400
    | UpdateUserGitCredResponse404
    | UpdateUserGitCredResponse500
]:
    """Update git credential accessor for a User

     Update a user's git credential. Required permissions: `UpdateUser`. *Note:* This only supports
    updating GitHub and GitHub Enterprise PATs.

    Args:
        user_id (str):
        credential_id (str):
        body (TokenGitCredentialV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GitCredentialAccessorEnvelopeV1 | UpdateUserGitCredResponse400 | UpdateUserGitCredResponse404 | UpdateUserGitCredResponse500]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        credential_id=credential_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    credential_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TokenGitCredentialV1,
) -> (
    FailureEnvelopeV1
    | GitCredentialAccessorEnvelopeV1
    | UpdateUserGitCredResponse400
    | UpdateUserGitCredResponse404
    | UpdateUserGitCredResponse500
    | None
):
    """Update git credential accessor for a User

     Update a user's git credential. Required permissions: `UpdateUser`. *Note:* This only supports
    updating GitHub and GitHub Enterprise PATs.

    Args:
        user_id (str):
        credential_id (str):
        body (TokenGitCredentialV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GitCredentialAccessorEnvelopeV1 | UpdateUserGitCredResponse400 | UpdateUserGitCredResponse404 | UpdateUserGitCredResponse500
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            credential_id=credential_id,
            client=client,
            body=body,
        )
    ).parsed
