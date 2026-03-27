from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_common_gateway_runs_runs_gateway_sequence import DominoCommonGatewayRunsRunsGatewaySequence
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    batch_id: None | str,
    limit: int | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_batch_id: None | str
    json_batch_id = batch_id
    params["batchId"] = json_batch_id

    json_limit: int | None | Unset
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["limit"] = json_limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/gateway/runs/getByBatchId",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoCommonGatewayRunsRunsGatewaySequence | None:
    if response.status_code == 200:
        response_200 = DominoCommonGatewayRunsRunsGatewaySequence.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoCommonGatewayRunsRunsGatewaySequence]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    batch_id: None | str,
    limit: int | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoCommonGatewayRunsRunsGatewaySequence]:
    """API to batch extract Runs data for import into a 3rd party tool

    Args:
        batch_id (None | str):
        limit (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoCommonGatewayRunsRunsGatewaySequence]
    """

    kwargs = _get_kwargs(
        batch_id=batch_id,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    batch_id: None | str,
    limit: int | None | Unset = UNSET,
) -> DominoApiErrorResponse | DominoCommonGatewayRunsRunsGatewaySequence | None:
    """API to batch extract Runs data for import into a 3rd party tool

    Args:
        batch_id (None | str):
        limit (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoCommonGatewayRunsRunsGatewaySequence
    """

    return sync_detailed(
        client=client,
        batch_id=batch_id,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    batch_id: None | str,
    limit: int | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoCommonGatewayRunsRunsGatewaySequence]:
    """API to batch extract Runs data for import into a 3rd party tool

    Args:
        batch_id (None | str):
        limit (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoCommonGatewayRunsRunsGatewaySequence]
    """

    kwargs = _get_kwargs(
        batch_id=batch_id,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    batch_id: None | str,
    limit: int | None | Unset = UNSET,
) -> DominoApiErrorResponse | DominoCommonGatewayRunsRunsGatewaySequence | None:
    """API to batch extract Runs data for import into a 3rd party tool

    Args:
        batch_id (None | str):
        limit (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoCommonGatewayRunsRunsGatewaySequence
    """

    return (
        await asyncio_detailed(
            client=client,
            batch_id=batch_id,
            limit=limit,
        )
    ).parsed
