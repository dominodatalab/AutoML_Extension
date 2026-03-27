from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_credential_api_full_data_source_credential_dto import (
    DominoCredentialApiFullDataSourceCredentialDto,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    data_source_name: str,
    user_name: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["dataSourceName"] = data_source_name

    params["userName"] = user_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/datasource/fullbyname",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | list[DominoCredentialApiFullDataSourceCredentialDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DominoCredentialApiFullDataSourceCredentialDto.from_dict(response_200_item_data)

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
) -> Response[DominoApiErrorResponse | list[DominoCredentialApiFullDataSourceCredentialDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    data_source_name: str,
    user_name: str,
) -> Response[DominoApiErrorResponse | list[DominoCredentialApiFullDataSourceCredentialDto]]:
    """Get all credentials by data source name and user name

    Args:
        data_source_name (str):
        user_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoCredentialApiFullDataSourceCredentialDto]]
    """

    kwargs = _get_kwargs(
        data_source_name=data_source_name,
        user_name=user_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    data_source_name: str,
    user_name: str,
) -> DominoApiErrorResponse | list[DominoCredentialApiFullDataSourceCredentialDto] | None:
    """Get all credentials by data source name and user name

    Args:
        data_source_name (str):
        user_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoCredentialApiFullDataSourceCredentialDto]
    """

    return sync_detailed(
        client=client,
        data_source_name=data_source_name,
        user_name=user_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    data_source_name: str,
    user_name: str,
) -> Response[DominoApiErrorResponse | list[DominoCredentialApiFullDataSourceCredentialDto]]:
    """Get all credentials by data source name and user name

    Args:
        data_source_name (str):
        user_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoCredentialApiFullDataSourceCredentialDto]]
    """

    kwargs = _get_kwargs(
        data_source_name=data_source_name,
        user_name=user_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    data_source_name: str,
    user_name: str,
) -> DominoApiErrorResponse | list[DominoCredentialApiFullDataSourceCredentialDto] | None:
    """Get all credentials by data source name and user name

    Args:
        data_source_name (str):
        user_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoCredentialApiFullDataSourceCredentialDto]
    """

    return (
        await asyncio_detailed(
            client=client,
            data_source_name=data_source_name,
            user_name=user_name,
        )
    ).parsed
