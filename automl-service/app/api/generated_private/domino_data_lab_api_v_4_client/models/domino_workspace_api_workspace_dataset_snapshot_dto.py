from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoWorkspaceApiWorkspaceDatasetSnapshotDto")


@_attrs_define
class DominoWorkspaceApiWorkspaceDatasetSnapshotDto:
    """
    Attributes:
        snapshot_id (str):
        snapshot_version (int):
    """

    snapshot_id: str
    snapshot_version: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        snapshot_id = self.snapshot_id

        snapshot_version = self.snapshot_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "snapshotId": snapshot_id,
                "snapshotVersion": snapshot_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        snapshot_id = d.pop("snapshotId")

        snapshot_version = d.pop("snapshotVersion")

        domino_workspace_api_workspace_dataset_snapshot_dto = cls(
            snapshot_id=snapshot_id,
            snapshot_version=snapshot_version,
        )

        domino_workspace_api_workspace_dataset_snapshot_dto.additional_properties = d
        return domino_workspace_api_workspace_dataset_snapshot_dto

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
