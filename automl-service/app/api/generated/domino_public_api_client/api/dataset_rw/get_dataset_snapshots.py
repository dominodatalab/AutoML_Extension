from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_dataset_snapshots_response_400 import GetDatasetSnapshotsResponse400
from ...models.get_dataset_snapshots_response_404 import GetDatasetSnapshotsResponse404
from ...models.get_dataset_snapshots_response_500 import GetDatasetSnapshotsResponse500
from ...models.paginated_snapshot_envelope_v1 import PaginatedSnapshotEnvelopeV1
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dataset_id: str,
    *,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/datasetrw/v1/datasets/{dataset_id}/snapshots".format(
            dataset_id=quote(str(dataset_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GetDatasetSnapshotsResponse400
    | GetDatasetSnapshotsResponse404
    | GetDatasetSnapshotsResponse500
    | PaginatedSnapshotEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedSnapshotEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetDatasetSnapshotsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetDatasetSnapshotsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetDatasetSnapshotsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | GetDatasetSnapshotsResponse400
    | GetDatasetSnapshotsResponse404
    | GetDatasetSnapshotsResponse500
    | PaginatedSnapshotEnvelopeV1
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
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1
    | GetDatasetSnapshotsResponse400
    | GetDatasetSnapshotsResponse404
    | GetDatasetSnapshotsResponse500
    | PaginatedSnapshotEnvelopeV1
]:
    """Get snapshots belonging to dataset

     Get Snapshots belonging to a dataset. Requires List access to the dataset

    Args:
        dataset_id (str):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetDatasetSnapshotsResponse400 | GetDatasetSnapshotsResponse404 | GetDatasetSnapshotsResponse500 | PaginatedSnapshotEnvelopeV1]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataset_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> (
    FailureEnvelopeV1
    | GetDatasetSnapshotsResponse400
    | GetDatasetSnapshotsResponse404
    | GetDatasetSnapshotsResponse500
    | PaginatedSnapshotEnvelopeV1
    | None
):
    """Get snapshots belonging to dataset

     Get Snapshots belonging to a dataset. Requires List access to the dataset

    Args:
        dataset_id (str):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetDatasetSnapshotsResponse400 | GetDatasetSnapshotsResponse404 | GetDatasetSnapshotsResponse500 | PaginatedSnapshotEnvelopeV1
    """

    return sync_detailed(
        dataset_id=dataset_id,
        client=client,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    dataset_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1
    | GetDatasetSnapshotsResponse400
    | GetDatasetSnapshotsResponse404
    | GetDatasetSnapshotsResponse500
    | PaginatedSnapshotEnvelopeV1
]:
    """Get snapshots belonging to dataset

     Get Snapshots belonging to a dataset. Requires List access to the dataset

    Args:
        dataset_id (str):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetDatasetSnapshotsResponse400 | GetDatasetSnapshotsResponse404 | GetDatasetSnapshotsResponse500 | PaginatedSnapshotEnvelopeV1]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataset_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> (
    FailureEnvelopeV1
    | GetDatasetSnapshotsResponse400
    | GetDatasetSnapshotsResponse404
    | GetDatasetSnapshotsResponse500
    | PaginatedSnapshotEnvelopeV1
    | None
):
    """Get snapshots belonging to dataset

     Get Snapshots belonging to a dataset. Requires List access to the dataset

    Args:
        dataset_id (str):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetDatasetSnapshotsResponse400 | GetDatasetSnapshotsResponse404 | GetDatasetSnapshotsResponse500 | PaginatedSnapshotEnvelopeV1
    """

    return (
        await asyncio_detailed(
            dataset_id=dataset_id,
            client=client,
            offset=offset,
            limit=limit,
        )
    ).parsed
