from __future__ import annotations
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.archive_project_response_400 import ArchiveProjectResponse400
from ...models.archive_project_response_404 import ArchiveProjectResponse404
from ...models.archive_project_response_500 import ArchiveProjectResponse500
from ...models.delete_envelope_v1 import DeleteEnvelopeV1
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...types import Response


def _get_kwargs(
    project_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/projects/beta/projects/{project_id}".format(
            project_id=quote(str(project_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ArchiveProjectResponse400
    | ArchiveProjectResponse404
    | ArchiveProjectResponse500
    | DeleteEnvelopeV1
    | FailureEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = DeleteEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ArchiveProjectResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ArchiveProjectResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ArchiveProjectResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ArchiveProjectResponse400
    | ArchiveProjectResponse404
    | ArchiveProjectResponse500
    | DeleteEnvelopeV1
    | FailureEnvelopeV1
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
) -> Response[
    ArchiveProjectResponse400
    | ArchiveProjectResponse404
    | ArchiveProjectResponse500
    | DeleteEnvelopeV1
    | FailureEnvelopeV1
]:
    """Archive project by id

     Archive a project by id. Required permissions: `ArchiveProject`. *Note:* This is a beta endpoint
    with known limitations.

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArchiveProjectResponse400 | ArchiveProjectResponse404 | ArchiveProjectResponse500 | DeleteEnvelopeV1 | FailureEnvelopeV1]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    ArchiveProjectResponse400
    | ArchiveProjectResponse404
    | ArchiveProjectResponse500
    | DeleteEnvelopeV1
    | FailureEnvelopeV1
    | None
):
    """Archive project by id

     Archive a project by id. Required permissions: `ArchiveProject`. *Note:* This is a beta endpoint
    with known limitations.

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArchiveProjectResponse400 | ArchiveProjectResponse404 | ArchiveProjectResponse500 | DeleteEnvelopeV1 | FailureEnvelopeV1
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    ArchiveProjectResponse400
    | ArchiveProjectResponse404
    | ArchiveProjectResponse500
    | DeleteEnvelopeV1
    | FailureEnvelopeV1
]:
    """Archive project by id

     Archive a project by id. Required permissions: `ArchiveProject`. *Note:* This is a beta endpoint
    with known limitations.

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArchiveProjectResponse400 | ArchiveProjectResponse404 | ArchiveProjectResponse500 | DeleteEnvelopeV1 | FailureEnvelopeV1]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    ArchiveProjectResponse400
    | ArchiveProjectResponse404
    | ArchiveProjectResponse500
    | DeleteEnvelopeV1
    | FailureEnvelopeV1
    | None
):
    """Archive project by id

     Archive a project by id. Required permissions: `ArchiveProject`. *Note:* This is a beta endpoint
    with known limitations.

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArchiveProjectResponse400 | ArchiveProjectResponse404 | ArchiveProjectResponse500 | DeleteEnvelopeV1 | FailureEnvelopeV1
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
        )
    ).parsed
