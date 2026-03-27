from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_projects_api_comment import DominoProjectsApiComment
from ...models.domino_projects_web_update_comment_info import DominoProjectsWebUpdateCommentInfo
from ...types import Response


def _get_kwargs(
    project_id: str,
    goal_id: str,
    *,
    body: DominoProjectsWebUpdateCommentInfo,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/projects/{project_id}/{goal_id}/comment".format(
            project_id=quote(str(project_id), safe=""),
            goal_id=quote(str(goal_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoProjectsApiComment | None:
    if response.status_code == 200:
        response_200 = DominoProjectsApiComment.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoProjectsApiComment]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    goal_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoProjectsWebUpdateCommentInfo,
) -> Response[DominoApiErrorResponse | DominoProjectsApiComment]:
    """Update comment on Goal

    Args:
        project_id (str):
        goal_id (str):
        body (DominoProjectsWebUpdateCommentInfo):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectsApiComment]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        goal_id=goal_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    goal_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoProjectsWebUpdateCommentInfo,
) -> DominoApiErrorResponse | DominoProjectsApiComment | None:
    """Update comment on Goal

    Args:
        project_id (str):
        goal_id (str):
        body (DominoProjectsWebUpdateCommentInfo):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectsApiComment
    """

    return sync_detailed(
        project_id=project_id,
        goal_id=goal_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    goal_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoProjectsWebUpdateCommentInfo,
) -> Response[DominoApiErrorResponse | DominoProjectsApiComment]:
    """Update comment on Goal

    Args:
        project_id (str):
        goal_id (str):
        body (DominoProjectsWebUpdateCommentInfo):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectsApiComment]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        goal_id=goal_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    goal_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoProjectsWebUpdateCommentInfo,
) -> DominoApiErrorResponse | DominoProjectsApiComment | None:
    """Update comment on Goal

    Args:
        project_id (str):
        goal_id (str):
        body (DominoProjectsWebUpdateCommentInfo):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectsApiComment
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            goal_id=goal_id,
            client=client,
            body=body,
        )
    ).parsed
