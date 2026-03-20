from __future__ import annotations
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.list_extensions_response import ListExtensionsResponse
from ...models.list_extensions_response_500 import ListExtensionsResponse500
from ...models.ui_mount_point_type import UIMountPointType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    mount_point_type: UIMountPointType | Unset = UNSET,
    project_id: list[str] | Unset = UNSET,
    is_deleted: bool | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_mount_point_type: str | Unset = UNSET
    if not isinstance(mount_point_type, Unset):
        json_mount_point_type = mount_point_type.value

    params["mountPointType"] = json_mount_point_type

    json_project_id: list[str] | Unset = UNSET
    if not isinstance(project_id, Unset):
        json_project_id = project_id

    params["project_id"] = json_project_id

    params["is_deleted"] = is_deleted

    params["enabled"] = enabled

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/extensions/beta/extensions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FailureEnvelopeV1 | ListExtensionsResponse | ListExtensionsResponse500 | None:
    if response.status_code == 200:
        response_200 = ListExtensionsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = ListExtensionsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FailureEnvelopeV1 | ListExtensionsResponse | ListExtensionsResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    mount_point_type: UIMountPointType | Unset = UNSET,
    project_id: list[str] | Unset = UNSET,
    is_deleted: bool | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[FailureEnvelopeV1 | ListExtensionsResponse | ListExtensionsResponse500]:
    """List Extensions

     List Extensions

    Args:
        mount_point_type (UIMountPointType | Unset): The type of mount point for the Extension.
        project_id (list[str] | Unset):
        is_deleted (bool | Unset):
        enabled (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | ListExtensionsResponse | ListExtensionsResponse500]
    """

    kwargs = _get_kwargs(
        mount_point_type=mount_point_type,
        project_id=project_id,
        is_deleted=is_deleted,
        enabled=enabled,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    mount_point_type: UIMountPointType | Unset = UNSET,
    project_id: list[str] | Unset = UNSET,
    is_deleted: bool | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> FailureEnvelopeV1 | ListExtensionsResponse | ListExtensionsResponse500 | None:
    """List Extensions

     List Extensions

    Args:
        mount_point_type (UIMountPointType | Unset): The type of mount point for the Extension.
        project_id (list[str] | Unset):
        is_deleted (bool | Unset):
        enabled (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | ListExtensionsResponse | ListExtensionsResponse500
    """

    return sync_detailed(
        client=client,
        mount_point_type=mount_point_type,
        project_id=project_id,
        is_deleted=is_deleted,
        enabled=enabled,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    mount_point_type: UIMountPointType | Unset = UNSET,
    project_id: list[str] | Unset = UNSET,
    is_deleted: bool | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[FailureEnvelopeV1 | ListExtensionsResponse | ListExtensionsResponse500]:
    """List Extensions

     List Extensions

    Args:
        mount_point_type (UIMountPointType | Unset): The type of mount point for the Extension.
        project_id (list[str] | Unset):
        is_deleted (bool | Unset):
        enabled (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | ListExtensionsResponse | ListExtensionsResponse500]
    """

    kwargs = _get_kwargs(
        mount_point_type=mount_point_type,
        project_id=project_id,
        is_deleted=is_deleted,
        enabled=enabled,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    mount_point_type: UIMountPointType | Unset = UNSET,
    project_id: list[str] | Unset = UNSET,
    is_deleted: bool | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> FailureEnvelopeV1 | ListExtensionsResponse | ListExtensionsResponse500 | None:
    """List Extensions

     List Extensions

    Args:
        mount_point_type (UIMountPointType | Unset): The type of mount point for the Extension.
        project_id (list[str] | Unset):
        is_deleted (bool | Unset):
        enabled (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | ListExtensionsResponse | ListExtensionsResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            mount_point_type=mount_point_type,
            project_id=project_id,
            is_deleted=is_deleted,
            enabled=enabled,
            limit=limit,
            offset=offset,
        )
    ).parsed
