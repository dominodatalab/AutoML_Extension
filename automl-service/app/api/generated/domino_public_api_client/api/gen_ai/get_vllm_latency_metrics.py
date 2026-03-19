import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_vllm_latency_metrics_aggregation_window import GetVllmLatencyMetricsAggregationWindow
from ...models.get_vllm_latency_metrics_response_400 import GetVllmLatencyMetricsResponse400
from ...models.get_vllm_latency_metrics_response_404 import GetVllmLatencyMetricsResponse404
from ...models.get_vllm_latency_metrics_response_500 import GetVllmLatencyMetricsResponse500
from ...models.vllm_latency_metrics_v1 import VllmLatencyMetricsV1
from ...types import UNSET, Response, Unset


def _get_kwargs(
    endpoint_id: str,
    version_number: int,
    *,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    aggregation_window: GetVllmLatencyMetricsAggregationWindow | Unset = UNSET,
    max_historical_executions: int | Unset = 3,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_start_time: str | Unset = UNSET
    if not isinstance(start_time, Unset):
        json_start_time = start_time.isoformat()
    params["startTime"] = json_start_time

    json_end_time: str | Unset = UNSET
    if not isinstance(end_time, Unset):
        json_end_time = end_time.isoformat()
    params["endTime"] = json_end_time

    json_aggregation_window: str | Unset = UNSET
    if not isinstance(aggregation_window, Unset):
        json_aggregation_window = aggregation_window.value

    params["aggregationWindow"] = json_aggregation_window

    params["maxHistoricalExecutions"] = max_historical_executions

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/gen-ai/beta/endpoints/{endpoint_id}/versions/{version_number}/vllm-latency-metrics".format(
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
    | GetVllmLatencyMetricsResponse400
    | GetVllmLatencyMetricsResponse404
    | GetVllmLatencyMetricsResponse500
    | VllmLatencyMetricsV1
    | None
):
    if response.status_code == 200:
        response_200 = VllmLatencyMetricsV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetVllmLatencyMetricsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetVllmLatencyMetricsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetVllmLatencyMetricsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | GetVllmLatencyMetricsResponse400
    | GetVllmLatencyMetricsResponse404
    | GetVllmLatencyMetricsResponse500
    | VllmLatencyMetricsV1
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
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    aggregation_window: GetVllmLatencyMetricsAggregationWindow | Unset = UNSET,
    max_historical_executions: int | Unset = 3,
) -> Response[
    FailureEnvelopeV1
    | GetVllmLatencyMetricsResponse400
    | GetVllmLatencyMetricsResponse404
    | GetVllmLatencyMetricsResponse500
    | VllmLatencyMetricsV1
]:
    """Get vLLM latency metrics for a model endpoint version

     Get vLLM latency metrics time series data for a specific model endpoint version from Prometheus.
    Returns smoothed averages for time to first token, end-to-end latency, and time per output token.

    Args:
        endpoint_id (str):  Example: 62313ce67a0af0281c01a6a5.
        version_number (int):  Example: 1.
        start_time (datetime.datetime | Unset):  Example: 2024-01-15T10:00:00Z.
        end_time (datetime.datetime | Unset):  Example: 2024-01-16T10:00:00Z.
        aggregation_window (GetVllmLatencyMetricsAggregationWindow | Unset):  Example: hourly.
        max_historical_executions (int | Unset):  Default: 3. Example: 3.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetVllmLatencyMetricsResponse400 | GetVllmLatencyMetricsResponse404 | GetVllmLatencyMetricsResponse500 | VllmLatencyMetricsV1]
    """

    kwargs = _get_kwargs(
        endpoint_id=endpoint_id,
        version_number=version_number,
        start_time=start_time,
        end_time=end_time,
        aggregation_window=aggregation_window,
        max_historical_executions=max_historical_executions,
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
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    aggregation_window: GetVllmLatencyMetricsAggregationWindow | Unset = UNSET,
    max_historical_executions: int | Unset = 3,
) -> (
    FailureEnvelopeV1
    | GetVllmLatencyMetricsResponse400
    | GetVllmLatencyMetricsResponse404
    | GetVllmLatencyMetricsResponse500
    | VllmLatencyMetricsV1
    | None
):
    """Get vLLM latency metrics for a model endpoint version

     Get vLLM latency metrics time series data for a specific model endpoint version from Prometheus.
    Returns smoothed averages for time to first token, end-to-end latency, and time per output token.

    Args:
        endpoint_id (str):  Example: 62313ce67a0af0281c01a6a5.
        version_number (int):  Example: 1.
        start_time (datetime.datetime | Unset):  Example: 2024-01-15T10:00:00Z.
        end_time (datetime.datetime | Unset):  Example: 2024-01-16T10:00:00Z.
        aggregation_window (GetVllmLatencyMetricsAggregationWindow | Unset):  Example: hourly.
        max_historical_executions (int | Unset):  Default: 3. Example: 3.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetVllmLatencyMetricsResponse400 | GetVllmLatencyMetricsResponse404 | GetVllmLatencyMetricsResponse500 | VllmLatencyMetricsV1
    """

    return sync_detailed(
        endpoint_id=endpoint_id,
        version_number=version_number,
        client=client,
        start_time=start_time,
        end_time=end_time,
        aggregation_window=aggregation_window,
        max_historical_executions=max_historical_executions,
    ).parsed


async def asyncio_detailed(
    endpoint_id: str,
    version_number: int,
    *,
    client: AuthenticatedClient | Client,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    aggregation_window: GetVllmLatencyMetricsAggregationWindow | Unset = UNSET,
    max_historical_executions: int | Unset = 3,
) -> Response[
    FailureEnvelopeV1
    | GetVllmLatencyMetricsResponse400
    | GetVllmLatencyMetricsResponse404
    | GetVllmLatencyMetricsResponse500
    | VllmLatencyMetricsV1
]:
    """Get vLLM latency metrics for a model endpoint version

     Get vLLM latency metrics time series data for a specific model endpoint version from Prometheus.
    Returns smoothed averages for time to first token, end-to-end latency, and time per output token.

    Args:
        endpoint_id (str):  Example: 62313ce67a0af0281c01a6a5.
        version_number (int):  Example: 1.
        start_time (datetime.datetime | Unset):  Example: 2024-01-15T10:00:00Z.
        end_time (datetime.datetime | Unset):  Example: 2024-01-16T10:00:00Z.
        aggregation_window (GetVllmLatencyMetricsAggregationWindow | Unset):  Example: hourly.
        max_historical_executions (int | Unset):  Default: 3. Example: 3.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetVllmLatencyMetricsResponse400 | GetVllmLatencyMetricsResponse404 | GetVllmLatencyMetricsResponse500 | VllmLatencyMetricsV1]
    """

    kwargs = _get_kwargs(
        endpoint_id=endpoint_id,
        version_number=version_number,
        start_time=start_time,
        end_time=end_time,
        aggregation_window=aggregation_window,
        max_historical_executions=max_historical_executions,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    endpoint_id: str,
    version_number: int,
    *,
    client: AuthenticatedClient | Client,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    aggregation_window: GetVllmLatencyMetricsAggregationWindow | Unset = UNSET,
    max_historical_executions: int | Unset = 3,
) -> (
    FailureEnvelopeV1
    | GetVllmLatencyMetricsResponse400
    | GetVllmLatencyMetricsResponse404
    | GetVllmLatencyMetricsResponse500
    | VllmLatencyMetricsV1
    | None
):
    """Get vLLM latency metrics for a model endpoint version

     Get vLLM latency metrics time series data for a specific model endpoint version from Prometheus.
    Returns smoothed averages for time to first token, end-to-end latency, and time per output token.

    Args:
        endpoint_id (str):  Example: 62313ce67a0af0281c01a6a5.
        version_number (int):  Example: 1.
        start_time (datetime.datetime | Unset):  Example: 2024-01-15T10:00:00Z.
        end_time (datetime.datetime | Unset):  Example: 2024-01-16T10:00:00Z.
        aggregation_window (GetVllmLatencyMetricsAggregationWindow | Unset):  Example: hourly.
        max_historical_executions (int | Unset):  Default: 3. Example: 3.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetVllmLatencyMetricsResponse400 | GetVllmLatencyMetricsResponse404 | GetVllmLatencyMetricsResponse500 | VllmLatencyMetricsV1
    """

    return (
        await asyncio_detailed(
            endpoint_id=endpoint_id,
            version_number=version_number,
            client=client,
            start_time=start_time,
            end_time=end_time,
            aggregation_window=aggregation_window,
            max_historical_executions=max_historical_executions,
        )
    ).parsed
