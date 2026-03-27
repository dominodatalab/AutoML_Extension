from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_datasource_api_data_source_dto import DominoDatasourceApiDataSourceDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    data_plane_id: str | Unset = UNSET,
    authenticated_only: bool | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["dataPlaneId"] = data_plane_id

    json_authenticated_only: bool | None | Unset
    if isinstance(authenticated_only, Unset):
        json_authenticated_only = UNSET
    else:
        json_authenticated_only = authenticated_only
    params["authenticatedOnly"] = json_authenticated_only

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/datasource/projects/{project_id}".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | list[DominoDatasourceApiDataSourceDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DominoDatasourceApiDataSourceDto.from_dict(response_200_item_data)

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
) -> Response[DominoApiErrorResponse | list[DominoDatasourceApiDataSourceDto]]:
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
    data_plane_id: str | Unset = UNSET,
    authenticated_only: bool | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoDatasourceApiDataSourceDto]]:
    """Get data sources by project

    Args:
        project_id (str):
        data_plane_id (str | Unset):
        authenticated_only (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoDatasourceApiDataSourceDto]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        data_plane_id=data_plane_id,
        authenticated_only=authenticated_only,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    data_plane_id: str | Unset = UNSET,
    authenticated_only: bool | None | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoDatasourceApiDataSourceDto] | None:
    """Get data sources by project

    Args:
        project_id (str):
        data_plane_id (str | Unset):
        authenticated_only (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoDatasourceApiDataSourceDto]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        data_plane_id=data_plane_id,
        authenticated_only=authenticated_only,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    data_plane_id: str | Unset = UNSET,
    authenticated_only: bool | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoDatasourceApiDataSourceDto]]:
    """Get data sources by project

    Args:
        project_id (str):
        data_plane_id (str | Unset):
        authenticated_only (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoDatasourceApiDataSourceDto]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        data_plane_id=data_plane_id,
        authenticated_only=authenticated_only,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    data_plane_id: str | Unset = UNSET,
    authenticated_only: bool | None | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoDatasourceApiDataSourceDto] | None:
    """Get data sources by project

    Args:
        project_id (str):
        data_plane_id (str | Unset):
        authenticated_only (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoDatasourceApiDataSourceDto]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            data_plane_id=data_plane_id,
            authenticated_only=authenticated_only,
        )
    ).parsed
