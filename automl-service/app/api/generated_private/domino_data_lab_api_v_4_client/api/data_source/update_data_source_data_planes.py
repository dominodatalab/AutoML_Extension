from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_datasource_api_data_source_data_plane_info import DominoDatasourceApiDataSourceDataPlaneInfo
from ...models.domino_datasource_web_update_data_source_data_planes_request import (
    DominoDatasourceWebUpdateDataSourceDataPlanesRequest,
)
from ...types import Response


def _get_kwargs(
    data_source_id: str,
    *,
    body: DominoDatasourceWebUpdateDataSourceDataPlanesRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/datasource/{data_source_id}/dataPlanes".format(
            data_source_id=quote(str(data_source_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | list[DominoDatasourceApiDataSourceDataPlaneInfo] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DominoDatasourceApiDataSourceDataPlaneInfo.from_dict(response_200_item_data)

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

    if response.status_code == 500:
        response_500 = DominoApiErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DominoApiErrorResponse | list[DominoDatasourceApiDataSourceDataPlaneInfo]]:
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
    body: DominoDatasourceWebUpdateDataSourceDataPlanesRequest,
) -> Response[DominoApiErrorResponse | list[DominoDatasourceApiDataSourceDataPlaneInfo]]:
    """Update the data planes from which a data source is accessible from

    Args:
        data_source_id (str):
        body (DominoDatasourceWebUpdateDataSourceDataPlanesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoDatasourceApiDataSourceDataPlaneInfo]]
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
    body: DominoDatasourceWebUpdateDataSourceDataPlanesRequest,
) -> DominoApiErrorResponse | list[DominoDatasourceApiDataSourceDataPlaneInfo] | None:
    """Update the data planes from which a data source is accessible from

    Args:
        data_source_id (str):
        body (DominoDatasourceWebUpdateDataSourceDataPlanesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoDatasourceApiDataSourceDataPlaneInfo]
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
    body: DominoDatasourceWebUpdateDataSourceDataPlanesRequest,
) -> Response[DominoApiErrorResponse | list[DominoDatasourceApiDataSourceDataPlaneInfo]]:
    """Update the data planes from which a data source is accessible from

    Args:
        data_source_id (str):
        body (DominoDatasourceWebUpdateDataSourceDataPlanesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoDatasourceApiDataSourceDataPlaneInfo]]
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
    body: DominoDatasourceWebUpdateDataSourceDataPlanesRequest,
) -> DominoApiErrorResponse | list[DominoDatasourceApiDataSourceDataPlaneInfo] | None:
    """Update the data planes from which a data source is accessible from

    Args:
        data_source_id (str):
        body (DominoDatasourceWebUpdateDataSourceDataPlanesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoDatasourceApiDataSourceDataPlaneInfo]
    """

    return (
        await asyncio_detailed(
            data_source_id=data_source_id,
            client=client,
            body=body,
        )
    ).parsed
