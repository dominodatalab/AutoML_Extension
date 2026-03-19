from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.audit_events_response import AuditEventsResponse
from ...models.error import Error
from ...models.fetch_audit_events_column import FetchAuditEventsColumn
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start_timestamp: int | Unset = UNSET,
    end_timestamp: int | Unset = UNSET,
    actor_id: str | Unset = UNSET,
    actor_name: str | Unset = UNSET,
    event: str | Unset = UNSET,
    target_type: str | Unset = UNSET,
    target_id: str | Unset = UNSET,
    target_name: str | Unset = UNSET,
    within_project_id: str | Unset = UNSET,
    within_project_name: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    column: FetchAuditEventsColumn | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["startTimestamp"] = start_timestamp

    params["endTimestamp"] = end_timestamp

    params["actorId"] = actor_id

    params["actorName"] = actor_name

    params["event"] = event

    params["targetType"] = target_type

    params["targetId"] = target_id

    params["targetName"] = target_name

    params["withinProjectId"] = within_project_id

    params["withinProjectName"] = within_project_name

    params["sort"] = sort

    params["limit"] = limit

    params["offset"] = offset

    json_column: str | Unset = UNSET
    if not isinstance(column, Unset):
        json_column = column.value

    params["column"] = json_column

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/auditevents",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AuditEventsResponse | Error | None:
    if response.status_code == 200:
        response_200 = AuditEventsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AuditEventsResponse | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    start_timestamp: int | Unset = UNSET,
    end_timestamp: int | Unset = UNSET,
    actor_id: str | Unset = UNSET,
    actor_name: str | Unset = UNSET,
    event: str | Unset = UNSET,
    target_type: str | Unset = UNSET,
    target_id: str | Unset = UNSET,
    target_name: str | Unset = UNSET,
    within_project_id: str | Unset = UNSET,
    within_project_name: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    column: FetchAuditEventsColumn | Unset = UNSET,
) -> Response[AuditEventsResponse | Error]:
    """
    Args:
        start_timestamp (int | Unset):
        end_timestamp (int | Unset):
        actor_id (str | Unset):
        actor_name (str | Unset):
        event (str | Unset):
        target_type (str | Unset):
        target_id (str | Unset):
        target_name (str | Unset):
        within_project_id (str | Unset):
        within_project_name (str | Unset):
        sort (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        column (FetchAuditEventsColumn | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditEventsResponse | Error]
    """

    kwargs = _get_kwargs(
        start_timestamp=start_timestamp,
        end_timestamp=end_timestamp,
        actor_id=actor_id,
        actor_name=actor_name,
        event=event,
        target_type=target_type,
        target_id=target_id,
        target_name=target_name,
        within_project_id=within_project_id,
        within_project_name=within_project_name,
        sort=sort,
        limit=limit,
        offset=offset,
        column=column,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    start_timestamp: int | Unset = UNSET,
    end_timestamp: int | Unset = UNSET,
    actor_id: str | Unset = UNSET,
    actor_name: str | Unset = UNSET,
    event: str | Unset = UNSET,
    target_type: str | Unset = UNSET,
    target_id: str | Unset = UNSET,
    target_name: str | Unset = UNSET,
    within_project_id: str | Unset = UNSET,
    within_project_name: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    column: FetchAuditEventsColumn | Unset = UNSET,
) -> AuditEventsResponse | Error | None:
    """
    Args:
        start_timestamp (int | Unset):
        end_timestamp (int | Unset):
        actor_id (str | Unset):
        actor_name (str | Unset):
        event (str | Unset):
        target_type (str | Unset):
        target_id (str | Unset):
        target_name (str | Unset):
        within_project_id (str | Unset):
        within_project_name (str | Unset):
        sort (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        column (FetchAuditEventsColumn | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditEventsResponse | Error
    """

    return sync_detailed(
        client=client,
        start_timestamp=start_timestamp,
        end_timestamp=end_timestamp,
        actor_id=actor_id,
        actor_name=actor_name,
        event=event,
        target_type=target_type,
        target_id=target_id,
        target_name=target_name,
        within_project_id=within_project_id,
        within_project_name=within_project_name,
        sort=sort,
        limit=limit,
        offset=offset,
        column=column,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    start_timestamp: int | Unset = UNSET,
    end_timestamp: int | Unset = UNSET,
    actor_id: str | Unset = UNSET,
    actor_name: str | Unset = UNSET,
    event: str | Unset = UNSET,
    target_type: str | Unset = UNSET,
    target_id: str | Unset = UNSET,
    target_name: str | Unset = UNSET,
    within_project_id: str | Unset = UNSET,
    within_project_name: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    column: FetchAuditEventsColumn | Unset = UNSET,
) -> Response[AuditEventsResponse | Error]:
    """
    Args:
        start_timestamp (int | Unset):
        end_timestamp (int | Unset):
        actor_id (str | Unset):
        actor_name (str | Unset):
        event (str | Unset):
        target_type (str | Unset):
        target_id (str | Unset):
        target_name (str | Unset):
        within_project_id (str | Unset):
        within_project_name (str | Unset):
        sort (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        column (FetchAuditEventsColumn | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditEventsResponse | Error]
    """

    kwargs = _get_kwargs(
        start_timestamp=start_timestamp,
        end_timestamp=end_timestamp,
        actor_id=actor_id,
        actor_name=actor_name,
        event=event,
        target_type=target_type,
        target_id=target_id,
        target_name=target_name,
        within_project_id=within_project_id,
        within_project_name=within_project_name,
        sort=sort,
        limit=limit,
        offset=offset,
        column=column,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    start_timestamp: int | Unset = UNSET,
    end_timestamp: int | Unset = UNSET,
    actor_id: str | Unset = UNSET,
    actor_name: str | Unset = UNSET,
    event: str | Unset = UNSET,
    target_type: str | Unset = UNSET,
    target_id: str | Unset = UNSET,
    target_name: str | Unset = UNSET,
    within_project_id: str | Unset = UNSET,
    within_project_name: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    column: FetchAuditEventsColumn | Unset = UNSET,
) -> AuditEventsResponse | Error | None:
    """
    Args:
        start_timestamp (int | Unset):
        end_timestamp (int | Unset):
        actor_id (str | Unset):
        actor_name (str | Unset):
        event (str | Unset):
        target_type (str | Unset):
        target_id (str | Unset):
        target_name (str | Unset):
        within_project_id (str | Unset):
        within_project_name (str | Unset):
        sort (str | Unset):
        limit (int | Unset):
        offset (int | Unset):
        column (FetchAuditEventsColumn | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditEventsResponse | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            start_timestamp=start_timestamp,
            end_timestamp=end_timestamp,
            actor_id=actor_id,
            actor_name=actor_name,
            event=event,
            target_type=target_type,
            target_id=target_id,
            target_name=target_name,
            within_project_id=within_project_id,
            within_project_name=within_project_name,
            sort=sort,
            limit=limit,
            offset=offset,
            column=column,
        )
    ).parsed
