from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.project_config_response import ProjectConfigResponse
from ...models.workspace_config_response_404 import WorkspaceConfigResponse404
from ...models.workspace_config_response_500 import WorkspaceConfigResponse500
from ...types import Response


def _get_kwargs(
    project_id: str,
    workspace_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v4/ppm/projects/{project_id}/workspaces/{workspace_id}/config".format(
            project_id=quote(str(project_id), safe=""),
            workspace_id=quote(str(workspace_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProjectConfigResponse | WorkspaceConfigResponse404 | WorkspaceConfigResponse500 | None:
    if response.status_code == 200:
        response_200 = ProjectConfigResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = WorkspaceConfigResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = WorkspaceConfigResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ProjectConfigResponse | WorkspaceConfigResponse404 | WorkspaceConfigResponse500]:
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
) -> Response[ProjectConfigResponse | WorkspaceConfigResponse404 | WorkspaceConfigResponse500]:
    """Get Workspace PPM Config with Repository Detection

     Get PPM configuration including repositories detected from workspace renv.lock file

    Args:
        project_id (str):
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectConfigResponse | WorkspaceConfigResponse404 | WorkspaceConfigResponse500]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        workspace_id=workspace_id,
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
) -> ProjectConfigResponse | WorkspaceConfigResponse404 | WorkspaceConfigResponse500 | None:
    """Get Workspace PPM Config with Repository Detection

     Get PPM configuration including repositories detected from workspace renv.lock file

    Args:
        project_id (str):
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectConfigResponse | WorkspaceConfigResponse404 | WorkspaceConfigResponse500
    """

    return sync_detailed(
        project_id=project_id,
        workspace_id=workspace_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProjectConfigResponse | WorkspaceConfigResponse404 | WorkspaceConfigResponse500]:
    """Get Workspace PPM Config with Repository Detection

     Get PPM configuration including repositories detected from workspace renv.lock file

    Args:
        project_id (str):
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectConfigResponse | WorkspaceConfigResponse404 | WorkspaceConfigResponse500]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        workspace_id=workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ProjectConfigResponse | WorkspaceConfigResponse404 | WorkspaceConfigResponse500 | None:
    """Get Workspace PPM Config with Repository Detection

     Get PPM configuration including repositories detected from workspace renv.lock file

    Args:
        project_id (str):
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectConfigResponse | WorkspaceConfigResponse404 | WorkspaceConfigResponse500
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            workspace_id=workspace_id,
            client=client,
        )
    ).parsed
