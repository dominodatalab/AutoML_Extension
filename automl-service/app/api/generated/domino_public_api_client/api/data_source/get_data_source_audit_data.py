from __future__ import annotations
import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_source_audit_data_v1 import DataSourceAuditDataV1
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_data_source_audit_data_response_400 import GetDataSourceAuditDataResponse400
from ...models.get_data_source_audit_data_response_404 import GetDataSourceAuditDataResponse404
from ...models.get_data_source_audit_data_response_500 import GetDataSourceAuditDataResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    data_source_ids: list[str] | Unset = UNSET,
    data_source_names: list[str] | Unset = UNSET,
    event_kinds: list[str] | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_data_source_ids: list[str] | Unset = UNSET
    if not isinstance(data_source_ids, Unset):
        json_data_source_ids = data_source_ids

    params["dataSourceIds"] = json_data_source_ids

    json_data_source_names: list[str] | Unset = UNSET
    if not isinstance(data_source_names, Unset):
        json_data_source_names = data_source_names

    params["dataSourceNames"] = json_data_source_names

    json_event_kinds: list[str] | Unset = UNSET
    if not isinstance(event_kinds, Unset):
        json_event_kinds = event_kinds

    params["eventKinds"] = json_event_kinds

    json_start_time: str | Unset = UNSET
    if not isinstance(start_time, Unset):
        json_start_time = start_time.isoformat()
    params["startTime"] = json_start_time

    json_end_time: str | Unset = UNSET
    if not isinstance(end_time, Unset):
        json_end_time = end_time.isoformat()
    params["endTime"] = json_end_time

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/datasource/v1/audit",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GetDataSourceAuditDataResponse400
    | GetDataSourceAuditDataResponse404
    | GetDataSourceAuditDataResponse500
    | list[DataSourceAuditDataV1]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DataSourceAuditDataV1.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = GetDataSourceAuditDataResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetDataSourceAuditDataResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetDataSourceAuditDataResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | GetDataSourceAuditDataResponse400
    | GetDataSourceAuditDataResponse404
    | GetDataSourceAuditDataResponse500
    | list[DataSourceAuditDataV1]
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
    data_source_ids: list[str] | Unset = UNSET,
    data_source_names: list[str] | Unset = UNSET,
    event_kinds: list[str] | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1
    | GetDataSourceAuditDataResponse400
    | GetDataSourceAuditDataResponse404
    | GetDataSourceAuditDataResponse500
    | list[DataSourceAuditDataV1]
]:
    """Get Data Source Audit Data

     Gets Data Source audit data given filter input parameters

    Args:
        data_source_ids (list[str] | Unset):
        data_source_names (list[str] | Unset):
        event_kinds (list[str] | Unset):
        start_time (datetime.datetime | Unset):
        end_time (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetDataSourceAuditDataResponse400 | GetDataSourceAuditDataResponse404 | GetDataSourceAuditDataResponse500 | list[DataSourceAuditDataV1]]
    """

    kwargs = _get_kwargs(
        data_source_ids=data_source_ids,
        data_source_names=data_source_names,
        event_kinds=event_kinds,
        start_time=start_time,
        end_time=end_time,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    data_source_ids: list[str] | Unset = UNSET,
    data_source_names: list[str] | Unset = UNSET,
    event_kinds: list[str] | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
) -> (
    FailureEnvelopeV1
    | GetDataSourceAuditDataResponse400
    | GetDataSourceAuditDataResponse404
    | GetDataSourceAuditDataResponse500
    | list[DataSourceAuditDataV1]
    | None
):
    """Get Data Source Audit Data

     Gets Data Source audit data given filter input parameters

    Args:
        data_source_ids (list[str] | Unset):
        data_source_names (list[str] | Unset):
        event_kinds (list[str] | Unset):
        start_time (datetime.datetime | Unset):
        end_time (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetDataSourceAuditDataResponse400 | GetDataSourceAuditDataResponse404 | GetDataSourceAuditDataResponse500 | list[DataSourceAuditDataV1]
    """

    return sync_detailed(
        client=client,
        data_source_ids=data_source_ids,
        data_source_names=data_source_names,
        event_kinds=event_kinds,
        start_time=start_time,
        end_time=end_time,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    data_source_ids: list[str] | Unset = UNSET,
    data_source_names: list[str] | Unset = UNSET,
    event_kinds: list[str] | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1
    | GetDataSourceAuditDataResponse400
    | GetDataSourceAuditDataResponse404
    | GetDataSourceAuditDataResponse500
    | list[DataSourceAuditDataV1]
]:
    """Get Data Source Audit Data

     Gets Data Source audit data given filter input parameters

    Args:
        data_source_ids (list[str] | Unset):
        data_source_names (list[str] | Unset):
        event_kinds (list[str] | Unset):
        start_time (datetime.datetime | Unset):
        end_time (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetDataSourceAuditDataResponse400 | GetDataSourceAuditDataResponse404 | GetDataSourceAuditDataResponse500 | list[DataSourceAuditDataV1]]
    """

    kwargs = _get_kwargs(
        data_source_ids=data_source_ids,
        data_source_names=data_source_names,
        event_kinds=event_kinds,
        start_time=start_time,
        end_time=end_time,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    data_source_ids: list[str] | Unset = UNSET,
    data_source_names: list[str] | Unset = UNSET,
    event_kinds: list[str] | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
) -> (
    FailureEnvelopeV1
    | GetDataSourceAuditDataResponse400
    | GetDataSourceAuditDataResponse404
    | GetDataSourceAuditDataResponse500
    | list[DataSourceAuditDataV1]
    | None
):
    """Get Data Source Audit Data

     Gets Data Source audit data given filter input parameters

    Args:
        data_source_ids (list[str] | Unset):
        data_source_names (list[str] | Unset):
        event_kinds (list[str] | Unset):
        start_time (datetime.datetime | Unset):
        end_time (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetDataSourceAuditDataResponse400 | GetDataSourceAuditDataResponse404 | GetDataSourceAuditDataResponse500 | list[DataSourceAuditDataV1]
    """

    return (
        await asyncio_detailed(
            client=client,
            data_source_ids=data_source_ids,
            data_source_names=data_source_names,
            event_kinds=event_kinds,
            start_time=start_time,
            end_time=end_time,
        )
    ).parsed
