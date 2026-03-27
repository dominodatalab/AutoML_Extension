from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_environments_api_environment_revision_details import (
    DominoEnvironmentsApiEnvironmentRevisionDetails,
)
from ...models.domino_environments_api_new_environment_revision import DominoEnvironmentsApiNewEnvironmentRevision
from ...types import Response


def _get_kwargs(
    environment_id: str,
    *,
    body: DominoEnvironmentsApiNewEnvironmentRevision,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/environments/{environment_id}/environmentRevision".format(
            environment_id=quote(str(environment_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentRevisionDetails | None:
    if response.status_code == 201:
        response_201 = DominoEnvironmentsApiEnvironmentRevisionDetails.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = DominoApiErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DominoApiErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DominoApiErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = DominoApiErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentRevisionDetails]:
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
    body: DominoEnvironmentsApiNewEnvironmentRevision,
) -> Response[DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentRevisionDetails]:
    """Create environment revision

    Args:
        environment_id (str):
        body (DominoEnvironmentsApiNewEnvironmentRevision):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentRevisionDetails]
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
    body: DominoEnvironmentsApiNewEnvironmentRevision,
) -> DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentRevisionDetails | None:
    """Create environment revision

    Args:
        environment_id (str):
        body (DominoEnvironmentsApiNewEnvironmentRevision):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentRevisionDetails
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
    body: DominoEnvironmentsApiNewEnvironmentRevision,
) -> Response[DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentRevisionDetails]:
    """Create environment revision

    Args:
        environment_id (str):
        body (DominoEnvironmentsApiNewEnvironmentRevision):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentRevisionDetails]
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
    body: DominoEnvironmentsApiNewEnvironmentRevision,
) -> DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentRevisionDetails | None:
    """Create environment revision

    Args:
        environment_id (str):
        body (DominoEnvironmentsApiNewEnvironmentRevision):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentRevisionDetails
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            client=client,
            body=body,
        )
    ).parsed
