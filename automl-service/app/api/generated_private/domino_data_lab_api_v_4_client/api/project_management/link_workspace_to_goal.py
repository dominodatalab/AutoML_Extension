from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_project_management_api_response_message import DominoProjectManagementApiResponseMessage
from ...models.domino_project_management_web_error_response import DominoProjectManagementWebErrorResponse
from ...models.domino_project_management_web_link_workspace_to_goal_request import (
    DominoProjectManagementWebLinkWorkspaceToGoalRequest,
)
from ...types import Response


def _get_kwargs(
    workspace_id: str,
    *,
    body: DominoProjectManagementWebLinkWorkspaceToGoalRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projectManagement/{workspace_id}/linkWorkspaceToGoal".format(
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
    DominoApiErrorResponse | DominoProjectManagementApiResponseMessage | DominoProjectManagementWebErrorResponse | None
):
    if response.status_code == 200:
        response_200 = DominoProjectManagementApiResponseMessage.from_dict(response.json())

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
        response_409 = DominoProjectManagementWebErrorResponse.from_dict(response.json())

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
) -> Response[
    DominoApiErrorResponse | DominoProjectManagementApiResponseMessage | DominoProjectManagementWebErrorResponse
]:
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
    body: DominoProjectManagementWebLinkWorkspaceToGoalRequest,
) -> Response[
    DominoApiErrorResponse | DominoProjectManagementApiResponseMessage | DominoProjectManagementWebErrorResponse
]:
    """Link workspace to goal

    Args:
        workspace_id (str):
        body (DominoProjectManagementWebLinkWorkspaceToGoalRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectManagementApiResponseMessage | DominoProjectManagementWebErrorResponse]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoProjectManagementWebLinkWorkspaceToGoalRequest,
) -> (
    DominoApiErrorResponse | DominoProjectManagementApiResponseMessage | DominoProjectManagementWebErrorResponse | None
):
    """Link workspace to goal

    Args:
        workspace_id (str):
        body (DominoProjectManagementWebLinkWorkspaceToGoalRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectManagementApiResponseMessage | DominoProjectManagementWebErrorResponse
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoProjectManagementWebLinkWorkspaceToGoalRequest,
) -> Response[
    DominoApiErrorResponse | DominoProjectManagementApiResponseMessage | DominoProjectManagementWebErrorResponse
]:
    """Link workspace to goal

    Args:
        workspace_id (str):
        body (DominoProjectManagementWebLinkWorkspaceToGoalRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectManagementApiResponseMessage | DominoProjectManagementWebErrorResponse]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoProjectManagementWebLinkWorkspaceToGoalRequest,
) -> (
    DominoApiErrorResponse | DominoProjectManagementApiResponseMessage | DominoProjectManagementWebErrorResponse | None
):
    """Link workspace to goal

    Args:
        workspace_id (str):
        body (DominoProjectManagementWebLinkWorkspaceToGoalRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectManagementApiResponseMessage | DominoProjectManagementWebErrorResponse
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            body=body,
        )
    ).parsed
