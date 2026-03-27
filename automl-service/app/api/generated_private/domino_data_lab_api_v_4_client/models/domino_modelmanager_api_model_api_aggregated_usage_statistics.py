from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoModelmanagerApiModelApiAggregatedUsageStatistics")


@_attrs_define
class DominoModelmanagerApiModelApiAggregatedUsageStatistics:
    """
    Attributes:
        model_version_id (str):
        status_code (int):
        timestamp (int):
        invocation_count (int):
    """

    model_version_id: str
    status_code: int
    timestamp: int
    invocation_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_version_id = self.model_version_id

        status_code = self.status_code

        timestamp = self.timestamp

        invocation_count = self.invocation_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modelVersionId": model_version_id,
                "statusCode": status_code,
                "timestamp": timestamp,
                "invocationCount": invocation_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model_version_id = d.pop("modelVersionId")

        status_code = d.pop("statusCode")

        timestamp = d.pop("timestamp")

        invocation_count = d.pop("invocationCount")

        domino_modelmanager_api_model_api_aggregated_usage_statistics = cls(
            model_version_id=model_version_id,
            status_code=status_code,
            timestamp=timestamp,
            invocation_count=invocation_count,
        )

        domino_modelmanager_api_model_api_aggregated_usage_statistics.additional_properties = d
        return domino_modelmanager_api_model_api_aggregated_usage_statistics

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
