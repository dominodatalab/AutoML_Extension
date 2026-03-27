from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_projects_api_repositories_responses_git_api_response_wrapperdomino_gitproviders_api_get_owners_api_response import (
    DominoProjectsApiRepositoriesResponsesGitApiResponseWrapperdominoGitprovidersApiGetOwnersApiResponse,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    service_provider: Any,
    credential_id: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["serviceProvider"] = service_provider

    params["credentialId"] = credential_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/gitProviders/metadata/owners",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DominoApiErrorResponse
    | DominoProjectsApiRepositoriesResponsesGitApiResponseWrapperdominoGitprovidersApiGetOwnersApiResponse
    | None
):
    if response.status_code == 200:
        response_200 = DominoProjectsApiRepositoriesResponsesGitApiResponseWrapperdominoGitprovidersApiGetOwnersApiResponse.from_dict(
            response.json()
        )

        return response_200

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
) -> Response[
    DominoApiErrorResponse
    | DominoProjectsApiRepositoriesResponsesGitApiResponseWrapperdominoGitprovidersApiGetOwnersApiResponse
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
    service_provider: Any,
    credential_id: str,
) -> Response[
    DominoApiErrorResponse
    | DominoProjectsApiRepositoriesResponsesGitApiResponseWrapperdominoGitprovidersApiGetOwnersApiResponse
]:
    """retrieves potential owners for a given git service provider and credential id

    Args:
        service_provider (Any):
        credential_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectsApiRepositoriesResponsesGitApiResponseWrapperdominoGitprovidersApiGetOwnersApiResponse]
    """

    kwargs = _get_kwargs(
        service_provider=service_provider,
        credential_id=credential_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    service_provider: Any,
    credential_id: str,
) -> (
    DominoApiErrorResponse
    | DominoProjectsApiRepositoriesResponsesGitApiResponseWrapperdominoGitprovidersApiGetOwnersApiResponse
    | None
):
    """retrieves potential owners for a given git service provider and credential id

    Args:
        service_provider (Any):
        credential_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectsApiRepositoriesResponsesGitApiResponseWrapperdominoGitprovidersApiGetOwnersApiResponse
    """

    return sync_detailed(
        client=client,
        service_provider=service_provider,
        credential_id=credential_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    service_provider: Any,
    credential_id: str,
) -> Response[
    DominoApiErrorResponse
    | DominoProjectsApiRepositoriesResponsesGitApiResponseWrapperdominoGitprovidersApiGetOwnersApiResponse
]:
    """retrieves potential owners for a given git service provider and credential id

    Args:
        service_provider (Any):
        credential_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectsApiRepositoriesResponsesGitApiResponseWrapperdominoGitprovidersApiGetOwnersApiResponse]
    """

    kwargs = _get_kwargs(
        service_provider=service_provider,
        credential_id=credential_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    service_provider: Any,
    credential_id: str,
) -> (
    DominoApiErrorResponse
    | DominoProjectsApiRepositoriesResponsesGitApiResponseWrapperdominoGitprovidersApiGetOwnersApiResponse
    | None
):
    """retrieves potential owners for a given git service provider and credential id

    Args:
        service_provider (Any):
        credential_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectsApiRepositoriesResponsesGitApiResponseWrapperdominoGitprovidersApiGetOwnersApiResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            service_provider=service_provider,
            credential_id=credential_id,
        )
    ).parsed
