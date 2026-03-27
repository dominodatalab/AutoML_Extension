from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_datasetrw_api_dataset_rw_storage_dto import DominoDatasetrwApiDatasetRwStorageDto
from ...types import Response


def _get_kwargs(
    dataset_storage_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/datasetrw/storage/{dataset_storage_id}".format(
            dataset_storage_id=quote(str(dataset_storage_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoDatasetrwApiDatasetRwStorageDto | None:
    if response.status_code == 200:
        response_200 = DominoDatasetrwApiDatasetRwStorageDto.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoDatasetrwApiDatasetRwStorageDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataset_storage_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DominoApiErrorResponse | DominoDatasetrwApiDatasetRwStorageDto]:
    """Unregister dataset storage

    Args:
        dataset_storage_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoDatasetrwApiDatasetRwStorageDto]
    """

    kwargs = _get_kwargs(
        dataset_storage_id=dataset_storage_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataset_storage_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> DominoApiErrorResponse | DominoDatasetrwApiDatasetRwStorageDto | None:
    """Unregister dataset storage

    Args:
        dataset_storage_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoDatasetrwApiDatasetRwStorageDto
    """

    return sync_detailed(
        dataset_storage_id=dataset_storage_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    dataset_storage_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DominoApiErrorResponse | DominoDatasetrwApiDatasetRwStorageDto]:
    """Unregister dataset storage

    Args:
        dataset_storage_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoDatasetrwApiDatasetRwStorageDto]
    """

    kwargs = _get_kwargs(
        dataset_storage_id=dataset_storage_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataset_storage_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> DominoApiErrorResponse | DominoDatasetrwApiDatasetRwStorageDto | None:
    """Unregister dataset storage

    Args:
        dataset_storage_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoDatasetrwApiDatasetRwStorageDto
    """

    return (
        await asyncio_detailed(
            dataset_storage_id=dataset_storage_id,
            client=client,
        )
    ).parsed
