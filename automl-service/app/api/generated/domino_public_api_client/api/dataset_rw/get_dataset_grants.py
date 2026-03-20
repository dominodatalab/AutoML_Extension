from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataset_rw_grant_details_envelope_v1 import DatasetRwGrantDetailsEnvelopeV1
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_dataset_grants_response_400 import GetDatasetGrantsResponse400
from ...models.get_dataset_grants_response_404 import GetDatasetGrantsResponse404
from ...models.get_dataset_grants_response_500 import GetDatasetGrantsResponse500
from ...types import Response


def _get_kwargs(
    dataset_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/datasetrw/v1/datasets/{dataset_id}/grants".format(
            dataset_id=quote(str(dataset_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DatasetRwGrantDetailsEnvelopeV1
    | FailureEnvelopeV1
    | GetDatasetGrantsResponse400
    | GetDatasetGrantsResponse404
    | GetDatasetGrantsResponse500
    | None
):
    if response.status_code == 200:
        response_200 = DatasetRwGrantDetailsEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetDatasetGrantsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetDatasetGrantsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetDatasetGrantsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DatasetRwGrantDetailsEnvelopeV1
    | FailureEnvelopeV1
    | GetDatasetGrantsResponse400
    | GetDatasetGrantsResponse404
    | GetDatasetGrantsResponse500
]:
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
) -> Response[
    DatasetRwGrantDetailsEnvelopeV1
    | FailureEnvelopeV1
    | GetDatasetGrantsResponse400
    | GetDatasetGrantsResponse404
    | GetDatasetGrantsResponse500
]:
    """Get dataset grants by ID

     Get Dataset grants by ID. Requires List access to the dataset

    Args:
        dataset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetRwGrantDetailsEnvelopeV1 | FailureEnvelopeV1 | GetDatasetGrantsResponse400 | GetDatasetGrantsResponse404 | GetDatasetGrantsResponse500]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataset_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    DatasetRwGrantDetailsEnvelopeV1
    | FailureEnvelopeV1
    | GetDatasetGrantsResponse400
    | GetDatasetGrantsResponse404
    | GetDatasetGrantsResponse500
    | None
):
    """Get dataset grants by ID

     Get Dataset grants by ID. Requires List access to the dataset

    Args:
        dataset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetRwGrantDetailsEnvelopeV1 | FailureEnvelopeV1 | GetDatasetGrantsResponse400 | GetDatasetGrantsResponse404 | GetDatasetGrantsResponse500
    """

    return sync_detailed(
        dataset_id=dataset_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    dataset_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    DatasetRwGrantDetailsEnvelopeV1
    | FailureEnvelopeV1
    | GetDatasetGrantsResponse400
    | GetDatasetGrantsResponse404
    | GetDatasetGrantsResponse500
]:
    """Get dataset grants by ID

     Get Dataset grants by ID. Requires List access to the dataset

    Args:
        dataset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetRwGrantDetailsEnvelopeV1 | FailureEnvelopeV1 | GetDatasetGrantsResponse400 | GetDatasetGrantsResponse404 | GetDatasetGrantsResponse500]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataset_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    DatasetRwGrantDetailsEnvelopeV1
    | FailureEnvelopeV1
    | GetDatasetGrantsResponse400
    | GetDatasetGrantsResponse404
    | GetDatasetGrantsResponse500
    | None
):
    """Get dataset grants by ID

     Get Dataset grants by ID. Requires List access to the dataset

    Args:
        dataset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetRwGrantDetailsEnvelopeV1 | FailureEnvelopeV1 | GetDatasetGrantsResponse400 | GetDatasetGrantsResponse404 | GetDatasetGrantsResponse500
    """

    return (
        await asyncio_detailed(
            dataset_id=dataset_id,
            client=client,
        )
    ).parsed
