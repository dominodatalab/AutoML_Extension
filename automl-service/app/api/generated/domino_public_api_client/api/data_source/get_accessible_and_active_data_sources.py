from __future__ import annotations
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_accessible_and_active_data_sources_response_400 import GetAccessibleAndActiveDataSourcesResponse400
from ...models.get_accessible_and_active_data_sources_response_404 import GetAccessibleAndActiveDataSourcesResponse404
from ...models.get_accessible_and_active_data_sources_response_500 import GetAccessibleAndActiveDataSourcesResponse500
from ...models.paginated_data_source_envelope_v1 import PaginatedDataSourceEnvelopeV1
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    data_source_names: list[str] | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_data_source_names: list[str] | Unset = UNSET
    if not isinstance(data_source_names, Unset):
        json_data_source_names = data_source_names

    params["dataSourceNames"] = json_data_source_names

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/datasource/v1/datasources",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GetAccessibleAndActiveDataSourcesResponse400
    | GetAccessibleAndActiveDataSourcesResponse404
    | GetAccessibleAndActiveDataSourcesResponse500
    | PaginatedDataSourceEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedDataSourceEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetAccessibleAndActiveDataSourcesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetAccessibleAndActiveDataSourcesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetAccessibleAndActiveDataSourcesResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | GetAccessibleAndActiveDataSourcesResponse400
    | GetAccessibleAndActiveDataSourcesResponse404
    | GetAccessibleAndActiveDataSourcesResponse500
    | PaginatedDataSourceEnvelopeV1
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
    data_source_names: list[str] | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
) -> Response[
    FailureEnvelopeV1
    | GetAccessibleAndActiveDataSourcesResponse400
    | GetAccessibleAndActiveDataSourcesResponse404
    | GetAccessibleAndActiveDataSourcesResponse500
    | PaginatedDataSourceEnvelopeV1
]:
    """Get all active Data Source the user has access to

     Get Data Sources that a user has access to based on Data Source permissions and input filters

    Args:
        data_source_names (list[str] | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetAccessibleAndActiveDataSourcesResponse400 | GetAccessibleAndActiveDataSourcesResponse404 | GetAccessibleAndActiveDataSourcesResponse500 | PaginatedDataSourceEnvelopeV1]
    """

    kwargs = _get_kwargs(
        data_source_names=data_source_names,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    data_source_names: list[str] | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
) -> (
    FailureEnvelopeV1
    | GetAccessibleAndActiveDataSourcesResponse400
    | GetAccessibleAndActiveDataSourcesResponse404
    | GetAccessibleAndActiveDataSourcesResponse500
    | PaginatedDataSourceEnvelopeV1
    | None
):
    """Get all active Data Source the user has access to

     Get Data Sources that a user has access to based on Data Source permissions and input filters

    Args:
        data_source_names (list[str] | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetAccessibleAndActiveDataSourcesResponse400 | GetAccessibleAndActiveDataSourcesResponse404 | GetAccessibleAndActiveDataSourcesResponse500 | PaginatedDataSourceEnvelopeV1
    """

    return sync_detailed(
        client=client,
        data_source_names=data_source_names,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    data_source_names: list[str] | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
) -> Response[
    FailureEnvelopeV1
    | GetAccessibleAndActiveDataSourcesResponse400
    | GetAccessibleAndActiveDataSourcesResponse404
    | GetAccessibleAndActiveDataSourcesResponse500
    | PaginatedDataSourceEnvelopeV1
]:
    """Get all active Data Source the user has access to

     Get Data Sources that a user has access to based on Data Source permissions and input filters

    Args:
        data_source_names (list[str] | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetAccessibleAndActiveDataSourcesResponse400 | GetAccessibleAndActiveDataSourcesResponse404 | GetAccessibleAndActiveDataSourcesResponse500 | PaginatedDataSourceEnvelopeV1]
    """

    kwargs = _get_kwargs(
        data_source_names=data_source_names,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    data_source_names: list[str] | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
) -> (
    FailureEnvelopeV1
    | GetAccessibleAndActiveDataSourcesResponse400
    | GetAccessibleAndActiveDataSourcesResponse404
    | GetAccessibleAndActiveDataSourcesResponse500
    | PaginatedDataSourceEnvelopeV1
    | None
):
    """Get all active Data Source the user has access to

     Get Data Sources that a user has access to based on Data Source permissions and input filters

    Args:
        data_source_names (list[str] | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetAccessibleAndActiveDataSourcesResponse400 | GetAccessibleAndActiveDataSourcesResponse404 | GetAccessibleAndActiveDataSourcesResponse500 | PaginatedDataSourceEnvelopeV1
    """

    return (
        await asyncio_detailed(
            client=client,
            data_source_names=data_source_names,
            offset=offset,
            limit=limit,
        )
    ).parsed
