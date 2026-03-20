from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AppInstanceAutoscalingInfo")


@_attrs_define
class AppInstanceAutoscalingInfo:
    """
    Attributes:
        ready_replicas (int):
    """

    ready_replicas: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ready_replicas = self.ready_replicas

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "readyReplicas": ready_replicas,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ready_replicas = d.pop("readyReplicas")

        app_instance_autoscaling_info = cls(
            ready_replicas=ready_replicas,
        )

        app_instance_autoscaling_info.additional_properties = d
        return app_instance_autoscaling_info

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
