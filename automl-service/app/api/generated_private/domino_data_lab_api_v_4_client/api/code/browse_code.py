from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_files_interface_project_code_browse_dto import DominoFilesInterfaceProjectCodeBrowseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    owner_username: str,
    project_name: str,
    path_string: str,
    commit_id_str: None | str | Unset = UNSET,
    branch_name: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["ownerUsername"] = owner_username

    params["projectName"] = project_name

    params["pathString"] = path_string

    json_commit_id_str: None | str | Unset
    if isinstance(commit_id_str, Unset):
        json_commit_id_str = UNSET
    else:
        json_commit_id_str = commit_id_str
    params["commitIdStr"] = json_commit_id_str

    json_branch_name: None | str | Unset
    if isinstance(branch_name, Unset):
        json_branch_name = UNSET
    else:
        json_branch_name = branch_name
    params["branchName"] = json_branch_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/code/browseCode",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoFilesInterfaceProjectCodeBrowseDto | None:
    if response.status_code == 200:
        response_200 = DominoFilesInterfaceProjectCodeBrowseDto.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoFilesInterfaceProjectCodeBrowseDto]:
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
    path_string: str,
    commit_id_str: None | str | Unset = UNSET,
    branch_name: None | str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoFilesInterfaceProjectCodeBrowseDto]:
    """Retrieves directory for browse files table

    Args:
        owner_username (str):
        project_name (str):
        path_string (str):
        commit_id_str (None | str | Unset):
        branch_name (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoFilesInterfaceProjectCodeBrowseDto]
    """

    kwargs = _get_kwargs(
        owner_username=owner_username,
        project_name=project_name,
        path_string=path_string,
        commit_id_str=commit_id_str,
        branch_name=branch_name,
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
    path_string: str,
    commit_id_str: None | str | Unset = UNSET,
    branch_name: None | str | Unset = UNSET,
) -> DominoApiErrorResponse | DominoFilesInterfaceProjectCodeBrowseDto | None:
    """Retrieves directory for browse files table

    Args:
        owner_username (str):
        project_name (str):
        path_string (str):
        commit_id_str (None | str | Unset):
        branch_name (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoFilesInterfaceProjectCodeBrowseDto
    """

    return sync_detailed(
        client=client,
        owner_username=owner_username,
        project_name=project_name,
        path_string=path_string,
        commit_id_str=commit_id_str,
        branch_name=branch_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    owner_username: str,
    project_name: str,
    path_string: str,
    commit_id_str: None | str | Unset = UNSET,
    branch_name: None | str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoFilesInterfaceProjectCodeBrowseDto]:
    """Retrieves directory for browse files table

    Args:
        owner_username (str):
        project_name (str):
        path_string (str):
        commit_id_str (None | str | Unset):
        branch_name (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoFilesInterfaceProjectCodeBrowseDto]
    """

    kwargs = _get_kwargs(
        owner_username=owner_username,
        project_name=project_name,
        path_string=path_string,
        commit_id_str=commit_id_str,
        branch_name=branch_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    owner_username: str,
    project_name: str,
    path_string: str,
    commit_id_str: None | str | Unset = UNSET,
    branch_name: None | str | Unset = UNSET,
) -> DominoApiErrorResponse | DominoFilesInterfaceProjectCodeBrowseDto | None:
    """Retrieves directory for browse files table

    Args:
        owner_username (str):
        project_name (str):
        path_string (str):
        commit_id_str (None | str | Unset):
        branch_name (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoFilesInterfaceProjectCodeBrowseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            owner_username=owner_username,
            project_name=project_name,
            path_string=path_string,
            commit_id_str=commit_id_str,
            branch_name=branch_name,
        )
    ).parsed
