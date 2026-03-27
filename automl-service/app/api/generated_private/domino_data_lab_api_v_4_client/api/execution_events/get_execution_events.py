from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_computegrid_execution_event_dto import DominoComputegridExecutionEventDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    execution_id: str,
    *,
    page_size: float | None | Unset = UNSET,
    page_number: float | None | Unset = UNSET,
    sort_order: float | None | Unset = UNSET,
    sort_by: None | str | Unset = UNSET,
    fields: None | str | Unset = UNSET,
    exclude_ignored_events: None | str | Unset = UNSET,
    exclude_ignored_heartbeats: None | str | Unset = UNSET,
    inline: None | str | Unset = "True",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_page_size: float | None | Unset
    if isinstance(page_size, Unset):
        json_page_size = UNSET
    else:
        json_page_size = page_size
    params["pageSize"] = json_page_size

    json_page_number: float | None | Unset
    if isinstance(page_number, Unset):
        json_page_number = UNSET
    else:
        json_page_number = page_number
    params["pageNumber"] = json_page_number

    json_sort_order: float | None | Unset
    if isinstance(sort_order, Unset):
        json_sort_order = UNSET
    else:
        json_sort_order = sort_order
    params["sortOrder"] = json_sort_order

    json_sort_by: None | str | Unset
    if isinstance(sort_by, Unset):
        json_sort_by = UNSET
    else:
        json_sort_by = sort_by
    params["sortBy"] = json_sort_by

    json_fields: None | str | Unset
    if isinstance(fields, Unset):
        json_fields = UNSET
    else:
        json_fields = fields
    params["fields"] = json_fields

    json_exclude_ignored_events: None | str | Unset
    if isinstance(exclude_ignored_events, Unset):
        json_exclude_ignored_events = UNSET
    else:
        json_exclude_ignored_events = exclude_ignored_events
    params["excludeIgnoredEvents"] = json_exclude_ignored_events

    json_exclude_ignored_heartbeats: None | str | Unset
    if isinstance(exclude_ignored_heartbeats, Unset):
        json_exclude_ignored_heartbeats = UNSET
    else:
        json_exclude_ignored_heartbeats = exclude_ignored_heartbeats
    params["excludeIgnoredHeartbeats"] = json_exclude_ignored_heartbeats

    json_inline: None | str | Unset
    if isinstance(inline, Unset):
        json_inline = UNSET
    else:
        json_inline = inline
    params["inline"] = json_inline

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/executions/{execution_id}/events".format(
            execution_id=quote(str(execution_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | list[DominoComputegridExecutionEventDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DominoComputegridExecutionEventDto.from_dict(response_200_item_data)

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
) -> Response[DominoApiErrorResponse | list[DominoComputegridExecutionEventDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    page_size: float | None | Unset = UNSET,
    page_number: float | None | Unset = UNSET,
    sort_order: float | None | Unset = UNSET,
    sort_by: None | str | Unset = UNSET,
    fields: None | str | Unset = UNSET,
    exclude_ignored_events: None | str | Unset = UNSET,
    exclude_ignored_heartbeats: None | str | Unset = UNSET,
    inline: None | str | Unset = "True",
) -> Response[DominoApiErrorResponse | list[DominoComputegridExecutionEventDto]]:
    """Retrieves a list of execution events for a given execution id

    Args:
        execution_id (str):
        page_size (float | None | Unset):
        page_number (float | None | Unset):
        sort_order (float | None | Unset):
        sort_by (None | str | Unset):
        fields (None | str | Unset):
        exclude_ignored_events (None | str | Unset):
        exclude_ignored_heartbeats (None | str | Unset):
        inline (None | str | Unset):  Default: 'True'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoComputegridExecutionEventDto]]
    """

    kwargs = _get_kwargs(
        execution_id=execution_id,
        page_size=page_size,
        page_number=page_number,
        sort_order=sort_order,
        sort_by=sort_by,
        fields=fields,
        exclude_ignored_events=exclude_ignored_events,
        exclude_ignored_heartbeats=exclude_ignored_heartbeats,
        inline=inline,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    page_size: float | None | Unset = UNSET,
    page_number: float | None | Unset = UNSET,
    sort_order: float | None | Unset = UNSET,
    sort_by: None | str | Unset = UNSET,
    fields: None | str | Unset = UNSET,
    exclude_ignored_events: None | str | Unset = UNSET,
    exclude_ignored_heartbeats: None | str | Unset = UNSET,
    inline: None | str | Unset = "True",
) -> DominoApiErrorResponse | list[DominoComputegridExecutionEventDto] | None:
    """Retrieves a list of execution events for a given execution id

    Args:
        execution_id (str):
        page_size (float | None | Unset):
        page_number (float | None | Unset):
        sort_order (float | None | Unset):
        sort_by (None | str | Unset):
        fields (None | str | Unset):
        exclude_ignored_events (None | str | Unset):
        exclude_ignored_heartbeats (None | str | Unset):
        inline (None | str | Unset):  Default: 'True'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoComputegridExecutionEventDto]
    """

    return sync_detailed(
        execution_id=execution_id,
        client=client,
        page_size=page_size,
        page_number=page_number,
        sort_order=sort_order,
        sort_by=sort_by,
        fields=fields,
        exclude_ignored_events=exclude_ignored_events,
        exclude_ignored_heartbeats=exclude_ignored_heartbeats,
        inline=inline,
    ).parsed


async def asyncio_detailed(
    execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    page_size: float | None | Unset = UNSET,
    page_number: float | None | Unset = UNSET,
    sort_order: float | None | Unset = UNSET,
    sort_by: None | str | Unset = UNSET,
    fields: None | str | Unset = UNSET,
    exclude_ignored_events: None | str | Unset = UNSET,
    exclude_ignored_heartbeats: None | str | Unset = UNSET,
    inline: None | str | Unset = "True",
) -> Response[DominoApiErrorResponse | list[DominoComputegridExecutionEventDto]]:
    """Retrieves a list of execution events for a given execution id

    Args:
        execution_id (str):
        page_size (float | None | Unset):
        page_number (float | None | Unset):
        sort_order (float | None | Unset):
        sort_by (None | str | Unset):
        fields (None | str | Unset):
        exclude_ignored_events (None | str | Unset):
        exclude_ignored_heartbeats (None | str | Unset):
        inline (None | str | Unset):  Default: 'True'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoComputegridExecutionEventDto]]
    """

    kwargs = _get_kwargs(
        execution_id=execution_id,
        page_size=page_size,
        page_number=page_number,
        sort_order=sort_order,
        sort_by=sort_by,
        fields=fields,
        exclude_ignored_events=exclude_ignored_events,
        exclude_ignored_heartbeats=exclude_ignored_heartbeats,
        inline=inline,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    page_size: float | None | Unset = UNSET,
    page_number: float | None | Unset = UNSET,
    sort_order: float | None | Unset = UNSET,
    sort_by: None | str | Unset = UNSET,
    fields: None | str | Unset = UNSET,
    exclude_ignored_events: None | str | Unset = UNSET,
    exclude_ignored_heartbeats: None | str | Unset = UNSET,
    inline: None | str | Unset = "True",
) -> DominoApiErrorResponse | list[DominoComputegridExecutionEventDto] | None:
    """Retrieves a list of execution events for a given execution id

    Args:
        execution_id (str):
        page_size (float | None | Unset):
        page_number (float | None | Unset):
        sort_order (float | None | Unset):
        sort_by (None | str | Unset):
        fields (None | str | Unset):
        exclude_ignored_events (None | str | Unset):
        exclude_ignored_heartbeats (None | str | Unset):
        inline (None | str | Unset):  Default: 'True'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoComputegridExecutionEventDto]
    """

    return (
        await asyncio_detailed(
            execution_id=execution_id,
            client=client,
            page_size=page_size,
            page_number=page_number,
            sort_order=sort_order,
            sort_by=sort_by,
            fields=fields,
            exclude_ignored_events=exclude_ignored_events,
            exclude_ignored_heartbeats=exclude_ignored_heartbeats,
            inline=inline,
        )
    ).parsed
