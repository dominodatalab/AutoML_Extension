from __future__ import annotations
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataset_to_add_v1 import DatasetToAddV1
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.link_project_to_dataset_response_400 import LinkProjectToDatasetResponse400
from ...models.link_project_to_dataset_response_404 import LinkProjectToDatasetResponse404
from ...models.link_project_to_dataset_response_500 import LinkProjectToDatasetResponse500
from ...models.shared_datasets_envelope_v1 import SharedDatasetsEnvelopeV1
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: DatasetToAddV1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/projects/v1/projects/{project_id}/shared-datasets".format(
            project_id=quote(str(project_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | LinkProjectToDatasetResponse400
    | LinkProjectToDatasetResponse404
    | LinkProjectToDatasetResponse500
    | SharedDatasetsEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = SharedDatasetsEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = LinkProjectToDatasetResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = LinkProjectToDatasetResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = LinkProjectToDatasetResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | LinkProjectToDatasetResponse400
    | LinkProjectToDatasetResponse404
    | LinkProjectToDatasetResponse500
    | SharedDatasetsEnvelopeV1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DatasetToAddV1,
) -> Response[
    FailureEnvelopeV1
    | LinkProjectToDatasetResponse400
    | LinkProjectToDatasetResponse404
    | LinkProjectToDatasetResponse500
    | SharedDatasetsEnvelopeV1
]:
    """Link a shared dataset to this project

     Link a shared dataset to this project. Required permissions: `ManageDatasetsRw,UseFileStorage`

    Args:
        project_id (str):
        body (DatasetToAddV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | LinkProjectToDatasetResponse400 | LinkProjectToDatasetResponse404 | LinkProjectToDatasetResponse500 | SharedDatasetsEnvelopeV1]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DatasetToAddV1,
) -> (
    FailureEnvelopeV1
    | LinkProjectToDatasetResponse400
    | LinkProjectToDatasetResponse404
    | LinkProjectToDatasetResponse500
    | SharedDatasetsEnvelopeV1
    | None
):
    """Link a shared dataset to this project

     Link a shared dataset to this project. Required permissions: `ManageDatasetsRw,UseFileStorage`

    Args:
        project_id (str):
        body (DatasetToAddV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | LinkProjectToDatasetResponse400 | LinkProjectToDatasetResponse404 | LinkProjectToDatasetResponse500 | SharedDatasetsEnvelopeV1
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DatasetToAddV1,
) -> Response[
    FailureEnvelopeV1
    | LinkProjectToDatasetResponse400
    | LinkProjectToDatasetResponse404
    | LinkProjectToDatasetResponse500
    | SharedDatasetsEnvelopeV1
]:
    """Link a shared dataset to this project

     Link a shared dataset to this project. Required permissions: `ManageDatasetsRw,UseFileStorage`

    Args:
        project_id (str):
        body (DatasetToAddV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | LinkProjectToDatasetResponse400 | LinkProjectToDatasetResponse404 | LinkProjectToDatasetResponse500 | SharedDatasetsEnvelopeV1]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DatasetToAddV1,
) -> (
    FailureEnvelopeV1
    | LinkProjectToDatasetResponse400
    | LinkProjectToDatasetResponse404
    | LinkProjectToDatasetResponse500
    | SharedDatasetsEnvelopeV1
    | None
):
    """Link a shared dataset to this project

     Link a shared dataset to this project. Required permissions: `ManageDatasetsRw,UseFileStorage`

    Args:
        project_id (str):
        body (DatasetToAddV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | LinkProjectToDatasetResponse400 | LinkProjectToDatasetResponse404 | LinkProjectToDatasetResponse500 | SharedDatasetsEnvelopeV1
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
