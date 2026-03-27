from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_datasetrw_web_dataset_key_url_response import DominoDatasetrwWebDatasetKeyURLResponse
from ...types import Response


def _get_kwargs(
    dataset_id: str,
    snapshot_id: str,
    key: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/datasets/objectstore/datasets/{dataset_id}/snapshots/{snapshot_id}/keys/{key}/url".format(
            dataset_id=quote(str(dataset_id), safe=""),
            snapshot_id=quote(str(snapshot_id), safe=""),
            key=quote(str(key), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoDatasetrwWebDatasetKeyURLResponse | None:
    if response.status_code == 200:
        response_200 = DominoDatasetrwWebDatasetKeyURLResponse.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoDatasetrwWebDatasetKeyURLResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataset_id: str,
    snapshot_id: str,
    key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DominoApiErrorResponse | DominoDatasetrwWebDatasetKeyURLResponse]:
    """List keys in a snapshot

    Args:
        dataset_id (str):
        snapshot_id (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoDatasetrwWebDatasetKeyURLResponse]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        snapshot_id=snapshot_id,
        key=key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataset_id: str,
    snapshot_id: str,
    key: str,
    *,
    client: AuthenticatedClient | Client,
) -> DominoApiErrorResponse | DominoDatasetrwWebDatasetKeyURLResponse | None:
    """List keys in a snapshot

    Args:
        dataset_id (str):
        snapshot_id (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoDatasetrwWebDatasetKeyURLResponse
    """

    return sync_detailed(
        dataset_id=dataset_id,
        snapshot_id=snapshot_id,
        key=key,
        client=client,
    ).parsed


async def asyncio_detailed(
    dataset_id: str,
    snapshot_id: str,
    key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DominoApiErrorResponse | DominoDatasetrwWebDatasetKeyURLResponse]:
    """List keys in a snapshot

    Args:
        dataset_id (str):
        snapshot_id (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoDatasetrwWebDatasetKeyURLResponse]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        snapshot_id=snapshot_id,
        key=key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataset_id: str,
    snapshot_id: str,
    key: str,
    *,
    client: AuthenticatedClient | Client,
) -> DominoApiErrorResponse | DominoDatasetrwWebDatasetKeyURLResponse | None:
    """List keys in a snapshot

    Args:
        dataset_id (str):
        snapshot_id (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoDatasetrwWebDatasetKeyURLResponse
    """

    return (
        await asyncio_detailed(
            dataset_id=dataset_id,
            snapshot_id=snapshot_id,
            key=key,
            client=client,
        )
    ).parsed
