from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    repository_id: str,
    *,
    directory: None | str | Unset = UNSET,
    branch_name: None | str | Unset = UNSET,
    commit: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_directory: None | str | Unset
    if isinstance(directory, Unset):
        json_directory = UNSET
    else:
        json_directory = directory
    params["directory"] = json_directory

    json_branch_name: None | str | Unset
    if isinstance(branch_name, Unset):
        json_branch_name = UNSET
    else:
        json_branch_name = branch_name
    params["branchName"] = json_branch_name

    json_commit: None | str | Unset
    if isinstance(commit, Unset):
        json_commit = UNSET
    else:
        json_commit = commit
    params["commit"] = json_commit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/gitRepositories/{repository_id}/git/readme".format(
            project_id=quote(str(project_id), safe=""),
            repository_id=quote(str(repository_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | str | None:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
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
) -> Response[DominoApiErrorResponse | str]:
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
    directory: None | str | Unset = UNSET,
    branch_name: None | str | Unset = UNSET,
    commit: None | str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | str]:
    """gets a repository's default readme filename

    Args:
        project_id (str):
        repository_id (str):
        directory (None | str | Unset):
        branch_name (None | str | Unset):
        commit (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | str]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        repository_id=repository_id,
        directory=directory,
        branch_name=branch_name,
        commit=commit,
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
    directory: None | str | Unset = UNSET,
    branch_name: None | str | Unset = UNSET,
    commit: None | str | Unset = UNSET,
) -> DominoApiErrorResponse | str | None:
    """gets a repository's default readme filename

    Args:
        project_id (str):
        repository_id (str):
        directory (None | str | Unset):
        branch_name (None | str | Unset):
        commit (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | str
    """

    return sync_detailed(
        project_id=project_id,
        repository_id=repository_id,
        client=client,
        directory=directory,
        branch_name=branch_name,
        commit=commit,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    repository_id: str,
    *,
    client: AuthenticatedClient | Client,
    directory: None | str | Unset = UNSET,
    branch_name: None | str | Unset = UNSET,
    commit: None | str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | str]:
    """gets a repository's default readme filename

    Args:
        project_id (str):
        repository_id (str):
        directory (None | str | Unset):
        branch_name (None | str | Unset):
        commit (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | str]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        repository_id=repository_id,
        directory=directory,
        branch_name=branch_name,
        commit=commit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    repository_id: str,
    *,
    client: AuthenticatedClient | Client,
    directory: None | str | Unset = UNSET,
    branch_name: None | str | Unset = UNSET,
    commit: None | str | Unset = UNSET,
) -> DominoApiErrorResponse | str | None:
    """gets a repository's default readme filename

    Args:
        project_id (str):
        repository_id (str):
        directory (None | str | Unset):
        branch_name (None | str | Unset):
        commit (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | str
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            repository_id=repository_id,
            client=client,
            directory=directory,
            branch_name=branch_name,
            commit=commit,
        )
    ).parsed
