from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_source_envelope_v1 import DataSourceEnvelopeV1
from ...models.delete_data_source_response_400 import DeleteDataSourceResponse400
from ...models.delete_data_source_response_404 import DeleteDataSourceResponse404
from ...models.delete_data_source_response_500 import DeleteDataSourceResponse500
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...types import Response


def _get_kwargs(
    data_source_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/datasource/v1/datasources/{data_source_id}".format(
            data_source_id=quote(str(data_source_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DataSourceEnvelopeV1
    | DeleteDataSourceResponse400
    | DeleteDataSourceResponse404
    | DeleteDataSourceResponse500
    | FailureEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = DataSourceEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = DeleteDataSourceResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteDataSourceResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = DeleteDataSourceResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DataSourceEnvelopeV1
    | DeleteDataSourceResponse400
    | DeleteDataSourceResponse404
    | DeleteDataSourceResponse500
    | FailureEnvelopeV1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    data_source_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    DataSourceEnvelopeV1
    | DeleteDataSourceResponse400
    | DeleteDataSourceResponse404
    | DeleteDataSourceResponse500
    | FailureEnvelopeV1
]:
    """Delete Data Source with specified ID

     Delete Data Source with specified ID. Requires Data Source ownership privileges

    Args:
        data_source_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataSourceEnvelopeV1 | DeleteDataSourceResponse400 | DeleteDataSourceResponse404 | DeleteDataSourceResponse500 | FailureEnvelopeV1]
    """

    kwargs = _get_kwargs(
        data_source_id=data_source_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    data_source_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    DataSourceEnvelopeV1
    | DeleteDataSourceResponse400
    | DeleteDataSourceResponse404
    | DeleteDataSourceResponse500
    | FailureEnvelopeV1
    | None
):
    """Delete Data Source with specified ID

     Delete Data Source with specified ID. Requires Data Source ownership privileges

    Args:
        data_source_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataSourceEnvelopeV1 | DeleteDataSourceResponse400 | DeleteDataSourceResponse404 | DeleteDataSourceResponse500 | FailureEnvelopeV1
    """

    return sync_detailed(
        data_source_id=data_source_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    data_source_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    DataSourceEnvelopeV1
    | DeleteDataSourceResponse400
    | DeleteDataSourceResponse404
    | DeleteDataSourceResponse500
    | FailureEnvelopeV1
]:
    """Delete Data Source with specified ID

     Delete Data Source with specified ID. Requires Data Source ownership privileges

    Args:
        data_source_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataSourceEnvelopeV1 | DeleteDataSourceResponse400 | DeleteDataSourceResponse404 | DeleteDataSourceResponse500 | FailureEnvelopeV1]
    """

    kwargs = _get_kwargs(
        data_source_id=data_source_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_source_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    DataSourceEnvelopeV1
    | DeleteDataSourceResponse400
    | DeleteDataSourceResponse404
    | DeleteDataSourceResponse500
    | FailureEnvelopeV1
    | None
):
    """Delete Data Source with specified ID

     Delete Data Source with specified ID. Requires Data Source ownership privileges

    Args:
        data_source_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataSourceEnvelopeV1 | DeleteDataSourceResponse400 | DeleteDataSourceResponse404 | DeleteDataSourceResponse500 | FailureEnvelopeV1
    """

    return (
        await asyncio_detailed(
            data_source_id=data_source_id,
            client=client,
        )
    ).parsed
