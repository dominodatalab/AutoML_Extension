from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_datasetrw_api_dataset_rw_details_dto import DominoDatasetrwApiDatasetRwDetailsDto
from ...types import Response


def _get_kwargs(
    dataset_unique_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/datasetrw/datasets/uniqueName/{dataset_unique_name}".format(
            dataset_unique_name=quote(str(dataset_unique_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoDatasetrwApiDatasetRwDetailsDto | None:
    if response.status_code == 200:
        response_200 = DominoDatasetrwApiDatasetRwDetailsDto.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoDatasetrwApiDatasetRwDetailsDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataset_unique_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DominoApiErrorResponse | DominoDatasetrwApiDatasetRwDetailsDto]:
    """Lookup Dataset by unique name

    Args:
        dataset_unique_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoDatasetrwApiDatasetRwDetailsDto]
    """

    kwargs = _get_kwargs(
        dataset_unique_name=dataset_unique_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataset_unique_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> DominoApiErrorResponse | DominoDatasetrwApiDatasetRwDetailsDto | None:
    """Lookup Dataset by unique name

    Args:
        dataset_unique_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoDatasetrwApiDatasetRwDetailsDto
    """

    return sync_detailed(
        dataset_unique_name=dataset_unique_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    dataset_unique_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DominoApiErrorResponse | DominoDatasetrwApiDatasetRwDetailsDto]:
    """Lookup Dataset by unique name

    Args:
        dataset_unique_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoDatasetrwApiDatasetRwDetailsDto]
    """

    kwargs = _get_kwargs(
        dataset_unique_name=dataset_unique_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataset_unique_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> DominoApiErrorResponse | DominoDatasetrwApiDatasetRwDetailsDto | None:
    """Lookup Dataset by unique name

    Args:
        dataset_unique_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoDatasetrwApiDatasetRwDetailsDto
    """

    return (
        await asyncio_detailed(
            dataset_unique_name=dataset_unique_name,
            client=client,
        )
    ).parsed
