from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelEndpointLogsResponseLogContentItem")


@_attrs_define
class ModelEndpointLogsResponseLogContentItem:
    """
    Attributes:
        log (str):
        log_type (str):
        size (float):
        timestamp (float):
    """

    log: str
    log_type: str
    size: float
    timestamp: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        log = self.log

        log_type = self.log_type

        size = self.size

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "log": log,
                "logType": log_type,
                "size": size,
                "timestamp": timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        log = d.pop("log")

        log_type = d.pop("logType")

        size = d.pop("size")

        timestamp = d.pop("timestamp")

        model_endpoint_logs_response_log_content_item = cls(
            log=log,
            log_type=log_type,
            size=size,
            timestamp=timestamp,
        )

        model_endpoint_logs_response_log_content_item.additional_properties = d
        return model_endpoint_logs_response_log_content_item

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
