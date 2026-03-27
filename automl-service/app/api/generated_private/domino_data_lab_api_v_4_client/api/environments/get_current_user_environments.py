from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_environments_api_environment_details import DominoEnvironmentsApiEnvironmentDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    is_restricted: bool | None | Unset = UNSET,
    get_only_active_revisions: bool | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_is_restricted: bool | None | Unset
    if isinstance(is_restricted, Unset):
        json_is_restricted = UNSET
    else:
        json_is_restricted = is_restricted
    params["isRestricted"] = json_is_restricted

    json_get_only_active_revisions: bool | None | Unset
    if isinstance(get_only_active_revisions, Unset):
        json_get_only_active_revisions = UNSET
    else:
        json_get_only_active_revisions = get_only_active_revisions
    params["getOnlyActiveRevisions"] = json_get_only_active_revisions

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/environments/self",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | list[DominoEnvironmentsApiEnvironmentDetails] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DominoEnvironmentsApiEnvironmentDetails.from_dict(response_200_item_data)

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
) -> Response[DominoApiErrorResponse | list[DominoEnvironmentsApiEnvironmentDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    is_restricted: bool | None | Unset = UNSET,
    get_only_active_revisions: bool | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoEnvironmentsApiEnvironmentDetails]]:
    """retrieves the current user's Environments

    Args:
        is_restricted (bool | None | Unset):
        get_only_active_revisions (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoEnvironmentsApiEnvironmentDetails]]
    """

    kwargs = _get_kwargs(
        is_restricted=is_restricted,
        get_only_active_revisions=get_only_active_revisions,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    is_restricted: bool | None | Unset = UNSET,
    get_only_active_revisions: bool | None | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoEnvironmentsApiEnvironmentDetails] | None:
    """retrieves the current user's Environments

    Args:
        is_restricted (bool | None | Unset):
        get_only_active_revisions (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoEnvironmentsApiEnvironmentDetails]
    """

    return sync_detailed(
        client=client,
        is_restricted=is_restricted,
        get_only_active_revisions=get_only_active_revisions,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    is_restricted: bool | None | Unset = UNSET,
    get_only_active_revisions: bool | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoEnvironmentsApiEnvironmentDetails]]:
    """retrieves the current user's Environments

    Args:
        is_restricted (bool | None | Unset):
        get_only_active_revisions (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoEnvironmentsApiEnvironmentDetails]]
    """

    kwargs = _get_kwargs(
        is_restricted=is_restricted,
        get_only_active_revisions=get_only_active_revisions,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    is_restricted: bool | None | Unset = UNSET,
    get_only_active_revisions: bool | None | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoEnvironmentsApiEnvironmentDetails] | None:
    """retrieves the current user's Environments

    Args:
        is_restricted (bool | None | Unset):
        get_only_active_revisions (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoEnvironmentsApiEnvironmentDetails]
    """

    return (
        await asyncio_detailed(
            client=client,
            is_restricted=is_restricted,
            get_only_active_revisions=get_only_active_revisions,
        )
    ).parsed
