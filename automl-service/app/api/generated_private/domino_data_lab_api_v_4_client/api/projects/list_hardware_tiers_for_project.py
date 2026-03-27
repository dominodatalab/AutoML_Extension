from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_hardwaretier_api_hardware_tier_with_capacity_dto import (
    DominoHardwaretierApiHardwareTierWithCapacityDto,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    show_archived: bool | None | Unset = UNSET,
    for_model_api: bool | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_show_archived: bool | None | Unset
    if isinstance(show_archived, Unset):
        json_show_archived = UNSET
    else:
        json_show_archived = show_archived
    params["showArchived"] = json_show_archived

    json_for_model_api: bool | None | Unset
    if isinstance(for_model_api, Unset):
        json_for_model_api = UNSET
    else:
        json_for_model_api = for_model_api
    params["forModelApi"] = json_for_model_api

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/hardwareTiers".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | list[DominoHardwaretierApiHardwareTierWithCapacityDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DominoHardwaretierApiHardwareTierWithCapacityDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

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
) -> Response[DominoApiErrorResponse | list[DominoHardwaretierApiHardwareTierWithCapacityDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    show_archived: bool | None | Unset = UNSET,
    for_model_api: bool | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoHardwaretierApiHardwareTierWithCapacityDto]]:
    """retrieves the Hardware Tiers accessible for a Project

    Args:
        project_id (str):
        show_archived (bool | None | Unset):
        for_model_api (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoHardwaretierApiHardwareTierWithCapacityDto]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        show_archived=show_archived,
        for_model_api=for_model_api,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    show_archived: bool | None | Unset = UNSET,
    for_model_api: bool | None | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoHardwaretierApiHardwareTierWithCapacityDto] | None:
    """retrieves the Hardware Tiers accessible for a Project

    Args:
        project_id (str):
        show_archived (bool | None | Unset):
        for_model_api (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoHardwaretierApiHardwareTierWithCapacityDto]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        show_archived=show_archived,
        for_model_api=for_model_api,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    show_archived: bool | None | Unset = UNSET,
    for_model_api: bool | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoHardwaretierApiHardwareTierWithCapacityDto]]:
    """retrieves the Hardware Tiers accessible for a Project

    Args:
        project_id (str):
        show_archived (bool | None | Unset):
        for_model_api (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoHardwaretierApiHardwareTierWithCapacityDto]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        show_archived=show_archived,
        for_model_api=for_model_api,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    show_archived: bool | None | Unset = UNSET,
    for_model_api: bool | None | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoHardwaretierApiHardwareTierWithCapacityDto] | None:
    """retrieves the Hardware Tiers accessible for a Project

    Args:
        project_id (str):
        show_archived (bool | None | Unset):
        for_model_api (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoHardwaretierApiHardwareTierWithCapacityDto]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            show_archived=show_archived,
            for_model_api=for_model_api,
        )
    ).parsed
