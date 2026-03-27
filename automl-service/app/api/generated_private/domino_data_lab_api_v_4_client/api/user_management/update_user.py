from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_admin_usermanagement_api_admin_user_management_user import (
    DominoAdminUsermanagementApiAdminUserManagementUser,
)
from ...models.domino_admin_usermanagement_api_update_user_request import DominoAdminUsermanagementApiUpdateUserRequest
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...types import Response


def _get_kwargs(
    target_user_idp_id: str,
    *,
    body: DominoAdminUsermanagementApiUpdateUserRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/admin/user-management/users/{target_user_idp_id}".format(
            target_user_idp_id=quote(str(target_user_idp_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoAdminUsermanagementApiAdminUserManagementUser | DominoApiErrorResponse | None:
    if response.status_code == 200:
        response_200 = DominoAdminUsermanagementApiAdminUserManagementUser.from_dict(response.json())

        return response_200

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
) -> Response[DominoAdminUsermanagementApiAdminUserManagementUser | DominoApiErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    target_user_idp_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoAdminUsermanagementApiUpdateUserRequest,
) -> Response[DominoAdminUsermanagementApiAdminUserManagementUser | DominoApiErrorResponse]:
    """Update a user.

    Args:
        target_user_idp_id (str):
        body (DominoAdminUsermanagementApiUpdateUserRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoAdminUsermanagementApiAdminUserManagementUser | DominoApiErrorResponse]
    """

    kwargs = _get_kwargs(
        target_user_idp_id=target_user_idp_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    target_user_idp_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoAdminUsermanagementApiUpdateUserRequest,
) -> DominoAdminUsermanagementApiAdminUserManagementUser | DominoApiErrorResponse | None:
    """Update a user.

    Args:
        target_user_idp_id (str):
        body (DominoAdminUsermanagementApiUpdateUserRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoAdminUsermanagementApiAdminUserManagementUser | DominoApiErrorResponse
    """

    return sync_detailed(
        target_user_idp_id=target_user_idp_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    target_user_idp_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoAdminUsermanagementApiUpdateUserRequest,
) -> Response[DominoAdminUsermanagementApiAdminUserManagementUser | DominoApiErrorResponse]:
    """Update a user.

    Args:
        target_user_idp_id (str):
        body (DominoAdminUsermanagementApiUpdateUserRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoAdminUsermanagementApiAdminUserManagementUser | DominoApiErrorResponse]
    """

    kwargs = _get_kwargs(
        target_user_idp_id=target_user_idp_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    target_user_idp_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoAdminUsermanagementApiUpdateUserRequest,
) -> DominoAdminUsermanagementApiAdminUserManagementUser | DominoApiErrorResponse | None:
    """Update a user.

    Args:
        target_user_idp_id (str):
        body (DominoAdminUsermanagementApiUpdateUserRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoAdminUsermanagementApiAdminUserManagementUser | DominoApiErrorResponse
    """

    return (
        await asyncio_detailed(
            target_user_idp_id=target_user_idp_id,
            client=client,
            body=body,
        )
    ).parsed
