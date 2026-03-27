from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_datasetrw_api_dataset_rw_storage_dto import DominoDatasetrwApiDatasetRwStorageDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    dataset_storage_ids: list[str] | None | Unset = UNSET,
    data_plane_ids: list[str] | None | Unset = UNSET,
    names: list[str] | None | Unset = UNSET,
    is_registered: bool | None | Unset = UNSET,
    include_number_of_active_datasets: bool | None | Unset = UNSET,
    include_hardware_tiers: bool | None | Unset = UNSET,
    include_hostname: bool | None | Unset = UNSET,
    include_mount_info: bool | None | Unset = UNSET,
    include_readiness_info: bool | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_dataset_storage_ids: list[str] | None | Unset
    if isinstance(dataset_storage_ids, Unset):
        json_dataset_storage_ids = UNSET
    elif isinstance(dataset_storage_ids, list):
        json_dataset_storage_ids = dataset_storage_ids

    else:
        json_dataset_storage_ids = dataset_storage_ids
    params["datasetStorageIds"] = json_dataset_storage_ids

    json_data_plane_ids: list[str] | None | Unset
    if isinstance(data_plane_ids, Unset):
        json_data_plane_ids = UNSET
    elif isinstance(data_plane_ids, list):
        json_data_plane_ids = data_plane_ids

    else:
        json_data_plane_ids = data_plane_ids
    params["dataPlaneIds"] = json_data_plane_ids

    json_names: list[str] | None | Unset
    if isinstance(names, Unset):
        json_names = UNSET
    elif isinstance(names, list):
        json_names = names

    else:
        json_names = names
    params["names"] = json_names

    json_is_registered: bool | None | Unset
    if isinstance(is_registered, Unset):
        json_is_registered = UNSET
    else:
        json_is_registered = is_registered
    params["isRegistered"] = json_is_registered

    json_include_number_of_active_datasets: bool | None | Unset
    if isinstance(include_number_of_active_datasets, Unset):
        json_include_number_of_active_datasets = UNSET
    else:
        json_include_number_of_active_datasets = include_number_of_active_datasets
    params["includeNumberOfActiveDatasets"] = json_include_number_of_active_datasets

    json_include_hardware_tiers: bool | None | Unset
    if isinstance(include_hardware_tiers, Unset):
        json_include_hardware_tiers = UNSET
    else:
        json_include_hardware_tiers = include_hardware_tiers
    params["includeHardwareTiers"] = json_include_hardware_tiers

    json_include_hostname: bool | None | Unset
    if isinstance(include_hostname, Unset):
        json_include_hostname = UNSET
    else:
        json_include_hostname = include_hostname
    params["includeHostname"] = json_include_hostname

    json_include_mount_info: bool | None | Unset
    if isinstance(include_mount_info, Unset):
        json_include_mount_info = UNSET
    else:
        json_include_mount_info = include_mount_info
    params["includeMountInfo"] = json_include_mount_info

    json_include_readiness_info: bool | None | Unset
    if isinstance(include_readiness_info, Unset):
        json_include_readiness_info = UNSET
    else:
        json_include_readiness_info = include_readiness_info
    params["includeReadinessInfo"] = json_include_readiness_info

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/datasetrw/storage",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | list[DominoDatasetrwApiDatasetRwStorageDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DominoDatasetrwApiDatasetRwStorageDto.from_dict(response_200_item_data)

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
) -> Response[DominoApiErrorResponse | list[DominoDatasetrwApiDatasetRwStorageDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    dataset_storage_ids: list[str] | None | Unset = UNSET,
    data_plane_ids: list[str] | None | Unset = UNSET,
    names: list[str] | None | Unset = UNSET,
    is_registered: bool | None | Unset = UNSET,
    include_number_of_active_datasets: bool | None | Unset = UNSET,
    include_hardware_tiers: bool | None | Unset = UNSET,
    include_hostname: bool | None | Unset = UNSET,
    include_mount_info: bool | None | Unset = UNSET,
    include_readiness_info: bool | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoDatasetrwApiDatasetRwStorageDto]]:
    """Get DatasetRwStorages by IDs

    Args:
        dataset_storage_ids (list[str] | None | Unset):
        data_plane_ids (list[str] | None | Unset):
        names (list[str] | None | Unset):
        is_registered (bool | None | Unset):
        include_number_of_active_datasets (bool | None | Unset):
        include_hardware_tiers (bool | None | Unset):
        include_hostname (bool | None | Unset):
        include_mount_info (bool | None | Unset):
        include_readiness_info (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoDatasetrwApiDatasetRwStorageDto]]
    """

    kwargs = _get_kwargs(
        dataset_storage_ids=dataset_storage_ids,
        data_plane_ids=data_plane_ids,
        names=names,
        is_registered=is_registered,
        include_number_of_active_datasets=include_number_of_active_datasets,
        include_hardware_tiers=include_hardware_tiers,
        include_hostname=include_hostname,
        include_mount_info=include_mount_info,
        include_readiness_info=include_readiness_info,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    dataset_storage_ids: list[str] | None | Unset = UNSET,
    data_plane_ids: list[str] | None | Unset = UNSET,
    names: list[str] | None | Unset = UNSET,
    is_registered: bool | None | Unset = UNSET,
    include_number_of_active_datasets: bool | None | Unset = UNSET,
    include_hardware_tiers: bool | None | Unset = UNSET,
    include_hostname: bool | None | Unset = UNSET,
    include_mount_info: bool | None | Unset = UNSET,
    include_readiness_info: bool | None | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoDatasetrwApiDatasetRwStorageDto] | None:
    """Get DatasetRwStorages by IDs

    Args:
        dataset_storage_ids (list[str] | None | Unset):
        data_plane_ids (list[str] | None | Unset):
        names (list[str] | None | Unset):
        is_registered (bool | None | Unset):
        include_number_of_active_datasets (bool | None | Unset):
        include_hardware_tiers (bool | None | Unset):
        include_hostname (bool | None | Unset):
        include_mount_info (bool | None | Unset):
        include_readiness_info (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoDatasetrwApiDatasetRwStorageDto]
    """

    return sync_detailed(
        client=client,
        dataset_storage_ids=dataset_storage_ids,
        data_plane_ids=data_plane_ids,
        names=names,
        is_registered=is_registered,
        include_number_of_active_datasets=include_number_of_active_datasets,
        include_hardware_tiers=include_hardware_tiers,
        include_hostname=include_hostname,
        include_mount_info=include_mount_info,
        include_readiness_info=include_readiness_info,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    dataset_storage_ids: list[str] | None | Unset = UNSET,
    data_plane_ids: list[str] | None | Unset = UNSET,
    names: list[str] | None | Unset = UNSET,
    is_registered: bool | None | Unset = UNSET,
    include_number_of_active_datasets: bool | None | Unset = UNSET,
    include_hardware_tiers: bool | None | Unset = UNSET,
    include_hostname: bool | None | Unset = UNSET,
    include_mount_info: bool | None | Unset = UNSET,
    include_readiness_info: bool | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoDatasetrwApiDatasetRwStorageDto]]:
    """Get DatasetRwStorages by IDs

    Args:
        dataset_storage_ids (list[str] | None | Unset):
        data_plane_ids (list[str] | None | Unset):
        names (list[str] | None | Unset):
        is_registered (bool | None | Unset):
        include_number_of_active_datasets (bool | None | Unset):
        include_hardware_tiers (bool | None | Unset):
        include_hostname (bool | None | Unset):
        include_mount_info (bool | None | Unset):
        include_readiness_info (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoDatasetrwApiDatasetRwStorageDto]]
    """

    kwargs = _get_kwargs(
        dataset_storage_ids=dataset_storage_ids,
        data_plane_ids=data_plane_ids,
        names=names,
        is_registered=is_registered,
        include_number_of_active_datasets=include_number_of_active_datasets,
        include_hardware_tiers=include_hardware_tiers,
        include_hostname=include_hostname,
        include_mount_info=include_mount_info,
        include_readiness_info=include_readiness_info,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    dataset_storage_ids: list[str] | None | Unset = UNSET,
    data_plane_ids: list[str] | None | Unset = UNSET,
    names: list[str] | None | Unset = UNSET,
    is_registered: bool | None | Unset = UNSET,
    include_number_of_active_datasets: bool | None | Unset = UNSET,
    include_hardware_tiers: bool | None | Unset = UNSET,
    include_hostname: bool | None | Unset = UNSET,
    include_mount_info: bool | None | Unset = UNSET,
    include_readiness_info: bool | None | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoDatasetrwApiDatasetRwStorageDto] | None:
    """Get DatasetRwStorages by IDs

    Args:
        dataset_storage_ids (list[str] | None | Unset):
        data_plane_ids (list[str] | None | Unset):
        names (list[str] | None | Unset):
        is_registered (bool | None | Unset):
        include_number_of_active_datasets (bool | None | Unset):
        include_hardware_tiers (bool | None | Unset):
        include_hostname (bool | None | Unset):
        include_mount_info (bool | None | Unset):
        include_readiness_info (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoDatasetrwApiDatasetRwStorageDto]
    """

    return (
        await asyncio_detailed(
            client=client,
            dataset_storage_ids=dataset_storage_ids,
            data_plane_ids=data_plane_ids,
            names=names,
            is_registered=is_registered,
            include_number_of_active_datasets=include_number_of_active_datasets,
            include_hardware_tiers=include_hardware_tiers,
            include_hostname=include_hostname,
            include_mount_info=include_mount_info,
            include_readiness_info=include_readiness_info,
        )
    ).parsed
