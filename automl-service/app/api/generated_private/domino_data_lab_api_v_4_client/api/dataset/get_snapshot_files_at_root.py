from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_nucleus_dataset_ui_data_set_file_browser_view_model import (
    DominoNucleusDatasetUiDataSetFileBrowserViewModel,
)
from ...types import Response


def _get_kwargs(
    data_set_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/datasetUi/{data_set_id}/files".format(
            data_set_id=quote(str(data_set_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoNucleusDatasetUiDataSetFileBrowserViewModel | None:
    if response.status_code == 200:
        response_200 = DominoNucleusDatasetUiDataSetFileBrowserViewModel.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoNucleusDatasetUiDataSetFileBrowserViewModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    data_set_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DominoApiErrorResponse | DominoNucleusDatasetUiDataSetFileBrowserViewModel]:
    """retrieves the files in a specified data set at the root directory

    Args:
        data_set_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoNucleusDatasetUiDataSetFileBrowserViewModel]
    """

    kwargs = _get_kwargs(
        data_set_id=data_set_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    data_set_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> DominoApiErrorResponse | DominoNucleusDatasetUiDataSetFileBrowserViewModel | None:
    """retrieves the files in a specified data set at the root directory

    Args:
        data_set_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoNucleusDatasetUiDataSetFileBrowserViewModel
    """

    return sync_detailed(
        data_set_id=data_set_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    data_set_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DominoApiErrorResponse | DominoNucleusDatasetUiDataSetFileBrowserViewModel]:
    """retrieves the files in a specified data set at the root directory

    Args:
        data_set_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoNucleusDatasetUiDataSetFileBrowserViewModel]
    """

    kwargs = _get_kwargs(
        data_set_id=data_set_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_set_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> DominoApiErrorResponse | DominoNucleusDatasetUiDataSetFileBrowserViewModel | None:
    """retrieves the files in a specified data set at the root directory

    Args:
        data_set_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoNucleusDatasetUiDataSetFileBrowserViewModel
    """

    return (
        await asyncio_detailed(
            data_set_id=data_set_id,
            client=client,
        )
    ).parsed
