from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_dataset_api_dataset_snapshot_dto_labels import DominoDatasetApiDatasetSnapshotDtoLabels


T = TypeVar("T", bound="DominoDatasetApiDatasetSnapshotDto")


@_attrs_define
class DominoDatasetApiDatasetSnapshotDto:
    """
    Attributes:
        resource_id (str):
        creation_time (int):
        version (int):
        labels (DominoDatasetApiDatasetSnapshotDtoLabels):
        deleted (bool):
        storage_size (int):
        dataset_id (str):
        id (str):
        is_partial_size (bool):
        status (str):
        author (None | str | Unset):
        deleted_by_user (None | str | Unset):
        description (None | str | Unset):
        last_used_time (int | None | Unset):
        marked_for_deletion_time (int | None | Unset):
        delete_time (int | None | Unset):
    """

    resource_id: str
    creation_time: int
    version: int
    labels: DominoDatasetApiDatasetSnapshotDtoLabels
    deleted: bool
    storage_size: int
    dataset_id: str
    id: str
    is_partial_size: bool
    status: str
    author: None | str | Unset = UNSET
    deleted_by_user: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    last_used_time: int | None | Unset = UNSET
    marked_for_deletion_time: int | None | Unset = UNSET
    delete_time: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_id = self.resource_id

        creation_time = self.creation_time

        version = self.version

        labels = self.labels.to_dict()

        deleted = self.deleted

        storage_size = self.storage_size

        dataset_id = self.dataset_id

        id = self.id

        is_partial_size = self.is_partial_size

        status = self.status

        author: None | str | Unset
        if isinstance(self.author, Unset):
            author = UNSET
        else:
            author = self.author

        deleted_by_user: None | str | Unset
        if isinstance(self.deleted_by_user, Unset):
            deleted_by_user = UNSET
        else:
            deleted_by_user = self.deleted_by_user

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

        marked_for_deletion_time: int | None | Unset
        if isinstance(self.marked_for_deletion_time, Unset):
            marked_for_deletion_time = UNSET
        else:
            marked_for_deletion_time = self.marked_for_deletion_time

        delete_time: int | None | Unset
        if isinstance(self.delete_time, Unset):
            delete_time = UNSET
        else:
            delete_time = self.delete_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resourceId": resource_id,
                "creationTime": creation_time,
                "version": version,
                "labels": labels,
                "deleted": deleted,
                "storageSize": storage_size,
                "datasetId": dataset_id,
                "id": id,
                "isPartialSize": is_partial_size,
                "status": status,
            }
        )
        if author is not UNSET:
            field_dict["author"] = author
        if deleted_by_user is not UNSET:
            field_dict["deletedByUser"] = deleted_by_user
        if description is not UNSET:
            field_dict["description"] = description
        if last_used_time is not UNSET:
            field_dict["lastUsedTime"] = last_used_time
        if marked_for_deletion_time is not UNSET:
            field_dict["markedForDeletionTime"] = marked_for_deletion_time
        if delete_time is not UNSET:
            field_dict["deleteTime"] = delete_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_dataset_api_dataset_snapshot_dto_labels import DominoDatasetApiDatasetSnapshotDtoLabels

        d = dict(src_dict)
        resource_id = d.pop("resourceId")

        creation_time = d.pop("creationTime")

        version = d.pop("version")

        labels = DominoDatasetApiDatasetSnapshotDtoLabels.from_dict(d.pop("labels"))

        deleted = d.pop("deleted")

        storage_size = d.pop("storageSize")

        dataset_id = d.pop("datasetId")

        id = d.pop("id")

        is_partial_size = d.pop("isPartialSize")

        status = d.pop("status")

        def _parse_author(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        author = _parse_author(d.pop("author", UNSET))

        def _parse_deleted_by_user(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_by_user = _parse_deleted_by_user(d.pop("deletedByUser", UNSET))

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

        def _parse_marked_for_deletion_time(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        marked_for_deletion_time = _parse_marked_for_deletion_time(d.pop("markedForDeletionTime", UNSET))

        def _parse_delete_time(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        delete_time = _parse_delete_time(d.pop("deleteTime", UNSET))

        domino_dataset_api_dataset_snapshot_dto = cls(
            resource_id=resource_id,
            creation_time=creation_time,
            version=version,
            labels=labels,
            deleted=deleted,
            storage_size=storage_size,
            dataset_id=dataset_id,
            id=id,
            is_partial_size=is_partial_size,
            status=status,
            author=author,
            deleted_by_user=deleted_by_user,
            description=description,
            last_used_time=last_used_time,
            marked_for_deletion_time=marked_for_deletion_time,
            delete_time=delete_time,
        )

        domino_dataset_api_dataset_snapshot_dto.additional_properties = d
        return domino_dataset_api_dataset_snapshot_dto

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
