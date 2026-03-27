from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoDatasetrwApiSharedDatasetRwEntryDto")


@_attrs_define
class DominoDatasetrwApiSharedDatasetRwEntryDto:
    """
    Attributes:
        project_id (str):
        shared_datasets (list[str]):
    """

    project_id: str
    shared_datasets: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        shared_datasets = self.shared_datasets

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectId": project_id,
                "sharedDatasets": shared_datasets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = d.pop("projectId")

        shared_datasets = cast(list[str], d.pop("sharedDatasets"))

        domino_datasetrw_api_shared_dataset_rw_entry_dto = cls(
            project_id=project_id,
            shared_datasets=shared_datasets,
        )

        domino_datasetrw_api_shared_dataset_rw_entry_dto.additional_properties = d
        return domino_datasetrw_api_shared_dataset_rw_entry_dto

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
