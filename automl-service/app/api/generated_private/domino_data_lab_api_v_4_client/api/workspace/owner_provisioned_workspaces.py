from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_workspace_api_workspace_page_dto import DominoWorkspaceApiWorkspacePageDto
from ...types import UNSET, Response


def _get_kwargs(
    project_id: str,
    owner_id: str,
    *,
    offset: int,
    limit: int,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspace/project/{project_id}/owner/{owner_id}".format(
            project_id=quote(str(project_id), safe=""),
            owner_id=quote(str(owner_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoWorkspaceApiWorkspacePageDto | None:
    if response.status_code == 200:
        response_200 = DominoWorkspaceApiWorkspacePageDto.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoWorkspaceApiWorkspacePageDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    owner_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int,
    limit: int,
) -> Response[DominoApiErrorResponse | DominoWorkspaceApiWorkspacePageDto]:
    """Get all provisioned (i.e. not deleted) workspaces for project by owner

    Args:
        project_id (str):
        owner_id (str):
        offset (int):
        limit (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoWorkspaceApiWorkspacePageDto]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        owner_id=owner_id,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    owner_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int,
    limit: int,
) -> DominoApiErrorResponse | DominoWorkspaceApiWorkspacePageDto | None:
    """Get all provisioned (i.e. not deleted) workspaces for project by owner

    Args:
        project_id (str):
        owner_id (str):
        offset (int):
        limit (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoWorkspaceApiWorkspacePageDto
    """

    return sync_detailed(
        project_id=project_id,
        owner_id=owner_id,
        client=client,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    owner_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int,
    limit: int,
) -> Response[DominoApiErrorResponse | DominoWorkspaceApiWorkspacePageDto]:
    """Get all provisioned (i.e. not deleted) workspaces for project by owner

    Args:
        project_id (str):
        owner_id (str):
        offset (int):
        limit (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoWorkspaceApiWorkspacePageDto]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        owner_id=owner_id,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    owner_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int,
    limit: int,
) -> DominoApiErrorResponse | DominoWorkspaceApiWorkspacePageDto | None:
    """Get all provisioned (i.e. not deleted) workspaces for project by owner

    Args:
        project_id (str):
        owner_id (str):
        offset (int):
        limit (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoWorkspaceApiWorkspacePageDto
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            owner_id=owner_id,
            client=client,
            offset=offset,
            limit=limit,
        )
    ).parsed
