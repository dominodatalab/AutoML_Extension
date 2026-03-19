from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cost_allocation_envelope_v2 import CostAllocationEnvelopeV2
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_accumulated_cost_allocation_v2_response_400 import GetAccumulatedCostAllocationV2Response400
from ...models.get_accumulated_cost_allocation_v2_response_404 import GetAccumulatedCostAllocationV2Response404
from ...models.get_accumulated_cost_allocation_v2_response_500 import GetAccumulatedCostAllocationV2Response500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    window: str,
    aggregate: list[str] | Unset = UNSET,
    interval: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    share_idle: bool | Unset = UNSET,
    share_namespaces: str | Unset = UNSET,
    share_split: str | Unset = UNSET,
    share_cost: str | Unset = UNSET,
    share_labels: str | Unset = UNSET,
    reconcile: bool | Unset = UNSET,
    share_tenancy_costs: bool | Unset = UNSET,
    idle: bool | Unset = UNSET,
    external: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["window"] = window

    json_aggregate: list[str] | Unset = UNSET
    if not isinstance(aggregate, Unset):
        json_aggregate = aggregate

    params["aggregate"] = json_aggregate

    params["interval"] = interval

    params["filter"] = filter_

    params["shareIdle"] = share_idle

    params["shareNamespaces"] = share_namespaces

    params["shareSplit"] = share_split

    params["shareCost"] = share_cost

    params["shareLabels"] = share_labels

    params["reconcile"] = reconcile

    params["shareTenancyCosts"] = share_tenancy_costs

    params["idle"] = idle

    params["external"] = external

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/cost/v2/allocation/accumulated",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CostAllocationEnvelopeV2
    | FailureEnvelopeV1
    | GetAccumulatedCostAllocationV2Response400
    | GetAccumulatedCostAllocationV2Response404
    | GetAccumulatedCostAllocationV2Response500
    | None
):
    if response.status_code == 200:
        response_200 = CostAllocationEnvelopeV2.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetAccumulatedCostAllocationV2Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetAccumulatedCostAllocationV2Response404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetAccumulatedCostAllocationV2Response500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CostAllocationEnvelopeV2
    | FailureEnvelopeV1
    | GetAccumulatedCostAllocationV2Response400
    | GetAccumulatedCostAllocationV2Response404
    | GetAccumulatedCostAllocationV2Response500
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
    window: str,
    aggregate: list[str] | Unset = UNSET,
    interval: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    share_idle: bool | Unset = UNSET,
    share_namespaces: str | Unset = UNSET,
    share_split: str | Unset = UNSET,
    share_cost: str | Unset = UNSET,
    share_labels: str | Unset = UNSET,
    reconcile: bool | Unset = UNSET,
    share_tenancy_costs: bool | Unset = UNSET,
    idle: bool | Unset = UNSET,
    external: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[
    CostAllocationEnvelopeV2
    | FailureEnvelopeV1
    | GetAccumulatedCostAllocationV2Response400
    | GetAccumulatedCostAllocationV2Response404
    | GetAccumulatedCostAllocationV2Response500
]:
    """Get accumulated cost allocation over a time window

     Retrieve cost allocation accumulated v2

    Args:
        window (str):
        aggregate (list[str] | Unset):
        interval (str | Unset):
        filter_ (str | Unset):
        share_idle (bool | Unset):
        share_namespaces (str | Unset):
        share_split (str | Unset):
        share_cost (str | Unset):
        share_labels (str | Unset):
        reconcile (bool | Unset):
        share_tenancy_costs (bool | Unset):
        idle (bool | Unset):
        external (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CostAllocationEnvelopeV2 | FailureEnvelopeV1 | GetAccumulatedCostAllocationV2Response400 | GetAccumulatedCostAllocationV2Response404 | GetAccumulatedCostAllocationV2Response500]
    """

    kwargs = _get_kwargs(
        window=window,
        aggregate=aggregate,
        interval=interval,
        filter_=filter_,
        share_idle=share_idle,
        share_namespaces=share_namespaces,
        share_split=share_split,
        share_cost=share_cost,
        share_labels=share_labels,
        reconcile=reconcile,
        share_tenancy_costs=share_tenancy_costs,
        idle=idle,
        external=external,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    window: str,
    aggregate: list[str] | Unset = UNSET,
    interval: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    share_idle: bool | Unset = UNSET,
    share_namespaces: str | Unset = UNSET,
    share_split: str | Unset = UNSET,
    share_cost: str | Unset = UNSET,
    share_labels: str | Unset = UNSET,
    reconcile: bool | Unset = UNSET,
    share_tenancy_costs: bool | Unset = UNSET,
    idle: bool | Unset = UNSET,
    external: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> (
    CostAllocationEnvelopeV2
    | FailureEnvelopeV1
    | GetAccumulatedCostAllocationV2Response400
    | GetAccumulatedCostAllocationV2Response404
    | GetAccumulatedCostAllocationV2Response500
    | None
):
    """Get accumulated cost allocation over a time window

     Retrieve cost allocation accumulated v2

    Args:
        window (str):
        aggregate (list[str] | Unset):
        interval (str | Unset):
        filter_ (str | Unset):
        share_idle (bool | Unset):
        share_namespaces (str | Unset):
        share_split (str | Unset):
        share_cost (str | Unset):
        share_labels (str | Unset):
        reconcile (bool | Unset):
        share_tenancy_costs (bool | Unset):
        idle (bool | Unset):
        external (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CostAllocationEnvelopeV2 | FailureEnvelopeV1 | GetAccumulatedCostAllocationV2Response400 | GetAccumulatedCostAllocationV2Response404 | GetAccumulatedCostAllocationV2Response500
    """

    return sync_detailed(
        client=client,
        window=window,
        aggregate=aggregate,
        interval=interval,
        filter_=filter_,
        share_idle=share_idle,
        share_namespaces=share_namespaces,
        share_split=share_split,
        share_cost=share_cost,
        share_labels=share_labels,
        reconcile=reconcile,
        share_tenancy_costs=share_tenancy_costs,
        idle=idle,
        external=external,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    window: str,
    aggregate: list[str] | Unset = UNSET,
    interval: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    share_idle: bool | Unset = UNSET,
    share_namespaces: str | Unset = UNSET,
    share_split: str | Unset = UNSET,
    share_cost: str | Unset = UNSET,
    share_labels: str | Unset = UNSET,
    reconcile: bool | Unset = UNSET,
    share_tenancy_costs: bool | Unset = UNSET,
    idle: bool | Unset = UNSET,
    external: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[
    CostAllocationEnvelopeV2
    | FailureEnvelopeV1
    | GetAccumulatedCostAllocationV2Response400
    | GetAccumulatedCostAllocationV2Response404
    | GetAccumulatedCostAllocationV2Response500
]:
    """Get accumulated cost allocation over a time window

     Retrieve cost allocation accumulated v2

    Args:
        window (str):
        aggregate (list[str] | Unset):
        interval (str | Unset):
        filter_ (str | Unset):
        share_idle (bool | Unset):
        share_namespaces (str | Unset):
        share_split (str | Unset):
        share_cost (str | Unset):
        share_labels (str | Unset):
        reconcile (bool | Unset):
        share_tenancy_costs (bool | Unset):
        idle (bool | Unset):
        external (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CostAllocationEnvelopeV2 | FailureEnvelopeV1 | GetAccumulatedCostAllocationV2Response400 | GetAccumulatedCostAllocationV2Response404 | GetAccumulatedCostAllocationV2Response500]
    """

    kwargs = _get_kwargs(
        window=window,
        aggregate=aggregate,
        interval=interval,
        filter_=filter_,
        share_idle=share_idle,
        share_namespaces=share_namespaces,
        share_split=share_split,
        share_cost=share_cost,
        share_labels=share_labels,
        reconcile=reconcile,
        share_tenancy_costs=share_tenancy_costs,
        idle=idle,
        external=external,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    window: str,
    aggregate: list[str] | Unset = UNSET,
    interval: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    share_idle: bool | Unset = UNSET,
    share_namespaces: str | Unset = UNSET,
    share_split: str | Unset = UNSET,
    share_cost: str | Unset = UNSET,
    share_labels: str | Unset = UNSET,
    reconcile: bool | Unset = UNSET,
    share_tenancy_costs: bool | Unset = UNSET,
    idle: bool | Unset = UNSET,
    external: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> (
    CostAllocationEnvelopeV2
    | FailureEnvelopeV1
    | GetAccumulatedCostAllocationV2Response400
    | GetAccumulatedCostAllocationV2Response404
    | GetAccumulatedCostAllocationV2Response500
    | None
):
    """Get accumulated cost allocation over a time window

     Retrieve cost allocation accumulated v2

    Args:
        window (str):
        aggregate (list[str] | Unset):
        interval (str | Unset):
        filter_ (str | Unset):
        share_idle (bool | Unset):
        share_namespaces (str | Unset):
        share_split (str | Unset):
        share_cost (str | Unset):
        share_labels (str | Unset):
        reconcile (bool | Unset):
        share_tenancy_costs (bool | Unset):
        idle (bool | Unset):
        external (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CostAllocationEnvelopeV2 | FailureEnvelopeV1 | GetAccumulatedCostAllocationV2Response400 | GetAccumulatedCostAllocationV2Response404 | GetAccumulatedCostAllocationV2Response500
    """

    return (
        await asyncio_detailed(
            client=client,
            window=window,
            aggregate=aggregate,
            interval=interval,
            filter_=filter_,
            share_idle=share_idle,
            share_namespaces=share_namespaces,
            share_split=share_split,
            share_cost=share_cost,
            share_labels=share_labels,
            reconcile=reconcile,
            share_tenancy_costs=share_tenancy_costs,
            idle=idle,
            external=external,
            limit=limit,
            offset=offset,
        )
    ).parsed
