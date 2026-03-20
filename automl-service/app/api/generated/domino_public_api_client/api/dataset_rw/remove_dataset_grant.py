from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataset_rw_grant_envelope_v1 import DatasetRwGrantEnvelopeV1
from ...models.dataset_rw_grant_v1 import DatasetRwGrantV1
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.remove_dataset_grant_response_400 import RemoveDatasetGrantResponse400
from ...models.remove_dataset_grant_response_404 import RemoveDatasetGrantResponse404
from ...models.remove_dataset_grant_response_500 import RemoveDatasetGrantResponse500
from ...types import Response


def _get_kwargs(
    dataset_id: str,
    *,
    body: DatasetRwGrantV1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/datasetrw/v1/datasets/{dataset_id}/grants".format(
            dataset_id=quote(str(dataset_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DatasetRwGrantEnvelopeV1
    | FailureEnvelopeV1
    | RemoveDatasetGrantResponse400
    | RemoveDatasetGrantResponse404
    | RemoveDatasetGrantResponse500
    | None
):
    if response.status_code == 200:
        response_200 = DatasetRwGrantEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RemoveDatasetGrantResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = RemoveDatasetGrantResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = RemoveDatasetGrantResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DatasetRwGrantEnvelopeV1
    | FailureEnvelopeV1
    | RemoveDatasetGrantResponse400
    | RemoveDatasetGrantResponse404
    | RemoveDatasetGrantResponse500
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
    body: DatasetRwGrantV1,
) -> Response[
    DatasetRwGrantEnvelopeV1
    | FailureEnvelopeV1
    | RemoveDatasetGrantResponse400
    | RemoveDatasetGrantResponse404
    | RemoveDatasetGrantResponse500
]:
    """Remove a grant from a dataset's existing sequence of grants

     Remove a grant from a dataset's existing sequence of grants. Requires EditSecurity access to the
    dataset

    Args:
        dataset_id (str):
        body (DatasetRwGrantV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetRwGrantEnvelopeV1 | FailureEnvelopeV1 | RemoveDatasetGrantResponse400 | RemoveDatasetGrantResponse404 | RemoveDatasetGrantResponse500]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DatasetRwGrantV1,
) -> (
    DatasetRwGrantEnvelopeV1
    | FailureEnvelopeV1
    | RemoveDatasetGrantResponse400
    | RemoveDatasetGrantResponse404
    | RemoveDatasetGrantResponse500
    | None
):
    """Remove a grant from a dataset's existing sequence of grants

     Remove a grant from a dataset's existing sequence of grants. Requires EditSecurity access to the
    dataset

    Args:
        dataset_id (str):
        body (DatasetRwGrantV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetRwGrantEnvelopeV1 | FailureEnvelopeV1 | RemoveDatasetGrantResponse400 | RemoveDatasetGrantResponse404 | RemoveDatasetGrantResponse500
    """

    return sync_detailed(
        dataset_id=dataset_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    dataset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DatasetRwGrantV1,
) -> Response[
    DatasetRwGrantEnvelopeV1
    | FailureEnvelopeV1
    | RemoveDatasetGrantResponse400
    | RemoveDatasetGrantResponse404
    | RemoveDatasetGrantResponse500
]:
    """Remove a grant from a dataset's existing sequence of grants

     Remove a grant from a dataset's existing sequence of grants. Requires EditSecurity access to the
    dataset

    Args:
        dataset_id (str):
        body (DatasetRwGrantV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetRwGrantEnvelopeV1 | FailureEnvelopeV1 | RemoveDatasetGrantResponse400 | RemoveDatasetGrantResponse404 | RemoveDatasetGrantResponse500]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataset_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DatasetRwGrantV1,
) -> (
    DatasetRwGrantEnvelopeV1
    | FailureEnvelopeV1
    | RemoveDatasetGrantResponse400
    | RemoveDatasetGrantResponse404
    | RemoveDatasetGrantResponse500
    | None
):
    """Remove a grant from a dataset's existing sequence of grants

     Remove a grant from a dataset's existing sequence of grants. Requires EditSecurity access to the
    dataset

    Args:
        dataset_id (str):
        body (DatasetRwGrantV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetRwGrantEnvelopeV1 | FailureEnvelopeV1 | RemoveDatasetGrantResponse400 | RemoveDatasetGrantResponse404 | RemoveDatasetGrantResponse500
    """

    return (
        await asyncio_detailed(
            dataset_id=dataset_id,
            client=client,
            body=body,
        )
    ).parsed
