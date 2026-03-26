from __future__ import annotations
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.copy_project_response_400 import CopyProjectResponse400
from ...models.copy_project_response_404 import CopyProjectResponse404
from ...models.copy_project_response_500 import CopyProjectResponse500
from ...models.copy_project_spec_v1 import CopyProjectSpecV1
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.project_copy_result_envelope_v1 import ProjectCopyResultEnvelopeV1
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: CopyProjectSpecV1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/projects/v1/projects/{project_id}/copy-project".format(
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
    CopyProjectResponse400
    | CopyProjectResponse404
    | CopyProjectResponse500
    | FailureEnvelopeV1
    | ProjectCopyResultEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = ProjectCopyResultEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CopyProjectResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CopyProjectResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = FailureEnvelopeV1.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = CopyProjectResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CopyProjectResponse400
    | CopyProjectResponse404
    | CopyProjectResponse500
    | FailureEnvelopeV1
    | ProjectCopyResultEnvelopeV1
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
    body: CopyProjectSpecV1,
) -> Response[
    CopyProjectResponse400
    | CopyProjectResponse404
    | CopyProjectResponse500
    | FailureEnvelopeV1
    | ProjectCopyResultEnvelopeV1
]:
    """Create a new project by copying an existing project and providing optional overrides.

     Create a new project by copying an existing project and providing optional overrides. Specify a git
    repository to link to the copied project or copy the original project's git repository for the
    copied project.

    Args:
        project_id (str):
        body (CopyProjectSpecV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CopyProjectResponse400 | CopyProjectResponse404 | CopyProjectResponse500 | FailureEnvelopeV1 | ProjectCopyResultEnvelopeV1]
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
    body: CopyProjectSpecV1,
) -> (
    CopyProjectResponse400
    | CopyProjectResponse404
    | CopyProjectResponse500
    | FailureEnvelopeV1
    | ProjectCopyResultEnvelopeV1
    | None
):
    """Create a new project by copying an existing project and providing optional overrides.

     Create a new project by copying an existing project and providing optional overrides. Specify a git
    repository to link to the copied project or copy the original project's git repository for the
    copied project.

    Args:
        project_id (str):
        body (CopyProjectSpecV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CopyProjectResponse400 | CopyProjectResponse404 | CopyProjectResponse500 | FailureEnvelopeV1 | ProjectCopyResultEnvelopeV1
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
    body: CopyProjectSpecV1,
) -> Response[
    CopyProjectResponse400
    | CopyProjectResponse404
    | CopyProjectResponse500
    | FailureEnvelopeV1
    | ProjectCopyResultEnvelopeV1
]:
    """Create a new project by copying an existing project and providing optional overrides.

     Create a new project by copying an existing project and providing optional overrides. Specify a git
    repository to link to the copied project or copy the original project's git repository for the
    copied project.

    Args:
        project_id (str):
        body (CopyProjectSpecV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CopyProjectResponse400 | CopyProjectResponse404 | CopyProjectResponse500 | FailureEnvelopeV1 | ProjectCopyResultEnvelopeV1]
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
    body: CopyProjectSpecV1,
) -> (
    CopyProjectResponse400
    | CopyProjectResponse404
    | CopyProjectResponse500
    | FailureEnvelopeV1
    | ProjectCopyResultEnvelopeV1
    | None
):
    """Create a new project by copying an existing project and providing optional overrides.

     Create a new project by copying an existing project and providing optional overrides. Specify a git
    repository to link to the copied project or copy the original project's git repository for the
    copied project.

    Args:
        project_id (str):
        body (CopyProjectSpecV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CopyProjectResponse400 | CopyProjectResponse404 | CopyProjectResponse500 | FailureEnvelopeV1 | ProjectCopyResultEnvelopeV1
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
