from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_provenance_api_provenance_checkpoint_dto import DominoProvenanceApiProvenanceCheckpointDto
from ...models.get_provenance_checkpoints_for_workspace_sort_order import GetProvenanceCheckpointsForWorkspaceSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    workspace_id: str,
    *,
    offset: int | None | Unset = 0,
    limit: int | None | Unset = 50,
    sort_by: Any | Unset = UNSET,
    sort_order: GetProvenanceCheckpointsForWorkspaceSortOrder | Unset = UNSET,
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
        "url": "/workspace/project/{project_id}/workspaceId/{workspace_id}/provenanceCheckpoints".format(
            project_id=quote(str(project_id), safe=""),
            workspace_id=quote(str(workspace_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | list[DominoProvenanceApiProvenanceCheckpointDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DominoProvenanceApiProvenanceCheckpointDto.from_dict(response_200_item_data)

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
) -> Response[DominoApiErrorResponse | list[DominoProvenanceApiProvenanceCheckpointDto]]:
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
    offset: int | None | Unset = 0,
    limit: int | None | Unset = 50,
    sort_by: Any | Unset = UNSET,
    sort_order: GetProvenanceCheckpointsForWorkspaceSortOrder | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoProvenanceApiProvenanceCheckpointDto]]:
    """Get all provenance checkpoints for a workspace

    Args:
        project_id (str):
        workspace_id (str):
        offset (int | None | Unset):  Default: 0.
        limit (int | None | Unset):  Default: 50.
        sort_by (Any | Unset):
        sort_order (GetProvenanceCheckpointsForWorkspaceSortOrder | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoProvenanceApiProvenanceCheckpointDto]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        workspace_id=workspace_id,
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
    project_id: str,
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | None | Unset = 0,
    limit: int | None | Unset = 50,
    sort_by: Any | Unset = UNSET,
    sort_order: GetProvenanceCheckpointsForWorkspaceSortOrder | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoProvenanceApiProvenanceCheckpointDto] | None:
    """Get all provenance checkpoints for a workspace

    Args:
        project_id (str):
        workspace_id (str):
        offset (int | None | Unset):  Default: 0.
        limit (int | None | Unset):  Default: 50.
        sort_by (Any | Unset):
        sort_order (GetProvenanceCheckpointsForWorkspaceSortOrder | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoProvenanceApiProvenanceCheckpointDto]
    """

    return sync_detailed(
        project_id=project_id,
        workspace_id=workspace_id,
        client=client,
        offset=offset,
        limit=limit,
        sort_by=sort_by,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | None | Unset = 0,
    limit: int | None | Unset = 50,
    sort_by: Any | Unset = UNSET,
    sort_order: GetProvenanceCheckpointsForWorkspaceSortOrder | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoProvenanceApiProvenanceCheckpointDto]]:
    """Get all provenance checkpoints for a workspace

    Args:
        project_id (str):
        workspace_id (str):
        offset (int | None | Unset):  Default: 0.
        limit (int | None | Unset):  Default: 50.
        sort_by (Any | Unset):
        sort_order (GetProvenanceCheckpointsForWorkspaceSortOrder | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoProvenanceApiProvenanceCheckpointDto]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        workspace_id=workspace_id,
        offset=offset,
        limit=limit,
        sort_by=sort_by,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | None | Unset = 0,
    limit: int | None | Unset = 50,
    sort_by: Any | Unset = UNSET,
    sort_order: GetProvenanceCheckpointsForWorkspaceSortOrder | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoProvenanceApiProvenanceCheckpointDto] | None:
    """Get all provenance checkpoints for a workspace

    Args:
        project_id (str):
        workspace_id (str):
        offset (int | None | Unset):  Default: 0.
        limit (int | None | Unset):  Default: 50.
        sort_by (Any | Unset):
        sort_order (GetProvenanceCheckpointsForWorkspaceSortOrder | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoProvenanceApiProvenanceCheckpointDto]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            workspace_id=workspace_id,
            client=client,
            offset=offset,
            limit=limit,
            sort_by=sort_by,
            sort_order=sort_order,
        )
    ).parsed
