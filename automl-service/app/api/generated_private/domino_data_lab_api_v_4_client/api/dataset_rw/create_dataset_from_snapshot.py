from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_datasetrw_api_dataset_rw_view_dto import DominoDatasetrwApiDatasetRwViewDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    snapshot_id: str,
    *,
    name: str,
    description: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["name"] = name

    json_description: None | str | Unset
    if isinstance(description, Unset):
        json_description = UNSET
    else:
        json_description = description
    params["description"] = json_description

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/datasetrw/dataset/{snapshot_id}/create".format(
            snapshot_id=quote(str(snapshot_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoDatasetrwApiDatasetRwViewDto | None:
    if response.status_code == 200:
        response_200 = DominoDatasetrwApiDatasetRwViewDto.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoDatasetrwApiDatasetRwViewDto]:
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
    name: str,
    description: None | str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoDatasetrwApiDatasetRwViewDto]:
    """Create dataset from snapshot

    Args:
        snapshot_id (str):
        name (str):
        description (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoDatasetrwApiDatasetRwViewDto]
    """

    kwargs = _get_kwargs(
        snapshot_id=snapshot_id,
        name=name,
        description=description,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    snapshot_id: str,
    *,
    client: AuthenticatedClient | Client,
    name: str,
    description: None | str | Unset = UNSET,
) -> DominoApiErrorResponse | DominoDatasetrwApiDatasetRwViewDto | None:
    """Create dataset from snapshot

    Args:
        snapshot_id (str):
        name (str):
        description (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoDatasetrwApiDatasetRwViewDto
    """

    return sync_detailed(
        snapshot_id=snapshot_id,
        client=client,
        name=name,
        description=description,
    ).parsed


async def asyncio_detailed(
    snapshot_id: str,
    *,
    client: AuthenticatedClient | Client,
    name: str,
    description: None | str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoDatasetrwApiDatasetRwViewDto]:
    """Create dataset from snapshot

    Args:
        snapshot_id (str):
        name (str):
        description (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoDatasetrwApiDatasetRwViewDto]
    """

    kwargs = _get_kwargs(
        snapshot_id=snapshot_id,
        name=name,
        description=description,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    snapshot_id: str,
    *,
    client: AuthenticatedClient | Client,
    name: str,
    description: None | str | Unset = UNSET,
) -> DominoApiErrorResponse | DominoDatasetrwApiDatasetRwViewDto | None:
    """Create dataset from snapshot

    Args:
        snapshot_id (str):
        name (str):
        description (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoDatasetrwApiDatasetRwViewDto
    """

    return (
        await asyncio_detailed(
            snapshot_id=snapshot_id,
            client=client,
            name=name,
            description=description,
        )
    ).parsed
