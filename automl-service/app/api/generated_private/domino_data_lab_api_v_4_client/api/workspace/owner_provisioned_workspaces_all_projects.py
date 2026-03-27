from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_workspace_api_workspace_page_collection_dto import DominoWorkspaceApiWorkspacePageCollectionDto
from ...models.owner_provisioned_workspaces_all_projects_sort_field import (
    OwnerProvisionedWorkspacesAllProjectsSortField,
)
from ...models.owner_provisioned_workspaces_all_projects_sort_order import (
    OwnerProvisionedWorkspacesAllProjectsSortOrder,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_size: int | Unset = 10,
    page_number: int | Unset = 1,
    q: None | str | Unset = UNSET,
    sort_field: OwnerProvisionedWorkspacesAllProjectsSortField
    | Unset = OwnerProvisionedWorkspacesAllProjectsSortField.LASTSTARTED,
    sort_order: OwnerProvisionedWorkspacesAllProjectsSortOrder
    | Unset = OwnerProvisionedWorkspacesAllProjectsSortOrder.DESC,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["pageSize"] = page_size

    params["pageNumber"] = page_number

    json_q: None | str | Unset
    if isinstance(q, Unset):
        json_q = UNSET
    else:
        json_q = q
    params["q"] = json_q

    json_sort_field: str | Unset = UNSET
    if not isinstance(sort_field, Unset):
        json_sort_field = sort_field.value

    params["sortField"] = json_sort_field

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sortOrder"] = json_sort_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspace",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoWorkspaceApiWorkspacePageCollectionDto | None:
    if response.status_code == 200:
        response_200 = DominoWorkspaceApiWorkspacePageCollectionDto.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoWorkspaceApiWorkspacePageCollectionDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = 10,
    page_number: int | Unset = 1,
    q: None | str | Unset = UNSET,
    sort_field: OwnerProvisionedWorkspacesAllProjectsSortField
    | Unset = OwnerProvisionedWorkspacesAllProjectsSortField.LASTSTARTED,
    sort_order: OwnerProvisionedWorkspacesAllProjectsSortOrder
    | Unset = OwnerProvisionedWorkspacesAllProjectsSortOrder.DESC,
) -> Response[DominoApiErrorResponse | DominoWorkspaceApiWorkspacePageCollectionDto]:
    """Get all provisioned (i.e. not deleted) workspaces owned by a user across projects, sorted by last
    started time descending.

    Args:
        page_size (int | Unset):  Default: 10.
        page_number (int | Unset):  Default: 1.
        q (None | str | Unset):
        sort_field (OwnerProvisionedWorkspacesAllProjectsSortField | Unset):  Default:
            OwnerProvisionedWorkspacesAllProjectsSortField.LASTSTARTED.
        sort_order (OwnerProvisionedWorkspacesAllProjectsSortOrder | Unset):  Default:
            OwnerProvisionedWorkspacesAllProjectsSortOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoWorkspaceApiWorkspacePageCollectionDto]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        page_number=page_number,
        q=q,
        sort_field=sort_field,
        sort_order=sort_order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = 10,
    page_number: int | Unset = 1,
    q: None | str | Unset = UNSET,
    sort_field: OwnerProvisionedWorkspacesAllProjectsSortField
    | Unset = OwnerProvisionedWorkspacesAllProjectsSortField.LASTSTARTED,
    sort_order: OwnerProvisionedWorkspacesAllProjectsSortOrder
    | Unset = OwnerProvisionedWorkspacesAllProjectsSortOrder.DESC,
) -> DominoApiErrorResponse | DominoWorkspaceApiWorkspacePageCollectionDto | None:
    """Get all provisioned (i.e. not deleted) workspaces owned by a user across projects, sorted by last
    started time descending.

    Args:
        page_size (int | Unset):  Default: 10.
        page_number (int | Unset):  Default: 1.
        q (None | str | Unset):
        sort_field (OwnerProvisionedWorkspacesAllProjectsSortField | Unset):  Default:
            OwnerProvisionedWorkspacesAllProjectsSortField.LASTSTARTED.
        sort_order (OwnerProvisionedWorkspacesAllProjectsSortOrder | Unset):  Default:
            OwnerProvisionedWorkspacesAllProjectsSortOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoWorkspaceApiWorkspacePageCollectionDto
    """

    return sync_detailed(
        client=client,
        page_size=page_size,
        page_number=page_number,
        q=q,
        sort_field=sort_field,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = 10,
    page_number: int | Unset = 1,
    q: None | str | Unset = UNSET,
    sort_field: OwnerProvisionedWorkspacesAllProjectsSortField
    | Unset = OwnerProvisionedWorkspacesAllProjectsSortField.LASTSTARTED,
    sort_order: OwnerProvisionedWorkspacesAllProjectsSortOrder
    | Unset = OwnerProvisionedWorkspacesAllProjectsSortOrder.DESC,
) -> Response[DominoApiErrorResponse | DominoWorkspaceApiWorkspacePageCollectionDto]:
    """Get all provisioned (i.e. not deleted) workspaces owned by a user across projects, sorted by last
    started time descending.

    Args:
        page_size (int | Unset):  Default: 10.
        page_number (int | Unset):  Default: 1.
        q (None | str | Unset):
        sort_field (OwnerProvisionedWorkspacesAllProjectsSortField | Unset):  Default:
            OwnerProvisionedWorkspacesAllProjectsSortField.LASTSTARTED.
        sort_order (OwnerProvisionedWorkspacesAllProjectsSortOrder | Unset):  Default:
            OwnerProvisionedWorkspacesAllProjectsSortOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoWorkspaceApiWorkspacePageCollectionDto]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        page_number=page_number,
        q=q,
        sort_field=sort_field,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = 10,
    page_number: int | Unset = 1,
    q: None | str | Unset = UNSET,
    sort_field: OwnerProvisionedWorkspacesAllProjectsSortField
    | Unset = OwnerProvisionedWorkspacesAllProjectsSortField.LASTSTARTED,
    sort_order: OwnerProvisionedWorkspacesAllProjectsSortOrder
    | Unset = OwnerProvisionedWorkspacesAllProjectsSortOrder.DESC,
) -> DominoApiErrorResponse | DominoWorkspaceApiWorkspacePageCollectionDto | None:
    """Get all provisioned (i.e. not deleted) workspaces owned by a user across projects, sorted by last
    started time descending.

    Args:
        page_size (int | Unset):  Default: 10.
        page_number (int | Unset):  Default: 1.
        q (None | str | Unset):
        sort_field (OwnerProvisionedWorkspacesAllProjectsSortField | Unset):  Default:
            OwnerProvisionedWorkspacesAllProjectsSortField.LASTSTARTED.
        sort_order (OwnerProvisionedWorkspacesAllProjectsSortOrder | Unset):  Default:
            OwnerProvisionedWorkspacesAllProjectsSortOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoWorkspaceApiWorkspacePageCollectionDto
    """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            page_number=page_number,
            q=q,
            sort_field=sort_field,
            sort_order=sort_order,
        )
    ).parsed
