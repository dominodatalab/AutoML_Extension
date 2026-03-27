from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="DominoModelmanagerApiModelHttpRequestSnapshot")


@_attrs_define
class DominoModelmanagerApiModelHttpRequestSnapshot:
    """
    Attributes:
        timestamp (datetime.datetime):
        status (int):
        request_count (int):
    """

    timestamp: datetime.datetime
    status: int
    request_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp.isoformat()

        status = self.status

        request_count = self.request_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "status": status,
                "requestCount": request_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamp = isoparse(d.pop("timestamp"))

        status = d.pop("status")

        request_count = d.pop("requestCount")

        domino_modelmanager_api_model_http_request_snapshot = cls(
            timestamp=timestamp,
            status=status,
            request_count=request_count,
        )

        domino_modelmanager_api_model_http_request_snapshot.additional_properties = d
        return domino_modelmanager_api_model_http_request_snapshot

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
