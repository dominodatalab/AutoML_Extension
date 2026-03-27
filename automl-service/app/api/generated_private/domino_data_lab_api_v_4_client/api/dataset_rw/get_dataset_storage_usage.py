from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_datasetrw_api_dataset_storage_usage_dto import DominoDatasetrwApiDatasetStorageUsageDto
from ...types import UNSET, Response


def _get_kwargs(
    *,
    user_ids: list[str],
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_user_ids = user_ids

    params["userIds"] = json_user_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/datasetrw/storage-usage",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | list[DominoDatasetrwApiDatasetStorageUsageDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DominoDatasetrwApiDatasetStorageUsageDto.from_dict(response_200_item_data)

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
) -> Response[DominoApiErrorResponse | list[DominoDatasetrwApiDatasetStorageUsageDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    user_ids: list[str],
) -> Response[DominoApiErrorResponse | list[DominoDatasetrwApiDatasetStorageUsageDto]]:
    """Checks if users have reached the threshold of their dataset usage with respect to their quota

    Args:
        user_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoDatasetrwApiDatasetStorageUsageDto]]
    """

    kwargs = _get_kwargs(
        user_ids=user_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    user_ids: list[str],
) -> DominoApiErrorResponse | list[DominoDatasetrwApiDatasetStorageUsageDto] | None:
    """Checks if users have reached the threshold of their dataset usage with respect to their quota

    Args:
        user_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoDatasetrwApiDatasetStorageUsageDto]
    """

    return sync_detailed(
        client=client,
        user_ids=user_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    user_ids: list[str],
) -> Response[DominoApiErrorResponse | list[DominoDatasetrwApiDatasetStorageUsageDto]]:
    """Checks if users have reached the threshold of their dataset usage with respect to their quota

    Args:
        user_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoDatasetrwApiDatasetStorageUsageDto]]
    """

    kwargs = _get_kwargs(
        user_ids=user_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    user_ids: list[str],
) -> DominoApiErrorResponse | list[DominoDatasetrwApiDatasetStorageUsageDto] | None:
    """Checks if users have reached the threshold of their dataset usage with respect to their quota

    Args:
        user_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoDatasetrwApiDatasetStorageUsageDto]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_ids=user_ids,
        )
    ).parsed
