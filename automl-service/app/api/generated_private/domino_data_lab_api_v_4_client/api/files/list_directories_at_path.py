from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_files_interface_project_directory_for_table import DominoFilesInterfaceProjectDirectoryForTable
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    owner_username: str,
    project_name: str,
    file_path: str,
    commit_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["ownerUsername"] = owner_username

    params["projectName"] = project_name

    params["filePath"] = file_path

    params["commitId"] = commit_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/files/browseDirectories",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | list[DominoFilesInterfaceProjectDirectoryForTable] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DominoFilesInterfaceProjectDirectoryForTable.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[DominoApiErrorResponse | list[DominoFilesInterfaceProjectDirectoryForTable]]:
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
    file_path: str,
    commit_id: str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoFilesInterfaceProjectDirectoryForTable]]:
    """Get all directories for a commit at a path in a project

    Args:
        owner_username (str):
        project_name (str):
        file_path (str):
        commit_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoFilesInterfaceProjectDirectoryForTable]]
    """

    kwargs = _get_kwargs(
        owner_username=owner_username,
        project_name=project_name,
        file_path=file_path,
        commit_id=commit_id,
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
    file_path: str,
    commit_id: str | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoFilesInterfaceProjectDirectoryForTable] | None:
    """Get all directories for a commit at a path in a project

    Args:
        owner_username (str):
        project_name (str):
        file_path (str):
        commit_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoFilesInterfaceProjectDirectoryForTable]
    """

    return sync_detailed(
        client=client,
        owner_username=owner_username,
        project_name=project_name,
        file_path=file_path,
        commit_id=commit_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    owner_username: str,
    project_name: str,
    file_path: str,
    commit_id: str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoFilesInterfaceProjectDirectoryForTable]]:
    """Get all directories for a commit at a path in a project

    Args:
        owner_username (str):
        project_name (str):
        file_path (str):
        commit_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoFilesInterfaceProjectDirectoryForTable]]
    """

    kwargs = _get_kwargs(
        owner_username=owner_username,
        project_name=project_name,
        file_path=file_path,
        commit_id=commit_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    owner_username: str,
    project_name: str,
    file_path: str,
    commit_id: str | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoFilesInterfaceProjectDirectoryForTable] | None:
    """Get all directories for a commit at a path in a project

    Args:
        owner_username (str):
        project_name (str):
        file_path (str):
        commit_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoFilesInterfaceProjectDirectoryForTable]
    """

    return (
        await asyncio_detailed(
            client=client,
            owner_username=owner_username,
            project_name=project_name,
            file_path=file_path,
            commit_id=commit_id,
        )
    ).parsed
