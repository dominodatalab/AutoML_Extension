from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_datasource_api_data_source_proxy_config_dto import DominoDatasourceApiDataSourceProxyConfigDto
from ...types import Response


def _get_kwargs(
    data_source_id: str,
    username: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/datasource/{data_source_id}/user/{username}/config/proxy".format(
            data_source_id=quote(str(data_source_id), safe=""),
            username=quote(str(username), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoDatasourceApiDataSourceProxyConfigDto | None:
    if response.status_code == 200:
        response_200 = DominoDatasourceApiDataSourceProxyConfigDto.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoDatasourceApiDataSourceProxyConfigDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    data_source_id: str,
    username: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DominoApiErrorResponse | DominoDatasourceApiDataSourceProxyConfigDto]:
    """Get data source config object for proxy service

    Args:
        data_source_id (str):
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoDatasourceApiDataSourceProxyConfigDto]
    """

    kwargs = _get_kwargs(
        data_source_id=data_source_id,
        username=username,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    data_source_id: str,
    username: str,
    *,
    client: AuthenticatedClient | Client,
) -> DominoApiErrorResponse | DominoDatasourceApiDataSourceProxyConfigDto | None:
    """Get data source config object for proxy service

    Args:
        data_source_id (str):
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoDatasourceApiDataSourceProxyConfigDto
    """

    return sync_detailed(
        data_source_id=data_source_id,
        username=username,
        client=client,
    ).parsed


async def asyncio_detailed(
    data_source_id: str,
    username: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DominoApiErrorResponse | DominoDatasourceApiDataSourceProxyConfigDto]:
    """Get data source config object for proxy service

    Args:
        data_source_id (str):
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoDatasourceApiDataSourceProxyConfigDto]
    """

    kwargs = _get_kwargs(
        data_source_id=data_source_id,
        username=username,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_source_id: str,
    username: str,
    *,
    client: AuthenticatedClient | Client,
) -> DominoApiErrorResponse | DominoDatasourceApiDataSourceProxyConfigDto | None:
    """Get data source config object for proxy service

    Args:
        data_source_id (str):
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoDatasourceApiDataSourceProxyConfigDto
    """

    return (
        await asyncio_detailed(
            data_source_id=data_source_id,
            username=username,
            client=client,
        )
    ).parsed
