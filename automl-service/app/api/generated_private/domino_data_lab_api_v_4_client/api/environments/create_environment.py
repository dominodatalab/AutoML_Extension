from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_environments_api_create_new_environment import DominoEnvironmentsApiCreateNewEnvironment
from ...models.domino_environments_api_environment_details import DominoEnvironmentsApiEnvironmentDetails
from ...types import Response


def _get_kwargs(
    *,
    body: DominoEnvironmentsApiCreateNewEnvironment,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/environments",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentDetails | None:
    if response.status_code == 201:
        response_201 = DominoEnvironmentsApiEnvironmentDetails.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DominoEnvironmentsApiCreateNewEnvironment,
) -> Response[DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentDetails]:
    """Create environment

    Args:
        body (DominoEnvironmentsApiCreateNewEnvironment):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentDetails]
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
    body: DominoEnvironmentsApiCreateNewEnvironment,
) -> DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentDetails | None:
    """Create environment

    Args:
        body (DominoEnvironmentsApiCreateNewEnvironment):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentDetails
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DominoEnvironmentsApiCreateNewEnvironment,
) -> Response[DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentDetails]:
    """Create environment

    Args:
        body (DominoEnvironmentsApiCreateNewEnvironment):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentDetails]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DominoEnvironmentsApiCreateNewEnvironment,
) -> DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentDetails | None:
    """Create environment

    Args:
        body (DominoEnvironmentsApiCreateNewEnvironment):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentDetails
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
