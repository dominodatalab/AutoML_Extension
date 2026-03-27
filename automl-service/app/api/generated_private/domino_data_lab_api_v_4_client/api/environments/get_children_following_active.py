from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_environments_api_environment_overview_page import DominoEnvironmentsApiEnvironmentOverviewPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    environment_id: str,
    *,
    offset: int | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_offset: int | None | Unset
    if isinstance(offset, Unset):
        json_offset = UNSET
    else:
        json_offset = offset
    params["offset"] = json_offset

    json_limit: int | None | Unset
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["limit"] = json_limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/environments/{environment_id}/childrenFollowingActive".format(
            environment_id=quote(str(environment_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentOverviewPage | None:
    if response.status_code == 200:
        response_200 = DominoEnvironmentsApiEnvironmentOverviewPage.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentOverviewPage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    environment_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentOverviewPage]:
    """Get all children Environemnts that will get rebuilt if the active revision changes

    Args:
        environment_id (str):
        offset (int | None | Unset):
        limit (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentOverviewPage]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
) -> DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentOverviewPage | None:
    """Get all children Environemnts that will get rebuilt if the active revision changes

    Args:
        environment_id (str):
        offset (int | None | Unset):
        limit (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentOverviewPage
    """

    return sync_detailed(
        environment_id=environment_id,
        client=client,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentOverviewPage]:
    """Get all children Environemnts that will get rebuilt if the active revision changes

    Args:
        environment_id (str):
        offset (int | None | Unset):
        limit (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentOverviewPage]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
) -> DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentOverviewPage | None:
    """Get all children Environemnts that will get rebuilt if the active revision changes

    Args:
        environment_id (str):
        offset (int | None | Unset):
        limit (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentOverviewPage
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            client=client,
            offset=offset,
            limit=limit,
        )
    ).parsed
