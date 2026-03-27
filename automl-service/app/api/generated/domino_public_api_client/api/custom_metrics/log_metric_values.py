from __future__ import annotations
from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.log_metric_values_response_400 import LogMetricValuesResponse400
from ...models.log_metric_values_response_404 import LogMetricValuesResponse404
from ...models.log_metric_values_response_500 import LogMetricValuesResponse500
from ...models.new_metric_values_envelope_v1 import NewMetricValuesEnvelopeV1
from ...types import Response


def _get_kwargs(
    *,
    body: NewMetricValuesEnvelopeV1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/metricValues/v1",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | FailureEnvelopeV1
    | LogMetricValuesResponse400
    | LogMetricValuesResponse404
    | LogMetricValuesResponse500
    | None
):
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201

    if response.status_code == 400:
        response_400 = LogMetricValuesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = LogMetricValuesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = LogMetricValuesResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | FailureEnvelopeV1 | LogMetricValuesResponse400 | LogMetricValuesResponse404 | LogMetricValuesResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: NewMetricValuesEnvelopeV1,
) -> Response[
    Any | FailureEnvelopeV1 | LogMetricValuesResponse400 | LogMetricValuesResponse404 | LogMetricValuesResponse500
]:
    """Log metric values

     Log metric values. Required Permissions: `RegisterMonitoringDataset`

    Args:
        body (NewMetricValuesEnvelopeV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FailureEnvelopeV1 | LogMetricValuesResponse400 | LogMetricValuesResponse404 | LogMetricValuesResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: NewMetricValuesEnvelopeV1,
) -> (
    Any
    | FailureEnvelopeV1
    | LogMetricValuesResponse400
    | LogMetricValuesResponse404
    | LogMetricValuesResponse500
    | None
):
    """Log metric values

     Log metric values. Required Permissions: `RegisterMonitoringDataset`

    Args:
        body (NewMetricValuesEnvelopeV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FailureEnvelopeV1 | LogMetricValuesResponse400 | LogMetricValuesResponse404 | LogMetricValuesResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: NewMetricValuesEnvelopeV1,
) -> Response[
    Any | FailureEnvelopeV1 | LogMetricValuesResponse400 | LogMetricValuesResponse404 | LogMetricValuesResponse500
]:
    """Log metric values

     Log metric values. Required Permissions: `RegisterMonitoringDataset`

    Args:
        body (NewMetricValuesEnvelopeV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FailureEnvelopeV1 | LogMetricValuesResponse400 | LogMetricValuesResponse404 | LogMetricValuesResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: NewMetricValuesEnvelopeV1,
) -> (
    Any
    | FailureEnvelopeV1
    | LogMetricValuesResponse400
    | LogMetricValuesResponse404
    | LogMetricValuesResponse500
    | None
):
    """Log metric values

     Log metric values. Required Permissions: `RegisterMonitoringDataset`

    Args:
        body (NewMetricValuesEnvelopeV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FailureEnvelopeV1 | LogMetricValuesResponse400 | LogMetricValuesResponse404 | LogMetricValuesResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
