from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_nucleus_dataset_ui_dataset_view_model import DominoNucleusDatasetUiDatasetViewModel
from ...types import Response


def _get_kwargs(
    dataset_id: str,
    tag_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/datasetUi/collections/{dataset_id}/tags/{tag_name}".format(
            dataset_id=quote(str(dataset_id), safe=""),
            tag_name=quote(str(tag_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoNucleusDatasetUiDatasetViewModel | None:
    if response.status_code == 200:
        response_200 = DominoNucleusDatasetUiDatasetViewModel.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoNucleusDatasetUiDatasetViewModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataset_id: str,
    tag_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DominoApiErrorResponse | DominoNucleusDatasetUiDatasetViewModel]:
    """removes a tag from a dataset by updating the dataset's collection tags map

    Args:
        dataset_id (str):
        tag_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoNucleusDatasetUiDatasetViewModel]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        tag_name=tag_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataset_id: str,
    tag_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> DominoApiErrorResponse | DominoNucleusDatasetUiDatasetViewModel | None:
    """removes a tag from a dataset by updating the dataset's collection tags map

    Args:
        dataset_id (str):
        tag_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoNucleusDatasetUiDatasetViewModel
    """

    return sync_detailed(
        dataset_id=dataset_id,
        tag_name=tag_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    dataset_id: str,
    tag_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DominoApiErrorResponse | DominoNucleusDatasetUiDatasetViewModel]:
    """removes a tag from a dataset by updating the dataset's collection tags map

    Args:
        dataset_id (str):
        tag_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoNucleusDatasetUiDatasetViewModel]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        tag_name=tag_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataset_id: str,
    tag_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> DominoApiErrorResponse | DominoNucleusDatasetUiDatasetViewModel | None:
    """removes a tag from a dataset by updating the dataset's collection tags map

    Args:
        dataset_id (str):
        tag_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoNucleusDatasetUiDatasetViewModel
    """

    return (
        await asyncio_detailed(
            dataset_id=dataset_id,
            tag_name=tag_name,
            client=client,
        )
    ).parsed
