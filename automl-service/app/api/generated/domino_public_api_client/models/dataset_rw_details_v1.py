from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataset_rw_tags_v1 import DatasetRwTagsV1


T = TypeVar("T", bound="DatasetRwDetailsV1")


@_attrs_define
class DatasetRwDetailsV1:
    """
    Attributes:
        created_at (datetime.datetime): When the dataset was created Example: 2022-03-12T02:13:44.467Z.
        id (str): ID of the dataset Example: 62313ce67a0af0281c01a6a5.
        name (str): Name of the dataset Example: My Dataset.
        snapshot_ids (list[str]): List of snapshot IDs belonging to this dataset
        tags (DatasetRwTagsV1): A map of tagName -> snapshotId Example: {'bar': '62313ce67a0af0281c01a6a5', 'foo':
            '62313ce67a0af0281c01a6a5'}.
        description (str | Unset): A description of the dataset
        project_id (str | Unset): ID of the project this dataset belongs to Example: 62313ce67a0af0281c01a6a5.
    """

    created_at: datetime.datetime
    id: str
    name: str
    snapshot_ids: list[str]
    tags: DatasetRwTagsV1
    description: str | Unset = UNSET
    project_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id

        name = self.name

        snapshot_ids = self.snapshot_ids

        tags = self.tags.to_dict()

        description = self.description

        project_id = self.project_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "id": id,
                "name": name,
                "snapshotIds": snapshot_ids,
                "tags": tags,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if project_id is not UNSET:
            field_dict["projectId"] = project_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_rw_tags_v1 import DatasetRwTagsV1

        d = dict(src_dict)
        created_at = isoparse(d.pop("createdAt"))

        id = d.pop("id")

        name = d.pop("name")

        snapshot_ids = cast(list[str], d.pop("snapshotIds"))

        tags = DatasetRwTagsV1.from_dict(d.pop("tags"))

        description = d.pop("description", UNSET)

        project_id = d.pop("projectId", UNSET)

        dataset_rw_details_v1 = cls(
            created_at=created_at,
            id=id,
            name=name,
            snapshot_ids=snapshot_ids,
            tags=tags,
            description=description,
            project_id=project_id,
        )

        dataset_rw_details_v1.additional_properties = d
        return dataset_rw_details_v1

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
