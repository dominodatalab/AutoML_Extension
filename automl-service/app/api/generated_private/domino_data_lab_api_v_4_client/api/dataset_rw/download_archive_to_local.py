from http import HTTPStatus
from io import BytesIO
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...types import File, Response


def _get_kwargs(
    snapshot_id: str,
    task_key: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/datasetrw/snapshot/{snapshot_id}/download-local/{task_key}".format(
            snapshot_id=quote(str(snapshot_id), safe=""),
            task_key=quote(str(task_key), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | File | None:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.json()))

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
    task_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DominoApiErrorResponse | File]:
    """Download archive file from Domino to local

    Args:
        snapshot_id (str):
        task_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | File]
    """

    kwargs = _get_kwargs(
        snapshot_id=snapshot_id,
        task_key=task_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    snapshot_id: str,
    task_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> DominoApiErrorResponse | File | None:
    """Download archive file from Domino to local

    Args:
        snapshot_id (str):
        task_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | File
    """

    return sync_detailed(
        snapshot_id=snapshot_id,
        task_key=task_key,
        client=client,
    ).parsed


async def asyncio_detailed(
    snapshot_id: str,
    task_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DominoApiErrorResponse | File]:
    """Download archive file from Domino to local

    Args:
        snapshot_id (str):
        task_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | File]
    """

    kwargs = _get_kwargs(
        snapshot_id=snapshot_id,
        task_key=task_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    snapshot_id: str,
    task_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> DominoApiErrorResponse | File | None:
    """Download archive file from Domino to local

    Args:
        snapshot_id (str):
        task_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | File
    """

    return (
        await asyncio_detailed(
            snapshot_id=snapshot_id,
            task_key=task_key,
            client=client,
        )
    ).parsed
