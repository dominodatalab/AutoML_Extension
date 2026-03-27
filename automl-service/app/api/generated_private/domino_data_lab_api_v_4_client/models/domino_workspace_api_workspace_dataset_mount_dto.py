from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_workspace_api_workspace_dataset_snapshot_dto import (
        DominoWorkspaceApiWorkspaceDatasetSnapshotDto,
    )


T = TypeVar("T", bound="DominoWorkspaceApiWorkspaceDatasetMountDto")


@_attrs_define
class DominoWorkspaceApiWorkspaceDatasetMountDto:
    """
    Attributes:
        dataset_id (str):
        dataset_name (str):
        container_path (str):
        is_input (bool):
        snapshot (DominoWorkspaceApiWorkspaceDatasetSnapshotDto | Unset):
    """

    dataset_id: str
    dataset_name: str
    container_path: str
    is_input: bool
    snapshot: DominoWorkspaceApiWorkspaceDatasetSnapshotDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataset_id = self.dataset_id

        dataset_name = self.dataset_name

        container_path = self.container_path

        is_input = self.is_input

        snapshot: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snapshot, Unset):
            snapshot = self.snapshot.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "datasetId": dataset_id,
                "datasetName": dataset_name,
                "containerPath": container_path,
                "isInput": is_input,
            }
        )
        if snapshot is not UNSET:
            field_dict["snapshot"] = snapshot

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_workspace_api_workspace_dataset_snapshot_dto import (
            DominoWorkspaceApiWorkspaceDatasetSnapshotDto,
        )

        d = dict(src_dict)
        dataset_id = d.pop("datasetId")

        dataset_name = d.pop("datasetName")

        container_path = d.pop("containerPath")

        is_input = d.pop("isInput")

        _snapshot = d.pop("snapshot", UNSET)
        snapshot: DominoWorkspaceApiWorkspaceDatasetSnapshotDto | Unset
        if isinstance(_snapshot, Unset):
            snapshot = UNSET
        else:
            snapshot = DominoWorkspaceApiWorkspaceDatasetSnapshotDto.from_dict(_snapshot)

        domino_workspace_api_workspace_dataset_mount_dto = cls(
            dataset_id=dataset_id,
            dataset_name=dataset_name,
            container_path=container_path,
            is_input=is_input,
            snapshot=snapshot,
        )

        domino_workspace_api_workspace_dataset_mount_dto.additional_properties = d
        return domino_workspace_api_workspace_dataset_mount_dto

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
