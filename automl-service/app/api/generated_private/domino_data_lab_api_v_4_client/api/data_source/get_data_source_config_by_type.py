from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_datasource_model_datasource_config import DominoDatasourceModelDatasourceConfig
from ...types import Response


def _get_kwargs(
    data_source_type: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/datasource/type/{data_source_type}/config".format(
            data_source_type=quote(str(data_source_type), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoDatasourceModelDatasourceConfig | None:
    if response.status_code == 200:
        response_200 = DominoDatasourceModelDatasourceConfig.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoDatasourceModelDatasourceConfig]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    data_source_type: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DominoApiErrorResponse | DominoDatasourceModelDatasourceConfig]:
    """Get config metadata for a datasource type

    Args:
        data_source_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoDatasourceModelDatasourceConfig]
    """

    kwargs = _get_kwargs(
        data_source_type=data_source_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    data_source_type: str,
    *,
    client: AuthenticatedClient | Client,
) -> DominoApiErrorResponse | DominoDatasourceModelDatasourceConfig | None:
    """Get config metadata for a datasource type

    Args:
        data_source_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoDatasourceModelDatasourceConfig
    """

    return sync_detailed(
        data_source_type=data_source_type,
        client=client,
    ).parsed


async def asyncio_detailed(
    data_source_type: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DominoApiErrorResponse | DominoDatasourceModelDatasourceConfig]:
    """Get config metadata for a datasource type

    Args:
        data_source_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoDatasourceModelDatasourceConfig]
    """

    kwargs = _get_kwargs(
        data_source_type=data_source_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_source_type: str,
    *,
    client: AuthenticatedClient | Client,
) -> DominoApiErrorResponse | DominoDatasourceModelDatasourceConfig | None:
    """Get config metadata for a datasource type

    Args:
        data_source_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoDatasourceModelDatasourceConfig
    """

    return (
        await asyncio_detailed(
            data_source_type=data_source_type,
            client=client,
        )
    ).parsed
