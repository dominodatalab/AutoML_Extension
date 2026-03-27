from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_datasetrw_api_dataset_rw_copy_time_estimate_dto import (
    DominoDatasetrwApiDatasetRwCopyTimeEstimateDto,
)
from ...types import UNSET, Response


def _get_kwargs(
    snapshot_id: str,
    *,
    relative_file_paths: list[str],
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_relative_file_paths = relative_file_paths

    params["relativeFilePaths"] = json_relative_file_paths

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/datasetrw/snapshot/{snapshot_id}/copy-estimate".format(
            snapshot_id=quote(str(snapshot_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoDatasetrwApiDatasetRwCopyTimeEstimateDto | None:
    if response.status_code == 200:
        response_200 = DominoDatasetrwApiDatasetRwCopyTimeEstimateDto.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoDatasetrwApiDatasetRwCopyTimeEstimateDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    snapshot_id: str,
    *,
    client: AuthenticatedClient | Client,
    relative_file_paths: list[str],
) -> Response[DominoApiErrorResponse | DominoDatasetrwApiDatasetRwCopyTimeEstimateDto]:
    """Get time estimate of copy task

    Args:
        snapshot_id (str):
        relative_file_paths (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoDatasetrwApiDatasetRwCopyTimeEstimateDto]
    """

    kwargs = _get_kwargs(
        snapshot_id=snapshot_id,
        relative_file_paths=relative_file_paths,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    snapshot_id: str,
    *,
    client: AuthenticatedClient | Client,
    relative_file_paths: list[str],
) -> DominoApiErrorResponse | DominoDatasetrwApiDatasetRwCopyTimeEstimateDto | None:
    """Get time estimate of copy task

    Args:
        snapshot_id (str):
        relative_file_paths (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoDatasetrwApiDatasetRwCopyTimeEstimateDto
    """

    return sync_detailed(
        snapshot_id=snapshot_id,
        client=client,
        relative_file_paths=relative_file_paths,
    ).parsed


async def asyncio_detailed(
    snapshot_id: str,
    *,
    client: AuthenticatedClient | Client,
    relative_file_paths: list[str],
) -> Response[DominoApiErrorResponse | DominoDatasetrwApiDatasetRwCopyTimeEstimateDto]:
    """Get time estimate of copy task

    Args:
        snapshot_id (str):
        relative_file_paths (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoDatasetrwApiDatasetRwCopyTimeEstimateDto]
    """

    kwargs = _get_kwargs(
        snapshot_id=snapshot_id,
        relative_file_paths=relative_file_paths,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    snapshot_id: str,
    *,
    client: AuthenticatedClient | Client,
    relative_file_paths: list[str],
) -> DominoApiErrorResponse | DominoDatasetrwApiDatasetRwCopyTimeEstimateDto | None:
    """Get time estimate of copy task

    Args:
        snapshot_id (str):
        relative_file_paths (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoDatasetrwApiDatasetRwCopyTimeEstimateDto
    """

    return (
        await asyncio_detailed(
            snapshot_id=snapshot_id,
            client=client,
            relative_file_paths=relative_file_paths,
        )
    ).parsed
