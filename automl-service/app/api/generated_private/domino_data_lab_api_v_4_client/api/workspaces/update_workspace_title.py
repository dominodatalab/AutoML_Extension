from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_workspaces_web_update_workspace_title import DominoWorkspacesWebUpdateWorkspaceTitle
from ...types import UNSET, Response


def _get_kwargs(
    workspace_id: str,
    *,
    body: DominoWorkspacesWebUpdateWorkspaceTitle,
    project_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["projectId"] = project_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/workspaces/{workspace_id}/updateTitle".format(
            workspace_id=quote(str(workspace_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | str | None:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
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
) -> Response[DominoApiErrorResponse | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoWorkspacesWebUpdateWorkspaceTitle,
    project_id: str,
) -> Response[DominoApiErrorResponse | str]:
    """Update title of the workspace

    Args:
        workspace_id (str):
        project_id (str):
        body (DominoWorkspacesWebUpdateWorkspaceTitle):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | str]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        body=body,
        project_id=project_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoWorkspacesWebUpdateWorkspaceTitle,
    project_id: str,
) -> DominoApiErrorResponse | str | None:
    """Update title of the workspace

    Args:
        workspace_id (str):
        project_id (str):
        body (DominoWorkspacesWebUpdateWorkspaceTitle):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | str
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        body=body,
        project_id=project_id,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoWorkspacesWebUpdateWorkspaceTitle,
    project_id: str,
) -> Response[DominoApiErrorResponse | str]:
    """Update title of the workspace

    Args:
        workspace_id (str):
        project_id (str):
        body (DominoWorkspacesWebUpdateWorkspaceTitle):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | str]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        body=body,
        project_id=project_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoWorkspacesWebUpdateWorkspaceTitle,
    project_id: str,
) -> DominoApiErrorResponse | str | None:
    """Update title of the workspace

    Args:
        workspace_id (str):
        project_id (str):
        body (DominoWorkspacesWebUpdateWorkspaceTitle):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | str
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            body=body,
            project_id=project_id,
        )
    ).parsed
