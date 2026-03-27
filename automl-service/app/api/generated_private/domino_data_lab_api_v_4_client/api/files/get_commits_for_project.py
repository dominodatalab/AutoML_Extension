from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_files_interface_commit_info import DominoFilesInterfaceCommitInfo
from ...types import UNSET, Response


def _get_kwargs(
    project_id: str,
    *,
    branch_name: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["branchName"] = branch_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/files/{project_id}/commits".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | list[DominoFilesInterfaceCommitInfo] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DominoFilesInterfaceCommitInfo.from_dict(response_200_item_data)

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
) -> Response[DominoApiErrorResponse | list[DominoFilesInterfaceCommitInfo]]:
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
    branch_name: str,
) -> Response[DominoApiErrorResponse | list[DominoFilesInterfaceCommitInfo]]:
    """Get all commits for a branch for a Project

    Args:
        project_id (str):
        branch_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoFilesInterfaceCommitInfo]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        branch_name=branch_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    branch_name: str,
) -> DominoApiErrorResponse | list[DominoFilesInterfaceCommitInfo] | None:
    """Get all commits for a branch for a Project

    Args:
        project_id (str):
        branch_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoFilesInterfaceCommitInfo]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        branch_name=branch_name,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    branch_name: str,
) -> Response[DominoApiErrorResponse | list[DominoFilesInterfaceCommitInfo]]:
    """Get all commits for a branch for a Project

    Args:
        project_id (str):
        branch_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoFilesInterfaceCommitInfo]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        branch_name=branch_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    branch_name: str,
) -> DominoApiErrorResponse | list[DominoFilesInterfaceCommitInfo] | None:
    """Get all commits for a branch for a Project

    Args:
        project_id (str):
        branch_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoFilesInterfaceCommitInfo]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            branch_name=branch_name,
        )
    ).parsed
