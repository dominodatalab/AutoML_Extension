from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoProjectsApiAssetUsageValues")


@_attrs_define
class DominoProjectsApiAssetUsageValues:
    """
    Attributes:
        timestamp (int):
        status_code (int):
        usage_count (int):
    """

    timestamp: int
    status_code: int
    usage_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        status_code = self.status_code

        usage_count = self.usage_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "statusCode": status_code,
                "usageCount": usage_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamp = d.pop("timestamp")

        status_code = d.pop("statusCode")

        usage_count = d.pop("usageCount")

        domino_projects_api_asset_usage_values = cls(
            timestamp=timestamp,
            status_code=status_code,
            usage_count=usage_count,
        )

        domino_projects_api_asset_usage_values.additional_properties = d
        return domino_projects_api_asset_usage_values

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
