from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_files_interface_project_code_create_edit_dto import DominoFilesInterfaceProjectCodeCreateEditDto
from ...types import UNSET, Response


def _get_kwargs(
    *,
    owner_username: str,
    project_name: str,
    path_string: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["ownerUsername"] = owner_username

    params["projectName"] = project_name

    params["pathString"] = path_string

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/files/createCode",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoFilesInterfaceProjectCodeCreateEditDto | None:
    if response.status_code == 200:
        response_200 = DominoFilesInterfaceProjectCodeCreateEditDto.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoFilesInterfaceProjectCodeCreateEditDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    owner_username: str,
    project_name: str,
    path_string: str,
) -> Response[DominoApiErrorResponse | DominoFilesInterfaceProjectCodeCreateEditDto]:
    """Get values to build FE for create file

    Args:
        owner_username (str):
        project_name (str):
        path_string (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoFilesInterfaceProjectCodeCreateEditDto]
    """

    kwargs = _get_kwargs(
        owner_username=owner_username,
        project_name=project_name,
        path_string=path_string,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    owner_username: str,
    project_name: str,
    path_string: str,
) -> DominoApiErrorResponse | DominoFilesInterfaceProjectCodeCreateEditDto | None:
    """Get values to build FE for create file

    Args:
        owner_username (str):
        project_name (str):
        path_string (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoFilesInterfaceProjectCodeCreateEditDto
    """

    return sync_detailed(
        client=client,
        owner_username=owner_username,
        project_name=project_name,
        path_string=path_string,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    owner_username: str,
    project_name: str,
    path_string: str,
) -> Response[DominoApiErrorResponse | DominoFilesInterfaceProjectCodeCreateEditDto]:
    """Get values to build FE for create file

    Args:
        owner_username (str):
        project_name (str):
        path_string (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoFilesInterfaceProjectCodeCreateEditDto]
    """

    kwargs = _get_kwargs(
        owner_username=owner_username,
        project_name=project_name,
        path_string=path_string,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    owner_username: str,
    project_name: str,
    path_string: str,
) -> DominoApiErrorResponse | DominoFilesInterfaceProjectCodeCreateEditDto | None:
    """Get values to build FE for create file

    Args:
        owner_username (str):
        project_name (str):
        path_string (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoFilesInterfaceProjectCodeCreateEditDto
    """

    return (
        await asyncio_detailed(
            client=client,
            owner_username=owner_username,
            project_name=project_name,
            path_string=path_string,
        )
    ).parsed
