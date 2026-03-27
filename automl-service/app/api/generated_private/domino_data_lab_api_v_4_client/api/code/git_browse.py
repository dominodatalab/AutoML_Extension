from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_files_interface_project_git_browse_dto import DominoFilesInterfaceProjectGitBrowseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    owner_username: str,
    project_name: str,
    commit_id_str: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["ownerUsername"] = owner_username

    params["projectName"] = project_name

    json_commit_id_str: None | str | Unset
    if isinstance(commit_id_str, Unset):
        json_commit_id_str = UNSET
    else:
        json_commit_id_str = commit_id_str
    params["commitIdStr"] = json_commit_id_str

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/code/gitBrowse",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoFilesInterfaceProjectGitBrowseDto | None:
    if response.status_code == 200:
        response_200 = DominoFilesInterfaceProjectGitBrowseDto.from_dict(response.json())

        return response_200

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
) -> Response[DominoApiErrorResponse | DominoFilesInterfaceProjectGitBrowseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    owner_username: str,
    project_name: str,
    commit_id_str: None | str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoFilesInterfaceProjectGitBrowseDto]:
    """Retrieves directory for browse files table

    Args:
        owner_username (str):
        project_name (str):
        commit_id_str (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoFilesInterfaceProjectGitBrowseDto]
    """

    kwargs = _get_kwargs(
        owner_username=owner_username,
        project_name=project_name,
        commit_id_str=commit_id_str,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    owner_username: str,
    project_name: str,
    commit_id_str: None | str | Unset = UNSET,
) -> DominoApiErrorResponse | DominoFilesInterfaceProjectGitBrowseDto | None:
    """Retrieves directory for browse files table

    Args:
        owner_username (str):
        project_name (str):
        commit_id_str (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoFilesInterfaceProjectGitBrowseDto
    """

    return sync_detailed(
        client=client,
        owner_username=owner_username,
        project_name=project_name,
        commit_id_str=commit_id_str,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    owner_username: str,
    project_name: str,
    commit_id_str: None | str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoFilesInterfaceProjectGitBrowseDto]:
    """Retrieves directory for browse files table

    Args:
        owner_username (str):
        project_name (str):
        commit_id_str (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoFilesInterfaceProjectGitBrowseDto]
    """

    kwargs = _get_kwargs(
        owner_username=owner_username,
        project_name=project_name,
        commit_id_str=commit_id_str,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    owner_username: str,
    project_name: str,
    commit_id_str: None | str | Unset = UNSET,
) -> DominoApiErrorResponse | DominoFilesInterfaceProjectGitBrowseDto | None:
    """Retrieves directory for browse files table

    Args:
        owner_username (str):
        project_name (str):
        commit_id_str (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoFilesInterfaceProjectGitBrowseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            owner_username=owner_username,
            project_name=project_name,
            commit_id_str=commit_id_str,
        )
    ).parsed
