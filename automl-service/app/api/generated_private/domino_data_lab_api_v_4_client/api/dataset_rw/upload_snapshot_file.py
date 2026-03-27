from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dataset_id: str,
    *,
    resumable_chunk_number: int | Unset = UNSET,
    resumable_total_chunks: int | Unset = UNSET,
    resumable_identifier: str | Unset = UNSET,
    key: str | Unset = UNSET,
    resumable_relative_path: str | Unset = UNSET,
    resumable_chunk_size: int | Unset = UNSET,
    resumable_current_chunk_size: int | Unset = UNSET,
    checksum: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["resumableChunkNumber"] = resumable_chunk_number

    params["resumableTotalChunks"] = resumable_total_chunks

    params["resumableIdentifier"] = resumable_identifier

    params["key"] = key

    params["resumableRelativePath"] = resumable_relative_path

    params["resumableChunkSize"] = resumable_chunk_size

    params["resumableCurrentChunkSize"] = resumable_current_chunk_size

    params["checksum"] = checksum

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/datasetrw/datasets/{dataset_id}/snapshot/file".format(
            dataset_id=quote(str(dataset_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | str | None:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
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
) -> Response[DominoApiErrorResponse | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataset_id: str,
    *,
    client: AuthenticatedClient | Client,
    resumable_chunk_number: int | Unset = UNSET,
    resumable_total_chunks: int | Unset = UNSET,
    resumable_identifier: str | Unset = UNSET,
    key: str | Unset = UNSET,
    resumable_relative_path: str | Unset = UNSET,
    resumable_chunk_size: int | Unset = UNSET,
    resumable_current_chunk_size: int | Unset = UNSET,
    checksum: str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | str]:
    """Sends file upload chunks

    Args:
        dataset_id (str):
        resumable_chunk_number (int | Unset):
        resumable_total_chunks (int | Unset):
        resumable_identifier (str | Unset):
        key (str | Unset):
        resumable_relative_path (str | Unset):
        resumable_chunk_size (int | Unset):
        resumable_current_chunk_size (int | Unset):
        checksum (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | str]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        resumable_chunk_number=resumable_chunk_number,
        resumable_total_chunks=resumable_total_chunks,
        resumable_identifier=resumable_identifier,
        key=key,
        resumable_relative_path=resumable_relative_path,
        resumable_chunk_size=resumable_chunk_size,
        resumable_current_chunk_size=resumable_current_chunk_size,
        checksum=checksum,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataset_id: str,
    *,
    client: AuthenticatedClient | Client,
    resumable_chunk_number: int | Unset = UNSET,
    resumable_total_chunks: int | Unset = UNSET,
    resumable_identifier: str | Unset = UNSET,
    key: str | Unset = UNSET,
    resumable_relative_path: str | Unset = UNSET,
    resumable_chunk_size: int | Unset = UNSET,
    resumable_current_chunk_size: int | Unset = UNSET,
    checksum: str | Unset = UNSET,
) -> DominoApiErrorResponse | str | None:
    """Sends file upload chunks

    Args:
        dataset_id (str):
        resumable_chunk_number (int | Unset):
        resumable_total_chunks (int | Unset):
        resumable_identifier (str | Unset):
        key (str | Unset):
        resumable_relative_path (str | Unset):
        resumable_chunk_size (int | Unset):
        resumable_current_chunk_size (int | Unset):
        checksum (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | str
    """

    return sync_detailed(
        dataset_id=dataset_id,
        client=client,
        resumable_chunk_number=resumable_chunk_number,
        resumable_total_chunks=resumable_total_chunks,
        resumable_identifier=resumable_identifier,
        key=key,
        resumable_relative_path=resumable_relative_path,
        resumable_chunk_size=resumable_chunk_size,
        resumable_current_chunk_size=resumable_current_chunk_size,
        checksum=checksum,
    ).parsed


async def asyncio_detailed(
    dataset_id: str,
    *,
    client: AuthenticatedClient | Client,
    resumable_chunk_number: int | Unset = UNSET,
    resumable_total_chunks: int | Unset = UNSET,
    resumable_identifier: str | Unset = UNSET,
    key: str | Unset = UNSET,
    resumable_relative_path: str | Unset = UNSET,
    resumable_chunk_size: int | Unset = UNSET,
    resumable_current_chunk_size: int | Unset = UNSET,
    checksum: str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | str]:
    """Sends file upload chunks

    Args:
        dataset_id (str):
        resumable_chunk_number (int | Unset):
        resumable_total_chunks (int | Unset):
        resumable_identifier (str | Unset):
        key (str | Unset):
        resumable_relative_path (str | Unset):
        resumable_chunk_size (int | Unset):
        resumable_current_chunk_size (int | Unset):
        checksum (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | str]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        resumable_chunk_number=resumable_chunk_number,
        resumable_total_chunks=resumable_total_chunks,
        resumable_identifier=resumable_identifier,
        key=key,
        resumable_relative_path=resumable_relative_path,
        resumable_chunk_size=resumable_chunk_size,
        resumable_current_chunk_size=resumable_current_chunk_size,
        checksum=checksum,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataset_id: str,
    *,
    client: AuthenticatedClient | Client,
    resumable_chunk_number: int | Unset = UNSET,
    resumable_total_chunks: int | Unset = UNSET,
    resumable_identifier: str | Unset = UNSET,
    key: str | Unset = UNSET,
    resumable_relative_path: str | Unset = UNSET,
    resumable_chunk_size: int | Unset = UNSET,
    resumable_current_chunk_size: int | Unset = UNSET,
    checksum: str | Unset = UNSET,
) -> DominoApiErrorResponse | str | None:
    """Sends file upload chunks

    Args:
        dataset_id (str):
        resumable_chunk_number (int | Unset):
        resumable_total_chunks (int | Unset):
        resumable_identifier (str | Unset):
        key (str | Unset):
        resumable_relative_path (str | Unset):
        resumable_chunk_size (int | Unset):
        resumable_current_chunk_size (int | Unset):
        checksum (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | str
    """

    return (
        await asyncio_detailed(
            dataset_id=dataset_id,
            client=client,
            resumable_chunk_number=resumable_chunk_number,
            resumable_total_chunks=resumable_total_chunks,
            resumable_identifier=resumable_identifier,
            key=key,
            resumable_relative_path=resumable_relative_path,
            resumable_chunk_size=resumable_chunk_size,
            resumable_current_chunk_size=resumable_current_chunk_size,
            checksum=checksum,
        )
    ).parsed
