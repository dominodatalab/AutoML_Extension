from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_workspaces_api_workspace_summary import DominoWorkspacesApiWorkspaceSummary
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    project_id: str,
    user_to_filter: str | Unset = UNSET,
    status: Any | Unset = UNSET,
    tag: str | Unset = UNSET,
    show_archived: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["projectId"] = project_id

    params["userToFilter"] = user_to_filter

    params["status"] = status

    params["tag"] = tag

    params["show_archived"] = show_archived

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspaces",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | list[DominoWorkspacesApiWorkspaceSummary] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DominoWorkspacesApiWorkspaceSummary.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = DominoApiErrorResponse.from_dict(response.json())

        return response_400

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
) -> Response[DominoApiErrorResponse | list[DominoWorkspacesApiWorkspaceSummary]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    project_id: str,
    user_to_filter: str | Unset = UNSET,
    status: Any | Unset = UNSET,
    tag: str | Unset = UNSET,
    show_archived: bool | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoWorkspacesApiWorkspaceSummary]]:
    """Gets the available workspaces for the given Project

    Args:
        project_id (str):
        user_to_filter (str | Unset):
        status (Any | Unset):
        tag (str | Unset):
        show_archived (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoWorkspacesApiWorkspaceSummary]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        user_to_filter=user_to_filter,
        status=status,
        tag=tag,
        show_archived=show_archived,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    project_id: str,
    user_to_filter: str | Unset = UNSET,
    status: Any | Unset = UNSET,
    tag: str | Unset = UNSET,
    show_archived: bool | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoWorkspacesApiWorkspaceSummary] | None:
    """Gets the available workspaces for the given Project

    Args:
        project_id (str):
        user_to_filter (str | Unset):
        status (Any | Unset):
        tag (str | Unset):
        show_archived (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoWorkspacesApiWorkspaceSummary]
    """

    return sync_detailed(
        client=client,
        project_id=project_id,
        user_to_filter=user_to_filter,
        status=status,
        tag=tag,
        show_archived=show_archived,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    project_id: str,
    user_to_filter: str | Unset = UNSET,
    status: Any | Unset = UNSET,
    tag: str | Unset = UNSET,
    show_archived: bool | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoWorkspacesApiWorkspaceSummary]]:
    """Gets the available workspaces for the given Project

    Args:
        project_id (str):
        user_to_filter (str | Unset):
        status (Any | Unset):
        tag (str | Unset):
        show_archived (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoWorkspacesApiWorkspaceSummary]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        user_to_filter=user_to_filter,
        status=status,
        tag=tag,
        show_archived=show_archived,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    project_id: str,
    user_to_filter: str | Unset = UNSET,
    status: Any | Unset = UNSET,
    tag: str | Unset = UNSET,
    show_archived: bool | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoWorkspacesApiWorkspaceSummary] | None:
    """Gets the available workspaces for the given Project

    Args:
        project_id (str):
        user_to_filter (str | Unset):
        status (Any | Unset):
        tag (str | Unset):
        show_archived (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoWorkspacesApiWorkspaceSummary]
    """

    return (
        await asyncio_detailed(
            client=client,
            project_id=project_id,
            user_to_filter=user_to_filter,
            status=status,
            tag=tag,
            show_archived=show_archived,
        )
    ).parsed
