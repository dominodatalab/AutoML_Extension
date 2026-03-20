from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.metric_values_envelope_v1 import MetricValuesEnvelopeV1
from ...models.retrieve_metric_values_response_400 import RetrieveMetricValuesResponse400
from ...models.retrieve_metric_values_response_404 import RetrieveMetricValuesResponse404
from ...models.retrieve_metric_values_response_500 import RetrieveMetricValuesResponse500
from ...types import UNSET, Response


def _get_kwargs(
    model_monitoring_id: str,
    metric: str,
    *,
    starting_reference_timestamp_inclusive: str,
    ending_reference_timestamp_inclusive: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["startingReferenceTimestampInclusive"] = starting_reference_timestamp_inclusive

    params["endingReferenceTimestampInclusive"] = ending_reference_timestamp_inclusive

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/metricValues/v1/{model_monitoring_id}/{metric}".format(
            model_monitoring_id=quote(str(model_monitoring_id), safe=""),
            metric=quote(str(metric), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | MetricValuesEnvelopeV1
    | RetrieveMetricValuesResponse400
    | RetrieveMetricValuesResponse404
    | RetrieveMetricValuesResponse500
    | None
):
    if response.status_code == 200:
        response_200 = MetricValuesEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RetrieveMetricValuesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = RetrieveMetricValuesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = RetrieveMetricValuesResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | MetricValuesEnvelopeV1
    | RetrieveMetricValuesResponse400
    | RetrieveMetricValuesResponse404
    | RetrieveMetricValuesResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    model_monitoring_id: str,
    metric: str,
    *,
    client: AuthenticatedClient | Client,
    starting_reference_timestamp_inclusive: str,
    ending_reference_timestamp_inclusive: str,
) -> Response[
    FailureEnvelopeV1
    | MetricValuesEnvelopeV1
    | RetrieveMetricValuesResponse400
    | RetrieveMetricValuesResponse404
    | RetrieveMetricValuesResponse500
]:
    """Retrieve metric values

     Retrieve metric values. Required Permissions: `UpdateMonitoringSettings`

    Args:
        model_monitoring_id (str):
        metric (str):
        starting_reference_timestamp_inclusive (str):
        ending_reference_timestamp_inclusive (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | MetricValuesEnvelopeV1 | RetrieveMetricValuesResponse400 | RetrieveMetricValuesResponse404 | RetrieveMetricValuesResponse500]
    """

    kwargs = _get_kwargs(
        model_monitoring_id=model_monitoring_id,
        metric=metric,
        starting_reference_timestamp_inclusive=starting_reference_timestamp_inclusive,
        ending_reference_timestamp_inclusive=ending_reference_timestamp_inclusive,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    model_monitoring_id: str,
    metric: str,
    *,
    client: AuthenticatedClient | Client,
    starting_reference_timestamp_inclusive: str,
    ending_reference_timestamp_inclusive: str,
) -> (
    FailureEnvelopeV1
    | MetricValuesEnvelopeV1
    | RetrieveMetricValuesResponse400
    | RetrieveMetricValuesResponse404
    | RetrieveMetricValuesResponse500
    | None
):
    """Retrieve metric values

     Retrieve metric values. Required Permissions: `UpdateMonitoringSettings`

    Args:
        model_monitoring_id (str):
        metric (str):
        starting_reference_timestamp_inclusive (str):
        ending_reference_timestamp_inclusive (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | MetricValuesEnvelopeV1 | RetrieveMetricValuesResponse400 | RetrieveMetricValuesResponse404 | RetrieveMetricValuesResponse500
    """

    return sync_detailed(
        model_monitoring_id=model_monitoring_id,
        metric=metric,
        client=client,
        starting_reference_timestamp_inclusive=starting_reference_timestamp_inclusive,
        ending_reference_timestamp_inclusive=ending_reference_timestamp_inclusive,
    ).parsed


async def asyncio_detailed(
    model_monitoring_id: str,
    metric: str,
    *,
    client: AuthenticatedClient | Client,
    starting_reference_timestamp_inclusive: str,
    ending_reference_timestamp_inclusive: str,
) -> Response[
    FailureEnvelopeV1
    | MetricValuesEnvelopeV1
    | RetrieveMetricValuesResponse400
    | RetrieveMetricValuesResponse404
    | RetrieveMetricValuesResponse500
]:
    """Retrieve metric values

     Retrieve metric values. Required Permissions: `UpdateMonitoringSettings`

    Args:
        model_monitoring_id (str):
        metric (str):
        starting_reference_timestamp_inclusive (str):
        ending_reference_timestamp_inclusive (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | MetricValuesEnvelopeV1 | RetrieveMetricValuesResponse400 | RetrieveMetricValuesResponse404 | RetrieveMetricValuesResponse500]
    """

    kwargs = _get_kwargs(
        model_monitoring_id=model_monitoring_id,
        metric=metric,
        starting_reference_timestamp_inclusive=starting_reference_timestamp_inclusive,
        ending_reference_timestamp_inclusive=ending_reference_timestamp_inclusive,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    model_monitoring_id: str,
    metric: str,
    *,
    client: AuthenticatedClient | Client,
    starting_reference_timestamp_inclusive: str,
    ending_reference_timestamp_inclusive: str,
) -> (
    FailureEnvelopeV1
    | MetricValuesEnvelopeV1
    | RetrieveMetricValuesResponse400
    | RetrieveMetricValuesResponse404
    | RetrieveMetricValuesResponse500
    | None
):
    """Retrieve metric values

     Retrieve metric values. Required Permissions: `UpdateMonitoringSettings`

    Args:
        model_monitoring_id (str):
        metric (str):
        starting_reference_timestamp_inclusive (str):
        ending_reference_timestamp_inclusive (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | MetricValuesEnvelopeV1 | RetrieveMetricValuesResponse400 | RetrieveMetricValuesResponse404 | RetrieveMetricValuesResponse500
    """

    return (
        await asyncio_detailed(
            model_monitoring_id=model_monitoring_id,
            metric=metric,
            client=client,
            starting_reference_timestamp_inclusive=starting_reference_timestamp_inclusive,
            ending_reference_timestamp_inclusive=ending_reference_timestamp_inclusive,
        )
    ).parsed
