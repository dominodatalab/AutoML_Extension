from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    metric_type: str,
    count: int,
    unique: bool,
    data_points: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["metricType"] = metric_type

    params["count"] = count

    params["unique"] = unique

    params["dataPoints"] = data_points

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/metricsTesting/generateMetrics",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | str | None:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
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
) -> Response[DominoApiErrorResponse | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    metric_type: str,
    count: int,
    unique: bool,
    data_points: int | Unset = UNSET,
) -> Response[DominoApiErrorResponse | str]:
    """generate application metrics for testing

    Args:
        metric_type (str):
        count (int):
        unique (bool):
        data_points (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | str]
    """

    kwargs = _get_kwargs(
        metric_type=metric_type,
        count=count,
        unique=unique,
        data_points=data_points,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    metric_type: str,
    count: int,
    unique: bool,
    data_points: int | Unset = UNSET,
) -> DominoApiErrorResponse | str | None:
    """generate application metrics for testing

    Args:
        metric_type (str):
        count (int):
        unique (bool):
        data_points (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | str
    """

    return sync_detailed(
        client=client,
        metric_type=metric_type,
        count=count,
        unique=unique,
        data_points=data_points,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    metric_type: str,
    count: int,
    unique: bool,
    data_points: int | Unset = UNSET,
) -> Response[DominoApiErrorResponse | str]:
    """generate application metrics for testing

    Args:
        metric_type (str):
        count (int):
        unique (bool):
        data_points (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | str]
    """

    kwargs = _get_kwargs(
        metric_type=metric_type,
        count=count,
        unique=unique,
        data_points=data_points,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    metric_type: str,
    count: int,
    unique: bool,
    data_points: int | Unset = UNSET,
) -> DominoApiErrorResponse | str | None:
    """generate application metrics for testing

    Args:
        metric_type (str):
        count (int):
        unique (bool):
        data_points (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | str
    """

    return (
        await asyncio_detailed(
            client=client,
            metric_type=metric_type,
            count=count,
            unique=unique,
            data_points=data_points,
        )
    ).parsed
