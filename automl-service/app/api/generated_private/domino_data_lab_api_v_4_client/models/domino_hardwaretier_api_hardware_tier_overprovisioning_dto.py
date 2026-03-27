from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_hardwaretier_api_hardware_tier_overprovisioning_dto_days_of_week_item import (
    DominoHardwaretierApiHardwareTierOverprovisioningDtoDaysOfWeekItem,
)

T = TypeVar("T", bound="DominoHardwaretierApiHardwareTierOverprovisioningDto")


@_attrs_define
class DominoHardwaretierApiHardwareTierOverprovisioningDto:
    """
    Attributes:
        instances (int):
        scheduling_enabled (bool):
        days_of_week (list[DominoHardwaretierApiHardwareTierOverprovisioningDtoDaysOfWeekItem]):
        timezone (str):
        from_time (str):
        to_time (str):
    """

    instances: int
    scheduling_enabled: bool
    days_of_week: list[DominoHardwaretierApiHardwareTierOverprovisioningDtoDaysOfWeekItem]
    timezone: str
    from_time: str
    to_time: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instances = self.instances

        scheduling_enabled = self.scheduling_enabled

        days_of_week = []
        for days_of_week_item_data in self.days_of_week:
            days_of_week_item = days_of_week_item_data.value
            days_of_week.append(days_of_week_item)

        timezone = self.timezone

        from_time = self.from_time

        to_time = self.to_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instances": instances,
                "schedulingEnabled": scheduling_enabled,
                "daysOfWeek": days_of_week,
                "timezone": timezone,
                "fromTime": from_time,
                "toTime": to_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        instances = d.pop("instances")

        scheduling_enabled = d.pop("schedulingEnabled")

        days_of_week = []
        _days_of_week = d.pop("daysOfWeek")
        for days_of_week_item_data in _days_of_week:
            days_of_week_item = DominoHardwaretierApiHardwareTierOverprovisioningDtoDaysOfWeekItem(
                days_of_week_item_data
            )

            days_of_week.append(days_of_week_item)

        timezone = d.pop("timezone")

        from_time = d.pop("fromTime")

        to_time = d.pop("toTime")

        domino_hardwaretier_api_hardware_tier_overprovisioning_dto = cls(
            instances=instances,
            scheduling_enabled=scheduling_enabled,
            days_of_week=days_of_week,
            timezone=timezone,
            from_time=from_time,
            to_time=to_time,
        )

        domino_hardwaretier_api_hardware_tier_overprovisioning_dto.additional_properties = d
        return domino_hardwaretier_api_hardware_tier_overprovisioning_dto

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
