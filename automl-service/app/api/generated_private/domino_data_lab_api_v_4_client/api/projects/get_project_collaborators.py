from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_common_user_person import DominoCommonUserPerson
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    get_users: bool | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_get_users: bool | None | Unset
    if isinstance(get_users, Unset):
        json_get_users = UNSET
    else:
        json_get_users = get_users
    params["getUsers"] = json_get_users

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/collaborators".format(
            project_id=quote(str(project_id), safe=""),
        ),
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
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    get_users: bool | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoCommonUserPerson]]:
    """Retrieves all of the collaborators in a project

    Args:
        project_id (str):
        get_users (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoCommonUserPerson]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        get_users=get_users,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    get_users: bool | None | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoCommonUserPerson] | None:
    """Retrieves all of the collaborators in a project

    Args:
        project_id (str):
        get_users (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoCommonUserPerson]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        get_users=get_users,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    get_users: bool | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoCommonUserPerson]]:
    """Retrieves all of the collaborators in a project

    Args:
        project_id (str):
        get_users (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoCommonUserPerson]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        get_users=get_users,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    get_users: bool | None | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoCommonUserPerson] | None:
    """Retrieves all of the collaborators in a project

    Args:
        project_id (str):
        get_users (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoCommonUserPerson]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            get_users=get_users,
        )
    ).parsed
