from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_dataplane_data_plane_dto import DominoDataplaneDataPlaneDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    show_archived: bool | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_show_archived: bool | None | Unset
    if isinstance(show_archived, Unset):
        json_show_archived = UNSET
    else:
        json_show_archived = show_archived
    params["showArchived"] = json_show_archived

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dataplanes/dataplanes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | list[DominoDataplaneDataPlaneDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DominoDataplaneDataPlaneDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[DominoApiErrorResponse | list[DominoDataplaneDataPlaneDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    show_archived: bool | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoDataplaneDataPlaneDto]]:
    """List Data Planes

    Args:
        show_archived (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoDataplaneDataPlaneDto]]
    """

    kwargs = _get_kwargs(
        show_archived=show_archived,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    show_archived: bool | None | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoDataplaneDataPlaneDto] | None:
    """List Data Planes

    Args:
        show_archived (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoDataplaneDataPlaneDto]
    """

    return sync_detailed(
        client=client,
        show_archived=show_archived,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    show_archived: bool | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoDataplaneDataPlaneDto]]:
    """List Data Planes

    Args:
        show_archived (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoDataplaneDataPlaneDto]]
    """

    kwargs = _get_kwargs(
        show_archived=show_archived,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    show_archived: bool | None | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoDataplaneDataPlaneDto] | None:
    """List Data Planes

    Args:
        show_archived (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoDataplaneDataPlaneDto]
    """

    return (
        await asyncio_detailed(
            client=client,
            show_archived=show_archived,
        )
    ).parsed
