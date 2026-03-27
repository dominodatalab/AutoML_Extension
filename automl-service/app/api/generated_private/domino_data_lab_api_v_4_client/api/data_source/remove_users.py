from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_datasource_api_data_source_dto import DominoDatasourceApiDataSourceDto
from ...types import UNSET, Response


def _get_kwargs(
    data_source_id: str,
    *,
    user_ids: list[str],
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_user_ids = user_ids

    params["userIds"] = json_user_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/datasource/{data_source_id}/users".format(
            data_source_id=quote(str(data_source_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoDatasourceApiDataSourceDto | None:
    if response.status_code == 200:
        response_200 = DominoDatasourceApiDataSourceDto.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoDatasourceApiDataSourceDto]:
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
    user_ids: list[str],
) -> Response[DominoApiErrorResponse | DominoDatasourceApiDataSourceDto]:
    """Remove users from data source

    Args:
        data_source_id (str):
        user_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoDatasourceApiDataSourceDto]
    """

    kwargs = _get_kwargs(
        data_source_id=data_source_id,
        user_ids=user_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    data_source_id: str,
    *,
    client: AuthenticatedClient | Client,
    user_ids: list[str],
) -> DominoApiErrorResponse | DominoDatasourceApiDataSourceDto | None:
    """Remove users from data source

    Args:
        data_source_id (str):
        user_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoDatasourceApiDataSourceDto
    """

    return sync_detailed(
        data_source_id=data_source_id,
        client=client,
        user_ids=user_ids,
    ).parsed


async def asyncio_detailed(
    data_source_id: str,
    *,
    client: AuthenticatedClient | Client,
    user_ids: list[str],
) -> Response[DominoApiErrorResponse | DominoDatasourceApiDataSourceDto]:
    """Remove users from data source

    Args:
        data_source_id (str):
        user_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoDatasourceApiDataSourceDto]
    """

    kwargs = _get_kwargs(
        data_source_id=data_source_id,
        user_ids=user_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_source_id: str,
    *,
    client: AuthenticatedClient | Client,
    user_ids: list[str],
) -> DominoApiErrorResponse | DominoDatasourceApiDataSourceDto | None:
    """Remove users from data source

    Args:
        data_source_id (str):
        user_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoDatasourceApiDataSourceDto
    """

    return (
        await asyncio_detailed(
            data_source_id=data_source_id,
            client=client,
            user_ids=user_ids,
        )
    ).parsed
