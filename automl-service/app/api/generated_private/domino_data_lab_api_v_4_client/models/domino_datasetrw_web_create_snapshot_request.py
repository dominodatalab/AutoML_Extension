from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoDatasetrwWebCreateSnapshotRequest")


@_attrs_define
class DominoDatasetrwWebCreateSnapshotRequest:
    """
    Attributes:
        relative_file_paths (list[str]):
        dataset_id (str):
    """

    relative_file_paths: list[str]
    dataset_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        relative_file_paths = self.relative_file_paths

        dataset_id = self.dataset_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "relativeFilePaths": relative_file_paths,
                "datasetId": dataset_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        relative_file_paths = cast(list[str], d.pop("relativeFilePaths"))

        dataset_id = d.pop("datasetId")

        domino_datasetrw_web_create_snapshot_request = cls(
            relative_file_paths=relative_file_paths,
            dataset_id=dataset_id,
        )

        domino_datasetrw_web_create_snapshot_request.additional_properties = d
        return domino_datasetrw_web_create_snapshot_request

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
