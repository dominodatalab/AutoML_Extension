from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatasetInfoV1")


@_attrs_define
class DatasetInfoV1:
    """
    Attributes:
        created_at (datetime.datetime): When the dataset was created Example: 2022-03-12T02:13:44.467Z.
        id (str): Dataset ID Example: 62313ce67a0af0281c01a6a5.
        name (str): Name of the dataset Example: My Dataset.
        description (str | Unset): A description of the dataset
        project_id (str | Unset): ID of the project this dataset belongs to Example: 62313ce67a0af0281c01a6a5.
    """

    created_at: datetime.datetime
    id: str
    name: str
    description: str | Unset = UNSET
    project_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id

        name = self.name

        description = self.description

        project_id = self.project_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "id": id,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if project_id is not UNSET:
            field_dict["projectId"] = project_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = isoparse(d.pop("createdAt"))

        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description", UNSET)

        project_id = d.pop("projectId", UNSET)

        dataset_info_v1 = cls(
            created_at=created_at,
            id=id,
            name=name,
            description=description,
            project_id=project_id,
        )

        dataset_info_v1.additional_properties = d
        return dataset_info_v1

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
