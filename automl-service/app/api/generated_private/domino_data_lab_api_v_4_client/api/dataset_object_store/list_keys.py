from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_datasetrw_web_dataset_list_keys_response import DominoDatasetrwWebDatasetListKeysResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dataset_id: str,
    snapshot_id: str,
    *,
    prefix: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["prefix"] = prefix

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/datasets/objectstore/datasets/{dataset_id}/snapshots/{snapshot_id}/keys".format(
            dataset_id=quote(str(dataset_id), safe=""),
            snapshot_id=quote(str(snapshot_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoDatasetrwWebDatasetListKeysResponse | None:
    if response.status_code == 200:
        response_200 = DominoDatasetrwWebDatasetListKeysResponse.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoDatasetrwWebDatasetListKeysResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataset_id: str,
    snapshot_id: str,
    *,
    client: AuthenticatedClient | Client,
    prefix: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoDatasetrwWebDatasetListKeysResponse]:
    """List keys in a snapshot

    Args:
        dataset_id (str):
        snapshot_id (str):
        prefix (str | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoDatasetrwWebDatasetListKeysResponse]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        snapshot_id=snapshot_id,
        prefix=prefix,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataset_id: str,
    snapshot_id: str,
    *,
    client: AuthenticatedClient | Client,
    prefix: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> DominoApiErrorResponse | DominoDatasetrwWebDatasetListKeysResponse | None:
    """List keys in a snapshot

    Args:
        dataset_id (str):
        snapshot_id (str):
        prefix (str | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoDatasetrwWebDatasetListKeysResponse
    """

    return sync_detailed(
        dataset_id=dataset_id,
        snapshot_id=snapshot_id,
        client=client,
        prefix=prefix,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    dataset_id: str,
    snapshot_id: str,
    *,
    client: AuthenticatedClient | Client,
    prefix: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoDatasetrwWebDatasetListKeysResponse]:
    """List keys in a snapshot

    Args:
        dataset_id (str):
        snapshot_id (str):
        prefix (str | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoDatasetrwWebDatasetListKeysResponse]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        snapshot_id=snapshot_id,
        prefix=prefix,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataset_id: str,
    snapshot_id: str,
    *,
    client: AuthenticatedClient | Client,
    prefix: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> DominoApiErrorResponse | DominoDatasetrwWebDatasetListKeysResponse | None:
    """List keys in a snapshot

    Args:
        dataset_id (str):
        snapshot_id (str):
        prefix (str | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoDatasetrwWebDatasetListKeysResponse
    """

    return (
        await asyncio_detailed(
            dataset_id=dataset_id,
            snapshot_id=snapshot_id,
            client=client,
            prefix=prefix,
            page_size=page_size,
        )
    ).parsed
