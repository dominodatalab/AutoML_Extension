from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_datasetrw_api_dataset_rw_info_dto import DominoDatasetrwApiDatasetRwInfoDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include_project_info: bool | None | Unset = UNSET,
    include_has_project_access: bool | None | Unset = UNSET,
    include_storage_info: bool | None | Unset = UNSET,
    minimum_permission: None | str | Unset = UNSET,
    project_ids_to_exclude: list[str] | None | Unset = UNSET,
    project_ids_to_include: list[str] | None | Unset = UNSET,
    include_archived_projects: bool | None | Unset = UNSET,
    dataset_ids: list[str] | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_include_project_info: bool | None | Unset
    if isinstance(include_project_info, Unset):
        json_include_project_info = UNSET
    else:
        json_include_project_info = include_project_info
    params["includeProjectInfo"] = json_include_project_info

    json_include_has_project_access: bool | None | Unset
    if isinstance(include_has_project_access, Unset):
        json_include_has_project_access = UNSET
    else:
        json_include_has_project_access = include_has_project_access
    params["includeHasProjectAccess"] = json_include_has_project_access

    json_include_storage_info: bool | None | Unset
    if isinstance(include_storage_info, Unset):
        json_include_storage_info = UNSET
    else:
        json_include_storage_info = include_storage_info
    params["includeStorageInfo"] = json_include_storage_info

    json_minimum_permission: None | str | Unset
    if isinstance(minimum_permission, Unset):
        json_minimum_permission = UNSET
    else:
        json_minimum_permission = minimum_permission
    params["minimumPermission"] = json_minimum_permission

    json_project_ids_to_exclude: list[str] | None | Unset
    if isinstance(project_ids_to_exclude, Unset):
        json_project_ids_to_exclude = UNSET
    elif isinstance(project_ids_to_exclude, list):
        json_project_ids_to_exclude = project_ids_to_exclude

    else:
        json_project_ids_to_exclude = project_ids_to_exclude
    params["projectIdsToExclude"] = json_project_ids_to_exclude

    json_project_ids_to_include: list[str] | None | Unset
    if isinstance(project_ids_to_include, Unset):
        json_project_ids_to_include = UNSET
    elif isinstance(project_ids_to_include, list):
        json_project_ids_to_include = project_ids_to_include

    else:
        json_project_ids_to_include = project_ids_to_include
    params["projectIdsToInclude"] = json_project_ids_to_include

    json_include_archived_projects: bool | None | Unset
    if isinstance(include_archived_projects, Unset):
        json_include_archived_projects = UNSET
    else:
        json_include_archived_projects = include_archived_projects
    params["includeArchivedProjects"] = json_include_archived_projects

    json_dataset_ids: list[str] | None | Unset
    if isinstance(dataset_ids, Unset):
        json_dataset_ids = UNSET
    elif isinstance(dataset_ids, list):
        json_dataset_ids = dataset_ids

    else:
        json_dataset_ids = dataset_ids
    params["datasetIds"] = json_dataset_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/datasetrw/datasets-v2",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | list[DominoDatasetrwApiDatasetRwInfoDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DominoDatasetrwApiDatasetRwInfoDto.from_dict(response_200_item_data)

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
) -> Response[DominoApiErrorResponse | list[DominoDatasetrwApiDatasetRwInfoDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    include_project_info: bool | None | Unset = UNSET,
    include_has_project_access: bool | None | Unset = UNSET,
    include_storage_info: bool | None | Unset = UNSET,
    minimum_permission: None | str | Unset = UNSET,
    project_ids_to_exclude: list[str] | None | Unset = UNSET,
    project_ids_to_include: list[str] | None | Unset = UNSET,
    include_archived_projects: bool | None | Unset = UNSET,
    dataset_ids: list[str] | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoDatasetrwApiDatasetRwInfoDto]]:
    """Get Datasets

    Args:
        include_project_info (bool | None | Unset):
        include_has_project_access (bool | None | Unset):
        include_storage_info (bool | None | Unset):
        minimum_permission (None | str | Unset):
        project_ids_to_exclude (list[str] | None | Unset):
        project_ids_to_include (list[str] | None | Unset):
        include_archived_projects (bool | None | Unset):
        dataset_ids (list[str] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoDatasetrwApiDatasetRwInfoDto]]
    """

    kwargs = _get_kwargs(
        include_project_info=include_project_info,
        include_has_project_access=include_has_project_access,
        include_storage_info=include_storage_info,
        minimum_permission=minimum_permission,
        project_ids_to_exclude=project_ids_to_exclude,
        project_ids_to_include=project_ids_to_include,
        include_archived_projects=include_archived_projects,
        dataset_ids=dataset_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    include_project_info: bool | None | Unset = UNSET,
    include_has_project_access: bool | None | Unset = UNSET,
    include_storage_info: bool | None | Unset = UNSET,
    minimum_permission: None | str | Unset = UNSET,
    project_ids_to_exclude: list[str] | None | Unset = UNSET,
    project_ids_to_include: list[str] | None | Unset = UNSET,
    include_archived_projects: bool | None | Unset = UNSET,
    dataset_ids: list[str] | None | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoDatasetrwApiDatasetRwInfoDto] | None:
    """Get Datasets

    Args:
        include_project_info (bool | None | Unset):
        include_has_project_access (bool | None | Unset):
        include_storage_info (bool | None | Unset):
        minimum_permission (None | str | Unset):
        project_ids_to_exclude (list[str] | None | Unset):
        project_ids_to_include (list[str] | None | Unset):
        include_archived_projects (bool | None | Unset):
        dataset_ids (list[str] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoDatasetrwApiDatasetRwInfoDto]
    """

    return sync_detailed(
        client=client,
        include_project_info=include_project_info,
        include_has_project_access=include_has_project_access,
        include_storage_info=include_storage_info,
        minimum_permission=minimum_permission,
        project_ids_to_exclude=project_ids_to_exclude,
        project_ids_to_include=project_ids_to_include,
        include_archived_projects=include_archived_projects,
        dataset_ids=dataset_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    include_project_info: bool | None | Unset = UNSET,
    include_has_project_access: bool | None | Unset = UNSET,
    include_storage_info: bool | None | Unset = UNSET,
    minimum_permission: None | str | Unset = UNSET,
    project_ids_to_exclude: list[str] | None | Unset = UNSET,
    project_ids_to_include: list[str] | None | Unset = UNSET,
    include_archived_projects: bool | None | Unset = UNSET,
    dataset_ids: list[str] | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoDatasetrwApiDatasetRwInfoDto]]:
    """Get Datasets

    Args:
        include_project_info (bool | None | Unset):
        include_has_project_access (bool | None | Unset):
        include_storage_info (bool | None | Unset):
        minimum_permission (None | str | Unset):
        project_ids_to_exclude (list[str] | None | Unset):
        project_ids_to_include (list[str] | None | Unset):
        include_archived_projects (bool | None | Unset):
        dataset_ids (list[str] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoDatasetrwApiDatasetRwInfoDto]]
    """

    kwargs = _get_kwargs(
        include_project_info=include_project_info,
        include_has_project_access=include_has_project_access,
        include_storage_info=include_storage_info,
        minimum_permission=minimum_permission,
        project_ids_to_exclude=project_ids_to_exclude,
        project_ids_to_include=project_ids_to_include,
        include_archived_projects=include_archived_projects,
        dataset_ids=dataset_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    include_project_info: bool | None | Unset = UNSET,
    include_has_project_access: bool | None | Unset = UNSET,
    include_storage_info: bool | None | Unset = UNSET,
    minimum_permission: None | str | Unset = UNSET,
    project_ids_to_exclude: list[str] | None | Unset = UNSET,
    project_ids_to_include: list[str] | None | Unset = UNSET,
    include_archived_projects: bool | None | Unset = UNSET,
    dataset_ids: list[str] | None | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoDatasetrwApiDatasetRwInfoDto] | None:
    """Get Datasets

    Args:
        include_project_info (bool | None | Unset):
        include_has_project_access (bool | None | Unset):
        include_storage_info (bool | None | Unset):
        minimum_permission (None | str | Unset):
        project_ids_to_exclude (list[str] | None | Unset):
        project_ids_to_include (list[str] | None | Unset):
        include_archived_projects (bool | None | Unset):
        dataset_ids (list[str] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoDatasetrwApiDatasetRwInfoDto]
    """

    return (
        await asyncio_detailed(
            client=client,
            include_project_info=include_project_info,
            include_has_project_access=include_has_project_access,
            include_storage_info=include_storage_info,
            minimum_permission=minimum_permission,
            project_ids_to_exclude=project_ids_to_exclude,
            project_ids_to_include=project_ids_to_include,
            include_archived_projects=include_archived_projects,
            dataset_ids=dataset_ids,
        )
    ).parsed
