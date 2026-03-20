from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_datasets_response_400 import GetDatasetsResponse400
from ...models.get_datasets_response_404 import GetDatasetsResponse404
from ...models.get_datasets_response_500 import GetDatasetsResponse500
from ...models.paginated_dataset_rw_envelope_v1 import PaginatedDatasetRwEnvelopeV1
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    project_id: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["projectId"] = project_id

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/datasetrw/v1/datasets",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GetDatasetsResponse400
    | GetDatasetsResponse404
    | GetDatasetsResponse500
    | PaginatedDatasetRwEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedDatasetRwEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetDatasetsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetDatasetsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetDatasetsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | GetDatasetsResponse400
    | GetDatasetsResponse404
    | GetDatasetsResponse500
    | PaginatedDatasetRwEnvelopeV1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1
    | GetDatasetsResponse400
    | GetDatasetsResponse404
    | GetDatasetsResponse500
    | PaginatedDatasetRwEnvelopeV1
]:
    """Deprecated - Get datasets accessible to user

     Deprecated: Use GetDatasetsV2. Get Datasets that a user has access to

    Args:
        project_id (str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetDatasetsResponse400 | GetDatasetsResponse404 | GetDatasetsResponse500 | PaginatedDatasetRwEnvelopeV1]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> (
    FailureEnvelopeV1
    | GetDatasetsResponse400
    | GetDatasetsResponse404
    | GetDatasetsResponse500
    | PaginatedDatasetRwEnvelopeV1
    | None
):
    """Deprecated - Get datasets accessible to user

     Deprecated: Use GetDatasetsV2. Get Datasets that a user has access to

    Args:
        project_id (str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetDatasetsResponse400 | GetDatasetsResponse404 | GetDatasetsResponse500 | PaginatedDatasetRwEnvelopeV1
    """

    return sync_detailed(
        client=client,
        project_id=project_id,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1
    | GetDatasetsResponse400
    | GetDatasetsResponse404
    | GetDatasetsResponse500
    | PaginatedDatasetRwEnvelopeV1
]:
    """Deprecated - Get datasets accessible to user

     Deprecated: Use GetDatasetsV2. Get Datasets that a user has access to

    Args:
        project_id (str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetDatasetsResponse400 | GetDatasetsResponse404 | GetDatasetsResponse500 | PaginatedDatasetRwEnvelopeV1]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> (
    FailureEnvelopeV1
    | GetDatasetsResponse400
    | GetDatasetsResponse404
    | GetDatasetsResponse500
    | PaginatedDatasetRwEnvelopeV1
    | None
):
    """Deprecated - Get datasets accessible to user

     Deprecated: Use GetDatasetsV2. Get Datasets that a user has access to

    Args:
        project_id (str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetDatasetsResponse400 | GetDatasetsResponse404 | GetDatasetsResponse500 | PaginatedDatasetRwEnvelopeV1
    """

    return (
        await asyncio_detailed(
            client=client,
            project_id=project_id,
            offset=offset,
            limit=limit,
        )
    ).parsed
