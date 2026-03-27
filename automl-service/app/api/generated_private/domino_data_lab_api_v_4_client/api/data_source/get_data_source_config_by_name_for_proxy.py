from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_datasource_api_data_source_proxy_config_dto import DominoDatasourceApiDataSourceProxyConfigDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    data_source_name: str,
    username: str,
    *,
    run_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["runId"] = run_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/datasource/name/{data_source_name}/user/{username}/config/proxy".format(
            data_source_name=quote(str(data_source_name), safe=""),
            username=quote(str(username), safe=""),
        ),
        "params": params,
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
) -> Response[DominoApiErrorResponse | DominoDatasourceApiDataSourceProxyConfigDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    data_source_name: str,
    username: str,
    *,
    client: AuthenticatedClient | Client,
    run_id: str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoDatasourceApiDataSourceProxyConfigDto]:
    """Get data source config object by name for proxy service

    Args:
        data_source_name (str):
        username (str):
        run_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoDatasourceApiDataSourceProxyConfigDto]
    """

    kwargs = _get_kwargs(
        data_source_name=data_source_name,
        username=username,
        run_id=run_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    data_source_name: str,
    username: str,
    *,
    client: AuthenticatedClient | Client,
    run_id: str | Unset = UNSET,
) -> DominoApiErrorResponse | DominoDatasourceApiDataSourceProxyConfigDto | None:
    """Get data source config object by name for proxy service

    Args:
        data_source_name (str):
        username (str):
        run_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoDatasourceApiDataSourceProxyConfigDto
    """

    return sync_detailed(
        data_source_name=data_source_name,
        username=username,
        client=client,
        run_id=run_id,
    ).parsed


async def asyncio_detailed(
    data_source_name: str,
    username: str,
    *,
    client: AuthenticatedClient | Client,
    run_id: str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoDatasourceApiDataSourceProxyConfigDto]:
    """Get data source config object by name for proxy service

    Args:
        data_source_name (str):
        username (str):
        run_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoDatasourceApiDataSourceProxyConfigDto]
    """

    kwargs = _get_kwargs(
        data_source_name=data_source_name,
        username=username,
        run_id=run_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_source_name: str,
    username: str,
    *,
    client: AuthenticatedClient | Client,
    run_id: str | Unset = UNSET,
) -> DominoApiErrorResponse | DominoDatasourceApiDataSourceProxyConfigDto | None:
    """Get data source config object by name for proxy service

    Args:
        data_source_name (str):
        username (str):
        run_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoDatasourceApiDataSourceProxyConfigDto
    """

    return (
        await asyncio_detailed(
            data_source_name=data_source_name,
            username=username,
            client=client,
            run_id=run_id,
        )
    ).parsed
