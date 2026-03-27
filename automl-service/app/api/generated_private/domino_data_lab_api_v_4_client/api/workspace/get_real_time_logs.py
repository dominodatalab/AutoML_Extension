from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_computegrid_log_set import DominoComputegridLogSet
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    workspace_session_id: str,
    *,
    limit: float | None | Unset = 10000.0,
    offset: float | Unset = 0.0,
    latest_time_nano: None | str | Unset = "0",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_limit: float | None | Unset
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["limit"] = json_limit

    params["offset"] = offset

    json_latest_time_nano: None | str | Unset
    if isinstance(latest_time_nano, Unset):
        json_latest_time_nano = UNSET
    else:
        json_latest_time_nano = latest_time_nano
    params["latestTimeNano"] = json_latest_time_nano

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspace/{project_id}/{workspace_session_id}/realTimeLogs".format(
            project_id=quote(str(project_id), safe=""),
            workspace_session_id=quote(str(workspace_session_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoComputegridLogSet | None:
    if response.status_code == 200:
        response_200 = DominoComputegridLogSet.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoComputegridLogSet]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    workspace_session_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: float | None | Unset = 10000.0,
    offset: float | Unset = 0.0,
    latest_time_nano: None | str | Unset = "0",
) -> Response[DominoApiErrorResponse | DominoComputegridLogSet]:
    """Get the logs of a workspace

    Args:
        project_id (str):
        workspace_session_id (str):
        limit (float | None | Unset):  Default: 10000.0.
        offset (float | Unset):  Default: 0.0.
        latest_time_nano (None | str | Unset):  Default: '0'. Example: 1543538813745986325.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoComputegridLogSet]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        workspace_session_id=workspace_session_id,
        limit=limit,
        offset=offset,
        latest_time_nano=latest_time_nano,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    workspace_session_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: float | None | Unset = 10000.0,
    offset: float | Unset = 0.0,
    latest_time_nano: None | str | Unset = "0",
) -> DominoApiErrorResponse | DominoComputegridLogSet | None:
    """Get the logs of a workspace

    Args:
        project_id (str):
        workspace_session_id (str):
        limit (float | None | Unset):  Default: 10000.0.
        offset (float | Unset):  Default: 0.0.
        latest_time_nano (None | str | Unset):  Default: '0'. Example: 1543538813745986325.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoComputegridLogSet
    """

    return sync_detailed(
        project_id=project_id,
        workspace_session_id=workspace_session_id,
        client=client,
        limit=limit,
        offset=offset,
        latest_time_nano=latest_time_nano,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    workspace_session_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: float | None | Unset = 10000.0,
    offset: float | Unset = 0.0,
    latest_time_nano: None | str | Unset = "0",
) -> Response[DominoApiErrorResponse | DominoComputegridLogSet]:
    """Get the logs of a workspace

    Args:
        project_id (str):
        workspace_session_id (str):
        limit (float | None | Unset):  Default: 10000.0.
        offset (float | Unset):  Default: 0.0.
        latest_time_nano (None | str | Unset):  Default: '0'. Example: 1543538813745986325.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoComputegridLogSet]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        workspace_session_id=workspace_session_id,
        limit=limit,
        offset=offset,
        latest_time_nano=latest_time_nano,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    workspace_session_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: float | None | Unset = 10000.0,
    offset: float | Unset = 0.0,
    latest_time_nano: None | str | Unset = "0",
) -> DominoApiErrorResponse | DominoComputegridLogSet | None:
    """Get the logs of a workspace

    Args:
        project_id (str):
        workspace_session_id (str):
        limit (float | None | Unset):  Default: 10000.0.
        offset (float | Unset):  Default: 0.0.
        latest_time_nano (None | str | Unset):  Default: '0'. Example: 1543538813745986325.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoComputegridLogSet
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            workspace_session_id=workspace_session_id,
            client=client,
            limit=limit,
            offset=offset,
            latest_time_nano=latest_time_nano,
        )
    ).parsed
