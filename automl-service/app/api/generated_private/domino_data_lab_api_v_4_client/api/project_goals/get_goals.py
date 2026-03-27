from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_project_management_web_error_response import DominoProjectManagementWebErrorResponse
from ...models.domino_projects_api_model_goals_project_goal_collection_dto import (
    DominoProjectsApiModelGoalsProjectGoalCollectionDto,
)
from ...models.get_goals_sort_field import GetGoalsSortField
from ...models.get_goals_sort_order import GetGoalsSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_size: int | Unset = 10,
    page_number: int | Unset = 1,
    sort_field: GetGoalsSortField | Unset = GetGoalsSortField.LASTUPDATEDAT,
    sort_order: GetGoalsSortOrder | Unset = GetGoalsSortOrder.DESC,
    is_complete: bool | None | Unset = UNSET,
    assignee_id: list[str] | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["pageSize"] = page_size

    params["pageNumber"] = page_number

    json_sort_field: str | Unset = UNSET
    if not isinstance(sort_field, Unset):
        json_sort_field = sort_field.value

    params["sortField"] = json_sort_field

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sortOrder"] = json_sort_order

    json_is_complete: bool | None | Unset
    if isinstance(is_complete, Unset):
        json_is_complete = UNSET
    else:
        json_is_complete = is_complete
    params["isComplete"] = json_is_complete

    json_assignee_id: list[str] | None | Unset
    if isinstance(assignee_id, Unset):
        json_assignee_id = UNSET
    elif isinstance(assignee_id, list):
        json_assignee_id = assignee_id

    else:
        json_assignee_id = assignee_id
    params["assigneeId"] = json_assignee_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/project-goals",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DominoApiErrorResponse
    | DominoProjectManagementWebErrorResponse
    | DominoProjectsApiModelGoalsProjectGoalCollectionDto
    | None
):
    if response.status_code == 200:
        response_200 = DominoProjectsApiModelGoalsProjectGoalCollectionDto.from_dict(response.json())

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
    DominoApiErrorResponse
    | DominoProjectManagementWebErrorResponse
    | DominoProjectsApiModelGoalsProjectGoalCollectionDto
]:
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
    sort_field: GetGoalsSortField | Unset = GetGoalsSortField.LASTUPDATEDAT,
    sort_order: GetGoalsSortOrder | Unset = GetGoalsSortOrder.DESC,
    is_complete: bool | None | Unset = UNSET,
    assignee_id: list[str] | None | Unset = UNSET,
) -> Response[
    DominoApiErrorResponse
    | DominoProjectManagementWebErrorResponse
    | DominoProjectsApiModelGoalsProjectGoalCollectionDto
]:
    """Get goals across all projects, sorted by most recently updated.

    Args:
        page_size (int | Unset):  Default: 10.
        page_number (int | Unset):  Default: 1.
        sort_field (GetGoalsSortField | Unset):  Default: GetGoalsSortField.LASTUPDATEDAT.
        sort_order (GetGoalsSortOrder | Unset):  Default: GetGoalsSortOrder.DESC.
        is_complete (bool | None | Unset):
        assignee_id (list[str] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectManagementWebErrorResponse | DominoProjectsApiModelGoalsProjectGoalCollectionDto]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        page_number=page_number,
        sort_field=sort_field,
        sort_order=sort_order,
        is_complete=is_complete,
        assignee_id=assignee_id,
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
    sort_field: GetGoalsSortField | Unset = GetGoalsSortField.LASTUPDATEDAT,
    sort_order: GetGoalsSortOrder | Unset = GetGoalsSortOrder.DESC,
    is_complete: bool | None | Unset = UNSET,
    assignee_id: list[str] | None | Unset = UNSET,
) -> (
    DominoApiErrorResponse
    | DominoProjectManagementWebErrorResponse
    | DominoProjectsApiModelGoalsProjectGoalCollectionDto
    | None
):
    """Get goals across all projects, sorted by most recently updated.

    Args:
        page_size (int | Unset):  Default: 10.
        page_number (int | Unset):  Default: 1.
        sort_field (GetGoalsSortField | Unset):  Default: GetGoalsSortField.LASTUPDATEDAT.
        sort_order (GetGoalsSortOrder | Unset):  Default: GetGoalsSortOrder.DESC.
        is_complete (bool | None | Unset):
        assignee_id (list[str] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectManagementWebErrorResponse | DominoProjectsApiModelGoalsProjectGoalCollectionDto
    """

    return sync_detailed(
        client=client,
        page_size=page_size,
        page_number=page_number,
        sort_field=sort_field,
        sort_order=sort_order,
        is_complete=is_complete,
        assignee_id=assignee_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = 10,
    page_number: int | Unset = 1,
    sort_field: GetGoalsSortField | Unset = GetGoalsSortField.LASTUPDATEDAT,
    sort_order: GetGoalsSortOrder | Unset = GetGoalsSortOrder.DESC,
    is_complete: bool | None | Unset = UNSET,
    assignee_id: list[str] | None | Unset = UNSET,
) -> Response[
    DominoApiErrorResponse
    | DominoProjectManagementWebErrorResponse
    | DominoProjectsApiModelGoalsProjectGoalCollectionDto
]:
    """Get goals across all projects, sorted by most recently updated.

    Args:
        page_size (int | Unset):  Default: 10.
        page_number (int | Unset):  Default: 1.
        sort_field (GetGoalsSortField | Unset):  Default: GetGoalsSortField.LASTUPDATEDAT.
        sort_order (GetGoalsSortOrder | Unset):  Default: GetGoalsSortOrder.DESC.
        is_complete (bool | None | Unset):
        assignee_id (list[str] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectManagementWebErrorResponse | DominoProjectsApiModelGoalsProjectGoalCollectionDto]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        page_number=page_number,
        sort_field=sort_field,
        sort_order=sort_order,
        is_complete=is_complete,
        assignee_id=assignee_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = 10,
    page_number: int | Unset = 1,
    sort_field: GetGoalsSortField | Unset = GetGoalsSortField.LASTUPDATEDAT,
    sort_order: GetGoalsSortOrder | Unset = GetGoalsSortOrder.DESC,
    is_complete: bool | None | Unset = UNSET,
    assignee_id: list[str] | None | Unset = UNSET,
) -> (
    DominoApiErrorResponse
    | DominoProjectManagementWebErrorResponse
    | DominoProjectsApiModelGoalsProjectGoalCollectionDto
    | None
):
    """Get goals across all projects, sorted by most recently updated.

    Args:
        page_size (int | Unset):  Default: 10.
        page_number (int | Unset):  Default: 1.
        sort_field (GetGoalsSortField | Unset):  Default: GetGoalsSortField.LASTUPDATEDAT.
        sort_order (GetGoalsSortOrder | Unset):  Default: GetGoalsSortOrder.DESC.
        is_complete (bool | None | Unset):
        assignee_id (list[str] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectManagementWebErrorResponse | DominoProjectsApiModelGoalsProjectGoalCollectionDto
    """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            page_number=page_number,
            sort_field=sort_field,
            sort_order=sort_order,
            is_complete=is_complete,
            assignee_id=assignee_id,
        )
    ).parsed
