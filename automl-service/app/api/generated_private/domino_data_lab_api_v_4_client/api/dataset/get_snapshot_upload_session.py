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
    upload_key: str,
    *,
    resumable_chunk_number: int | Unset = UNSET,
    resumable_total_chunks: int | Unset = UNSET,
    resumable_identifier: str | Unset = UNSET,
    resumable_relative_path: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["resumableChunkNumber"] = resumable_chunk_number

    params["resumableTotalChunks"] = resumable_total_chunks

    params["resumableIdentifier"] = resumable_identifier

    params["resumableRelativePath"] = resumable_relative_path

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/datasetUi/collections/{dataset_id}/snapshot/file/session/{upload_key}".format(
            dataset_id=quote(str(dataset_id), safe=""),
            upload_key=quote(str(upload_key), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DominoApiErrorResponse | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
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
) -> Response[Any | DominoApiErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataset_id: str,
    upload_key: str,
    *,
    client: AuthenticatedClient | Client,
    resumable_chunk_number: int | Unset = UNSET,
    resumable_total_chunks: int | Unset = UNSET,
    resumable_identifier: str | Unset = UNSET,
    resumable_relative_path: str | Unset = UNSET,
) -> Response[Any | DominoApiErrorResponse]:
    """Tests whether or not an upload session exists

    Args:
        dataset_id (str):
        upload_key (str):
        resumable_chunk_number (int | Unset):
        resumable_total_chunks (int | Unset):
        resumable_identifier (str | Unset):
        resumable_relative_path (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DominoApiErrorResponse]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        upload_key=upload_key,
        resumable_chunk_number=resumable_chunk_number,
        resumable_total_chunks=resumable_total_chunks,
        resumable_identifier=resumable_identifier,
        resumable_relative_path=resumable_relative_path,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataset_id: str,
    upload_key: str,
    *,
    client: AuthenticatedClient | Client,
    resumable_chunk_number: int | Unset = UNSET,
    resumable_total_chunks: int | Unset = UNSET,
    resumable_identifier: str | Unset = UNSET,
    resumable_relative_path: str | Unset = UNSET,
) -> Any | DominoApiErrorResponse | None:
    """Tests whether or not an upload session exists

    Args:
        dataset_id (str):
        upload_key (str):
        resumable_chunk_number (int | Unset):
        resumable_total_chunks (int | Unset):
        resumable_identifier (str | Unset):
        resumable_relative_path (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DominoApiErrorResponse
    """

    return sync_detailed(
        dataset_id=dataset_id,
        upload_key=upload_key,
        client=client,
        resumable_chunk_number=resumable_chunk_number,
        resumable_total_chunks=resumable_total_chunks,
        resumable_identifier=resumable_identifier,
        resumable_relative_path=resumable_relative_path,
    ).parsed


async def asyncio_detailed(
    dataset_id: str,
    upload_key: str,
    *,
    client: AuthenticatedClient | Client,
    resumable_chunk_number: int | Unset = UNSET,
    resumable_total_chunks: int | Unset = UNSET,
    resumable_identifier: str | Unset = UNSET,
    resumable_relative_path: str | Unset = UNSET,
) -> Response[Any | DominoApiErrorResponse]:
    """Tests whether or not an upload session exists

    Args:
        dataset_id (str):
        upload_key (str):
        resumable_chunk_number (int | Unset):
        resumable_total_chunks (int | Unset):
        resumable_identifier (str | Unset):
        resumable_relative_path (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DominoApiErrorResponse]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        upload_key=upload_key,
        resumable_chunk_number=resumable_chunk_number,
        resumable_total_chunks=resumable_total_chunks,
        resumable_identifier=resumable_identifier,
        resumable_relative_path=resumable_relative_path,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataset_id: str,
    upload_key: str,
    *,
    client: AuthenticatedClient | Client,
    resumable_chunk_number: int | Unset = UNSET,
    resumable_total_chunks: int | Unset = UNSET,
    resumable_identifier: str | Unset = UNSET,
    resumable_relative_path: str | Unset = UNSET,
) -> Any | DominoApiErrorResponse | None:
    """Tests whether or not an upload session exists

    Args:
        dataset_id (str):
        upload_key (str):
        resumable_chunk_number (int | Unset):
        resumable_total_chunks (int | Unset):
        resumable_identifier (str | Unset):
        resumable_relative_path (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DominoApiErrorResponse
    """

    return (
        await asyncio_detailed(
            dataset_id=dataset_id,
            upload_key=upload_key,
            client=client,
            resumable_chunk_number=resumable_chunk_number,
            resumable_total_chunks=resumable_total_chunks,
            resumable_identifier=resumable_identifier,
            resumable_relative_path=resumable_relative_path,
        )
    ).parsed
