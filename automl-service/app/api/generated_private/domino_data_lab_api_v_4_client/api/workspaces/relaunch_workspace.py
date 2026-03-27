from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_workspaces_api_workspace import DominoWorkspacesApiWorkspace
from ...models.domino_workspaces_web_workspace_relaunch_operation_request import (
    DominoWorkspacesWebWorkspaceRelaunchOperationRequest,
)
from ...models.relaunch_workspace_response_409 import RelaunchWorkspaceResponse409
from ...types import Response


def _get_kwargs(
    *,
    body: DominoWorkspacesWebWorkspaceRelaunchOperationRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/workspaces/relaunch",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoWorkspacesApiWorkspace | RelaunchWorkspaceResponse409 | None:
    if response.status_code == 200:
        response_200 = DominoWorkspacesApiWorkspace.from_dict(response.json())

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

    if response.status_code == 409:
        response_409 = RelaunchWorkspaceResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 500:
        response_500 = DominoApiErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DominoApiErrorResponse | DominoWorkspacesApiWorkspace | RelaunchWorkspaceResponse409]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DominoWorkspacesWebWorkspaceRelaunchOperationRequest,
) -> Response[DominoApiErrorResponse | DominoWorkspacesApiWorkspace | RelaunchWorkspaceResponse409]:
    """Relaunch a Workspace for the given Project

    Args:
        body (DominoWorkspacesWebWorkspaceRelaunchOperationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoWorkspacesApiWorkspace | RelaunchWorkspaceResponse409]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: DominoWorkspacesWebWorkspaceRelaunchOperationRequest,
) -> DominoApiErrorResponse | DominoWorkspacesApiWorkspace | RelaunchWorkspaceResponse409 | None:
    """Relaunch a Workspace for the given Project

    Args:
        body (DominoWorkspacesWebWorkspaceRelaunchOperationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoWorkspacesApiWorkspace | RelaunchWorkspaceResponse409
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DominoWorkspacesWebWorkspaceRelaunchOperationRequest,
) -> Response[DominoApiErrorResponse | DominoWorkspacesApiWorkspace | RelaunchWorkspaceResponse409]:
    """Relaunch a Workspace for the given Project

    Args:
        body (DominoWorkspacesWebWorkspaceRelaunchOperationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoWorkspacesApiWorkspace | RelaunchWorkspaceResponse409]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DominoWorkspacesWebWorkspaceRelaunchOperationRequest,
) -> DominoApiErrorResponse | DominoWorkspacesApiWorkspace | RelaunchWorkspaceResponse409 | None:
    """Relaunch a Workspace for the given Project

    Args:
        body (DominoWorkspacesWebWorkspaceRelaunchOperationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoWorkspacesApiWorkspace | RelaunchWorkspaceResponse409
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
