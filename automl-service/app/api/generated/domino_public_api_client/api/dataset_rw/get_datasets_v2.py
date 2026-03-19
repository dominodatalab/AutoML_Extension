from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataset_rw_permission_v1 import DatasetRwPermissionV1
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_datasets_v2_response_400 import GetDatasetsV2Response400
from ...models.get_datasets_v2_response_404 import GetDatasetsV2Response404
from ...models.get_datasets_v2_response_500 import GetDatasetsV2Response500
from ...models.paginated_dataset_rw_envelope_v2 import PaginatedDatasetRwEnvelopeV2
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    minimum_permission: DatasetRwPermissionV1 | Unset = UNSET,
    project_ids_to_exclude: list[str] | Unset = UNSET,
    project_ids_to_include: list[str] | Unset = UNSET,
    include_project_info: bool | Unset = UNSET,
    include_archived_projects: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_minimum_permission: str | Unset = UNSET
    if not isinstance(minimum_permission, Unset):
        json_minimum_permission = minimum_permission.value

    params["minimumPermission"] = json_minimum_permission

    json_project_ids_to_exclude: list[str] | Unset = UNSET
    if not isinstance(project_ids_to_exclude, Unset):
        json_project_ids_to_exclude = project_ids_to_exclude

    params["projectIdsToExclude"] = json_project_ids_to_exclude

    json_project_ids_to_include: list[str] | Unset = UNSET
    if not isinstance(project_ids_to_include, Unset):
        json_project_ids_to_include = project_ids_to_include

    params["projectIdsToInclude"] = json_project_ids_to_include

    params["includeProjectInfo"] = include_project_info

    params["includeArchivedProjects"] = include_archived_projects

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/datasetrw/v2/datasets",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GetDatasetsV2Response400
    | GetDatasetsV2Response404
    | GetDatasetsV2Response500
    | PaginatedDatasetRwEnvelopeV2
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedDatasetRwEnvelopeV2.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetDatasetsV2Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetDatasetsV2Response404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetDatasetsV2Response500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | GetDatasetsV2Response400
    | GetDatasetsV2Response404
    | GetDatasetsV2Response500
    | PaginatedDatasetRwEnvelopeV2
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    minimum_permission: DatasetRwPermissionV1 | Unset = UNSET,
    project_ids_to_exclude: list[str] | Unset = UNSET,
    project_ids_to_include: list[str] | Unset = UNSET,
    include_project_info: bool | Unset = UNSET,
    include_archived_projects: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1
    | GetDatasetsV2Response400
    | GetDatasetsV2Response404
    | GetDatasetsV2Response500
    | PaginatedDatasetRwEnvelopeV2
]:
    """Get datasets the user has access to

     Get Datasets that a user has access to based on dataset permissions and input filters

    Args:
        minimum_permission (DatasetRwPermissionV1 | Unset): Permission within a dataset
        project_ids_to_exclude (list[str] | Unset):
        project_ids_to_include (list[str] | Unset):
        include_project_info (bool | Unset):
        include_archived_projects (bool | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetDatasetsV2Response400 | GetDatasetsV2Response404 | GetDatasetsV2Response500 | PaginatedDatasetRwEnvelopeV2]
    """

    kwargs = _get_kwargs(
        minimum_permission=minimum_permission,
        project_ids_to_exclude=project_ids_to_exclude,
        project_ids_to_include=project_ids_to_include,
        include_project_info=include_project_info,
        include_archived_projects=include_archived_projects,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    minimum_permission: DatasetRwPermissionV1 | Unset = UNSET,
    project_ids_to_exclude: list[str] | Unset = UNSET,
    project_ids_to_include: list[str] | Unset = UNSET,
    include_project_info: bool | Unset = UNSET,
    include_archived_projects: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> (
    FailureEnvelopeV1
    | GetDatasetsV2Response400
    | GetDatasetsV2Response404
    | GetDatasetsV2Response500
    | PaginatedDatasetRwEnvelopeV2
    | None
):
    """Get datasets the user has access to

     Get Datasets that a user has access to based on dataset permissions and input filters

    Args:
        minimum_permission (DatasetRwPermissionV1 | Unset): Permission within a dataset
        project_ids_to_exclude (list[str] | Unset):
        project_ids_to_include (list[str] | Unset):
        include_project_info (bool | Unset):
        include_archived_projects (bool | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetDatasetsV2Response400 | GetDatasetsV2Response404 | GetDatasetsV2Response500 | PaginatedDatasetRwEnvelopeV2
    """

    return sync_detailed(
        client=client,
        minimum_permission=minimum_permission,
        project_ids_to_exclude=project_ids_to_exclude,
        project_ids_to_include=project_ids_to_include,
        include_project_info=include_project_info,
        include_archived_projects=include_archived_projects,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    minimum_permission: DatasetRwPermissionV1 | Unset = UNSET,
    project_ids_to_exclude: list[str] | Unset = UNSET,
    project_ids_to_include: list[str] | Unset = UNSET,
    include_project_info: bool | Unset = UNSET,
    include_archived_projects: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1
    | GetDatasetsV2Response400
    | GetDatasetsV2Response404
    | GetDatasetsV2Response500
    | PaginatedDatasetRwEnvelopeV2
]:
    """Get datasets the user has access to

     Get Datasets that a user has access to based on dataset permissions and input filters

    Args:
        minimum_permission (DatasetRwPermissionV1 | Unset): Permission within a dataset
        project_ids_to_exclude (list[str] | Unset):
        project_ids_to_include (list[str] | Unset):
        include_project_info (bool | Unset):
        include_archived_projects (bool | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetDatasetsV2Response400 | GetDatasetsV2Response404 | GetDatasetsV2Response500 | PaginatedDatasetRwEnvelopeV2]
    """

    kwargs = _get_kwargs(
        minimum_permission=minimum_permission,
        project_ids_to_exclude=project_ids_to_exclude,
        project_ids_to_include=project_ids_to_include,
        include_project_info=include_project_info,
        include_archived_projects=include_archived_projects,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    minimum_permission: DatasetRwPermissionV1 | Unset = UNSET,
    project_ids_to_exclude: list[str] | Unset = UNSET,
    project_ids_to_include: list[str] | Unset = UNSET,
    include_project_info: bool | Unset = UNSET,
    include_archived_projects: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> (
    FailureEnvelopeV1
    | GetDatasetsV2Response400
    | GetDatasetsV2Response404
    | GetDatasetsV2Response500
    | PaginatedDatasetRwEnvelopeV2
    | None
):
    """Get datasets the user has access to

     Get Datasets that a user has access to based on dataset permissions and input filters

    Args:
        minimum_permission (DatasetRwPermissionV1 | Unset): Permission within a dataset
        project_ids_to_exclude (list[str] | Unset):
        project_ids_to_include (list[str] | Unset):
        include_project_info (bool | Unset):
        include_archived_projects (bool | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetDatasetsV2Response400 | GetDatasetsV2Response404 | GetDatasetsV2Response500 | PaginatedDatasetRwEnvelopeV2
    """

    return (
        await asyncio_detailed(
            client=client,
            minimum_permission=minimum_permission,
            project_ids_to_exclude=project_ids_to_exclude,
            project_ids_to_include=project_ids_to_include,
            include_project_info=include_project_info,
            include_archived_projects=include_archived_projects,
            offset=offset,
            limit=limit,
        )
    ).parsed
