from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_workspace_session_response_400 import CreateWorkspaceSessionResponse400
from ...models.create_workspace_session_response_404 import CreateWorkspaceSessionResponse404
from ...models.create_workspace_session_response_500 import CreateWorkspaceSessionResponse500
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.new_workspace_session_v1 import NewWorkspaceSessionV1
from ...models.workspace_session_created_envelope_v1 import WorkspaceSessionCreatedEnvelopeV1
from ...types import Response


def _get_kwargs(
    project_id: str,
    workspace_id: str,
    *,
    body: NewWorkspaceSessionV1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/projects/v1/projects/{project_id}/workspaces/{workspace_id}/sessions".format(
            project_id=quote(str(project_id), safe=""),
            workspace_id=quote(str(workspace_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreateWorkspaceSessionResponse400
    | CreateWorkspaceSessionResponse404
    | CreateWorkspaceSessionResponse500
    | FailureEnvelopeV1
    | WorkspaceSessionCreatedEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = WorkspaceSessionCreatedEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CreateWorkspaceSessionResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CreateWorkspaceSessionResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = CreateWorkspaceSessionResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateWorkspaceSessionResponse400
    | CreateWorkspaceSessionResponse404
    | CreateWorkspaceSessionResponse500
    | FailureEnvelopeV1
    | WorkspaceSessionCreatedEnvelopeV1
]:
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
    body: NewWorkspaceSessionV1,
) -> Response[
    CreateWorkspaceSessionResponse400
    | CreateWorkspaceSessionResponse404
    | CreateWorkspaceSessionResponse500
    | FailureEnvelopeV1
    | WorkspaceSessionCreatedEnvelopeV1
]:
    """Create workspace session

     Creates a new session given an existing workspace. Required permissions: `OpenWorkspace`,
    `UseGlobalCompute`

    Args:
        project_id (str):
        workspace_id (str):
        body (NewWorkspaceSessionV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateWorkspaceSessionResponse400 | CreateWorkspaceSessionResponse404 | CreateWorkspaceSessionResponse500 | FailureEnvelopeV1 | WorkspaceSessionCreatedEnvelopeV1]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        workspace_id=workspace_id,
        body=body,
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
    body: NewWorkspaceSessionV1,
) -> (
    CreateWorkspaceSessionResponse400
    | CreateWorkspaceSessionResponse404
    | CreateWorkspaceSessionResponse500
    | FailureEnvelopeV1
    | WorkspaceSessionCreatedEnvelopeV1
    | None
):
    """Create workspace session

     Creates a new session given an existing workspace. Required permissions: `OpenWorkspace`,
    `UseGlobalCompute`

    Args:
        project_id (str):
        workspace_id (str):
        body (NewWorkspaceSessionV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateWorkspaceSessionResponse400 | CreateWorkspaceSessionResponse404 | CreateWorkspaceSessionResponse500 | FailureEnvelopeV1 | WorkspaceSessionCreatedEnvelopeV1
    """

    return sync_detailed(
        project_id=project_id,
        workspace_id=workspace_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: NewWorkspaceSessionV1,
) -> Response[
    CreateWorkspaceSessionResponse400
    | CreateWorkspaceSessionResponse404
    | CreateWorkspaceSessionResponse500
    | FailureEnvelopeV1
    | WorkspaceSessionCreatedEnvelopeV1
]:
    """Create workspace session

     Creates a new session given an existing workspace. Required permissions: `OpenWorkspace`,
    `UseGlobalCompute`

    Args:
        project_id (str):
        workspace_id (str):
        body (NewWorkspaceSessionV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateWorkspaceSessionResponse400 | CreateWorkspaceSessionResponse404 | CreateWorkspaceSessionResponse500 | FailureEnvelopeV1 | WorkspaceSessionCreatedEnvelopeV1]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        workspace_id=workspace_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: NewWorkspaceSessionV1,
) -> (
    CreateWorkspaceSessionResponse400
    | CreateWorkspaceSessionResponse404
    | CreateWorkspaceSessionResponse500
    | FailureEnvelopeV1
    | WorkspaceSessionCreatedEnvelopeV1
    | None
):
    """Create workspace session

     Creates a new session given an existing workspace. Required permissions: `OpenWorkspace`,
    `UseGlobalCompute`

    Args:
        project_id (str):
        workspace_id (str):
        body (NewWorkspaceSessionV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateWorkspaceSessionResponse400 | CreateWorkspaceSessionResponse404 | CreateWorkspaceSessionResponse500 | FailureEnvelopeV1 | WorkspaceSessionCreatedEnvelopeV1
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            workspace_id=workspace_id,
            client=client,
            body=body,
        )
    ).parsed
