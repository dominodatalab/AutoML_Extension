from __future__ import annotations
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_instance_logs_response import AppInstanceLogsResponse
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_app_instance_real_time_logs_log_type import GetAppInstanceRealTimeLogsLogType
from ...models.get_app_instance_real_time_logs_response_400 import GetAppInstanceRealTimeLogsResponse400
from ...models.get_app_instance_real_time_logs_response_404 import GetAppInstanceRealTimeLogsResponse404
from ...models.get_app_instance_real_time_logs_response_500 import GetAppInstanceRealTimeLogsResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    app_id: str,
    version_id: str,
    instance_id: str,
    *,
    log_type: GetAppInstanceRealTimeLogsLogType | Unset = GetAppInstanceRealTimeLogsLogType.COMPLETE,
    limit: int | Unset = 10000,
    offset: int | Unset = 0,
    latest_time: str | Unset = "0",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_log_type: str | Unset = UNSET
    if not isinstance(log_type, Unset):
        json_log_type = log_type.value

    params["logType"] = json_log_type

    params["limit"] = limit

    params["offset"] = offset

    params["latestTime"] = latest_time

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/apps/beta/apps/{app_id}/versions/{version_id}/instances/{instance_id}/realTimeLogs".format(
            app_id=quote(str(app_id), safe=""),
            version_id=quote(str(version_id), safe=""),
            instance_id=quote(str(instance_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AppInstanceLogsResponse
    | FailureEnvelopeV1
    | GetAppInstanceRealTimeLogsResponse400
    | GetAppInstanceRealTimeLogsResponse404
    | GetAppInstanceRealTimeLogsResponse500
    | None
):
    if response.status_code == 200:
        response_200 = AppInstanceLogsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetAppInstanceRealTimeLogsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetAppInstanceRealTimeLogsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetAppInstanceRealTimeLogsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AppInstanceLogsResponse
    | FailureEnvelopeV1
    | GetAppInstanceRealTimeLogsResponse400
    | GetAppInstanceRealTimeLogsResponse404
    | GetAppInstanceRealTimeLogsResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_id: str,
    version_id: str,
    instance_id: str,
    *,
    client: AuthenticatedClient | Client,
    log_type: GetAppInstanceRealTimeLogsLogType | Unset = GetAppInstanceRealTimeLogsLogType.COMPLETE,
    limit: int | Unset = 10000,
    offset: int | Unset = 0,
    latest_time: str | Unset = "0",
) -> Response[
    AppInstanceLogsResponse
    | FailureEnvelopeV1
    | GetAppInstanceRealTimeLogsResponse400
    | GetAppInstanceRealTimeLogsResponse404
    | GetAppInstanceRealTimeLogsResponse500
]:
    """Get App Instance Real Time Logs

     Retrieve an App Instance Real Time Logs

    Args:
        app_id (str):
        version_id (str):
        instance_id (str):
        log_type (GetAppInstanceRealTimeLogsLogType | Unset):  Default:
            GetAppInstanceRealTimeLogsLogType.COMPLETE.
        limit (int | Unset):  Default: 10000.
        offset (int | Unset):  Default: 0.
        latest_time (str | Unset):  Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppInstanceLogsResponse | FailureEnvelopeV1 | GetAppInstanceRealTimeLogsResponse400 | GetAppInstanceRealTimeLogsResponse404 | GetAppInstanceRealTimeLogsResponse500]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        version_id=version_id,
        instance_id=instance_id,
        log_type=log_type,
        limit=limit,
        offset=offset,
        latest_time=latest_time,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_id: str,
    version_id: str,
    instance_id: str,
    *,
    client: AuthenticatedClient | Client,
    log_type: GetAppInstanceRealTimeLogsLogType | Unset = GetAppInstanceRealTimeLogsLogType.COMPLETE,
    limit: int | Unset = 10000,
    offset: int | Unset = 0,
    latest_time: str | Unset = "0",
) -> (
    AppInstanceLogsResponse
    | FailureEnvelopeV1
    | GetAppInstanceRealTimeLogsResponse400
    | GetAppInstanceRealTimeLogsResponse404
    | GetAppInstanceRealTimeLogsResponse500
    | None
):
    """Get App Instance Real Time Logs

     Retrieve an App Instance Real Time Logs

    Args:
        app_id (str):
        version_id (str):
        instance_id (str):
        log_type (GetAppInstanceRealTimeLogsLogType | Unset):  Default:
            GetAppInstanceRealTimeLogsLogType.COMPLETE.
        limit (int | Unset):  Default: 10000.
        offset (int | Unset):  Default: 0.
        latest_time (str | Unset):  Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppInstanceLogsResponse | FailureEnvelopeV1 | GetAppInstanceRealTimeLogsResponse400 | GetAppInstanceRealTimeLogsResponse404 | GetAppInstanceRealTimeLogsResponse500
    """

    return sync_detailed(
        app_id=app_id,
        version_id=version_id,
        instance_id=instance_id,
        client=client,
        log_type=log_type,
        limit=limit,
        offset=offset,
        latest_time=latest_time,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    version_id: str,
    instance_id: str,
    *,
    client: AuthenticatedClient | Client,
    log_type: GetAppInstanceRealTimeLogsLogType | Unset = GetAppInstanceRealTimeLogsLogType.COMPLETE,
    limit: int | Unset = 10000,
    offset: int | Unset = 0,
    latest_time: str | Unset = "0",
) -> Response[
    AppInstanceLogsResponse
    | FailureEnvelopeV1
    | GetAppInstanceRealTimeLogsResponse400
    | GetAppInstanceRealTimeLogsResponse404
    | GetAppInstanceRealTimeLogsResponse500
]:
    """Get App Instance Real Time Logs

     Retrieve an App Instance Real Time Logs

    Args:
        app_id (str):
        version_id (str):
        instance_id (str):
        log_type (GetAppInstanceRealTimeLogsLogType | Unset):  Default:
            GetAppInstanceRealTimeLogsLogType.COMPLETE.
        limit (int | Unset):  Default: 10000.
        offset (int | Unset):  Default: 0.
        latest_time (str | Unset):  Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppInstanceLogsResponse | FailureEnvelopeV1 | GetAppInstanceRealTimeLogsResponse400 | GetAppInstanceRealTimeLogsResponse404 | GetAppInstanceRealTimeLogsResponse500]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        version_id=version_id,
        instance_id=instance_id,
        log_type=log_type,
        limit=limit,
        offset=offset,
        latest_time=latest_time,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_id: str,
    version_id: str,
    instance_id: str,
    *,
    client: AuthenticatedClient | Client,
    log_type: GetAppInstanceRealTimeLogsLogType | Unset = GetAppInstanceRealTimeLogsLogType.COMPLETE,
    limit: int | Unset = 10000,
    offset: int | Unset = 0,
    latest_time: str | Unset = "0",
) -> (
    AppInstanceLogsResponse
    | FailureEnvelopeV1
    | GetAppInstanceRealTimeLogsResponse400
    | GetAppInstanceRealTimeLogsResponse404
    | GetAppInstanceRealTimeLogsResponse500
    | None
):
    """Get App Instance Real Time Logs

     Retrieve an App Instance Real Time Logs

    Args:
        app_id (str):
        version_id (str):
        instance_id (str):
        log_type (GetAppInstanceRealTimeLogsLogType | Unset):  Default:
            GetAppInstanceRealTimeLogsLogType.COMPLETE.
        limit (int | Unset):  Default: 10000.
        offset (int | Unset):  Default: 0.
        latest_time (str | Unset):  Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppInstanceLogsResponse | FailureEnvelopeV1 | GetAppInstanceRealTimeLogsResponse400 | GetAppInstanceRealTimeLogsResponse404 | GetAppInstanceRealTimeLogsResponse500
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            version_id=version_id,
            instance_id=instance_id,
            client=client,
            log_type=log_type,
            limit=limit,
            offset=offset,
            latest_time=latest_time,
        )
    ).parsed
