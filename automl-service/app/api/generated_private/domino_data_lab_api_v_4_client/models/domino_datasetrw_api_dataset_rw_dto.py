from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_datasetrw_api_dataset_rw_dto_lifecycle_status import DominoDatasetrwApiDatasetRwDtoLifecycleStatus
from ..models.domino_datasetrw_api_dataset_rw_size_status import DominoDatasetrwApiDatasetRwSizeStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_datasetrw_api_dataset_rw_dto_tags import DominoDatasetrwApiDatasetRwDtoTags


T = TypeVar("T", bound="DominoDatasetrwApiDatasetRwDto")


@_attrs_define
class DominoDatasetrwApiDatasetRwDto:
    """
    Attributes:
        lifecycle_status (DominoDatasetrwApiDatasetRwDtoLifecycleStatus):
        snapshot_ids (list[str]):
        status_last_updated_by (str):
        tags (DominoDatasetrwApiDatasetRwDtoTags):
        dataset_path (str):
        read_write_snapshot_id (str):
        name (str):
        created_time (int):
        status_last_updated_time (int):
        id (str):
        size_in_bytes (int | None | Unset):
        author (None | str | Unset):
        description (None | str | Unset):
        active_ro_snapshot_count (int | None | Unset):
        dataset_storage_id (str | Unset):
        unique_name (None | str | Unset):
        size_status (DominoDatasetrwApiDatasetRwSizeStatus | Unset):
        owner_usernames (list[str] | None | Unset):
        project_id (None | str | Unset):
    """

    lifecycle_status: DominoDatasetrwApiDatasetRwDtoLifecycleStatus
    snapshot_ids: list[str]
    status_last_updated_by: str
    tags: DominoDatasetrwApiDatasetRwDtoTags
    dataset_path: str
    read_write_snapshot_id: str
    name: str
    created_time: int
    status_last_updated_time: int
    id: str
    size_in_bytes: int | None | Unset = UNSET
    author: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    active_ro_snapshot_count: int | None | Unset = UNSET
    dataset_storage_id: str | Unset = UNSET
    unique_name: None | str | Unset = UNSET
    size_status: DominoDatasetrwApiDatasetRwSizeStatus | Unset = UNSET
    owner_usernames: list[str] | None | Unset = UNSET
    project_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lifecycle_status = self.lifecycle_status.value

        snapshot_ids = self.snapshot_ids

        status_last_updated_by = self.status_last_updated_by

        tags = self.tags.to_dict()

        dataset_path = self.dataset_path

        read_write_snapshot_id = self.read_write_snapshot_id

        name = self.name

        created_time = self.created_time

        status_last_updated_time = self.status_last_updated_time

        id = self.id

        size_in_bytes: int | None | Unset
        if isinstance(self.size_in_bytes, Unset):
            size_in_bytes = UNSET
        else:
            size_in_bytes = self.size_in_bytes

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

        active_ro_snapshot_count: int | None | Unset
        if isinstance(self.active_ro_snapshot_count, Unset):
            active_ro_snapshot_count = UNSET
        else:
            active_ro_snapshot_count = self.active_ro_snapshot_count

        dataset_storage_id = self.dataset_storage_id

        unique_name: None | str | Unset
        if isinstance(self.unique_name, Unset):
            unique_name = UNSET
        else:
            unique_name = self.unique_name

        size_status: str | Unset = UNSET
        if not isinstance(self.size_status, Unset):
            size_status = self.size_status.value

        owner_usernames: list[str] | None | Unset
        if isinstance(self.owner_usernames, Unset):
            owner_usernames = UNSET
        elif isinstance(self.owner_usernames, list):
            owner_usernames = self.owner_usernames

        else:
            owner_usernames = self.owner_usernames

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lifecycleStatus": lifecycle_status,
                "snapshotIds": snapshot_ids,
                "statusLastUpdatedBy": status_last_updated_by,
                "tags": tags,
                "datasetPath": dataset_path,
                "readWriteSnapshotId": read_write_snapshot_id,
                "name": name,
                "createdTime": created_time,
                "statusLastUpdatedTime": status_last_updated_time,
                "id": id,
            }
        )
        if size_in_bytes is not UNSET:
            field_dict["sizeInBytes"] = size_in_bytes
        if author is not UNSET:
            field_dict["author"] = author
        if description is not UNSET:
            field_dict["description"] = description
        if active_ro_snapshot_count is not UNSET:
            field_dict["activeROSnapshotCount"] = active_ro_snapshot_count
        if dataset_storage_id is not UNSET:
            field_dict["datasetStorageId"] = dataset_storage_id
        if unique_name is not UNSET:
            field_dict["uniqueName"] = unique_name
        if size_status is not UNSET:
            field_dict["sizeStatus"] = size_status
        if owner_usernames is not UNSET:
            field_dict["ownerUsernames"] = owner_usernames
        if project_id is not UNSET:
            field_dict["projectId"] = project_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_datasetrw_api_dataset_rw_dto_tags import DominoDatasetrwApiDatasetRwDtoTags

        d = dict(src_dict)
        lifecycle_status = DominoDatasetrwApiDatasetRwDtoLifecycleStatus(d.pop("lifecycleStatus"))

        snapshot_ids = cast(list[str], d.pop("snapshotIds"))

        status_last_updated_by = d.pop("statusLastUpdatedBy")

        tags = DominoDatasetrwApiDatasetRwDtoTags.from_dict(d.pop("tags"))

        dataset_path = d.pop("datasetPath")

        read_write_snapshot_id = d.pop("readWriteSnapshotId")

        name = d.pop("name")

        created_time = d.pop("createdTime")

        status_last_updated_time = d.pop("statusLastUpdatedTime")

        id = d.pop("id")

        def _parse_size_in_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        size_in_bytes = _parse_size_in_bytes(d.pop("sizeInBytes", UNSET))

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

        def _parse_active_ro_snapshot_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        active_ro_snapshot_count = _parse_active_ro_snapshot_count(d.pop("activeROSnapshotCount", UNSET))

        dataset_storage_id = d.pop("datasetStorageId", UNSET)

        def _parse_unique_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unique_name = _parse_unique_name(d.pop("uniqueName", UNSET))

        _size_status = d.pop("sizeStatus", UNSET)
        size_status: DominoDatasetrwApiDatasetRwSizeStatus | Unset
        if isinstance(_size_status, Unset):
            size_status = UNSET
        else:
            size_status = DominoDatasetrwApiDatasetRwSizeStatus(_size_status)

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

        def _parse_project_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_id = _parse_project_id(d.pop("projectId", UNSET))

        domino_datasetrw_api_dataset_rw_dto = cls(
            lifecycle_status=lifecycle_status,
            snapshot_ids=snapshot_ids,
            status_last_updated_by=status_last_updated_by,
            tags=tags,
            dataset_path=dataset_path,
            read_write_snapshot_id=read_write_snapshot_id,
            name=name,
            created_time=created_time,
            status_last_updated_time=status_last_updated_time,
            id=id,
            size_in_bytes=size_in_bytes,
            author=author,
            description=description,
            active_ro_snapshot_count=active_ro_snapshot_count,
            dataset_storage_id=dataset_storage_id,
            unique_name=unique_name,
            size_status=size_status,
            owner_usernames=owner_usernames,
            project_id=project_id,
        )

        domino_datasetrw_api_dataset_rw_dto.additional_properties = d
        return domino_datasetrw_api_dataset_rw_dto

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
