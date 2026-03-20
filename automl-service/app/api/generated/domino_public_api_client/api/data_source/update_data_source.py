from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_source_envelope_v1 import DataSourceEnvelopeV1
from ...models.data_source_update_v1 import DataSourceUpdateV1
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.update_data_source_response_400 import UpdateDataSourceResponse400
from ...models.update_data_source_response_404 import UpdateDataSourceResponse404
from ...models.update_data_source_response_500 import UpdateDataSourceResponse500
from ...types import Response


def _get_kwargs(
    data_source_id: str,
    *,
    body: DataSourceUpdateV1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/datasource/v1/datasources/{data_source_id}".format(
            data_source_id=quote(str(data_source_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DataSourceEnvelopeV1
    | FailureEnvelopeV1
    | UpdateDataSourceResponse400
    | UpdateDataSourceResponse404
    | UpdateDataSourceResponse500
    | None
):
    if response.status_code == 200:
        response_200 = DataSourceEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateDataSourceResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UpdateDataSourceResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = UpdateDataSourceResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DataSourceEnvelopeV1
    | FailureEnvelopeV1
    | UpdateDataSourceResponse400
    | UpdateDataSourceResponse404
    | UpdateDataSourceResponse500
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
    body: DataSourceUpdateV1,
) -> Response[
    DataSourceEnvelopeV1
    | FailureEnvelopeV1
    | UpdateDataSourceResponse400
    | UpdateDataSourceResponse404
    | UpdateDataSourceResponse500
]:
    """Update Data Source with specified ID

     Update Data Source with specified ID. If the current user is not an admin, then only their
    individual credentials are updated. Otherwise, the shared credentials are updated. If updating a
    Starburst-powered Data Source, please remember to restart the Starburst cluster in the UI for the
    changes to take effect. Requires Data Source management privileges

    Args:
        data_source_id (str):
        body (DataSourceUpdateV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataSourceEnvelopeV1 | FailureEnvelopeV1 | UpdateDataSourceResponse400 | UpdateDataSourceResponse404 | UpdateDataSourceResponse500]
    """

    kwargs = _get_kwargs(
        data_source_id=data_source_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    data_source_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DataSourceUpdateV1,
) -> (
    DataSourceEnvelopeV1
    | FailureEnvelopeV1
    | UpdateDataSourceResponse400
    | UpdateDataSourceResponse404
    | UpdateDataSourceResponse500
    | None
):
    """Update Data Source with specified ID

     Update Data Source with specified ID. If the current user is not an admin, then only their
    individual credentials are updated. Otherwise, the shared credentials are updated. If updating a
    Starburst-powered Data Source, please remember to restart the Starburst cluster in the UI for the
    changes to take effect. Requires Data Source management privileges

    Args:
        data_source_id (str):
        body (DataSourceUpdateV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataSourceEnvelopeV1 | FailureEnvelopeV1 | UpdateDataSourceResponse400 | UpdateDataSourceResponse404 | UpdateDataSourceResponse500
    """

    return sync_detailed(
        data_source_id=data_source_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    data_source_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DataSourceUpdateV1,
) -> Response[
    DataSourceEnvelopeV1
    | FailureEnvelopeV1
    | UpdateDataSourceResponse400
    | UpdateDataSourceResponse404
    | UpdateDataSourceResponse500
]:
    """Update Data Source with specified ID

     Update Data Source with specified ID. If the current user is not an admin, then only their
    individual credentials are updated. Otherwise, the shared credentials are updated. If updating a
    Starburst-powered Data Source, please remember to restart the Starburst cluster in the UI for the
    changes to take effect. Requires Data Source management privileges

    Args:
        data_source_id (str):
        body (DataSourceUpdateV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataSourceEnvelopeV1 | FailureEnvelopeV1 | UpdateDataSourceResponse400 | UpdateDataSourceResponse404 | UpdateDataSourceResponse500]
    """

    kwargs = _get_kwargs(
        data_source_id=data_source_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_source_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DataSourceUpdateV1,
) -> (
    DataSourceEnvelopeV1
    | FailureEnvelopeV1
    | UpdateDataSourceResponse400
    | UpdateDataSourceResponse404
    | UpdateDataSourceResponse500
    | None
):
    """Update Data Source with specified ID

     Update Data Source with specified ID. If the current user is not an admin, then only their
    individual credentials are updated. Otherwise, the shared credentials are updated. If updating a
    Starburst-powered Data Source, please remember to restart the Starburst cluster in the UI for the
    changes to take effect. Requires Data Source management privileges

    Args:
        data_source_id (str):
        body (DataSourceUpdateV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataSourceEnvelopeV1 | FailureEnvelopeV1 | UpdateDataSourceResponse400 | UpdateDataSourceResponse404 | UpdateDataSourceResponse500
    """

    return (
        await asyncio_detailed(
            data_source_id=data_source_id,
            client=client,
            body=body,
        )
    ).parsed
