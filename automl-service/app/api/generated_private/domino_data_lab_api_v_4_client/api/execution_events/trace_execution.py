from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    execution_id: str,
    metric_name: str,
    *,
    epoch_millis_or_zero: int | Unset = 0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["epochMillisOrZero"] = epoch_millis_or_zero

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/executions/{execution_id}/metrics/{metric_name}/trace".format(
            execution_id=quote(str(execution_id), safe=""),
            metric_name=quote(str(metric_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DominoApiErrorResponse | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
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
) -> Response[Any | DominoApiErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    execution_id: str,
    metric_name: str,
    *,
    client: AuthenticatedClient | Client,
    epoch_millis_or_zero: int | Unset = 0,
) -> Response[Any | DominoApiErrorResponse]:
    """Starts (or ends) an execution trace event for a given execution id

    Args:
        execution_id (str):
        metric_name (str):
        epoch_millis_or_zero (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DominoApiErrorResponse]
    """

    kwargs = _get_kwargs(
        execution_id=execution_id,
        metric_name=metric_name,
        epoch_millis_or_zero=epoch_millis_or_zero,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    execution_id: str,
    metric_name: str,
    *,
    client: AuthenticatedClient | Client,
    epoch_millis_or_zero: int | Unset = 0,
) -> Any | DominoApiErrorResponse | None:
    """Starts (or ends) an execution trace event for a given execution id

    Args:
        execution_id (str):
        metric_name (str):
        epoch_millis_or_zero (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DominoApiErrorResponse
    """

    return sync_detailed(
        execution_id=execution_id,
        metric_name=metric_name,
        client=client,
        epoch_millis_or_zero=epoch_millis_or_zero,
    ).parsed


async def asyncio_detailed(
    execution_id: str,
    metric_name: str,
    *,
    client: AuthenticatedClient | Client,
    epoch_millis_or_zero: int | Unset = 0,
) -> Response[Any | DominoApiErrorResponse]:
    """Starts (or ends) an execution trace event for a given execution id

    Args:
        execution_id (str):
        metric_name (str):
        epoch_millis_or_zero (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DominoApiErrorResponse]
    """

    kwargs = _get_kwargs(
        execution_id=execution_id,
        metric_name=metric_name,
        epoch_millis_or_zero=epoch_millis_or_zero,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    execution_id: str,
    metric_name: str,
    *,
    client: AuthenticatedClient | Client,
    epoch_millis_or_zero: int | Unset = 0,
) -> Any | DominoApiErrorResponse | None:
    """Starts (or ends) an execution trace event for a given execution id

    Args:
        execution_id (str):
        metric_name (str):
        epoch_millis_or_zero (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DominoApiErrorResponse
    """

    return (
        await asyncio_detailed(
            execution_id=execution_id,
            metric_name=metric_name,
            client=client,
            epoch_millis_or_zero=epoch_millis_or_zero,
        )
    ).parsed
