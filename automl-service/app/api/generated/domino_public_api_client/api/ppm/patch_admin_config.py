from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.admin_config_patch_request import AdminConfigPatchRequest
from ...models.patch_admin_config_response_400 import PatchAdminConfigResponse400
from ...models.patch_admin_config_response_500 import PatchAdminConfigResponse500
from ...types import Response


def _get_kwargs(
    config_id: str,
    *,
    body: AdminConfigPatchRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v4/ppm/admin/config/{config_id}".format(
            config_id=quote(str(config_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PatchAdminConfigResponse400 | PatchAdminConfigResponse500 | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = PatchAdminConfigResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 500:
        response_500 = PatchAdminConfigResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PatchAdminConfigResponse400 | PatchAdminConfigResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    config_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AdminConfigPatchRequest,
) -> Response[Any | PatchAdminConfigResponse400 | PatchAdminConfigResponse500]:
    """Update Admin Config

     Partially update a specific PPM admin configuration by ID (only provided fields will be updated)

    Args:
        config_id (str):
        body (AdminConfigPatchRequest): Partial PPM admin configuration (all fields optional)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchAdminConfigResponse400 | PatchAdminConfigResponse500]
    """

    kwargs = _get_kwargs(
        config_id=config_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    config_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AdminConfigPatchRequest,
) -> Any | PatchAdminConfigResponse400 | PatchAdminConfigResponse500 | None:
    """Update Admin Config

     Partially update a specific PPM admin configuration by ID (only provided fields will be updated)

    Args:
        config_id (str):
        body (AdminConfigPatchRequest): Partial PPM admin configuration (all fields optional)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchAdminConfigResponse400 | PatchAdminConfigResponse500
    """

    return sync_detailed(
        config_id=config_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    config_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AdminConfigPatchRequest,
) -> Response[Any | PatchAdminConfigResponse400 | PatchAdminConfigResponse500]:
    """Update Admin Config

     Partially update a specific PPM admin configuration by ID (only provided fields will be updated)

    Args:
        config_id (str):
        body (AdminConfigPatchRequest): Partial PPM admin configuration (all fields optional)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchAdminConfigResponse400 | PatchAdminConfigResponse500]
    """

    kwargs = _get_kwargs(
        config_id=config_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    config_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AdminConfigPatchRequest,
) -> Any | PatchAdminConfigResponse400 | PatchAdminConfigResponse500 | None:
    """Update Admin Config

     Partially update a specific PPM admin configuration by ID (only provided fields will be updated)

    Args:
        config_id (str):
        body (AdminConfigPatchRequest): Partial PPM admin configuration (all fields optional)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchAdminConfigResponse400 | PatchAdminConfigResponse500
    """

    return (
        await asyncio_detailed(
            config_id=config_id,
            client=client,
            body=body,
        )
    ).parsed
