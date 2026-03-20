from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataset_rw_envelope_v1 import DatasetRwEnvelopeV1
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.remove_dataset_tag_response_400 import RemoveDatasetTagResponse400
from ...models.remove_dataset_tag_response_404 import RemoveDatasetTagResponse404
from ...models.remove_dataset_tag_response_500 import RemoveDatasetTagResponse500
from ...types import Response


def _get_kwargs(
    dataset_id: str,
    tag_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/datasetrw/v1/datasets/{dataset_id}/tags/{tag_name}".format(
            dataset_id=quote(str(dataset_id), safe=""),
            tag_name=quote(str(tag_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DatasetRwEnvelopeV1
    | FailureEnvelopeV1
    | RemoveDatasetTagResponse400
    | RemoveDatasetTagResponse404
    | RemoveDatasetTagResponse500
    | None
):
    if response.status_code == 200:
        response_200 = DatasetRwEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RemoveDatasetTagResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = RemoveDatasetTagResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = RemoveDatasetTagResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DatasetRwEnvelopeV1
    | FailureEnvelopeV1
    | RemoveDatasetTagResponse400
    | RemoveDatasetTagResponse404
    | RemoveDatasetTagResponse500
]:
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
) -> Response[
    DatasetRwEnvelopeV1
    | FailureEnvelopeV1
    | RemoveDatasetTagResponse400
    | RemoveDatasetTagResponse404
    | RemoveDatasetTagResponse500
]:
    """Remove a tag from a Dataset

     Remove a Tag from a dataset. Requires Update access to the dataset

    Args:
        dataset_id (str):
        tag_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetRwEnvelopeV1 | FailureEnvelopeV1 | RemoveDatasetTagResponse400 | RemoveDatasetTagResponse404 | RemoveDatasetTagResponse500]
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
) -> (
    DatasetRwEnvelopeV1
    | FailureEnvelopeV1
    | RemoveDatasetTagResponse400
    | RemoveDatasetTagResponse404
    | RemoveDatasetTagResponse500
    | None
):
    """Remove a tag from a Dataset

     Remove a Tag from a dataset. Requires Update access to the dataset

    Args:
        dataset_id (str):
        tag_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetRwEnvelopeV1 | FailureEnvelopeV1 | RemoveDatasetTagResponse400 | RemoveDatasetTagResponse404 | RemoveDatasetTagResponse500
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
) -> Response[
    DatasetRwEnvelopeV1
    | FailureEnvelopeV1
    | RemoveDatasetTagResponse400
    | RemoveDatasetTagResponse404
    | RemoveDatasetTagResponse500
]:
    """Remove a tag from a Dataset

     Remove a Tag from a dataset. Requires Update access to the dataset

    Args:
        dataset_id (str):
        tag_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetRwEnvelopeV1 | FailureEnvelopeV1 | RemoveDatasetTagResponse400 | RemoveDatasetTagResponse404 | RemoveDatasetTagResponse500]
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
) -> (
    DatasetRwEnvelopeV1
    | FailureEnvelopeV1
    | RemoveDatasetTagResponse400
    | RemoveDatasetTagResponse404
    | RemoveDatasetTagResponse500
    | None
):
    """Remove a tag from a Dataset

     Remove a Tag from a dataset. Requires Update access to the dataset

    Args:
        dataset_id (str):
        tag_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetRwEnvelopeV1 | FailureEnvelopeV1 | RemoveDatasetTagResponse400 | RemoveDatasetTagResponse404 | RemoveDatasetTagResponse500
    """

    return (
        await asyncio_detailed(
            dataset_id=dataset_id,
            tag_name=tag_name,
            client=client,
        )
    ).parsed
