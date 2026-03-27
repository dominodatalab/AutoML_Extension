from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoWorkspaceApiWorkspaceGlobalSettingsDto")


@_attrs_define
class DominoWorkspaceApiWorkspaceGlobalSettingsDto:
    """
    Attributes:
        stop_to_delete_delay_seconds (int):
        per_user_quota (int):
        high_disk_usage_threshold_percent (int):
    """

    stop_to_delete_delay_seconds: int
    per_user_quota: int
    high_disk_usage_threshold_percent: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stop_to_delete_delay_seconds = self.stop_to_delete_delay_seconds

        per_user_quota = self.per_user_quota

        high_disk_usage_threshold_percent = self.high_disk_usage_threshold_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stopToDeleteDelaySeconds": stop_to_delete_delay_seconds,
                "perUserQuota": per_user_quota,
                "highDiskUsageThresholdPercent": high_disk_usage_threshold_percent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        stop_to_delete_delay_seconds = d.pop("stopToDeleteDelaySeconds")

        per_user_quota = d.pop("perUserQuota")

        high_disk_usage_threshold_percent = d.pop("highDiskUsageThresholdPercent")

        domino_workspace_api_workspace_global_settings_dto = cls(
            stop_to_delete_delay_seconds=stop_to_delete_delay_seconds,
            per_user_quota=per_user_quota,
            high_disk_usage_threshold_percent=high_disk_usage_threshold_percent,
        )

        domino_workspace_api_workspace_global_settings_dto.additional_properties = d
        return domino_workspace_api_workspace_global_settings_dto

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
