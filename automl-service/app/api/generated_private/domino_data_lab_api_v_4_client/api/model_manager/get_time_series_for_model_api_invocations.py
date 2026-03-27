from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_modelmanager_api_model_api_aggregated_usage_statistics import (
    DominoModelmanagerApiModelApiAggregatedUsageStatistics,
)
from ...types import UNSET, Response


def _get_kwargs(
    model_version_id: str,
    *,
    start_time: float,
    end_time: float,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["startTime"] = start_time

    params["endTime"] = end_time

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/modelManager/{model_version_id}/getTimeSeries".format(
            model_version_id=quote(str(model_version_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | list[DominoModelmanagerApiModelApiAggregatedUsageStatistics] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DominoModelmanagerApiModelApiAggregatedUsageStatistics.from_dict(response_200_item_data)

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

    if response.status_code == 500:
        response_500 = DominoApiErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DominoApiErrorResponse | list[DominoModelmanagerApiModelApiAggregatedUsageStatistics]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    model_version_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_time: float,
    end_time: float,
) -> Response[DominoApiErrorResponse | list[DominoModelmanagerApiModelApiAggregatedUsageStatistics]]:
    """Get timeseries of data for model API invocation

    Args:
        model_version_id (str):
        start_time (float):
        end_time (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoModelmanagerApiModelApiAggregatedUsageStatistics]]
    """

    kwargs = _get_kwargs(
        model_version_id=model_version_id,
        start_time=start_time,
        end_time=end_time,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    model_version_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_time: float,
    end_time: float,
) -> DominoApiErrorResponse | list[DominoModelmanagerApiModelApiAggregatedUsageStatistics] | None:
    """Get timeseries of data for model API invocation

    Args:
        model_version_id (str):
        start_time (float):
        end_time (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoModelmanagerApiModelApiAggregatedUsageStatistics]
    """

    return sync_detailed(
        model_version_id=model_version_id,
        client=client,
        start_time=start_time,
        end_time=end_time,
    ).parsed


async def asyncio_detailed(
    model_version_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_time: float,
    end_time: float,
) -> Response[DominoApiErrorResponse | list[DominoModelmanagerApiModelApiAggregatedUsageStatistics]]:
    """Get timeseries of data for model API invocation

    Args:
        model_version_id (str):
        start_time (float):
        end_time (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoModelmanagerApiModelApiAggregatedUsageStatistics]]
    """

    kwargs = _get_kwargs(
        model_version_id=model_version_id,
        start_time=start_time,
        end_time=end_time,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    model_version_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_time: float,
    end_time: float,
) -> DominoApiErrorResponse | list[DominoModelmanagerApiModelApiAggregatedUsageStatistics] | None:
    """Get timeseries of data for model API invocation

    Args:
        model_version_id (str):
        start_time (float):
        end_time (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoModelmanagerApiModelApiAggregatedUsageStatistics]
    """

    return (
        await asyncio_detailed(
            model_version_id=model_version_id,
            client=client,
            start_time=start_time,
            end_time=end_time,
        )
    ).parsed
