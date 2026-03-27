from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoDatasetrwWebCreateSnapshotFromExecutionRequest")


@_attrs_define
class DominoDatasetrwWebCreateSnapshotFromExecutionRequest:
    """
    Attributes:
        creating_user_id (str):
        execution_id (str):
        dataset_id (str):
    """

    creating_user_id: str
    execution_id: str
    dataset_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        creating_user_id = self.creating_user_id

        execution_id = self.execution_id

        dataset_id = self.dataset_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "creatingUserId": creating_user_id,
                "executionId": execution_id,
                "datasetId": dataset_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        creating_user_id = d.pop("creatingUserId")

        execution_id = d.pop("executionId")

        dataset_id = d.pop("datasetId")

        domino_datasetrw_web_create_snapshot_from_execution_request = cls(
            creating_user_id=creating_user_id,
            execution_id=execution_id,
            dataset_id=dataset_id,
        )

        domino_datasetrw_web_create_snapshot_from_execution_request.additional_properties = d
        return domino_datasetrw_web_create_snapshot_from_execution_request

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
