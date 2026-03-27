from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_datasetrw_api_dataset_rw_snapshot_dto_lifecycle_status import (
    DominoDatasetrwApiDatasetRwSnapshotDtoLifecycleStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoDatasetrwApiDatasetRwSnapshotDto")


@_attrs_define
class DominoDatasetrwApiDatasetRwSnapshotDto:
    """
    Attributes:
        id (str):
        dataset_id (str):
        version (int):
        creation_time (int):
        lifecycle_status (DominoDatasetrwApiDatasetRwSnapshotDtoLifecycleStatus):
        status_last_updated_by (str):
        status_last_updated_time (int):
        storage_size (int):
        is_partial_size (bool):
        is_read_write (bool):
        dataset_storage_id (str):
        resource_id (str):
        author (None | str | Unset):
        description (None | str | Unset):
        last_used_time (int | None | Unset):
    """

    id: str
    dataset_id: str
    version: int
    creation_time: int
    lifecycle_status: DominoDatasetrwApiDatasetRwSnapshotDtoLifecycleStatus
    status_last_updated_by: str
    status_last_updated_time: int
    storage_size: int
    is_partial_size: bool
    is_read_write: bool
    dataset_storage_id: str
    resource_id: str
    author: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    last_used_time: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        dataset_id = self.dataset_id

        version = self.version

        creation_time = self.creation_time

        lifecycle_status = self.lifecycle_status.value

        status_last_updated_by = self.status_last_updated_by

        status_last_updated_time = self.status_last_updated_time

        storage_size = self.storage_size

        is_partial_size = self.is_partial_size

        is_read_write = self.is_read_write

        dataset_storage_id = self.dataset_storage_id

        resource_id = self.resource_id

        author: None | str | Unset
        if isinstance(self.author, Unset):
            author = UNSET
        else:
            author = self.author

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        last_used_time: int | None | Unset
        if isinstance(self.last_used_time, Unset):
            last_used_time = UNSET
        else:
            last_used_time = self.last_used_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "datasetId": dataset_id,
                "version": version,
                "creationTime": creation_time,
                "lifecycleStatus": lifecycle_status,
                "statusLastUpdatedBy": status_last_updated_by,
                "statusLastUpdatedTime": status_last_updated_time,
                "storageSize": storage_size,
                "isPartialSize": is_partial_size,
                "isReadWrite": is_read_write,
                "datasetStorageId": dataset_storage_id,
                "resourceId": resource_id,
            }
        )
        if author is not UNSET:
            field_dict["author"] = author
        if description is not UNSET:
            field_dict["description"] = description
        if last_used_time is not UNSET:
            field_dict["lastUsedTime"] = last_used_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        dataset_id = d.pop("datasetId")

        version = d.pop("version")

        creation_time = d.pop("creationTime")

        lifecycle_status = DominoDatasetrwApiDatasetRwSnapshotDtoLifecycleStatus(d.pop("lifecycleStatus"))

        status_last_updated_by = d.pop("statusLastUpdatedBy")

        status_last_updated_time = d.pop("statusLastUpdatedTime")

        storage_size = d.pop("storageSize")

        is_partial_size = d.pop("isPartialSize")

        is_read_write = d.pop("isReadWrite")

        dataset_storage_id = d.pop("datasetStorageId")

        resource_id = d.pop("resourceId")

        def _parse_author(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        author = _parse_author(d.pop("author", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_last_used_time(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_used_time = _parse_last_used_time(d.pop("lastUsedTime", UNSET))

        domino_datasetrw_api_dataset_rw_snapshot_dto = cls(
            id=id,
            dataset_id=dataset_id,
            version=version,
            creation_time=creation_time,
            lifecycle_status=lifecycle_status,
            status_last_updated_by=status_last_updated_by,
            status_last_updated_time=status_last_updated_time,
            storage_size=storage_size,
            is_partial_size=is_partial_size,
            is_read_write=is_read_write,
            dataset_storage_id=dataset_storage_id,
            resource_id=resource_id,
            author=author,
            description=description,
            last_used_time=last_used_time,
        )

        domino_datasetrw_api_dataset_rw_snapshot_dto.additional_properties = d
        return domino_datasetrw_api_dataset_rw_snapshot_dto

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
