from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.log_type_v1 import LogTypeV1

T = TypeVar("T", bound="LogContentV1")


@_attrs_define
class LogContentV1:
    """
    Attributes:
        log (str): Log message Example: Pulling image
            "172.20.22.242:5000/noahjax11699-compute/environment:622a6879dde1a920fcccfef5-1".
        log_type (LogTypeV1): Type of log. Complete includes all log types.
        size (int): Length of log line. Example: 94.
        timestamp (datetime.datetime): Time logs were written. Example: 2022-03-12T02:13:51.616Z.
    """

    log: str
    log_type: LogTypeV1
    size: int
    timestamp: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        log = self.log

        log_type = self.log_type.value

        size = self.size

        timestamp = self.timestamp.isoformat()

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

        log_type = LogTypeV1(d.pop("logType"))

        size = d.pop("size")

        timestamp = isoparse(d.pop("timestamp"))

        log_content_v1 = cls(
            log=log,
            log_type=log_type,
            size=size,
            timestamp=timestamp,
        )

        log_content_v1.additional_properties = d
        return log_content_v1

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
