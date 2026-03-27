from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_workspaces_api_log_set import DominoWorkspacesApiLogSet
from ...models.get_logs_log_type import GetLogsLogType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace_id: str,
    *,
    log_type: GetLogsLogType | Unset = GetLogsLogType.CONSOLE,
    limit: float | Unset = 10000.0,
    offset: float | Unset = 0.0,
    latest_time_nano: str | Unset = "0",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_log_type: str | Unset = UNSET
    if not isinstance(log_type, Unset):
        json_log_type = log_type.value

    params["logType"] = json_log_type

    params["limit"] = limit

    params["offset"] = offset

    params["latestTimeNano"] = latest_time_nano

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspaces/{workspace_id}/logs".format(
            workspace_id=quote(str(workspace_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoWorkspacesApiLogSet | None:
    if response.status_code == 200:
        response_200 = DominoWorkspacesApiLogSet.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoWorkspacesApiLogSet]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    log_type: GetLogsLogType | Unset = GetLogsLogType.CONSOLE,
    limit: float | Unset = 10000.0,
    offset: float | Unset = 0.0,
    latest_time_nano: str | Unset = "0",
) -> Response[DominoApiErrorResponse | DominoWorkspacesApiLogSet]:
    """Get the logs of a workspace

    Args:
        workspace_id (str):
        log_type (GetLogsLogType | Unset):  Default: GetLogsLogType.CONSOLE. Example: console  |
            stdout  |  stderr  |  stdoutstderr  |  prepareoutput.
        limit (float | Unset):  Default: 10000.0.
        offset (float | Unset):  Default: 0.0.
        latest_time_nano (str | Unset):  Default: '0'. Example: 1543538813745986325.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoWorkspacesApiLogSet]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        log_type=log_type,
        limit=limit,
        offset=offset,
        latest_time_nano=latest_time_nano,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    log_type: GetLogsLogType | Unset = GetLogsLogType.CONSOLE,
    limit: float | Unset = 10000.0,
    offset: float | Unset = 0.0,
    latest_time_nano: str | Unset = "0",
) -> DominoApiErrorResponse | DominoWorkspacesApiLogSet | None:
    """Get the logs of a workspace

    Args:
        workspace_id (str):
        log_type (GetLogsLogType | Unset):  Default: GetLogsLogType.CONSOLE. Example: console  |
            stdout  |  stderr  |  stdoutstderr  |  prepareoutput.
        limit (float | Unset):  Default: 10000.0.
        offset (float | Unset):  Default: 0.0.
        latest_time_nano (str | Unset):  Default: '0'. Example: 1543538813745986325.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoWorkspacesApiLogSet
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        log_type=log_type,
        limit=limit,
        offset=offset,
        latest_time_nano=latest_time_nano,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    log_type: GetLogsLogType | Unset = GetLogsLogType.CONSOLE,
    limit: float | Unset = 10000.0,
    offset: float | Unset = 0.0,
    latest_time_nano: str | Unset = "0",
) -> Response[DominoApiErrorResponse | DominoWorkspacesApiLogSet]:
    """Get the logs of a workspace

    Args:
        workspace_id (str):
        log_type (GetLogsLogType | Unset):  Default: GetLogsLogType.CONSOLE. Example: console  |
            stdout  |  stderr  |  stdoutstderr  |  prepareoutput.
        limit (float | Unset):  Default: 10000.0.
        offset (float | Unset):  Default: 0.0.
        latest_time_nano (str | Unset):  Default: '0'. Example: 1543538813745986325.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoWorkspacesApiLogSet]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        log_type=log_type,
        limit=limit,
        offset=offset,
        latest_time_nano=latest_time_nano,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    log_type: GetLogsLogType | Unset = GetLogsLogType.CONSOLE,
    limit: float | Unset = 10000.0,
    offset: float | Unset = 0.0,
    latest_time_nano: str | Unset = "0",
) -> DominoApiErrorResponse | DominoWorkspacesApiLogSet | None:
    """Get the logs of a workspace

    Args:
        workspace_id (str):
        log_type (GetLogsLogType | Unset):  Default: GetLogsLogType.CONSOLE. Example: console  |
            stdout  |  stderr  |  stdoutstderr  |  prepareoutput.
        limit (float | Unset):  Default: 10000.0.
        offset (float | Unset):  Default: 0.0.
        latest_time_nano (str | Unset):  Default: '0'. Example: 1543538813745986325.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoWorkspacesApiLogSet
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            log_type=log_type,
            limit=limit,
            offset=offset,
            latest_time_nano=latest_time_nano,
        )
    ).parsed
