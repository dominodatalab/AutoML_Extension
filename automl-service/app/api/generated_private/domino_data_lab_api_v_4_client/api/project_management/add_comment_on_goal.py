from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_project_management_web_comment_request import DominoProjectManagementWebCommentRequest
from ...models.domino_project_management_web_error_response import DominoProjectManagementWebErrorResponse
from ...models.domino_projects_api_comment_thread import DominoProjectsApiCommentThread
from ...types import Response


def _get_kwargs(
    goal_id: str,
    *,
    body: DominoProjectManagementWebCommentRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projectManagement/goal/{goal_id}/comment".format(
            goal_id=quote(str(goal_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoProjectManagementWebErrorResponse | DominoProjectsApiCommentThread | None:
    if response.status_code == 200:
        response_200 = DominoProjectsApiCommentThread.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoProjectManagementWebErrorResponse | DominoProjectsApiCommentThread]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    goal_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoProjectManagementWebCommentRequest,
) -> Response[DominoApiErrorResponse | DominoProjectManagementWebErrorResponse | DominoProjectsApiCommentThread]:
    """Add comment on Goal

    Args:
        goal_id (str):
        body (DominoProjectManagementWebCommentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectManagementWebErrorResponse | DominoProjectsApiCommentThread]
    """

    kwargs = _get_kwargs(
        goal_id=goal_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    goal_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoProjectManagementWebCommentRequest,
) -> DominoApiErrorResponse | DominoProjectManagementWebErrorResponse | DominoProjectsApiCommentThread | None:
    """Add comment on Goal

    Args:
        goal_id (str):
        body (DominoProjectManagementWebCommentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectManagementWebErrorResponse | DominoProjectsApiCommentThread
    """

    return sync_detailed(
        goal_id=goal_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    goal_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoProjectManagementWebCommentRequest,
) -> Response[DominoApiErrorResponse | DominoProjectManagementWebErrorResponse | DominoProjectsApiCommentThread]:
    """Add comment on Goal

    Args:
        goal_id (str):
        body (DominoProjectManagementWebCommentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectManagementWebErrorResponse | DominoProjectsApiCommentThread]
    """

    kwargs = _get_kwargs(
        goal_id=goal_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    goal_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoProjectManagementWebCommentRequest,
) -> DominoApiErrorResponse | DominoProjectManagementWebErrorResponse | DominoProjectsApiCommentThread | None:
    """Add comment on Goal

    Args:
        goal_id (str):
        body (DominoProjectManagementWebCommentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectManagementWebErrorResponse | DominoProjectsApiCommentThread
    """

    return (
        await asyncio_detailed(
            goal_id=goal_id,
            client=client,
            body=body,
        )
    ).parsed
