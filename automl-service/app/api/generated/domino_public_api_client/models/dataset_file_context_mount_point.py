from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DatasetFileContextMountPoint")


@_attrs_define
class DatasetFileContextMountPoint:
    """Additional mount point information for the Dataset file context.

    Attributes:
        enabled (bool): Whether the Extension is enabled for this specific mount point in the Dataset file context.
        project_id (str): Project IDs where the dataset file context mount point is enabled.
    """

    enabled: bool
    project_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        project_id = self.project_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "projectId": project_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        project_id = d.pop("projectId")

        dataset_file_context_mount_point = cls(
            enabled=enabled,
            project_id=project_id,
        )

        dataset_file_context_mount_point.additional_properties = d
        return dataset_file_context_mount_point

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
