from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_projects_api_repositories_reference_dto import DominoProjectsApiRepositoriesReferenceDTO
from ...models.domino_projects_api_repositories_responses_git_api_response_wrapperdomino_projects_api_repositories_responses_get_repo_files_api_response import (
    DominoProjectsApiRepositoriesResponsesGitApiResponseWrapperdominoProjectsApiRepositoriesResponsesGetRepoFilesApiResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    repository_id: str,
    *,
    body: DominoProjectsApiRepositoriesReferenceDTO,
    search_pattern: None | str | Unset = UNSET,
    max_results: int | None | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_search_pattern: None | str | Unset
    if isinstance(search_pattern, Unset):
        json_search_pattern = UNSET
    else:
        json_search_pattern = search_pattern
    params["searchPattern"] = json_search_pattern

    json_max_results: int | None | Unset
    if isinstance(max_results, Unset):
        json_max_results = UNSET
    else:
        json_max_results = max_results
    params["maxResults"] = json_max_results

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/gitRepositories/{repository_id}/git/filesV2".format(
            project_id=quote(str(project_id), safe=""),
            repository_id=quote(str(repository_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DominoApiErrorResponse
    | DominoProjectsApiRepositoriesResponsesGitApiResponseWrapperdominoProjectsApiRepositoriesResponsesGetRepoFilesApiResponse
    | None
):
    if response.status_code == 200:
        response_200 = DominoProjectsApiRepositoriesResponsesGitApiResponseWrapperdominoProjectsApiRepositoriesResponsesGetRepoFilesApiResponse.from_dict(
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
    | DominoProjectsApiRepositoriesResponsesGitApiResponseWrapperdominoProjectsApiRepositoriesResponsesGetRepoFilesApiResponse
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    repository_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoProjectsApiRepositoriesReferenceDTO,
    search_pattern: None | str | Unset = UNSET,
    max_results: int | None | Unset = UNSET,
) -> Response[
    DominoApiErrorResponse
    | DominoProjectsApiRepositoriesResponsesGitApiResponseWrapperdominoProjectsApiRepositoriesResponsesGetRepoFilesApiResponse
]:
    """gets a list of a repository's files

    Args:
        project_id (str):
        repository_id (str):
        search_pattern (None | str | Unset):
        max_results (int | None | Unset):
        body (DominoProjectsApiRepositoriesReferenceDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectsApiRepositoriesResponsesGitApiResponseWrapperdominoProjectsApiRepositoriesResponsesGetRepoFilesApiResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        repository_id=repository_id,
        body=body,
        search_pattern=search_pattern,
        max_results=max_results,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    repository_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoProjectsApiRepositoriesReferenceDTO,
    search_pattern: None | str | Unset = UNSET,
    max_results: int | None | Unset = UNSET,
) -> (
    DominoApiErrorResponse
    | DominoProjectsApiRepositoriesResponsesGitApiResponseWrapperdominoProjectsApiRepositoriesResponsesGetRepoFilesApiResponse
    | None
):
    """gets a list of a repository's files

    Args:
        project_id (str):
        repository_id (str):
        search_pattern (None | str | Unset):
        max_results (int | None | Unset):
        body (DominoProjectsApiRepositoriesReferenceDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectsApiRepositoriesResponsesGitApiResponseWrapperdominoProjectsApiRepositoriesResponsesGetRepoFilesApiResponse
    """

    return sync_detailed(
        project_id=project_id,
        repository_id=repository_id,
        client=client,
        body=body,
        search_pattern=search_pattern,
        max_results=max_results,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    repository_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoProjectsApiRepositoriesReferenceDTO,
    search_pattern: None | str | Unset = UNSET,
    max_results: int | None | Unset = UNSET,
) -> Response[
    DominoApiErrorResponse
    | DominoProjectsApiRepositoriesResponsesGitApiResponseWrapperdominoProjectsApiRepositoriesResponsesGetRepoFilesApiResponse
]:
    """gets a list of a repository's files

    Args:
        project_id (str):
        repository_id (str):
        search_pattern (None | str | Unset):
        max_results (int | None | Unset):
        body (DominoProjectsApiRepositoriesReferenceDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectsApiRepositoriesResponsesGitApiResponseWrapperdominoProjectsApiRepositoriesResponsesGetRepoFilesApiResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        repository_id=repository_id,
        body=body,
        search_pattern=search_pattern,
        max_results=max_results,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    repository_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoProjectsApiRepositoriesReferenceDTO,
    search_pattern: None | str | Unset = UNSET,
    max_results: int | None | Unset = UNSET,
) -> (
    DominoApiErrorResponse
    | DominoProjectsApiRepositoriesResponsesGitApiResponseWrapperdominoProjectsApiRepositoriesResponsesGetRepoFilesApiResponse
    | None
):
    """gets a list of a repository's files

    Args:
        project_id (str):
        repository_id (str):
        search_pattern (None | str | Unset):
        max_results (int | None | Unset):
        body (DominoProjectsApiRepositoriesReferenceDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectsApiRepositoriesResponsesGitApiResponseWrapperdominoProjectsApiRepositoriesResponsesGetRepoFilesApiResponse
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            repository_id=repository_id,
            client=client,
            body=body,
            search_pattern=search_pattern,
            max_results=max_results,
        )
    ).parsed
