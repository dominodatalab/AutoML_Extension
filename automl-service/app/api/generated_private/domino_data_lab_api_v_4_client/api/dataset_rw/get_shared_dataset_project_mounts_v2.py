from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_datasetrw_api_dataset_rw_project_mount_dto import DominoDatasetrwApiDatasetRwProjectMountDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    minimum_permission: None | str | Unset = UNSET,
    data_plane_id: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_minimum_permission: None | str | Unset
    if isinstance(minimum_permission, Unset):
        json_minimum_permission = UNSET
    else:
        json_minimum_permission = minimum_permission
    params["minimumPermission"] = json_minimum_permission

    json_data_plane_id: list[str] | Unset = UNSET
    if not isinstance(data_plane_id, Unset):
        json_data_plane_id = data_plane_id

    params["dataPlaneId"] = json_data_plane_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/datasetrw/mounts-v2/{project_id}/shared".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | list[DominoDatasetrwApiDatasetRwProjectMountDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DominoDatasetrwApiDatasetRwProjectMountDto.from_dict(response_200_item_data)

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
) -> Response[DominoApiErrorResponse | list[DominoDatasetrwApiDatasetRwProjectMountDto]]:
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
    minimum_permission: None | str | Unset = UNSET,
    data_plane_id: list[str] | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoDatasetrwApiDatasetRwProjectMountDto]]:
    """Get shared mounts in a project

    Args:
        project_id (str):
        minimum_permission (None | str | Unset):
        data_plane_id (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoDatasetrwApiDatasetRwProjectMountDto]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        minimum_permission=minimum_permission,
        data_plane_id=data_plane_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    minimum_permission: None | str | Unset = UNSET,
    data_plane_id: list[str] | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoDatasetrwApiDatasetRwProjectMountDto] | None:
    """Get shared mounts in a project

    Args:
        project_id (str):
        minimum_permission (None | str | Unset):
        data_plane_id (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoDatasetrwApiDatasetRwProjectMountDto]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        minimum_permission=minimum_permission,
        data_plane_id=data_plane_id,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    minimum_permission: None | str | Unset = UNSET,
    data_plane_id: list[str] | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoDatasetrwApiDatasetRwProjectMountDto]]:
    """Get shared mounts in a project

    Args:
        project_id (str):
        minimum_permission (None | str | Unset):
        data_plane_id (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoDatasetrwApiDatasetRwProjectMountDto]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        minimum_permission=minimum_permission,
        data_plane_id=data_plane_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    minimum_permission: None | str | Unset = UNSET,
    data_plane_id: list[str] | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoDatasetrwApiDatasetRwProjectMountDto] | None:
    """Get shared mounts in a project

    Args:
        project_id (str):
        minimum_permission (None | str | Unset):
        data_plane_id (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoDatasetrwApiDatasetRwProjectMountDto]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            minimum_permission=minimum_permission,
            data_plane_id=data_plane_id,
        )
    ).parsed
