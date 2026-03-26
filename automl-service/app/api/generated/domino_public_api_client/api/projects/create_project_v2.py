from __future__ import annotations
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_project_v2_response_400 import CreateProjectV2Response400
from ...models.create_project_v2_response_404 import CreateProjectV2Response404
from ...models.create_project_v2_response_500 import CreateProjectV2Response500
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.new_project_v2 import NewProjectV2
from ...models.project_envelope_v1 import ProjectEnvelopeV1
from ...types import Response


def _get_kwargs(
    *,
    body: NewProjectV2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/projects/v2/projects",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreateProjectV2Response400
    | CreateProjectV2Response404
    | CreateProjectV2Response500
    | FailureEnvelopeV1
    | ProjectEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = ProjectEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CreateProjectV2Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CreateProjectV2Response404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = CreateProjectV2Response500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateProjectV2Response400
    | CreateProjectV2Response404
    | CreateProjectV2Response500
    | FailureEnvelopeV1
    | ProjectEnvelopeV1
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
    body: NewProjectV2,
) -> Response[
    CreateProjectV2Response400
    | CreateProjectV2Response404
    | CreateProjectV2Response500
    | FailureEnvelopeV1
    | ProjectEnvelopeV1
]:
    """Create a project

     Create a project. Required permissions: `CreateProject, UseFileStorage`.

    Args:
        body (NewProjectV2):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateProjectV2Response400 | CreateProjectV2Response404 | CreateProjectV2Response500 | FailureEnvelopeV1 | ProjectEnvelopeV1]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: NewProjectV2,
) -> (
    CreateProjectV2Response400
    | CreateProjectV2Response404
    | CreateProjectV2Response500
    | FailureEnvelopeV1
    | ProjectEnvelopeV1
    | None
):
    """Create a project

     Create a project. Required permissions: `CreateProject, UseFileStorage`.

    Args:
        body (NewProjectV2):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateProjectV2Response400 | CreateProjectV2Response404 | CreateProjectV2Response500 | FailureEnvelopeV1 | ProjectEnvelopeV1
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: NewProjectV2,
) -> Response[
    CreateProjectV2Response400
    | CreateProjectV2Response404
    | CreateProjectV2Response500
    | FailureEnvelopeV1
    | ProjectEnvelopeV1
]:
    """Create a project

     Create a project. Required permissions: `CreateProject, UseFileStorage`.

    Args:
        body (NewProjectV2):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateProjectV2Response400 | CreateProjectV2Response404 | CreateProjectV2Response500 | FailureEnvelopeV1 | ProjectEnvelopeV1]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: NewProjectV2,
) -> (
    CreateProjectV2Response400
    | CreateProjectV2Response404
    | CreateProjectV2Response500
    | FailureEnvelopeV1
    | ProjectEnvelopeV1
    | None
):
    """Create a project

     Create a project. Required permissions: `CreateProject, UseFileStorage`.

    Args:
        body (NewProjectV2):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateProjectV2Response400 | CreateProjectV2Response404 | CreateProjectV2Response500 | FailureEnvelopeV1 | ProjectEnvelopeV1
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
