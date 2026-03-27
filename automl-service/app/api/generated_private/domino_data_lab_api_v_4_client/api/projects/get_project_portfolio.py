from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_projects_api_project_portfolio_set import DominoProjectsApiProjectPortfolioSet
from ...models.get_project_portfolio_sort_order import GetProjectPortfolioSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_size: int | None | Unset = UNSET,
    sort_order: GetProjectPortfolioSortOrder | Unset = UNSET,
    sort_by: None | str | Unset = UNSET,
    page_no: int | None | Unset = UNSET,
    search_query: None | str | Unset = UNSET,
    stage_id: list[str] | None | Unset = UNSET,
    status: list[str] | None | Unset = UNSET,
    is_blocked: bool | None | Unset = UNSET,
    include_pm_linked_projects: bool | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_page_size: int | None | Unset
    if isinstance(page_size, Unset):
        json_page_size = UNSET
    else:
        json_page_size = page_size
    params["pageSize"] = json_page_size

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sortOrder"] = json_sort_order

    json_sort_by: None | str | Unset
    if isinstance(sort_by, Unset):
        json_sort_by = UNSET
    else:
        json_sort_by = sort_by
    params["sortBy"] = json_sort_by

    json_page_no: int | None | Unset
    if isinstance(page_no, Unset):
        json_page_no = UNSET
    else:
        json_page_no = page_no
    params["pageNo"] = json_page_no

    json_search_query: None | str | Unset
    if isinstance(search_query, Unset):
        json_search_query = UNSET
    else:
        json_search_query = search_query
    params["searchQuery"] = json_search_query

    json_stage_id: list[str] | None | Unset
    if isinstance(stage_id, Unset):
        json_stage_id = UNSET
    elif isinstance(stage_id, list):
        json_stage_id = stage_id

    else:
        json_stage_id = stage_id
    params["stageId"] = json_stage_id

    json_status: list[str] | None | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    elif isinstance(status, list):
        json_status = status

    else:
        json_status = status
    params["status"] = json_status

    json_is_blocked: bool | None | Unset
    if isinstance(is_blocked, Unset):
        json_is_blocked = UNSET
    else:
        json_is_blocked = is_blocked
    params["isBlocked"] = json_is_blocked

    json_include_pm_linked_projects: bool | None | Unset
    if isinstance(include_pm_linked_projects, Unset):
        json_include_pm_linked_projects = UNSET
    else:
        json_include_pm_linked_projects = include_pm_linked_projects
    params["includePmLinkedProjects"] = json_include_pm_linked_projects

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/portfolio/getProjectPortfolio",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoProjectsApiProjectPortfolioSet | None:
    if response.status_code == 200:
        response_200 = DominoProjectsApiProjectPortfolioSet.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoProjectsApiProjectPortfolioSet]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | None | Unset = UNSET,
    sort_order: GetProjectPortfolioSortOrder | Unset = UNSET,
    sort_by: None | str | Unset = UNSET,
    page_no: int | None | Unset = UNSET,
    search_query: None | str | Unset = UNSET,
    stage_id: list[str] | None | Unset = UNSET,
    status: list[str] | None | Unset = UNSET,
    is_blocked: bool | None | Unset = UNSET,
    include_pm_linked_projects: bool | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoProjectsApiProjectPortfolioSet]:
    """Get project portfolio stats

    Args:
        page_size (int | None | Unset):
        sort_order (GetProjectPortfolioSortOrder | Unset):
        sort_by (None | str | Unset):
        page_no (int | None | Unset):
        search_query (None | str | Unset):
        stage_id (list[str] | None | Unset):
        status (list[str] | None | Unset):
        is_blocked (bool | None | Unset):
        include_pm_linked_projects (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectsApiProjectPortfolioSet]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        sort_order=sort_order,
        sort_by=sort_by,
        page_no=page_no,
        search_query=search_query,
        stage_id=stage_id,
        status=status,
        is_blocked=is_blocked,
        include_pm_linked_projects=include_pm_linked_projects,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | None | Unset = UNSET,
    sort_order: GetProjectPortfolioSortOrder | Unset = UNSET,
    sort_by: None | str | Unset = UNSET,
    page_no: int | None | Unset = UNSET,
    search_query: None | str | Unset = UNSET,
    stage_id: list[str] | None | Unset = UNSET,
    status: list[str] | None | Unset = UNSET,
    is_blocked: bool | None | Unset = UNSET,
    include_pm_linked_projects: bool | None | Unset = UNSET,
) -> DominoApiErrorResponse | DominoProjectsApiProjectPortfolioSet | None:
    """Get project portfolio stats

    Args:
        page_size (int | None | Unset):
        sort_order (GetProjectPortfolioSortOrder | Unset):
        sort_by (None | str | Unset):
        page_no (int | None | Unset):
        search_query (None | str | Unset):
        stage_id (list[str] | None | Unset):
        status (list[str] | None | Unset):
        is_blocked (bool | None | Unset):
        include_pm_linked_projects (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectsApiProjectPortfolioSet
    """

    return sync_detailed(
        client=client,
        page_size=page_size,
        sort_order=sort_order,
        sort_by=sort_by,
        page_no=page_no,
        search_query=search_query,
        stage_id=stage_id,
        status=status,
        is_blocked=is_blocked,
        include_pm_linked_projects=include_pm_linked_projects,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | None | Unset = UNSET,
    sort_order: GetProjectPortfolioSortOrder | Unset = UNSET,
    sort_by: None | str | Unset = UNSET,
    page_no: int | None | Unset = UNSET,
    search_query: None | str | Unset = UNSET,
    stage_id: list[str] | None | Unset = UNSET,
    status: list[str] | None | Unset = UNSET,
    is_blocked: bool | None | Unset = UNSET,
    include_pm_linked_projects: bool | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoProjectsApiProjectPortfolioSet]:
    """Get project portfolio stats

    Args:
        page_size (int | None | Unset):
        sort_order (GetProjectPortfolioSortOrder | Unset):
        sort_by (None | str | Unset):
        page_no (int | None | Unset):
        search_query (None | str | Unset):
        stage_id (list[str] | None | Unset):
        status (list[str] | None | Unset):
        is_blocked (bool | None | Unset):
        include_pm_linked_projects (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectsApiProjectPortfolioSet]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        sort_order=sort_order,
        sort_by=sort_by,
        page_no=page_no,
        search_query=search_query,
        stage_id=stage_id,
        status=status,
        is_blocked=is_blocked,
        include_pm_linked_projects=include_pm_linked_projects,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page_size: int | None | Unset = UNSET,
    sort_order: GetProjectPortfolioSortOrder | Unset = UNSET,
    sort_by: None | str | Unset = UNSET,
    page_no: int | None | Unset = UNSET,
    search_query: None | str | Unset = UNSET,
    stage_id: list[str] | None | Unset = UNSET,
    status: list[str] | None | Unset = UNSET,
    is_blocked: bool | None | Unset = UNSET,
    include_pm_linked_projects: bool | None | Unset = UNSET,
) -> DominoApiErrorResponse | DominoProjectsApiProjectPortfolioSet | None:
    """Get project portfolio stats

    Args:
        page_size (int | None | Unset):
        sort_order (GetProjectPortfolioSortOrder | Unset):
        sort_by (None | str | Unset):
        page_no (int | None | Unset):
        search_query (None | str | Unset):
        stage_id (list[str] | None | Unset):
        status (list[str] | None | Unset):
        is_blocked (bool | None | Unset):
        include_pm_linked_projects (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectsApiProjectPortfolioSet
    """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            sort_order=sort_order,
            sort_by=sort_by,
            page_no=page_no,
            search_query=search_query,
            stage_id=stage_id,
            status=status,
            is_blocked=is_blocked,
            include_pm_linked_projects=include_pm_linked_projects,
        )
    ).parsed
