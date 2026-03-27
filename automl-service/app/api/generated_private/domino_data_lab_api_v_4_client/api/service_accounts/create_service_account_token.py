from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_admin_interface_create_service_account_token_request import (
    DominoAdminInterfaceCreateServiceAccountTokenRequest,
)
from ...models.domino_admin_interface_service_account_token_metadata_and_token import (
    DominoAdminInterfaceServiceAccountTokenMetadataAndToken,
)
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...types import Response


def _get_kwargs(
    service_account_idp_id: str,
    *,
    body: DominoAdminInterfaceCreateServiceAccountTokenRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/serviceAccounts/{service_account_idp_id}/tokens".format(
            service_account_idp_id=quote(str(service_account_idp_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | list[DominoAdminInterfaceServiceAccountTokenMetadataAndToken] | None:
    if response.status_code == 201:
        response_201 = []
        _response_201 = response.json()
        for response_201_item_data in _response_201:
            response_201_item = DominoAdminInterfaceServiceAccountTokenMetadataAndToken.from_dict(
                response_201_item_data
            )

            response_201.append(response_201_item)

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
) -> Response[DominoApiErrorResponse | list[DominoAdminInterfaceServiceAccountTokenMetadataAndToken]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_account_idp_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoAdminInterfaceCreateServiceAccountTokenRequest,
) -> Response[DominoApiErrorResponse | list[DominoAdminInterfaceServiceAccountTokenMetadataAndToken]]:
    """Create a service account token

    Args:
        service_account_idp_id (str):
        body (DominoAdminInterfaceCreateServiceAccountTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoAdminInterfaceServiceAccountTokenMetadataAndToken]]
    """

    kwargs = _get_kwargs(
        service_account_idp_id=service_account_idp_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_account_idp_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoAdminInterfaceCreateServiceAccountTokenRequest,
) -> DominoApiErrorResponse | list[DominoAdminInterfaceServiceAccountTokenMetadataAndToken] | None:
    """Create a service account token

    Args:
        service_account_idp_id (str):
        body (DominoAdminInterfaceCreateServiceAccountTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoAdminInterfaceServiceAccountTokenMetadataAndToken]
    """

    return sync_detailed(
        service_account_idp_id=service_account_idp_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    service_account_idp_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoAdminInterfaceCreateServiceAccountTokenRequest,
) -> Response[DominoApiErrorResponse | list[DominoAdminInterfaceServiceAccountTokenMetadataAndToken]]:
    """Create a service account token

    Args:
        service_account_idp_id (str):
        body (DominoAdminInterfaceCreateServiceAccountTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoAdminInterfaceServiceAccountTokenMetadataAndToken]]
    """

    kwargs = _get_kwargs(
        service_account_idp_id=service_account_idp_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_account_idp_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoAdminInterfaceCreateServiceAccountTokenRequest,
) -> DominoApiErrorResponse | list[DominoAdminInterfaceServiceAccountTokenMetadataAndToken] | None:
    """Create a service account token

    Args:
        service_account_idp_id (str):
        body (DominoAdminInterfaceCreateServiceAccountTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoAdminInterfaceServiceAccountTokenMetadataAndToken]
    """

    return (
        await asyncio_detailed(
            service_account_idp_id=service_account_idp_id,
            client=client,
            body=body,
        )
    ).parsed
