from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoDatasetrwApiDatasetRwFiletaskTaskDto")


@_attrs_define
class DominoDatasetrwApiDatasetRwFiletaskTaskDto:
    """
    Attributes:
        task_id (str):
        task_key (str):
        task_status (str):
    """

    task_id: str
    task_key: str
    task_status: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_id = self.task_id

        task_key = self.task_key

        task_status = self.task_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "taskId": task_id,
                "taskKey": task_key,
                "taskStatus": task_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        task_id = d.pop("taskId")

        task_key = d.pop("taskKey")

        task_status = d.pop("taskStatus")

        domino_datasetrw_api_dataset_rw_filetask_task_dto = cls(
            task_id=task_id,
            task_key=task_key,
            task_status=task_status,
        )

        domino_datasetrw_api_dataset_rw_filetask_task_dto.additional_properties = d
        return domino_datasetrw_api_dataset_rw_filetask_task_dto

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
