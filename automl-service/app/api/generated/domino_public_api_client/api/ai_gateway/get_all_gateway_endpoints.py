from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ai_gateway_envelope_v1 import AIGatewayEnvelopeV1
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_all_gateway_endpoints_response_400 import GetAllGatewayEndpointsResponse400
from ...models.get_all_gateway_endpoints_response_404 import GetAllGatewayEndpointsResponse404
from ...models.get_all_gateway_endpoints_response_500 import GetAllGatewayEndpointsResponse500
from ...models.get_all_gateway_endpoints_sort_by_field import GetAllGatewayEndpointsSortByField
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    sort_by_field: GetAllGatewayEndpointsSortByField | Unset = UNSET,
    should_sort_ascending: bool | Unset = UNSET,
    search_filter: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    json_sort_by_field: str | Unset = UNSET
    if not isinstance(sort_by_field, Unset):
        json_sort_by_field = sort_by_field.value

    params["sortByField"] = json_sort_by_field

    params["shouldSortAscending"] = should_sort_ascending

    params["searchFilter"] = search_filter

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/aigateway/v1/endpoints",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AIGatewayEnvelopeV1
    | FailureEnvelopeV1
    | GetAllGatewayEndpointsResponse400
    | GetAllGatewayEndpointsResponse404
    | GetAllGatewayEndpointsResponse500
    | None
):
    if response.status_code == 200:
        response_200 = AIGatewayEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetAllGatewayEndpointsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetAllGatewayEndpointsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetAllGatewayEndpointsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AIGatewayEnvelopeV1
    | FailureEnvelopeV1
    | GetAllGatewayEndpointsResponse400
    | GetAllGatewayEndpointsResponse404
    | GetAllGatewayEndpointsResponse500
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
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    sort_by_field: GetAllGatewayEndpointsSortByField | Unset = UNSET,
    should_sort_ascending: bool | Unset = UNSET,
    search_filter: str | Unset = UNSET,
) -> Response[
    AIGatewayEnvelopeV1
    | FailureEnvelopeV1
    | GetAllGatewayEndpointsResponse400
    | GetAllGatewayEndpointsResponse404
    | GetAllGatewayEndpointsResponse500
]:
    """Get all active Gateway LLMs accessible by the user

     Get all active Gateway LLMs accessible by the user

    Args:
        offset (int | Unset):
        limit (int | Unset):
        sort_by_field (GetAllGatewayEndpointsSortByField | Unset):
        should_sort_ascending (bool | Unset):
        search_filter (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AIGatewayEnvelopeV1 | FailureEnvelopeV1 | GetAllGatewayEndpointsResponse400 | GetAllGatewayEndpointsResponse404 | GetAllGatewayEndpointsResponse500]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        sort_by_field=sort_by_field,
        should_sort_ascending=should_sort_ascending,
        search_filter=search_filter,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    sort_by_field: GetAllGatewayEndpointsSortByField | Unset = UNSET,
    should_sort_ascending: bool | Unset = UNSET,
    search_filter: str | Unset = UNSET,
) -> (
    AIGatewayEnvelopeV1
    | FailureEnvelopeV1
    | GetAllGatewayEndpointsResponse400
    | GetAllGatewayEndpointsResponse404
    | GetAllGatewayEndpointsResponse500
    | None
):
    """Get all active Gateway LLMs accessible by the user

     Get all active Gateway LLMs accessible by the user

    Args:
        offset (int | Unset):
        limit (int | Unset):
        sort_by_field (GetAllGatewayEndpointsSortByField | Unset):
        should_sort_ascending (bool | Unset):
        search_filter (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AIGatewayEnvelopeV1 | FailureEnvelopeV1 | GetAllGatewayEndpointsResponse400 | GetAllGatewayEndpointsResponse404 | GetAllGatewayEndpointsResponse500
    """

    return sync_detailed(
        client=client,
        offset=offset,
        limit=limit,
        sort_by_field=sort_by_field,
        should_sort_ascending=should_sort_ascending,
        search_filter=search_filter,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    sort_by_field: GetAllGatewayEndpointsSortByField | Unset = UNSET,
    should_sort_ascending: bool | Unset = UNSET,
    search_filter: str | Unset = UNSET,
) -> Response[
    AIGatewayEnvelopeV1
    | FailureEnvelopeV1
    | GetAllGatewayEndpointsResponse400
    | GetAllGatewayEndpointsResponse404
    | GetAllGatewayEndpointsResponse500
]:
    """Get all active Gateway LLMs accessible by the user

     Get all active Gateway LLMs accessible by the user

    Args:
        offset (int | Unset):
        limit (int | Unset):
        sort_by_field (GetAllGatewayEndpointsSortByField | Unset):
        should_sort_ascending (bool | Unset):
        search_filter (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AIGatewayEnvelopeV1 | FailureEnvelopeV1 | GetAllGatewayEndpointsResponse400 | GetAllGatewayEndpointsResponse404 | GetAllGatewayEndpointsResponse500]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        sort_by_field=sort_by_field,
        should_sort_ascending=should_sort_ascending,
        search_filter=search_filter,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    sort_by_field: GetAllGatewayEndpointsSortByField | Unset = UNSET,
    should_sort_ascending: bool | Unset = UNSET,
    search_filter: str | Unset = UNSET,
) -> (
    AIGatewayEnvelopeV1
    | FailureEnvelopeV1
    | GetAllGatewayEndpointsResponse400
    | GetAllGatewayEndpointsResponse404
    | GetAllGatewayEndpointsResponse500
    | None
):
    """Get all active Gateway LLMs accessible by the user

     Get all active Gateway LLMs accessible by the user

    Args:
        offset (int | Unset):
        limit (int | Unset):
        sort_by_field (GetAllGatewayEndpointsSortByField | Unset):
        should_sort_ascending (bool | Unset):
        search_filter (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AIGatewayEnvelopeV1 | FailureEnvelopeV1 | GetAllGatewayEndpointsResponse400 | GetAllGatewayEndpointsResponse404 | GetAllGatewayEndpointsResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            limit=limit,
            sort_by_field=sort_by_field,
            should_sort_ascending=should_sort_ascending,
            search_filter=search_filter,
        )
    ).parsed
