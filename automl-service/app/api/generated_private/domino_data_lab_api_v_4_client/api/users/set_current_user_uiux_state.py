from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_common_user_update_user_uiux_state_dto import DominoCommonUserUpdateUserUIUXStateDTO
from ...models.domino_common_user_user_uiux_state_dto import DominoCommonUserUserUIUXStateDTO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: DominoCommonUserUpdateUserUIUXStateDTO,
    x_domino_api_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_domino_api_key, Unset):
        headers["X-Domino-Api-Key"] = x_domino_api_key

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/users/uiuxState",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoCommonUserUserUIUXStateDTO | None:
    if response.status_code == 200:
        response_200 = DominoCommonUserUserUIUXStateDTO.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = DominoApiErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DominoApiErrorResponse.from_dict(response.json())

        return response_401

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
) -> Response[DominoApiErrorResponse | DominoCommonUserUserUIUXStateDTO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DominoCommonUserUpdateUserUIUXStateDTO,
    x_domino_api_key: str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoCommonUserUserUIUXStateDTO]:
    """Set server-stored UI/UX state for the current user

    Args:
        x_domino_api_key (str | Unset):
        body (DominoCommonUserUpdateUserUIUXStateDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoCommonUserUserUIUXStateDTO]
    """

    kwargs = _get_kwargs(
        body=body,
        x_domino_api_key=x_domino_api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: DominoCommonUserUpdateUserUIUXStateDTO,
    x_domino_api_key: str | Unset = UNSET,
) -> DominoApiErrorResponse | DominoCommonUserUserUIUXStateDTO | None:
    """Set server-stored UI/UX state for the current user

    Args:
        x_domino_api_key (str | Unset):
        body (DominoCommonUserUpdateUserUIUXStateDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoCommonUserUserUIUXStateDTO
    """

    return sync_detailed(
        client=client,
        body=body,
        x_domino_api_key=x_domino_api_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DominoCommonUserUpdateUserUIUXStateDTO,
    x_domino_api_key: str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoCommonUserUserUIUXStateDTO]:
    """Set server-stored UI/UX state for the current user

    Args:
        x_domino_api_key (str | Unset):
        body (DominoCommonUserUpdateUserUIUXStateDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoCommonUserUserUIUXStateDTO]
    """

    kwargs = _get_kwargs(
        body=body,
        x_domino_api_key=x_domino_api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DominoCommonUserUpdateUserUIUXStateDTO,
    x_domino_api_key: str | Unset = UNSET,
) -> DominoApiErrorResponse | DominoCommonUserUserUIUXStateDTO | None:
    """Set server-stored UI/UX state for the current user

    Args:
        x_domino_api_key (str | Unset):
        body (DominoCommonUserUpdateUserUIUXStateDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoCommonUserUserUIUXStateDTO
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_domino_api_key=x_domino_api_key,
        )
    ).parsed
