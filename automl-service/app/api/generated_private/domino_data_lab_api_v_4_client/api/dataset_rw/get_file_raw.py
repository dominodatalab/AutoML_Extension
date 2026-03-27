from http import HTTPStatus
from io import BytesIO
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    snapshot_id: str,
    *,
    path: str,
    download: bool | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["path"] = path

    json_download: bool | None | Unset
    if isinstance(download, Unset):
        json_download = UNSET
    else:
        json_download = download
    params["download"] = json_download

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/datasetrw/snapshot/{snapshot_id}/file/raw".format(
            snapshot_id=quote(str(snapshot_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | File | None:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

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
) -> Response[DominoApiErrorResponse | File]:
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
    path: str,
    download: bool | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | File]:
    """Get snapshot file raw content at specified path

    Args:
        snapshot_id (str):
        path (str):
        download (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | File]
    """

    kwargs = _get_kwargs(
        snapshot_id=snapshot_id,
        path=path,
        download=download,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    snapshot_id: str,
    *,
    client: AuthenticatedClient | Client,
    path: str,
    download: bool | None | Unset = UNSET,
) -> DominoApiErrorResponse | File | None:
    """Get snapshot file raw content at specified path

    Args:
        snapshot_id (str):
        path (str):
        download (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | File
    """

    return sync_detailed(
        snapshot_id=snapshot_id,
        client=client,
        path=path,
        download=download,
    ).parsed


async def asyncio_detailed(
    snapshot_id: str,
    *,
    client: AuthenticatedClient | Client,
    path: str,
    download: bool | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | File]:
    """Get snapshot file raw content at specified path

    Args:
        snapshot_id (str):
        path (str):
        download (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | File]
    """

    kwargs = _get_kwargs(
        snapshot_id=snapshot_id,
        path=path,
        download=download,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    snapshot_id: str,
    *,
    client: AuthenticatedClient | Client,
    path: str,
    download: bool | None | Unset = UNSET,
) -> DominoApiErrorResponse | File | None:
    """Get snapshot file raw content at specified path

    Args:
        snapshot_id (str):
        path (str):
        download (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | File
    """

    return (
        await asyncio_detailed(
            snapshot_id=snapshot_id,
            client=client,
            path=path,
            download=download,
        )
    ).parsed
