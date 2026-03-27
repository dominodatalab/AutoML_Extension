from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_activity_api_activity_stream import DominoActivityApiActivityStream
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.get_activity_stream_filter_by_type_0_item import GetActivityStreamFilterByType0Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    project_id: str,
    page_size: float | None | Unset = UNSET,
    latest_time_stamp: float | None | Unset = UNSET,
    filter_by: list[GetActivityStreamFilterByType0Item] | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["projectId"] = project_id

    json_page_size: float | None | Unset
    if isinstance(page_size, Unset):
        json_page_size = UNSET
    else:
        json_page_size = page_size
    params["pageSize"] = json_page_size

    json_latest_time_stamp: float | None | Unset
    if isinstance(latest_time_stamp, Unset):
        json_latest_time_stamp = UNSET
    else:
        json_latest_time_stamp = latest_time_stamp
    params["latestTimeStamp"] = json_latest_time_stamp

    json_filter_by: list[str] | None | Unset
    if isinstance(filter_by, Unset):
        json_filter_by = UNSET
    elif isinstance(filter_by, list):
        json_filter_by = []
        for filter_by_type_0_item_data in filter_by:
            filter_by_type_0_item = filter_by_type_0_item_data.value
            json_filter_by.append(filter_by_type_0_item)

    else:
        json_filter_by = filter_by
    params["filterBy"] = json_filter_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/activity",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoActivityApiActivityStream | DominoApiErrorResponse | None:
    if response.status_code == 200:
        response_200 = DominoActivityApiActivityStream.from_dict(response.json())

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
) -> Response[DominoActivityApiActivityStream | DominoApiErrorResponse]:
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
    page_size: float | None | Unset = UNSET,
    latest_time_stamp: float | None | Unset = UNSET,
    filter_by: list[GetActivityStreamFilterByType0Item] | None | Unset = UNSET,
) -> Response[DominoActivityApiActivityStream | DominoApiErrorResponse]:
    """Gets all activity stream

    Args:
        project_id (str):
        page_size (float | None | Unset):
        latest_time_stamp (float | None | Unset):
        filter_by (list[GetActivityStreamFilterByType0Item] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoActivityApiActivityStream | DominoApiErrorResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        page_size=page_size,
        latest_time_stamp=latest_time_stamp,
        filter_by=filter_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    project_id: str,
    page_size: float | None | Unset = UNSET,
    latest_time_stamp: float | None | Unset = UNSET,
    filter_by: list[GetActivityStreamFilterByType0Item] | None | Unset = UNSET,
) -> DominoActivityApiActivityStream | DominoApiErrorResponse | None:
    """Gets all activity stream

    Args:
        project_id (str):
        page_size (float | None | Unset):
        latest_time_stamp (float | None | Unset):
        filter_by (list[GetActivityStreamFilterByType0Item] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoActivityApiActivityStream | DominoApiErrorResponse
    """

    return sync_detailed(
        client=client,
        project_id=project_id,
        page_size=page_size,
        latest_time_stamp=latest_time_stamp,
        filter_by=filter_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    project_id: str,
    page_size: float | None | Unset = UNSET,
    latest_time_stamp: float | None | Unset = UNSET,
    filter_by: list[GetActivityStreamFilterByType0Item] | None | Unset = UNSET,
) -> Response[DominoActivityApiActivityStream | DominoApiErrorResponse]:
    """Gets all activity stream

    Args:
        project_id (str):
        page_size (float | None | Unset):
        latest_time_stamp (float | None | Unset):
        filter_by (list[GetActivityStreamFilterByType0Item] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoActivityApiActivityStream | DominoApiErrorResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        page_size=page_size,
        latest_time_stamp=latest_time_stamp,
        filter_by=filter_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    project_id: str,
    page_size: float | None | Unset = UNSET,
    latest_time_stamp: float | None | Unset = UNSET,
    filter_by: list[GetActivityStreamFilterByType0Item] | None | Unset = UNSET,
) -> DominoActivityApiActivityStream | DominoApiErrorResponse | None:
    """Gets all activity stream

    Args:
        project_id (str):
        page_size (float | None | Unset):
        latest_time_stamp (float | None | Unset):
        filter_by (list[GetActivityStreamFilterByType0Item] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoActivityApiActivityStream | DominoApiErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            project_id=project_id,
            page_size=page_size,
            latest_time_stamp=latest_time_stamp,
            filter_by=filter_by,
        )
    ).parsed
