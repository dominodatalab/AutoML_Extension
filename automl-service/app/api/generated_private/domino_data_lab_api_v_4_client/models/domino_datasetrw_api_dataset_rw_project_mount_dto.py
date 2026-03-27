from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_datasetrw_api_dataset_rw_project_mount_dto_size_status import (
    DominoDatasetrwApiDatasetRwProjectMountDtoSizeStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_dataplane_data_plane_dto import DominoDataplaneDataPlaneDto
    from ..models.domino_datasetrw_api_dataset_rw_storage_info_dto import DominoDatasetrwApiDatasetRwStorageInfoDto


T = TypeVar("T", bound="DominoDatasetrwApiDatasetRwProjectMountDto")


@_attrs_define
class DominoDatasetrwApiDatasetRwProjectMountDto:
    """
    Attributes:
        dataset_id (str):
        snapshot_id (str):
        name (str):
        owner_project_owner_username (str):
        owner_project_name (str):
        is_partial_size (bool):
        available_versions (int):
        mount_paths_for_project (list[str]):
        data_planes (list[DominoDataplaneDataPlaneDto]):
        version_number (int | None | Unset):
        unique_name (None | str | Unset):
        description (None | str | Unset):
        owner_project_id (None | str | Unset):
        storage_size (int | None | Unset):
        owner_usernames (list[str] | None | Unset):
        size_in_bytes (int | None | Unset):
        size_status (DominoDatasetrwApiDatasetRwProjectMountDtoSizeStatus | Unset):
        storage_info (DominoDatasetrwApiDatasetRwStorageInfoDto | Unset):
    """

    dataset_id: str
    snapshot_id: str
    name: str
    owner_project_owner_username: str
    owner_project_name: str
    is_partial_size: bool
    available_versions: int
    mount_paths_for_project: list[str]
    data_planes: list[DominoDataplaneDataPlaneDto]
    version_number: int | None | Unset = UNSET
    unique_name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    owner_project_id: None | str | Unset = UNSET
    storage_size: int | None | Unset = UNSET
    owner_usernames: list[str] | None | Unset = UNSET
    size_in_bytes: int | None | Unset = UNSET
    size_status: DominoDatasetrwApiDatasetRwProjectMountDtoSizeStatus | Unset = UNSET
    storage_info: DominoDatasetrwApiDatasetRwStorageInfoDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataset_id = self.dataset_id

        snapshot_id = self.snapshot_id

        name = self.name

        owner_project_owner_username = self.owner_project_owner_username

        owner_project_name = self.owner_project_name

        is_partial_size = self.is_partial_size

        available_versions = self.available_versions

        mount_paths_for_project = self.mount_paths_for_project

        data_planes = []
        for data_planes_item_data in self.data_planes:
            data_planes_item = data_planes_item_data.to_dict()
            data_planes.append(data_planes_item)

        version_number: int | None | Unset
        if isinstance(self.version_number, Unset):
            version_number = UNSET
        else:
            version_number = self.version_number

        unique_name: None | str | Unset
        if isinstance(self.unique_name, Unset):
            unique_name = UNSET
        else:
            unique_name = self.unique_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        owner_project_id: None | str | Unset
        if isinstance(self.owner_project_id, Unset):
            owner_project_id = UNSET
        else:
            owner_project_id = self.owner_project_id

        storage_size: int | None | Unset
        if isinstance(self.storage_size, Unset):
            storage_size = UNSET
        else:
            storage_size = self.storage_size

        owner_usernames: list[str] | None | Unset
        if isinstance(self.owner_usernames, Unset):
            owner_usernames = UNSET
        elif isinstance(self.owner_usernames, list):
            owner_usernames = self.owner_usernames

        else:
            owner_usernames = self.owner_usernames

        size_in_bytes: int | None | Unset
        if isinstance(self.size_in_bytes, Unset):
            size_in_bytes = UNSET
        else:
            size_in_bytes = self.size_in_bytes

        size_status: str | Unset = UNSET
        if not isinstance(self.size_status, Unset):
            size_status = self.size_status.value

        storage_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storage_info, Unset):
            storage_info = self.storage_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "datasetId": dataset_id,
                "snapshotId": snapshot_id,
                "name": name,
                "ownerProjectOwnerUsername": owner_project_owner_username,
                "ownerProjectName": owner_project_name,
                "isPartialSize": is_partial_size,
                "availableVersions": available_versions,
                "mountPathsForProject": mount_paths_for_project,
                "dataPlanes": data_planes,
            }
        )
        if version_number is not UNSET:
            field_dict["versionNumber"] = version_number
        if unique_name is not UNSET:
            field_dict["uniqueName"] = unique_name
        if description is not UNSET:
            field_dict["description"] = description
        if owner_project_id is not UNSET:
            field_dict["ownerProjectId"] = owner_project_id
        if storage_size is not UNSET:
            field_dict["storageSize"] = storage_size
        if owner_usernames is not UNSET:
            field_dict["ownerUsernames"] = owner_usernames
        if size_in_bytes is not UNSET:
            field_dict["sizeInBytes"] = size_in_bytes
        if size_status is not UNSET:
            field_dict["sizeStatus"] = size_status
        if storage_info is not UNSET:
            field_dict["storageInfo"] = storage_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_dataplane_data_plane_dto import DominoDataplaneDataPlaneDto
        from ..models.domino_datasetrw_api_dataset_rw_storage_info_dto import DominoDatasetrwApiDatasetRwStorageInfoDto

        d = dict(src_dict)
        dataset_id = d.pop("datasetId")

        snapshot_id = d.pop("snapshotId")

        name = d.pop("name")

        owner_project_owner_username = d.pop("ownerProjectOwnerUsername")

        owner_project_name = d.pop("ownerProjectName")

        is_partial_size = d.pop("isPartialSize")

        available_versions = d.pop("availableVersions")

        mount_paths_for_project = cast(list[str], d.pop("mountPathsForProject"))

        data_planes = []
        _data_planes = d.pop("dataPlanes")
        for data_planes_item_data in _data_planes:
            data_planes_item = DominoDataplaneDataPlaneDto.from_dict(data_planes_item_data)

            data_planes.append(data_planes_item)

        def _parse_version_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        version_number = _parse_version_number(d.pop("versionNumber", UNSET))

        def _parse_unique_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unique_name = _parse_unique_name(d.pop("uniqueName", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_owner_project_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_project_id = _parse_owner_project_id(d.pop("ownerProjectId", UNSET))

        def _parse_storage_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        storage_size = _parse_storage_size(d.pop("storageSize", UNSET))

        def _parse_owner_usernames(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_usernames_type_0 = cast(list[str], data)

                return owner_usernames_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        owner_usernames = _parse_owner_usernames(d.pop("ownerUsernames", UNSET))

        def _parse_size_in_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        size_in_bytes = _parse_size_in_bytes(d.pop("sizeInBytes", UNSET))

        _size_status = d.pop("sizeStatus", UNSET)
        size_status: DominoDatasetrwApiDatasetRwProjectMountDtoSizeStatus | Unset
        if isinstance(_size_status, Unset):
            size_status = UNSET
        else:
            size_status = DominoDatasetrwApiDatasetRwProjectMountDtoSizeStatus(_size_status)

        _storage_info = d.pop("storageInfo", UNSET)
        storage_info: DominoDatasetrwApiDatasetRwStorageInfoDto | Unset
        if isinstance(_storage_info, Unset):
            storage_info = UNSET
        else:
            storage_info = DominoDatasetrwApiDatasetRwStorageInfoDto.from_dict(_storage_info)

        domino_datasetrw_api_dataset_rw_project_mount_dto = cls(
            dataset_id=dataset_id,
            snapshot_id=snapshot_id,
            name=name,
            owner_project_owner_username=owner_project_owner_username,
            owner_project_name=owner_project_name,
            is_partial_size=is_partial_size,
            available_versions=available_versions,
            mount_paths_for_project=mount_paths_for_project,
            data_planes=data_planes,
            version_number=version_number,
            unique_name=unique_name,
            description=description,
            owner_project_id=owner_project_id,
            storage_size=storage_size,
            owner_usernames=owner_usernames,
            size_in_bytes=size_in_bytes,
            size_status=size_status,
            storage_info=storage_info,
        )

        domino_datasetrw_api_dataset_rw_project_mount_dto.additional_properties = d
        return domino_datasetrw_api_dataset_rw_project_mount_dto

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
