from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HardwareTierOverProvisioningV1")


@_attrs_define
class HardwareTierOverProvisioningV1:
    """Over provisioning settings for a hardware tier

    Attributes:
        days_of_week (list[str]):
        from_time (str):
        instances (int):
        scheduling_enabled (bool):
        timezone (str):
        to_time (str):
    """

    days_of_week: list[str]
    from_time: str
    instances: int
    scheduling_enabled: bool
    timezone: str
    to_time: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        days_of_week = self.days_of_week

        from_time = self.from_time

        instances = self.instances

        scheduling_enabled = self.scheduling_enabled

        timezone = self.timezone

        to_time = self.to_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "daysOfWeek": days_of_week,
                "fromTime": from_time,
                "instances": instances,
                "schedulingEnabled": scheduling_enabled,
                "timezone": timezone,
                "toTime": to_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        days_of_week = cast(list[str], d.pop("daysOfWeek"))

        from_time = d.pop("fromTime")

        instances = d.pop("instances")

        scheduling_enabled = d.pop("schedulingEnabled")

        timezone = d.pop("timezone")

        to_time = d.pop("toTime")

        hardware_tier_over_provisioning_v1 = cls(
            days_of_week=days_of_week,
            from_time=from_time,
            instances=instances,
            scheduling_enabled=scheduling_enabled,
            timezone=timezone,
            to_time=to_time,
        )

        hardware_tier_over_provisioning_v1.additional_properties = d
        return hardware_tier_over_provisioning_v1

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
