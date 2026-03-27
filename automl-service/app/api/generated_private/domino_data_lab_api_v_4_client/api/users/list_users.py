from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_common_user_person import DominoCommonUserPerson
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_id: list[str] | None | Unset = UNSET,
    user_name: None | str | Unset = UNSET,
    query: None | str | Unset = UNSET,
    list_only_users: bool | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_user_id: list[str] | None | Unset
    if isinstance(user_id, Unset):
        json_user_id = UNSET
    elif isinstance(user_id, list):
        json_user_id = user_id

    else:
        json_user_id = user_id
    params["userId"] = json_user_id

    json_user_name: None | str | Unset
    if isinstance(user_name, Unset):
        json_user_name = UNSET
    else:
        json_user_name = user_name
    params["userName"] = json_user_name

    json_query: None | str | Unset
    if isinstance(query, Unset):
        json_query = UNSET
    else:
        json_query = query
    params["query"] = json_query

    json_list_only_users: bool | None | Unset
    if isinstance(list_only_users, Unset):
        json_list_only_users = UNSET
    else:
        json_list_only_users = list_only_users
    params["listOnlyUsers"] = json_list_only_users

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | list[DominoCommonUserPerson] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DominoCommonUserPerson.from_dict(response_200_item_data)

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
) -> Response[DominoApiErrorResponse | list[DominoCommonUserPerson]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    user_id: list[str] | None | Unset = UNSET,
    user_name: None | str | Unset = UNSET,
    query: None | str | Unset = UNSET,
    list_only_users: bool | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoCommonUserPerson]]:
    """retrieves a list of users

    Args:
        user_id (list[str] | None | Unset):
        user_name (None | str | Unset):
        query (None | str | Unset):
        list_only_users (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoCommonUserPerson]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        user_name=user_name,
        query=query,
        list_only_users=list_only_users,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    user_id: list[str] | None | Unset = UNSET,
    user_name: None | str | Unset = UNSET,
    query: None | str | Unset = UNSET,
    list_only_users: bool | None | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoCommonUserPerson] | None:
    """retrieves a list of users

    Args:
        user_id (list[str] | None | Unset):
        user_name (None | str | Unset):
        query (None | str | Unset):
        list_only_users (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoCommonUserPerson]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        user_name=user_name,
        query=query,
        list_only_users=list_only_users,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    user_id: list[str] | None | Unset = UNSET,
    user_name: None | str | Unset = UNSET,
    query: None | str | Unset = UNSET,
    list_only_users: bool | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoCommonUserPerson]]:
    """retrieves a list of users

    Args:
        user_id (list[str] | None | Unset):
        user_name (None | str | Unset):
        query (None | str | Unset):
        list_only_users (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoCommonUserPerson]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        user_name=user_name,
        query=query,
        list_only_users=list_only_users,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    user_id: list[str] | None | Unset = UNSET,
    user_name: None | str | Unset = UNSET,
    query: None | str | Unset = UNSET,
    list_only_users: bool | None | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoCommonUserPerson] | None:
    """retrieves a list of users

    Args:
        user_id (list[str] | None | Unset):
        user_name (None | str | Unset):
        query (None | str | Unset):
        list_only_users (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoCommonUserPerson]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            user_name=user_name,
            query=query,
            list_only_users=list_only_users,
        )
    ).parsed
