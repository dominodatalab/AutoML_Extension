from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoNucleusDatasetUiCreateSnapshotWithRunInput")


@_attrs_define
class DominoNucleusDatasetUiCreateSnapshotWithRunInput:
    """
    Attributes:
        dataset_id (str):
        command (str):
        output_path (str):
    """

    dataset_id: str
    command: str
    output_path: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataset_id = self.dataset_id

        command = self.command

        output_path = self.output_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "datasetId": dataset_id,
                "command": command,
                "outputPath": output_path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dataset_id = d.pop("datasetId")

        command = d.pop("command")

        output_path = d.pop("outputPath")

        domino_nucleus_dataset_ui_create_snapshot_with_run_input = cls(
            dataset_id=dataset_id,
            command=command,
            output_path=output_path,
        )

        domino_nucleus_dataset_ui_create_snapshot_with_run_input.additional_properties = d
        return domino_nucleus_dataset_ui_create_snapshot_with_run_input

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
