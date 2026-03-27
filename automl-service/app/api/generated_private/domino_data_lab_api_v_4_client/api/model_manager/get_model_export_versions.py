from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.get_model_export_versions_sort import GetModelExportVersionsSort
from ...models.get_model_export_versions_sort_direction import GetModelExportVersionsSortDirection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    export_id: str,
    *,
    start_index: float | None | Unset = UNSET,
    count: float | None | Unset = UNSET,
    sort: GetModelExportVersionsSort | Unset = UNSET,
    sort_direction: GetModelExportVersionsSortDirection | Unset = UNSET,
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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/modelManager/getModelExportVersions/{export_id}".format(
            export_id=quote(str(export_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DominoApiErrorResponse | None:
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
) -> Response[DominoApiErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    export_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_index: float | None | Unset = UNSET,
    count: float | None | Unset = UNSET,
    sort: GetModelExportVersionsSort | Unset = UNSET,
    sort_direction: GetModelExportVersionsSortDirection | Unset = UNSET,
) -> Response[DominoApiErrorResponse]:
    """Gets all model API export versions for a given export id.

    Args:
        export_id (str):
        start_index (float | None | Unset):
        count (float | None | Unset):
        sort (GetModelExportVersionsSort | Unset):
        sort_direction (GetModelExportVersionsSortDirection | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse]
    """

    kwargs = _get_kwargs(
        export_id=export_id,
        start_index=start_index,
        count=count,
        sort=sort,
        sort_direction=sort_direction,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    export_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_index: float | None | Unset = UNSET,
    count: float | None | Unset = UNSET,
    sort: GetModelExportVersionsSort | Unset = UNSET,
    sort_direction: GetModelExportVersionsSortDirection | Unset = UNSET,
) -> DominoApiErrorResponse | None:
    """Gets all model API export versions for a given export id.

    Args:
        export_id (str):
        start_index (float | None | Unset):
        count (float | None | Unset):
        sort (GetModelExportVersionsSort | Unset):
        sort_direction (GetModelExportVersionsSortDirection | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse
    """

    return sync_detailed(
        export_id=export_id,
        client=client,
        start_index=start_index,
        count=count,
        sort=sort,
        sort_direction=sort_direction,
    ).parsed


async def asyncio_detailed(
    export_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_index: float | None | Unset = UNSET,
    count: float | None | Unset = UNSET,
    sort: GetModelExportVersionsSort | Unset = UNSET,
    sort_direction: GetModelExportVersionsSortDirection | Unset = UNSET,
) -> Response[DominoApiErrorResponse]:
    """Gets all model API export versions for a given export id.

    Args:
        export_id (str):
        start_index (float | None | Unset):
        count (float | None | Unset):
        sort (GetModelExportVersionsSort | Unset):
        sort_direction (GetModelExportVersionsSortDirection | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse]
    """

    kwargs = _get_kwargs(
        export_id=export_id,
        start_index=start_index,
        count=count,
        sort=sort,
        sort_direction=sort_direction,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    export_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_index: float | None | Unset = UNSET,
    count: float | None | Unset = UNSET,
    sort: GetModelExportVersionsSort | Unset = UNSET,
    sort_direction: GetModelExportVersionsSortDirection | Unset = UNSET,
) -> DominoApiErrorResponse | None:
    """Gets all model API export versions for a given export id.

    Args:
        export_id (str):
        start_index (float | None | Unset):
        count (float | None | Unset):
        sort (GetModelExportVersionsSort | Unset):
        sort_direction (GetModelExportVersionsSortDirection | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse
    """

    return (
        await asyncio_detailed(
            export_id=export_id,
            client=client,
            start_index=start_index,
            count=count,
            sort=sort,
            sort_direction=sort_direction,
        )
    ).parsed
