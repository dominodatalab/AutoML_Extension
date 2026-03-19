from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_model_endpoint_version_real_time_logs_log_type import GetModelEndpointVersionRealTimeLogsLogType
from ...models.get_model_endpoint_version_real_time_logs_response_400 import (
    GetModelEndpointVersionRealTimeLogsResponse400,
)
from ...models.get_model_endpoint_version_real_time_logs_response_404 import (
    GetModelEndpointVersionRealTimeLogsResponse404,
)
from ...models.get_model_endpoint_version_real_time_logs_response_500 import (
    GetModelEndpointVersionRealTimeLogsResponse500,
)
from ...models.model_endpoint_logs_response import ModelEndpointLogsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    endpoint_id: str,
    version_number: int,
    *,
    log_type: GetModelEndpointVersionRealTimeLogsLogType | Unset = GetModelEndpointVersionRealTimeLogsLogType.COMPLETE,
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
        "url": "/api/gen-ai/beta/endpoints/{endpoint_id}/versions/{version_number}/realTimeLogs".format(
            endpoint_id=quote(str(endpoint_id), safe=""),
            version_number=quote(str(version_number), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GetModelEndpointVersionRealTimeLogsResponse400
    | GetModelEndpointVersionRealTimeLogsResponse404
    | GetModelEndpointVersionRealTimeLogsResponse500
    | ModelEndpointLogsResponse
    | None
):
    if response.status_code == 200:
        response_200 = ModelEndpointLogsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetModelEndpointVersionRealTimeLogsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetModelEndpointVersionRealTimeLogsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetModelEndpointVersionRealTimeLogsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | GetModelEndpointVersionRealTimeLogsResponse400
    | GetModelEndpointVersionRealTimeLogsResponse404
    | GetModelEndpointVersionRealTimeLogsResponse500
    | ModelEndpointLogsResponse
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    endpoint_id: str,
    version_number: int,
    *,
    client: AuthenticatedClient | Client,
    log_type: GetModelEndpointVersionRealTimeLogsLogType | Unset = GetModelEndpointVersionRealTimeLogsLogType.COMPLETE,
    limit: int | Unset = 10000,
    offset: int | Unset = 0,
    latest_time: str | Unset = "0",
) -> Response[
    FailureEnvelopeV1
    | GetModelEndpointVersionRealTimeLogsResponse400
    | GetModelEndpointVersionRealTimeLogsResponse404
    | GetModelEndpointVersionRealTimeLogsResponse500
    | ModelEndpointLogsResponse
]:
    """Get Gen AI Endpoint Version Real Time Logs

     Retrieve a Gen AI Endpoint Version Real Time Logs

    Args:
        endpoint_id (str):
        version_number (int):
        log_type (GetModelEndpointVersionRealTimeLogsLogType | Unset):  Default:
            GetModelEndpointVersionRealTimeLogsLogType.COMPLETE.
        limit (int | Unset):  Default: 10000.
        offset (int | Unset):  Default: 0.
        latest_time (str | Unset):  Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetModelEndpointVersionRealTimeLogsResponse400 | GetModelEndpointVersionRealTimeLogsResponse404 | GetModelEndpointVersionRealTimeLogsResponse500 | ModelEndpointLogsResponse]
    """

    kwargs = _get_kwargs(
        endpoint_id=endpoint_id,
        version_number=version_number,
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
    endpoint_id: str,
    version_number: int,
    *,
    client: AuthenticatedClient | Client,
    log_type: GetModelEndpointVersionRealTimeLogsLogType | Unset = GetModelEndpointVersionRealTimeLogsLogType.COMPLETE,
    limit: int | Unset = 10000,
    offset: int | Unset = 0,
    latest_time: str | Unset = "0",
) -> (
    FailureEnvelopeV1
    | GetModelEndpointVersionRealTimeLogsResponse400
    | GetModelEndpointVersionRealTimeLogsResponse404
    | GetModelEndpointVersionRealTimeLogsResponse500
    | ModelEndpointLogsResponse
    | None
):
    """Get Gen AI Endpoint Version Real Time Logs

     Retrieve a Gen AI Endpoint Version Real Time Logs

    Args:
        endpoint_id (str):
        version_number (int):
        log_type (GetModelEndpointVersionRealTimeLogsLogType | Unset):  Default:
            GetModelEndpointVersionRealTimeLogsLogType.COMPLETE.
        limit (int | Unset):  Default: 10000.
        offset (int | Unset):  Default: 0.
        latest_time (str | Unset):  Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetModelEndpointVersionRealTimeLogsResponse400 | GetModelEndpointVersionRealTimeLogsResponse404 | GetModelEndpointVersionRealTimeLogsResponse500 | ModelEndpointLogsResponse
    """

    return sync_detailed(
        endpoint_id=endpoint_id,
        version_number=version_number,
        client=client,
        log_type=log_type,
        limit=limit,
        offset=offset,
        latest_time=latest_time,
    ).parsed


async def asyncio_detailed(
    endpoint_id: str,
    version_number: int,
    *,
    client: AuthenticatedClient | Client,
    log_type: GetModelEndpointVersionRealTimeLogsLogType | Unset = GetModelEndpointVersionRealTimeLogsLogType.COMPLETE,
    limit: int | Unset = 10000,
    offset: int | Unset = 0,
    latest_time: str | Unset = "0",
) -> Response[
    FailureEnvelopeV1
    | GetModelEndpointVersionRealTimeLogsResponse400
    | GetModelEndpointVersionRealTimeLogsResponse404
    | GetModelEndpointVersionRealTimeLogsResponse500
    | ModelEndpointLogsResponse
]:
    """Get Gen AI Endpoint Version Real Time Logs

     Retrieve a Gen AI Endpoint Version Real Time Logs

    Args:
        endpoint_id (str):
        version_number (int):
        log_type (GetModelEndpointVersionRealTimeLogsLogType | Unset):  Default:
            GetModelEndpointVersionRealTimeLogsLogType.COMPLETE.
        limit (int | Unset):  Default: 10000.
        offset (int | Unset):  Default: 0.
        latest_time (str | Unset):  Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetModelEndpointVersionRealTimeLogsResponse400 | GetModelEndpointVersionRealTimeLogsResponse404 | GetModelEndpointVersionRealTimeLogsResponse500 | ModelEndpointLogsResponse]
    """

    kwargs = _get_kwargs(
        endpoint_id=endpoint_id,
        version_number=version_number,
        log_type=log_type,
        limit=limit,
        offset=offset,
        latest_time=latest_time,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    endpoint_id: str,
    version_number: int,
    *,
    client: AuthenticatedClient | Client,
    log_type: GetModelEndpointVersionRealTimeLogsLogType | Unset = GetModelEndpointVersionRealTimeLogsLogType.COMPLETE,
    limit: int | Unset = 10000,
    offset: int | Unset = 0,
    latest_time: str | Unset = "0",
) -> (
    FailureEnvelopeV1
    | GetModelEndpointVersionRealTimeLogsResponse400
    | GetModelEndpointVersionRealTimeLogsResponse404
    | GetModelEndpointVersionRealTimeLogsResponse500
    | ModelEndpointLogsResponse
    | None
):
    """Get Gen AI Endpoint Version Real Time Logs

     Retrieve a Gen AI Endpoint Version Real Time Logs

    Args:
        endpoint_id (str):
        version_number (int):
        log_type (GetModelEndpointVersionRealTimeLogsLogType | Unset):  Default:
            GetModelEndpointVersionRealTimeLogsLogType.COMPLETE.
        limit (int | Unset):  Default: 10000.
        offset (int | Unset):  Default: 0.
        latest_time (str | Unset):  Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetModelEndpointVersionRealTimeLogsResponse400 | GetModelEndpointVersionRealTimeLogsResponse404 | GetModelEndpointVersionRealTimeLogsResponse500 | ModelEndpointLogsResponse
    """

    return (
        await asyncio_detailed(
            endpoint_id=endpoint_id,
            version_number=version_number,
            client=client,
            log_type=log_type,
            limit=limit,
            offset=offset,
            latest_time=latest_time,
        )
    ).parsed
