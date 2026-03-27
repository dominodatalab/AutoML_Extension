from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_workspace_api_workspace_global_settings_dto import DominoWorkspaceApiWorkspaceGlobalSettingsDto
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspace/getGlobalSettings",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoWorkspaceApiWorkspaceGlobalSettingsDto | None:
    if response.status_code == 200:
        response_200 = DominoWorkspaceApiWorkspaceGlobalSettingsDto.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = DominoApiErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = DominoApiErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DominoApiErrorResponse | DominoWorkspaceApiWorkspaceGlobalSettingsDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[DominoApiErrorResponse | DominoWorkspaceApiWorkspaceGlobalSettingsDto]:
    """Get the global workspace settings

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoWorkspaceApiWorkspaceGlobalSettingsDto]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> DominoApiErrorResponse | DominoWorkspaceApiWorkspaceGlobalSettingsDto | None:
    """Get the global workspace settings

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoWorkspaceApiWorkspaceGlobalSettingsDto
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[DominoApiErrorResponse | DominoWorkspaceApiWorkspaceGlobalSettingsDto]:
    """Get the global workspace settings

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoWorkspaceApiWorkspaceGlobalSettingsDto]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> DominoApiErrorResponse | DominoWorkspaceApiWorkspaceGlobalSettingsDto | None:
    """Get the global workspace settings

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoWorkspaceApiWorkspaceGlobalSettingsDto
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
