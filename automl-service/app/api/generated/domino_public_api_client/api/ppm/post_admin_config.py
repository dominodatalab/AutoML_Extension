from __future__ import annotations
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.admin_config_request import AdminConfigRequest
from ...models.admin_config_response import AdminConfigResponse
from ...models.post_admin_config_response_400 import PostAdminConfigResponse400
from ...models.post_admin_config_response_500 import PostAdminConfigResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: AdminConfigRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v4/ppm/admin/config",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AdminConfigResponse | PostAdminConfigResponse400 | PostAdminConfigResponse500 | None:
    if response.status_code == 201:
        response_201 = AdminConfigResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = PostAdminConfigResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = PostAdminConfigResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AdminConfigResponse | PostAdminConfigResponse400 | PostAdminConfigResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AdminConfigRequest,
) -> Response[AdminConfigResponse | PostAdminConfigResponse400 | PostAdminConfigResponse500]:
    """Create Admin Config

     Create new PPM admin configuration

    Args:
        body (AdminConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminConfigResponse | PostAdminConfigResponse400 | PostAdminConfigResponse500]
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
    body: AdminConfigRequest,
) -> AdminConfigResponse | PostAdminConfigResponse400 | PostAdminConfigResponse500 | None:
    """Create Admin Config

     Create new PPM admin configuration

    Args:
        body (AdminConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminConfigResponse | PostAdminConfigResponse400 | PostAdminConfigResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AdminConfigRequest,
) -> Response[AdminConfigResponse | PostAdminConfigResponse400 | PostAdminConfigResponse500]:
    """Create Admin Config

     Create new PPM admin configuration

    Args:
        body (AdminConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminConfigResponse | PostAdminConfigResponse400 | PostAdminConfigResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AdminConfigRequest,
) -> AdminConfigResponse | PostAdminConfigResponse400 | PostAdminConfigResponse500 | None:
    """Create Admin Config

     Create new PPM admin configuration

    Args:
        body (AdminConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminConfigResponse | PostAdminConfigResponse400 | PostAdminConfigResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
