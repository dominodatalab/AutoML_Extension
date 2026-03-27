from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_gitproviders_api_get_repos_api_response import DominoGitprovidersApiGetReposApiResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    service_provider: Any,
    credential_id: str,
    user_owner: None | str | Unset = UNSET,
    org_owner: None | str | Unset = UNSET,
    name_query: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["serviceProvider"] = service_provider

    params["credentialId"] = credential_id

    json_user_owner: None | str | Unset
    if isinstance(user_owner, Unset):
        json_user_owner = UNSET
    else:
        json_user_owner = user_owner
    params["userOwner"] = json_user_owner

    json_org_owner: None | str | Unset
    if isinstance(org_owner, Unset):
        json_org_owner = UNSET
    else:
        json_org_owner = org_owner
    params["orgOwner"] = json_org_owner

    params["nameQuery"] = name_query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/gitProviders/metadata/repositories",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoGitprovidersApiGetReposApiResponse | None:
    if response.status_code == 200:
        response_200 = DominoGitprovidersApiGetReposApiResponse.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoGitprovidersApiGetReposApiResponse]:
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
    user_owner: None | str | Unset = UNSET,
    org_owner: None | str | Unset = UNSET,
    name_query: str,
) -> Response[DominoApiErrorResponse | DominoGitprovidersApiGetReposApiResponse]:
    """retrieves potential repos for a given git service provider, credential id, owner, and name query

    Args:
        service_provider (Any):
        credential_id (str):
        user_owner (None | str | Unset):
        org_owner (None | str | Unset):
        name_query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoGitprovidersApiGetReposApiResponse]
    """

    kwargs = _get_kwargs(
        service_provider=service_provider,
        credential_id=credential_id,
        user_owner=user_owner,
        org_owner=org_owner,
        name_query=name_query,
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
    user_owner: None | str | Unset = UNSET,
    org_owner: None | str | Unset = UNSET,
    name_query: str,
) -> DominoApiErrorResponse | DominoGitprovidersApiGetReposApiResponse | None:
    """retrieves potential repos for a given git service provider, credential id, owner, and name query

    Args:
        service_provider (Any):
        credential_id (str):
        user_owner (None | str | Unset):
        org_owner (None | str | Unset):
        name_query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoGitprovidersApiGetReposApiResponse
    """

    return sync_detailed(
        client=client,
        service_provider=service_provider,
        credential_id=credential_id,
        user_owner=user_owner,
        org_owner=org_owner,
        name_query=name_query,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    service_provider: Any,
    credential_id: str,
    user_owner: None | str | Unset = UNSET,
    org_owner: None | str | Unset = UNSET,
    name_query: str,
) -> Response[DominoApiErrorResponse | DominoGitprovidersApiGetReposApiResponse]:
    """retrieves potential repos for a given git service provider, credential id, owner, and name query

    Args:
        service_provider (Any):
        credential_id (str):
        user_owner (None | str | Unset):
        org_owner (None | str | Unset):
        name_query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoGitprovidersApiGetReposApiResponse]
    """

    kwargs = _get_kwargs(
        service_provider=service_provider,
        credential_id=credential_id,
        user_owner=user_owner,
        org_owner=org_owner,
        name_query=name_query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    service_provider: Any,
    credential_id: str,
    user_owner: None | str | Unset = UNSET,
    org_owner: None | str | Unset = UNSET,
    name_query: str,
) -> DominoApiErrorResponse | DominoGitprovidersApiGetReposApiResponse | None:
    """retrieves potential repos for a given git service provider, credential id, owner, and name query

    Args:
        service_provider (Any):
        credential_id (str):
        user_owner (None | str | Unset):
        org_owner (None | str | Unset):
        name_query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoGitprovidersApiGetReposApiResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            service_provider=service_provider,
            credential_id=credential_id,
            user_owner=user_owner,
            org_owner=org_owner,
            name_query=name_query,
        )
    ).parsed
