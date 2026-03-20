from __future__ import annotations
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_environment_revision_response_400 import CreateEnvironmentRevisionResponse400
from ...models.create_environment_revision_response_404 import CreateEnvironmentRevisionResponse404
from ...models.create_environment_revision_response_500 import CreateEnvironmentRevisionResponse500
from ...models.environment_revision_envelope_v1 import EnvironmentRevisionEnvelopeV1
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.new_environment_revision_v1 import NewEnvironmentRevisionV1
from ...types import Response


def _get_kwargs(
    environment_id: str,
    *,
    body: NewEnvironmentRevisionV1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/environments/beta/environments/{environment_id}/revisions".format(
            environment_id=quote(str(environment_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreateEnvironmentRevisionResponse400
    | CreateEnvironmentRevisionResponse404
    | CreateEnvironmentRevisionResponse500
    | EnvironmentRevisionEnvelopeV1
    | FailureEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = EnvironmentRevisionEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CreateEnvironmentRevisionResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CreateEnvironmentRevisionResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = CreateEnvironmentRevisionResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateEnvironmentRevisionResponse400
    | CreateEnvironmentRevisionResponse404
    | CreateEnvironmentRevisionResponse500
    | EnvironmentRevisionEnvelopeV1
    | FailureEnvelopeV1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    environment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: NewEnvironmentRevisionV1,
) -> Response[
    CreateEnvironmentRevisionResponse400
    | CreateEnvironmentRevisionResponse404
    | CreateEnvironmentRevisionResponse500
    | EnvironmentRevisionEnvelopeV1
    | FailureEnvelopeV1
]:
    """Create a Revision of an Environment

     Create a revision of an environment. Required permissions: `ManageEnvironments, EditEnvironment,
    UseFileStorage`. *Note:* This is a beta endpoint with known limitations.

    Args:
        environment_id (str):
        body (NewEnvironmentRevisionV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateEnvironmentRevisionResponse400 | CreateEnvironmentRevisionResponse404 | CreateEnvironmentRevisionResponse500 | EnvironmentRevisionEnvelopeV1 | FailureEnvelopeV1]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: NewEnvironmentRevisionV1,
) -> (
    CreateEnvironmentRevisionResponse400
    | CreateEnvironmentRevisionResponse404
    | CreateEnvironmentRevisionResponse500
    | EnvironmentRevisionEnvelopeV1
    | FailureEnvelopeV1
    | None
):
    """Create a Revision of an Environment

     Create a revision of an environment. Required permissions: `ManageEnvironments, EditEnvironment,
    UseFileStorage`. *Note:* This is a beta endpoint with known limitations.

    Args:
        environment_id (str):
        body (NewEnvironmentRevisionV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateEnvironmentRevisionResponse400 | CreateEnvironmentRevisionResponse404 | CreateEnvironmentRevisionResponse500 | EnvironmentRevisionEnvelopeV1 | FailureEnvelopeV1
    """

    return sync_detailed(
        environment_id=environment_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: NewEnvironmentRevisionV1,
) -> Response[
    CreateEnvironmentRevisionResponse400
    | CreateEnvironmentRevisionResponse404
    | CreateEnvironmentRevisionResponse500
    | EnvironmentRevisionEnvelopeV1
    | FailureEnvelopeV1
]:
    """Create a Revision of an Environment

     Create a revision of an environment. Required permissions: `ManageEnvironments, EditEnvironment,
    UseFileStorage`. *Note:* This is a beta endpoint with known limitations.

    Args:
        environment_id (str):
        body (NewEnvironmentRevisionV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateEnvironmentRevisionResponse400 | CreateEnvironmentRevisionResponse404 | CreateEnvironmentRevisionResponse500 | EnvironmentRevisionEnvelopeV1 | FailureEnvelopeV1]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: NewEnvironmentRevisionV1,
) -> (
    CreateEnvironmentRevisionResponse400
    | CreateEnvironmentRevisionResponse404
    | CreateEnvironmentRevisionResponse500
    | EnvironmentRevisionEnvelopeV1
    | FailureEnvelopeV1
    | None
):
    """Create a Revision of an Environment

     Create a revision of an environment. Required permissions: `ManageEnvironments, EditEnvironment,
    UseFileStorage`. *Note:* This is a beta endpoint with known limitations.

    Args:
        environment_id (str):
        body (NewEnvironmentRevisionV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateEnvironmentRevisionResponse400 | CreateEnvironmentRevisionResponse404 | CreateEnvironmentRevisionResponse500 | EnvironmentRevisionEnvelopeV1 | FailureEnvelopeV1
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            client=client,
            body=body,
        )
    ).parsed
