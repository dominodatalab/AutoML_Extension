from __future__ import annotations
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.environment_revision_update_envelope_v1 import EnvironmentRevisionUpdateEnvelopeV1
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.update_environment_revision_is_restricted_response_400 import (
    UpdateEnvironmentRevisionIsRestrictedResponse400,
)
from ...models.update_environment_revision_is_restricted_response_404 import (
    UpdateEnvironmentRevisionIsRestrictedResponse404,
)
from ...models.update_environment_revision_is_restricted_response_500 import (
    UpdateEnvironmentRevisionIsRestrictedResponse500,
)
from ...models.update_environment_revision_v1 import UpdateEnvironmentRevisionV1
from ...types import Response


def _get_kwargs(
    environment_id: str,
    revision_id: str,
    *,
    body: UpdateEnvironmentRevisionV1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/environments/beta/environments/{environment_id}/revisions/{revision_id}".format(
            environment_id=quote(str(environment_id), safe=""),
            revision_id=quote(str(revision_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    EnvironmentRevisionUpdateEnvelopeV1
    | FailureEnvelopeV1
    | UpdateEnvironmentRevisionIsRestrictedResponse400
    | UpdateEnvironmentRevisionIsRestrictedResponse404
    | UpdateEnvironmentRevisionIsRestrictedResponse500
    | None
):
    if response.status_code == 200:
        response_200 = EnvironmentRevisionUpdateEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateEnvironmentRevisionIsRestrictedResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UpdateEnvironmentRevisionIsRestrictedResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = UpdateEnvironmentRevisionIsRestrictedResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    EnvironmentRevisionUpdateEnvelopeV1
    | FailureEnvelopeV1
    | UpdateEnvironmentRevisionIsRestrictedResponse400
    | UpdateEnvironmentRevisionIsRestrictedResponse404
    | UpdateEnvironmentRevisionIsRestrictedResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    environment_id: str,
    revision_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateEnvironmentRevisionV1,
) -> Response[
    EnvironmentRevisionUpdateEnvelopeV1
    | FailureEnvelopeV1
    | UpdateEnvironmentRevisionIsRestrictedResponse400
    | UpdateEnvironmentRevisionIsRestrictedResponse404
    | UpdateEnvironmentRevisionIsRestrictedResponse500
]:
    """Update the restricted revision of an environment

     Update a revision of an environment to mark if isRestricted. Required permissions:
    `ClassifyEnvironments`. *Note:* This is a beta endpoint with known limitations.

    Args:
        environment_id (str):
        revision_id (str):
        body (UpdateEnvironmentRevisionV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnvironmentRevisionUpdateEnvelopeV1 | FailureEnvelopeV1 | UpdateEnvironmentRevisionIsRestrictedResponse400 | UpdateEnvironmentRevisionIsRestrictedResponse404 | UpdateEnvironmentRevisionIsRestrictedResponse500]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        revision_id=revision_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_id: str,
    revision_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateEnvironmentRevisionV1,
) -> (
    EnvironmentRevisionUpdateEnvelopeV1
    | FailureEnvelopeV1
    | UpdateEnvironmentRevisionIsRestrictedResponse400
    | UpdateEnvironmentRevisionIsRestrictedResponse404
    | UpdateEnvironmentRevisionIsRestrictedResponse500
    | None
):
    """Update the restricted revision of an environment

     Update a revision of an environment to mark if isRestricted. Required permissions:
    `ClassifyEnvironments`. *Note:* This is a beta endpoint with known limitations.

    Args:
        environment_id (str):
        revision_id (str):
        body (UpdateEnvironmentRevisionV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnvironmentRevisionUpdateEnvelopeV1 | FailureEnvelopeV1 | UpdateEnvironmentRevisionIsRestrictedResponse400 | UpdateEnvironmentRevisionIsRestrictedResponse404 | UpdateEnvironmentRevisionIsRestrictedResponse500
    """

    return sync_detailed(
        environment_id=environment_id,
        revision_id=revision_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    revision_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateEnvironmentRevisionV1,
) -> Response[
    EnvironmentRevisionUpdateEnvelopeV1
    | FailureEnvelopeV1
    | UpdateEnvironmentRevisionIsRestrictedResponse400
    | UpdateEnvironmentRevisionIsRestrictedResponse404
    | UpdateEnvironmentRevisionIsRestrictedResponse500
]:
    """Update the restricted revision of an environment

     Update a revision of an environment to mark if isRestricted. Required permissions:
    `ClassifyEnvironments`. *Note:* This is a beta endpoint with known limitations.

    Args:
        environment_id (str):
        revision_id (str):
        body (UpdateEnvironmentRevisionV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnvironmentRevisionUpdateEnvelopeV1 | FailureEnvelopeV1 | UpdateEnvironmentRevisionIsRestrictedResponse400 | UpdateEnvironmentRevisionIsRestrictedResponse404 | UpdateEnvironmentRevisionIsRestrictedResponse500]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        revision_id=revision_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    revision_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateEnvironmentRevisionV1,
) -> (
    EnvironmentRevisionUpdateEnvelopeV1
    | FailureEnvelopeV1
    | UpdateEnvironmentRevisionIsRestrictedResponse400
    | UpdateEnvironmentRevisionIsRestrictedResponse404
    | UpdateEnvironmentRevisionIsRestrictedResponse500
    | None
):
    """Update the restricted revision of an environment

     Update a revision of an environment to mark if isRestricted. Required permissions:
    `ClassifyEnvironments`. *Note:* This is a beta endpoint with known limitations.

    Args:
        environment_id (str):
        revision_id (str):
        body (UpdateEnvironmentRevisionV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnvironmentRevisionUpdateEnvelopeV1 | FailureEnvelopeV1 | UpdateEnvironmentRevisionIsRestrictedResponse400 | UpdateEnvironmentRevisionIsRestrictedResponse404 | UpdateEnvironmentRevisionIsRestrictedResponse500
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            revision_id=revision_id,
            client=client,
            body=body,
        )
    ).parsed
