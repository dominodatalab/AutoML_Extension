from __future__ import annotations
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_imported_repos_response_400 import GetImportedReposResponse400
from ...models.get_imported_repos_response_404 import GetImportedReposResponse404
from ...models.get_imported_repos_response_500 import GetImportedReposResponse500
from ...models.paginated_git_repositories_envelope_v1 import PaginatedGitRepositoriesEnvelopeV1
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
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
        "url": "/api/projects/v1/projects/{project_id}/repositories".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GetImportedReposResponse400
    | GetImportedReposResponse404
    | GetImportedReposResponse500
    | PaginatedGitRepositoriesEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedGitRepositoriesEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetImportedReposResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetImportedReposResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetImportedReposResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | GetImportedReposResponse400
    | GetImportedReposResponse404
    | GetImportedReposResponse500
    | PaginatedGitRepositoriesEnvelopeV1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1
    | GetImportedReposResponse400
    | GetImportedReposResponse404
    | GetImportedReposResponse500
    | PaginatedGitRepositoriesEnvelopeV1
]:
    """Get all imported git repositories in this project

     Get all imported git repositories in this project. Required permissions: `ListProject`

    Args:
        project_id (str):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetImportedReposResponse400 | GetImportedReposResponse404 | GetImportedReposResponse500 | PaginatedGitRepositoriesEnvelopeV1]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> (
    FailureEnvelopeV1
    | GetImportedReposResponse400
    | GetImportedReposResponse404
    | GetImportedReposResponse500
    | PaginatedGitRepositoriesEnvelopeV1
    | None
):
    """Get all imported git repositories in this project

     Get all imported git repositories in this project. Required permissions: `ListProject`

    Args:
        project_id (str):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetImportedReposResponse400 | GetImportedReposResponse404 | GetImportedReposResponse500 | PaginatedGitRepositoriesEnvelopeV1
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1
    | GetImportedReposResponse400
    | GetImportedReposResponse404
    | GetImportedReposResponse500
    | PaginatedGitRepositoriesEnvelopeV1
]:
    """Get all imported git repositories in this project

     Get all imported git repositories in this project. Required permissions: `ListProject`

    Args:
        project_id (str):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetImportedReposResponse400 | GetImportedReposResponse404 | GetImportedReposResponse500 | PaginatedGitRepositoriesEnvelopeV1]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> (
    FailureEnvelopeV1
    | GetImportedReposResponse400
    | GetImportedReposResponse404
    | GetImportedReposResponse500
    | PaginatedGitRepositoriesEnvelopeV1
    | None
):
    """Get all imported git repositories in this project

     Get all imported git repositories in this project. Required permissions: `ListProject`

    Args:
        project_id (str):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetImportedReposResponse400 | GetImportedReposResponse404 | GetImportedReposResponse500 | PaginatedGitRepositoriesEnvelopeV1
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            offset=offset,
            limit=limit,
        )
    ).parsed
