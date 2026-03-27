from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_common_run_interfaces_run_monolith_dto import DominoCommonRunInterfacesRunMonolithDTO
from ...models.list_recently_started_runs_with_limit_workload_type import ListRecentlyStartedRunsWithLimitWorkloadType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | None | Unset = 15,
    workload_type: ListRecentlyStartedRunsWithLimitWorkloadType | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_limit: int | None | Unset
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["limit"] = json_limit

    json_workload_type: str | Unset = UNSET
    if not isinstance(workload_type, Unset):
        json_workload_type = workload_type.value

    params["workloadType"] = json_workload_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/runs/recentlyStarted",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | list[DominoCommonRunInterfacesRunMonolithDTO] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DominoCommonRunInterfacesRunMonolithDTO.from_dict(response_200_item_data)

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
) -> Response[DominoApiErrorResponse | list[DominoCommonRunInterfacesRunMonolithDTO]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | None | Unset = 15,
    workload_type: ListRecentlyStartedRunsWithLimitWorkloadType | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoCommonRunInterfacesRunMonolithDTO]]:
    """retrieves list of recently started runs

    Args:
        limit (int | None | Unset):  Default: 15.
        workload_type (ListRecentlyStartedRunsWithLimitWorkloadType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoCommonRunInterfacesRunMonolithDTO]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        workload_type=workload_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | None | Unset = 15,
    workload_type: ListRecentlyStartedRunsWithLimitWorkloadType | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoCommonRunInterfacesRunMonolithDTO] | None:
    """retrieves list of recently started runs

    Args:
        limit (int | None | Unset):  Default: 15.
        workload_type (ListRecentlyStartedRunsWithLimitWorkloadType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoCommonRunInterfacesRunMonolithDTO]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        workload_type=workload_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | None | Unset = 15,
    workload_type: ListRecentlyStartedRunsWithLimitWorkloadType | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoCommonRunInterfacesRunMonolithDTO]]:
    """retrieves list of recently started runs

    Args:
        limit (int | None | Unset):  Default: 15.
        workload_type (ListRecentlyStartedRunsWithLimitWorkloadType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoCommonRunInterfacesRunMonolithDTO]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        workload_type=workload_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | None | Unset = 15,
    workload_type: ListRecentlyStartedRunsWithLimitWorkloadType | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoCommonRunInterfacesRunMonolithDTO] | None:
    """retrieves list of recently started runs

    Args:
        limit (int | None | Unset):  Default: 15.
        workload_type (ListRecentlyStartedRunsWithLimitWorkloadType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoCommonRunInterfacesRunMonolithDTO]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            workload_type=workload_type,
        )
    ).parsed
