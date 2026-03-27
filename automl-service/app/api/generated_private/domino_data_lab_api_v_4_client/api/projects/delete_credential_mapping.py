from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_projects_api_repositories_credential_mapping_dto import (
    DominoProjectsApiRepositoriesCredentialMappingDTO,
)
from ...types import Response


def _get_kwargs(
    project_id: str,
    repo_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/projects/{project_id}/repository/{repo_id}/credentialMapping".format(
            project_id=quote(str(project_id), safe=""),
            repo_id=quote(str(repo_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoProjectsApiRepositoriesCredentialMappingDTO | None:
    if response.status_code == 200:
        response_200 = DominoProjectsApiRepositoriesCredentialMappingDTO.from_dict(response.json())

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

    if response.status_code == 500:
        response_500 = DominoApiErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DominoApiErrorResponse | DominoProjectsApiRepositoriesCredentialMappingDTO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    repo_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DominoApiErrorResponse | DominoProjectsApiRepositoriesCredentialMappingDTO]:
    """delete credential mapping for a specific user-project-repo combination

    Args:
        project_id (str):
        repo_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectsApiRepositoriesCredentialMappingDTO]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        repo_id=repo_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    repo_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> DominoApiErrorResponse | DominoProjectsApiRepositoriesCredentialMappingDTO | None:
    """delete credential mapping for a specific user-project-repo combination

    Args:
        project_id (str):
        repo_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectsApiRepositoriesCredentialMappingDTO
    """

    return sync_detailed(
        project_id=project_id,
        repo_id=repo_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    repo_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DominoApiErrorResponse | DominoProjectsApiRepositoriesCredentialMappingDTO]:
    """delete credential mapping for a specific user-project-repo combination

    Args:
        project_id (str):
        repo_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectsApiRepositoriesCredentialMappingDTO]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        repo_id=repo_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    repo_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> DominoApiErrorResponse | DominoProjectsApiRepositoriesCredentialMappingDTO | None:
    """delete credential mapping for a specific user-project-repo combination

    Args:
        project_id (str):
        repo_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectsApiRepositoriesCredentialMappingDTO
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            repo_id=repo_id,
            client=client,
        )
    ).parsed
