from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoWorkspaceApiWorkspaceDiskUsageDto")


@_attrs_define
class DominoWorkspaceApiWorkspaceDiskUsageDto:
    """
    Attributes:
        disk_usage_gi_b (float):
        disk_usage_percent (float):
        max_disk_usage_gib (float):
        has_high_disk_usage (bool):
    """

    disk_usage_gi_b: float
    disk_usage_percent: float
    max_disk_usage_gib: float
    has_high_disk_usage: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        disk_usage_gi_b = self.disk_usage_gi_b

        disk_usage_percent = self.disk_usage_percent

        max_disk_usage_gib = self.max_disk_usage_gib

        has_high_disk_usage = self.has_high_disk_usage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "diskUsageGiB": disk_usage_gi_b,
                "diskUsagePercent": disk_usage_percent,
                "maxDiskUsageGib": max_disk_usage_gib,
                "hasHighDiskUsage": has_high_disk_usage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        disk_usage_gi_b = d.pop("diskUsageGiB")

        disk_usage_percent = d.pop("diskUsagePercent")

        max_disk_usage_gib = d.pop("maxDiskUsageGib")

        has_high_disk_usage = d.pop("hasHighDiskUsage")

        domino_workspace_api_workspace_disk_usage_dto = cls(
            disk_usage_gi_b=disk_usage_gi_b,
            disk_usage_percent=disk_usage_percent,
            max_disk_usage_gib=max_disk_usage_gib,
            has_high_disk_usage=has_high_disk_usage,
        )

        domino_workspace_api_workspace_disk_usage_dto.additional_properties = d
        return domino_workspace_api_workspace_disk_usage_dto

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
