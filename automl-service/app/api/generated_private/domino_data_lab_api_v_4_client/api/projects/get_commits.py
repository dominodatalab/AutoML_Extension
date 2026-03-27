from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_projects_api_repositories_responses_get_commits_api_response import (
    DominoProjectsApiRepositoriesResponsesGetCommitsApiResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    repository_id: str,
    *,
    branch: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_branch: None | str | Unset
    if isinstance(branch, Unset):
        json_branch = UNSET
    else:
        json_branch = branch
    params["branch"] = json_branch

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/gitRepositories/{repository_id}/git/commits".format(
            project_id=quote(str(project_id), safe=""),
            repository_id=quote(str(repository_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoProjectsApiRepositoriesResponsesGetCommitsApiResponse | None:
    if response.status_code == 200:
        response_200 = DominoProjectsApiRepositoriesResponsesGetCommitsApiResponse.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoProjectsApiRepositoriesResponsesGetCommitsApiResponse]:
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
    branch: None | str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoProjectsApiRepositoriesResponsesGetCommitsApiResponse]:
    """retrieves list of a repository's commits

    Args:
        project_id (str):
        repository_id (str):
        branch (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectsApiRepositoriesResponsesGetCommitsApiResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        repository_id=repository_id,
        branch=branch,
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
    branch: None | str | Unset = UNSET,
) -> DominoApiErrorResponse | DominoProjectsApiRepositoriesResponsesGetCommitsApiResponse | None:
    """retrieves list of a repository's commits

    Args:
        project_id (str):
        repository_id (str):
        branch (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectsApiRepositoriesResponsesGetCommitsApiResponse
    """

    return sync_detailed(
        project_id=project_id,
        repository_id=repository_id,
        client=client,
        branch=branch,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    repository_id: str,
    *,
    client: AuthenticatedClient | Client,
    branch: None | str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoProjectsApiRepositoriesResponsesGetCommitsApiResponse]:
    """retrieves list of a repository's commits

    Args:
        project_id (str):
        repository_id (str):
        branch (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectsApiRepositoriesResponsesGetCommitsApiResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        repository_id=repository_id,
        branch=branch,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    repository_id: str,
    *,
    client: AuthenticatedClient | Client,
    branch: None | str | Unset = UNSET,
) -> DominoApiErrorResponse | DominoProjectsApiRepositoriesResponsesGetCommitsApiResponse | None:
    """retrieves list of a repository's commits

    Args:
        project_id (str):
        repository_id (str):
        branch (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectsApiRepositoriesResponsesGetCommitsApiResponse
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            repository_id=repository_id,
            client=client,
            branch=branch,
        )
    ).parsed
