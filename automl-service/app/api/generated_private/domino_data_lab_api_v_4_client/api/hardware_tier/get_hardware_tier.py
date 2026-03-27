from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_hardwaretier_api_hardware_tier_dto import DominoHardwaretierApiHardwareTierDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    hardware_tier_id: str,
    *,
    project_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["projectId"] = project_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/hardwareTier/{hardware_tier_id}".format(
            hardware_tier_id=quote(str(hardware_tier_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoHardwaretierApiHardwareTierDto | None:
    if response.status_code == 200:
        response_200 = DominoHardwaretierApiHardwareTierDto.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoHardwaretierApiHardwareTierDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    hardware_tier_id: str,
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoHardwaretierApiHardwareTierDto]:
    """Get a hardware tier

    Args:
        hardware_tier_id (str):
        project_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoHardwaretierApiHardwareTierDto]
    """

    kwargs = _get_kwargs(
        hardware_tier_id=hardware_tier_id,
        project_id=project_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    hardware_tier_id: str,
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = UNSET,
) -> DominoApiErrorResponse | DominoHardwaretierApiHardwareTierDto | None:
    """Get a hardware tier

    Args:
        hardware_tier_id (str):
        project_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoHardwaretierApiHardwareTierDto
    """

    return sync_detailed(
        hardware_tier_id=hardware_tier_id,
        client=client,
        project_id=project_id,
    ).parsed


async def asyncio_detailed(
    hardware_tier_id: str,
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoHardwaretierApiHardwareTierDto]:
    """Get a hardware tier

    Args:
        hardware_tier_id (str):
        project_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoHardwaretierApiHardwareTierDto]
    """

    kwargs = _get_kwargs(
        hardware_tier_id=hardware_tier_id,
        project_id=project_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    hardware_tier_id: str,
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = UNSET,
) -> DominoApiErrorResponse | DominoHardwaretierApiHardwareTierDto | None:
    """Get a hardware tier

    Args:
        hardware_tier_id (str):
        project_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoHardwaretierApiHardwareTierDto
    """

    return (
        await asyncio_detailed(
            hardware_tier_id=hardware_tier_id,
            client=client,
            project_id=project_id,
        )
    ).parsed
