from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_modelmanager_api_responses_model_exports_api_response import (
    DominoModelmanagerApiResponsesModelExportsApiResponse,
)
from ...models.get_model_exports_by_project_id_sort import GetModelExportsByProjectIdSort
from ...models.get_model_exports_by_project_id_sort_direction import GetModelExportsByProjectIdSortDirection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    start_index: float | None | Unset = UNSET,
    count: float | None | Unset = UNSET,
    sort: GetModelExportsByProjectIdSort | Unset = UNSET,
    sort_direction: GetModelExportsByProjectIdSortDirection | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_start_index: float | None | Unset
    if isinstance(start_index, Unset):
        json_start_index = UNSET
    else:
        json_start_index = start_index
    params["startIndex"] = json_start_index

    json_count: float | None | Unset
    if isinstance(count, Unset):
        json_count = UNSET
    else:
        json_count = count
    params["count"] = json_count

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    json_sort_direction: str | Unset = UNSET
    if not isinstance(sort_direction, Unset):
        json_sort_direction = sort_direction.value

    params["sortDirection"] = json_sort_direction

    json_search_pattern: None | str | Unset
    if isinstance(search_pattern, Unset):
        json_search_pattern = UNSET
    else:
        json_search_pattern = search_pattern
    params["searchPattern"] = json_search_pattern

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/modelManager/getModelExports/{project_id}".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoModelmanagerApiResponsesModelExportsApiResponse | None:
    if response.status_code == 200:
        response_200 = DominoModelmanagerApiResponsesModelExportsApiResponse.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = DominoApiErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DominoApiErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = DominoApiErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DominoApiErrorResponse | DominoModelmanagerApiResponsesModelExportsApiResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_index: float | None | Unset = UNSET,
    count: float | None | Unset = UNSET,
    sort: GetModelExportsByProjectIdSort | Unset = UNSET,
    sort_direction: GetModelExportsByProjectIdSortDirection | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoModelmanagerApiResponsesModelExportsApiResponse]:
    """Gets all model API exports for a given project id.

    Args:
        project_id (str):
        start_index (float | None | Unset):
        count (float | None | Unset):
        sort (GetModelExportsByProjectIdSort | Unset):
        sort_direction (GetModelExportsByProjectIdSortDirection | Unset):
        search_pattern (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoModelmanagerApiResponsesModelExportsApiResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        start_index=start_index,
        count=count,
        sort=sort,
        sort_direction=sort_direction,
        search_pattern=search_pattern,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_index: float | None | Unset = UNSET,
    count: float | None | Unset = UNSET,
    sort: GetModelExportsByProjectIdSort | Unset = UNSET,
    sort_direction: GetModelExportsByProjectIdSortDirection | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
) -> DominoApiErrorResponse | DominoModelmanagerApiResponsesModelExportsApiResponse | None:
    """Gets all model API exports for a given project id.

    Args:
        project_id (str):
        start_index (float | None | Unset):
        count (float | None | Unset):
        sort (GetModelExportsByProjectIdSort | Unset):
        sort_direction (GetModelExportsByProjectIdSortDirection | Unset):
        search_pattern (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoModelmanagerApiResponsesModelExportsApiResponse
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        start_index=start_index,
        count=count,
        sort=sort,
        sort_direction=sort_direction,
        search_pattern=search_pattern,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_index: float | None | Unset = UNSET,
    count: float | None | Unset = UNSET,
    sort: GetModelExportsByProjectIdSort | Unset = UNSET,
    sort_direction: GetModelExportsByProjectIdSortDirection | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoModelmanagerApiResponsesModelExportsApiResponse]:
    """Gets all model API exports for a given project id.

    Args:
        project_id (str):
        start_index (float | None | Unset):
        count (float | None | Unset):
        sort (GetModelExportsByProjectIdSort | Unset):
        sort_direction (GetModelExportsByProjectIdSortDirection | Unset):
        search_pattern (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoModelmanagerApiResponsesModelExportsApiResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        start_index=start_index,
        count=count,
        sort=sort,
        sort_direction=sort_direction,
        search_pattern=search_pattern,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_index: float | None | Unset = UNSET,
    count: float | None | Unset = UNSET,
    sort: GetModelExportsByProjectIdSort | Unset = UNSET,
    sort_direction: GetModelExportsByProjectIdSortDirection | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
) -> DominoApiErrorResponse | DominoModelmanagerApiResponsesModelExportsApiResponse | None:
    """Gets all model API exports for a given project id.

    Args:
        project_id (str):
        start_index (float | None | Unset):
        count (float | None | Unset):
        sort (GetModelExportsByProjectIdSort | Unset):
        sort_direction (GetModelExportsByProjectIdSortDirection | Unset):
        search_pattern (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoModelmanagerApiResponsesModelExportsApiResponse
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            start_index=start_index,
            count=count,
            sort=sort,
            sort_direction=sort_direction,
            search_pattern=search_pattern,
        )
    ).parsed
