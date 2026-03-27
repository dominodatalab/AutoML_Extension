from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_jobs_interface_log_content_log_type import DominoJobsInterfaceLogContentLogType

T = TypeVar("T", bound="DominoJobsInterfaceLogContent")


@_attrs_define
class DominoJobsInterfaceLogContent:
    """
    Attributes:
        timestamp (int):
        log_type (DominoJobsInterfaceLogContentLogType):
        log (str):
        size (int):
    """

    timestamp: int
    log_type: DominoJobsInterfaceLogContentLogType
    log: str
    size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        log_type = self.log_type.value

        log = self.log

        size = self.size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "logType": log_type,
                "log": log,
                "size": size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamp = d.pop("timestamp")

        log_type = DominoJobsInterfaceLogContentLogType(d.pop("logType"))

        log = d.pop("log")

        size = d.pop("size")

        domino_jobs_interface_log_content = cls(
            timestamp=timestamp,
            log_type=log_type,
            log=log,
            size=size,
        )

        domino_jobs_interface_log_content.additional_properties = d
        return domino_jobs_interface_log_content

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
