from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_workspace_api_workspace_session_dto import DominoWorkspaceApiWorkspaceSessionDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    workspace_id: str,
    *,
    offset: int | Unset = 0,
    limit: int | Unset = 5,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspace/project/{project_id}/workspace/{workspace_id}/sessions".format(
            project_id=quote(str(project_id), safe=""),
            workspace_id=quote(str(workspace_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | list[DominoWorkspaceApiWorkspaceSessionDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DominoWorkspaceApiWorkspaceSessionDto.from_dict(response_200_item_data)

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
) -> Response[DominoApiErrorResponse | list[DominoWorkspaceApiWorkspaceSessionDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 5,
) -> Response[DominoApiErrorResponse | list[DominoWorkspaceApiWorkspaceSessionDto]]:
    """List workspace sessions

    Args:
        project_id (str):
        workspace_id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoWorkspaceApiWorkspaceSessionDto]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        workspace_id=workspace_id,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 5,
) -> DominoApiErrorResponse | list[DominoWorkspaceApiWorkspaceSessionDto] | None:
    """List workspace sessions

    Args:
        project_id (str):
        workspace_id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoWorkspaceApiWorkspaceSessionDto]
    """

    return sync_detailed(
        project_id=project_id,
        workspace_id=workspace_id,
        client=client,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 5,
) -> Response[DominoApiErrorResponse | list[DominoWorkspaceApiWorkspaceSessionDto]]:
    """List workspace sessions

    Args:
        project_id (str):
        workspace_id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoWorkspaceApiWorkspaceSessionDto]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        workspace_id=workspace_id,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 5,
) -> DominoApiErrorResponse | list[DominoWorkspaceApiWorkspaceSessionDto] | None:
    """List workspace sessions

    Args:
        project_id (str):
        workspace_id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoWorkspaceApiWorkspaceSessionDto]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            workspace_id=workspace_id,
            client=client,
            offset=offset,
            limit=limit,
        )
    ).parsed
