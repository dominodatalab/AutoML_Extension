from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatasetMountV1")


@_attrs_define
class DatasetMountV1:
    """
    Attributes:
        dataset_name (str): Name of dataset to be mounted. Example: MyDataset.
        id (str): Id of dataset to be mounted. Example: 623137f57a0af0281c01a6a0.
        is_input (bool): Whether a dataset was an input to be used in the execution, or an output created by the
            execution. Example: True.
        project_id (str): Id of project the dataset belongs to. Example: 6231383c7a0af0281c01a6a1.
        container_path (str | Unset): Location dataset is mounted at in the Job. Example: /domino/datasets/local/quick-
            start.
        snapshot_id (str | Unset): Id of snapshot to mount for this dataset. Example: 623138807a0af0281c01a6a2.
        snapshot_version (int | Unset): Version of dataset snapshot to mound. Example: 2.
    """

    dataset_name: str
    id: str
    is_input: bool
    project_id: str
    container_path: str | Unset = UNSET
    snapshot_id: str | Unset = UNSET
    snapshot_version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataset_name = self.dataset_name

        id = self.id

        is_input = self.is_input

        project_id = self.project_id

        container_path = self.container_path

        snapshot_id = self.snapshot_id

        snapshot_version = self.snapshot_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "datasetName": dataset_name,
                "id": id,
                "isInput": is_input,
                "projectId": project_id,
            }
        )
        if container_path is not UNSET:
            field_dict["containerPath"] = container_path
        if snapshot_id is not UNSET:
            field_dict["snapshotId"] = snapshot_id
        if snapshot_version is not UNSET:
            field_dict["snapshotVersion"] = snapshot_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dataset_name = d.pop("datasetName")

        id = d.pop("id")

        is_input = d.pop("isInput")

        project_id = d.pop("projectId")

        container_path = d.pop("containerPath", UNSET)

        snapshot_id = d.pop("snapshotId", UNSET)

        snapshot_version = d.pop("snapshotVersion", UNSET)

        dataset_mount_v1 = cls(
            dataset_name=dataset_name,
            id=id,
            is_input=is_input,
            project_id=project_id,
            container_path=container_path,
            snapshot_id=snapshot_id,
            snapshot_version=snapshot_version,
        )

        dataset_mount_v1.additional_properties = d
        return dataset_mount_v1

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
