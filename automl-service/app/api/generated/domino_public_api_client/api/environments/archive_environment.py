from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.archive_environment_response_400 import ArchiveEnvironmentResponse400
from ...models.archive_environment_response_404 import ArchiveEnvironmentResponse404
from ...models.archive_environment_response_500 import ArchiveEnvironmentResponse500
from ...models.environment_envelope_v1 import EnvironmentEnvelopeV1
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...types import Response


def _get_kwargs(
    environment_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/environments/v1/environments/{environment_id}".format(
            environment_id=quote(str(environment_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ArchiveEnvironmentResponse400
    | ArchiveEnvironmentResponse404
    | ArchiveEnvironmentResponse500
    | EnvironmentEnvelopeV1
    | FailureEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = EnvironmentEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ArchiveEnvironmentResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ArchiveEnvironmentResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ArchiveEnvironmentResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ArchiveEnvironmentResponse400
    | ArchiveEnvironmentResponse404
    | ArchiveEnvironmentResponse500
    | EnvironmentEnvelopeV1
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
) -> Response[
    ArchiveEnvironmentResponse400
    | ArchiveEnvironmentResponse404
    | ArchiveEnvironmentResponse500
    | EnvironmentEnvelopeV1
    | FailureEnvelopeV1
]:
    """Archive an environment

     Archive an Environment, removing it from the list of visible environments. Required permissions:
    `ManageEnvironments, EditEnvironment`

    Args:
        environment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArchiveEnvironmentResponse400 | ArchiveEnvironmentResponse404 | ArchiveEnvironmentResponse500 | EnvironmentEnvelopeV1 | FailureEnvelopeV1]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    ArchiveEnvironmentResponse400
    | ArchiveEnvironmentResponse404
    | ArchiveEnvironmentResponse500
    | EnvironmentEnvelopeV1
    | FailureEnvelopeV1
    | None
):
    """Archive an environment

     Archive an Environment, removing it from the list of visible environments. Required permissions:
    `ManageEnvironments, EditEnvironment`

    Args:
        environment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArchiveEnvironmentResponse400 | ArchiveEnvironmentResponse404 | ArchiveEnvironmentResponse500 | EnvironmentEnvelopeV1 | FailureEnvelopeV1
    """

    return sync_detailed(
        environment_id=environment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    ArchiveEnvironmentResponse400
    | ArchiveEnvironmentResponse404
    | ArchiveEnvironmentResponse500
    | EnvironmentEnvelopeV1
    | FailureEnvelopeV1
]:
    """Archive an environment

     Archive an Environment, removing it from the list of visible environments. Required permissions:
    `ManageEnvironments, EditEnvironment`

    Args:
        environment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArchiveEnvironmentResponse400 | ArchiveEnvironmentResponse404 | ArchiveEnvironmentResponse500 | EnvironmentEnvelopeV1 | FailureEnvelopeV1]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    ArchiveEnvironmentResponse400
    | ArchiveEnvironmentResponse404
    | ArchiveEnvironmentResponse500
    | EnvironmentEnvelopeV1
    | FailureEnvelopeV1
    | None
):
    """Archive an environment

     Archive an Environment, removing it from the list of visible environments. Required permissions:
    `ManageEnvironments, EditEnvironment`

    Args:
        environment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArchiveEnvironmentResponse400 | ArchiveEnvironmentResponse404 | ArchiveEnvironmentResponse500 | EnvironmentEnvelopeV1 | FailureEnvelopeV1
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            client=client,
        )
    ).parsed
