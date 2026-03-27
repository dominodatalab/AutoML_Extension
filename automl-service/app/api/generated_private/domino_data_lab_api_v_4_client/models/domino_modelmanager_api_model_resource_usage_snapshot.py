from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="DominoModelmanagerApiModelResourceUsageSnapshot")


@_attrs_define
class DominoModelmanagerApiModelResourceUsageSnapshot:
    """
    Attributes:
        timestamp (datetime.datetime):
        cpu (float):
        memory (float):
        pod (str):
    """

    timestamp: datetime.datetime
    cpu: float
    memory: float
    pod: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp.isoformat()

        cpu = self.cpu

        memory = self.memory

        pod = self.pod

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "cpu": cpu,
                "memory": memory,
                "pod": pod,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamp = isoparse(d.pop("timestamp"))

        cpu = d.pop("cpu")

        memory = d.pop("memory")

        pod = d.pop("pod")

        domino_modelmanager_api_model_resource_usage_snapshot = cls(
            timestamp=timestamp,
            cpu=cpu,
            memory=memory,
            pod=pod,
        )

        domino_modelmanager_api_model_resource_usage_snapshot.additional_properties = d
        return domino_modelmanager_api_model_resource_usage_snapshot

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
