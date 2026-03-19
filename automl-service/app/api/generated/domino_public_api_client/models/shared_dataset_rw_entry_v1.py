from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SharedDatasetRwEntryV1")


@_attrs_define
class SharedDatasetRwEntryV1:
    """An object describing the shared datasets imported into a project

    Attributes:
        project_id (str): Id of the project being described. Example: 62313ce67a0af0281c01a6a5.
        shared_dataset_ids (list[str]): List of dataset ids shared with this project
    """

    project_id: str
    shared_dataset_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        shared_dataset_ids = self.shared_dataset_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectId": project_id,
                "sharedDatasetIds": shared_dataset_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = d.pop("projectId")

        shared_dataset_ids = cast(list[str], d.pop("sharedDatasetIds"))

        shared_dataset_rw_entry_v1 = cls(
            project_id=project_id,
            shared_dataset_ids=shared_dataset_ids,
        )

        shared_dataset_rw_entry_v1.additional_properties = d
        return shared_dataset_rw_entry_v1

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
