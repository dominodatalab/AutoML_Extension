from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_jobs_interface_job_set import DominoJobsInterfaceJobSet
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    domino_stats_sort_field_name: None | str | Unset = UNSET,
    project_id: str,
    page_size: float | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    order_by: str | Unset = UNSET,
    page_no: float | Unset = UNSET,
    status: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    query: str | Unset = UNSET,
    show_archived: bool | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_domino_stats_sort_field_name: None | str | Unset
    if isinstance(domino_stats_sort_field_name, Unset):
        json_domino_stats_sort_field_name = UNSET
    else:
        json_domino_stats_sort_field_name = domino_stats_sort_field_name
    params["dominoStatsSortFieldName"] = json_domino_stats_sort_field_name

    params["projectId"] = project_id

    params["page_size"] = page_size

    params["sort_by"] = sort_by

    params["order_by"] = order_by

    params["page_no"] = page_no

    params["status"] = status

    params["tag"] = tag

    params["query"] = query

    params["show_archived"] = show_archived

    params["type"] = type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/jobs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoJobsInterfaceJobSet | None:
    if response.status_code == 200:
        response_200 = DominoJobsInterfaceJobSet.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoJobsInterfaceJobSet]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    domino_stats_sort_field_name: None | str | Unset = UNSET,
    project_id: str,
    page_size: float | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    order_by: str | Unset = UNSET,
    page_no: float | Unset = UNSET,
    status: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    query: str | Unset = UNSET,
    show_archived: bool | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoJobsInterfaceJobSet]:
    """Gets all Jobs for the given Project

    Args:
        domino_stats_sort_field_name (None | str | Unset):
        project_id (str):
        page_size (float | Unset):
        sort_by (str | Unset):
        order_by (str | Unset):
        page_no (float | Unset):
        status (str | Unset):
        tag (str | Unset):
        query (str | Unset):
        show_archived (bool | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoJobsInterfaceJobSet]
    """

    kwargs = _get_kwargs(
        domino_stats_sort_field_name=domino_stats_sort_field_name,
        project_id=project_id,
        page_size=page_size,
        sort_by=sort_by,
        order_by=order_by,
        page_no=page_no,
        status=status,
        tag=tag,
        query=query,
        show_archived=show_archived,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    domino_stats_sort_field_name: None | str | Unset = UNSET,
    project_id: str,
    page_size: float | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    order_by: str | Unset = UNSET,
    page_no: float | Unset = UNSET,
    status: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    query: str | Unset = UNSET,
    show_archived: bool | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> DominoApiErrorResponse | DominoJobsInterfaceJobSet | None:
    """Gets all Jobs for the given Project

    Args:
        domino_stats_sort_field_name (None | str | Unset):
        project_id (str):
        page_size (float | Unset):
        sort_by (str | Unset):
        order_by (str | Unset):
        page_no (float | Unset):
        status (str | Unset):
        tag (str | Unset):
        query (str | Unset):
        show_archived (bool | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoJobsInterfaceJobSet
    """

    return sync_detailed(
        client=client,
        domino_stats_sort_field_name=domino_stats_sort_field_name,
        project_id=project_id,
        page_size=page_size,
        sort_by=sort_by,
        order_by=order_by,
        page_no=page_no,
        status=status,
        tag=tag,
        query=query,
        show_archived=show_archived,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    domino_stats_sort_field_name: None | str | Unset = UNSET,
    project_id: str,
    page_size: float | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    order_by: str | Unset = UNSET,
    page_no: float | Unset = UNSET,
    status: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    query: str | Unset = UNSET,
    show_archived: bool | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoJobsInterfaceJobSet]:
    """Gets all Jobs for the given Project

    Args:
        domino_stats_sort_field_name (None | str | Unset):
        project_id (str):
        page_size (float | Unset):
        sort_by (str | Unset):
        order_by (str | Unset):
        page_no (float | Unset):
        status (str | Unset):
        tag (str | Unset):
        query (str | Unset):
        show_archived (bool | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoJobsInterfaceJobSet]
    """

    kwargs = _get_kwargs(
        domino_stats_sort_field_name=domino_stats_sort_field_name,
        project_id=project_id,
        page_size=page_size,
        sort_by=sort_by,
        order_by=order_by,
        page_no=page_no,
        status=status,
        tag=tag,
        query=query,
        show_archived=show_archived,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    domino_stats_sort_field_name: None | str | Unset = UNSET,
    project_id: str,
    page_size: float | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    order_by: str | Unset = UNSET,
    page_no: float | Unset = UNSET,
    status: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    query: str | Unset = UNSET,
    show_archived: bool | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> DominoApiErrorResponse | DominoJobsInterfaceJobSet | None:
    """Gets all Jobs for the given Project

    Args:
        domino_stats_sort_field_name (None | str | Unset):
        project_id (str):
        page_size (float | Unset):
        sort_by (str | Unset):
        order_by (str | Unset):
        page_no (float | Unset):
        status (str | Unset):
        tag (str | Unset):
        query (str | Unset):
        show_archived (bool | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoJobsInterfaceJobSet
    """

    return (
        await asyncio_detailed(
            client=client,
            domino_stats_sort_field_name=domino_stats_sort_field_name,
            project_id=project_id,
            page_size=page_size,
            sort_by=sort_by,
            order_by=order_by,
            page_no=page_no,
            status=status,
            tag=tag,
            query=query,
            show_archived=show_archived,
            type_=type_,
        )
    ).parsed
