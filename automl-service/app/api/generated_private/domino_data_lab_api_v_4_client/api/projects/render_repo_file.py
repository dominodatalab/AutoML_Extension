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
    file_name: str,
    branch_name: None | str | Unset = UNSET,
    commit: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["fileName"] = file_name

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
        "url": "/projects/{project_id}/gitRepositories/{repository_id}/git/render".format(
            project_id=quote(str(project_id), safe=""),
            repository_id=quote(str(repository_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DominoApiErrorResponse | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
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
) -> Response[Any | DominoApiErrorResponse]:
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
    file_name: str,
    branch_name: None | str | Unset = UNSET,
    commit: None | str | Unset = UNSET,
) -> Response[Any | DominoApiErrorResponse]:
    """returns html to render the file contents

    Args:
        project_id (str):
        repository_id (str):
        file_name (str):
        branch_name (None | str | Unset):
        commit (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DominoApiErrorResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        repository_id=repository_id,
        file_name=file_name,
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
    file_name: str,
    branch_name: None | str | Unset = UNSET,
    commit: None | str | Unset = UNSET,
) -> Any | DominoApiErrorResponse | None:
    """returns html to render the file contents

    Args:
        project_id (str):
        repository_id (str):
        file_name (str):
        branch_name (None | str | Unset):
        commit (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DominoApiErrorResponse
    """

    return sync_detailed(
        project_id=project_id,
        repository_id=repository_id,
        client=client,
        file_name=file_name,
        branch_name=branch_name,
        commit=commit,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    repository_id: str,
    *,
    client: AuthenticatedClient | Client,
    file_name: str,
    branch_name: None | str | Unset = UNSET,
    commit: None | str | Unset = UNSET,
) -> Response[Any | DominoApiErrorResponse]:
    """returns html to render the file contents

    Args:
        project_id (str):
        repository_id (str):
        file_name (str):
        branch_name (None | str | Unset):
        commit (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DominoApiErrorResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        repository_id=repository_id,
        file_name=file_name,
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
    file_name: str,
    branch_name: None | str | Unset = UNSET,
    commit: None | str | Unset = UNSET,
) -> Any | DominoApiErrorResponse | None:
    """returns html to render the file contents

    Args:
        project_id (str):
        repository_id (str):
        file_name (str):
        branch_name (None | str | Unset):
        commit (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DominoApiErrorResponse
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            repository_id=repository_id,
            client=client,
            file_name=file_name,
            branch_name=branch_name,
            commit=commit,
        )
    ).parsed
