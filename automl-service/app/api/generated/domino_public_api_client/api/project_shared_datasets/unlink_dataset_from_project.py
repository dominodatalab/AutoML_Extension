from __future__ import annotations
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_envelope_v1 import DeleteEnvelopeV1
from ...types import Response


def _get_kwargs(
    project_id: str,
    dataset_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/projects/v1/projects/{project_id}/shared-datasets/{dataset_id}".format(
            project_id=quote(str(project_id), safe=""),
            dataset_id=quote(str(dataset_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteEnvelopeV1 | None:
    if response.status_code == 200:
        response_200 = DeleteEnvelopeV1.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteEnvelopeV1]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    dataset_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DeleteEnvelopeV1]:
    """Unlink a shared dataset from this project

     Unlink the dataset with the specified Id from a project. Required permissions:
    `ManageDatasetsRw,UseFileStorage`

    Args:
        project_id (str):
        dataset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteEnvelopeV1]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        dataset_id=dataset_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    dataset_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> DeleteEnvelopeV1 | None:
    """Unlink a shared dataset from this project

     Unlink the dataset with the specified Id from a project. Required permissions:
    `ManageDatasetsRw,UseFileStorage`

    Args:
        project_id (str):
        dataset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteEnvelopeV1
    """

    return sync_detailed(
        project_id=project_id,
        dataset_id=dataset_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    dataset_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DeleteEnvelopeV1]:
    """Unlink a shared dataset from this project

     Unlink the dataset with the specified Id from a project. Required permissions:
    `ManageDatasetsRw,UseFileStorage`

    Args:
        project_id (str):
        dataset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteEnvelopeV1]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        dataset_id=dataset_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    dataset_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> DeleteEnvelopeV1 | None:
    """Unlink a shared dataset from this project

     Unlink the dataset with the specified Id from a project. Required permissions:
    `ManageDatasetsRw,UseFileStorage`

    Args:
        project_id (str):
        dataset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteEnvelopeV1
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            dataset_id=dataset_id,
            client=client,
        )
    ).parsed
