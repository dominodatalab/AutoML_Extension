from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_workspace_api_workspace_session_provenance_dto import (
    DominoWorkspaceApiWorkspaceSessionProvenanceDto,
)
from ...models.get_provenance_checkpoints_for_workspace_session_sort_order import (
    GetProvenanceCheckpointsForWorkspaceSessionSortOrder,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace_session_id: str,
    *,
    offset: int | None | Unset = 0,
    limit: int | None | Unset = 50,
    sort_by: Any | Unset = UNSET,
    sort_order: GetProvenanceCheckpointsForWorkspaceSessionSortOrder | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_offset: int | None | Unset
    if isinstance(offset, Unset):
        json_offset = UNSET
    else:
        json_offset = offset
    params["offset"] = json_offset

    json_limit: int | None | Unset
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["limit"] = json_limit

    params["sortBy"] = sort_by

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sortOrder"] = json_sort_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspace/workspaceSessionId/{workspace_session_id}/provenanceCheckpoints".format(
            workspace_session_id=quote(str(workspace_session_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoWorkspaceApiWorkspaceSessionProvenanceDto | None:
    if response.status_code == 200:
        response_200 = DominoWorkspaceApiWorkspaceSessionProvenanceDto.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoWorkspaceApiWorkspaceSessionProvenanceDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_session_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | None | Unset = 0,
    limit: int | None | Unset = 50,
    sort_by: Any | Unset = UNSET,
    sort_order: GetProvenanceCheckpointsForWorkspaceSessionSortOrder | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoWorkspaceApiWorkspaceSessionProvenanceDto]:
    """Get the provenance checkpoints for a workspace session

    Args:
        workspace_session_id (str):
        offset (int | None | Unset):  Default: 0.
        limit (int | None | Unset):  Default: 50.
        sort_by (Any | Unset):
        sort_order (GetProvenanceCheckpointsForWorkspaceSessionSortOrder | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoWorkspaceApiWorkspaceSessionProvenanceDto]
    """

    kwargs = _get_kwargs(
        workspace_session_id=workspace_session_id,
        offset=offset,
        limit=limit,
        sort_by=sort_by,
        sort_order=sort_order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_session_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | None | Unset = 0,
    limit: int | None | Unset = 50,
    sort_by: Any | Unset = UNSET,
    sort_order: GetProvenanceCheckpointsForWorkspaceSessionSortOrder | Unset = UNSET,
) -> DominoApiErrorResponse | DominoWorkspaceApiWorkspaceSessionProvenanceDto | None:
    """Get the provenance checkpoints for a workspace session

    Args:
        workspace_session_id (str):
        offset (int | None | Unset):  Default: 0.
        limit (int | None | Unset):  Default: 50.
        sort_by (Any | Unset):
        sort_order (GetProvenanceCheckpointsForWorkspaceSessionSortOrder | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoWorkspaceApiWorkspaceSessionProvenanceDto
    """

    return sync_detailed(
        workspace_session_id=workspace_session_id,
        client=client,
        offset=offset,
        limit=limit,
        sort_by=sort_by,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    workspace_session_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | None | Unset = 0,
    limit: int | None | Unset = 50,
    sort_by: Any | Unset = UNSET,
    sort_order: GetProvenanceCheckpointsForWorkspaceSessionSortOrder | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoWorkspaceApiWorkspaceSessionProvenanceDto]:
    """Get the provenance checkpoints for a workspace session

    Args:
        workspace_session_id (str):
        offset (int | None | Unset):  Default: 0.
        limit (int | None | Unset):  Default: 50.
        sort_by (Any | Unset):
        sort_order (GetProvenanceCheckpointsForWorkspaceSessionSortOrder | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoWorkspaceApiWorkspaceSessionProvenanceDto]
    """

    kwargs = _get_kwargs(
        workspace_session_id=workspace_session_id,
        offset=offset,
        limit=limit,
        sort_by=sort_by,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_session_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | None | Unset = 0,
    limit: int | None | Unset = 50,
    sort_by: Any | Unset = UNSET,
    sort_order: GetProvenanceCheckpointsForWorkspaceSessionSortOrder | Unset = UNSET,
) -> DominoApiErrorResponse | DominoWorkspaceApiWorkspaceSessionProvenanceDto | None:
    """Get the provenance checkpoints for a workspace session

    Args:
        workspace_session_id (str):
        offset (int | None | Unset):  Default: 0.
        limit (int | None | Unset):  Default: 50.
        sort_by (Any | Unset):
        sort_order (GetProvenanceCheckpointsForWorkspaceSessionSortOrder | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoWorkspaceApiWorkspaceSessionProvenanceDto
    """

    return (
        await asyncio_detailed(
            workspace_session_id=workspace_session_id,
            client=client,
            offset=offset,
            limit=limit,
            sort_by=sort_by,
            sort_order=sort_order,
        )
    ).parsed
