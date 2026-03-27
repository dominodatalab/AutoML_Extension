from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_hardwaretier_api_hardware_tier_envelope import DominoHardwaretierApiHardwareTierEnvelope
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    show_archived: bool | Unset = UNSET,
    user_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["show_archived"] = show_archived

    params["user_id"] = user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/hardwareTier",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoHardwaretierApiHardwareTierEnvelope | None:
    if response.status_code == 200:
        response_200 = DominoHardwaretierApiHardwareTierEnvelope.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoHardwaretierApiHardwareTierEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    show_archived: bool | Unset = UNSET,
    user_id: str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoHardwaretierApiHardwareTierEnvelope]:
    """Get all hardware tiers

    Args:
        show_archived (bool | Unset):
        user_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoHardwaretierApiHardwareTierEnvelope]
    """

    kwargs = _get_kwargs(
        show_archived=show_archived,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    show_archived: bool | Unset = UNSET,
    user_id: str | Unset = UNSET,
) -> DominoApiErrorResponse | DominoHardwaretierApiHardwareTierEnvelope | None:
    """Get all hardware tiers

    Args:
        show_archived (bool | Unset):
        user_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoHardwaretierApiHardwareTierEnvelope
    """

    return sync_detailed(
        client=client,
        show_archived=show_archived,
        user_id=user_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    show_archived: bool | Unset = UNSET,
    user_id: str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoHardwaretierApiHardwareTierEnvelope]:
    """Get all hardware tiers

    Args:
        show_archived (bool | Unset):
        user_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoHardwaretierApiHardwareTierEnvelope]
    """

    kwargs = _get_kwargs(
        show_archived=show_archived,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    show_archived: bool | Unset = UNSET,
    user_id: str | Unset = UNSET,
) -> DominoApiErrorResponse | DominoHardwaretierApiHardwareTierEnvelope | None:
    """Get all hardware tiers

    Args:
        show_archived (bool | Unset):
        user_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoHardwaretierApiHardwareTierEnvelope
    """

    return (
        await asyncio_detailed(
            client=client,
            show_archived=show_archived,
            user_id=user_id,
        )
    ).parsed
