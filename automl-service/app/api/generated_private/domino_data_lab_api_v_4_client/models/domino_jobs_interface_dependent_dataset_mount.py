from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoJobsInterfaceDependentDatasetMount")


@_attrs_define
class DominoJobsInterfaceDependentDatasetMount:
    """
    Attributes:
        dataset_id (str):
        dataset_name (str):
        project_id (str):
        is_input (bool):
        snapshot_id (None | str | Unset):
        snapshot_version (int | None | Unset):
        container_path (None | str | Unset):
    """

    dataset_id: str
    dataset_name: str
    project_id: str
    is_input: bool
    snapshot_id: None | str | Unset = UNSET
    snapshot_version: int | None | Unset = UNSET
    container_path: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataset_id = self.dataset_id

        dataset_name = self.dataset_name

        project_id = self.project_id

        is_input = self.is_input

        snapshot_id: None | str | Unset
        if isinstance(self.snapshot_id, Unset):
            snapshot_id = UNSET
        else:
            snapshot_id = self.snapshot_id

        snapshot_version: int | None | Unset
        if isinstance(self.snapshot_version, Unset):
            snapshot_version = UNSET
        else:
            snapshot_version = self.snapshot_version

        container_path: None | str | Unset
        if isinstance(self.container_path, Unset):
            container_path = UNSET
        else:
            container_path = self.container_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "datasetId": dataset_id,
                "datasetName": dataset_name,
                "projectId": project_id,
                "isInput": is_input,
            }
        )
        if snapshot_id is not UNSET:
            field_dict["snapshotId"] = snapshot_id
        if snapshot_version is not UNSET:
            field_dict["snapshotVersion"] = snapshot_version
        if container_path is not UNSET:
            field_dict["containerPath"] = container_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dataset_id = d.pop("datasetId")

        dataset_name = d.pop("datasetName")

        project_id = d.pop("projectId")

        is_input = d.pop("isInput")

        def _parse_snapshot_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        snapshot_id = _parse_snapshot_id(d.pop("snapshotId", UNSET))

        def _parse_snapshot_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        snapshot_version = _parse_snapshot_version(d.pop("snapshotVersion", UNSET))

        def _parse_container_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        container_path = _parse_container_path(d.pop("containerPath", UNSET))

        domino_jobs_interface_dependent_dataset_mount = cls(
            dataset_id=dataset_id,
            dataset_name=dataset_name,
            project_id=project_id,
            is_input=is_input,
            snapshot_id=snapshot_id,
            snapshot_version=snapshot_version,
            container_path=container_path,
        )

        domino_jobs_interface_dependent_dataset_mount.additional_properties = d
        return domino_jobs_interface_dependent_dataset_mount

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
