from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoScheduledjobApiCronScheduleDTO")


@_attrs_define
class DominoScheduledjobApiCronScheduleDTO:
    """
    Attributes:
        cron_string (str):
        is_custom (bool):
        human_readable_cron_string (str):
    """

    cron_string: str
    is_custom: bool
    human_readable_cron_string: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cron_string = self.cron_string

        is_custom = self.is_custom

        human_readable_cron_string = self.human_readable_cron_string

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cronString": cron_string,
                "isCustom": is_custom,
                "humanReadableCronString": human_readable_cron_string,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cron_string = d.pop("cronString")

        is_custom = d.pop("isCustom")

        human_readable_cron_string = d.pop("humanReadableCronString")

        domino_scheduledjob_api_cron_schedule_dto = cls(
            cron_string=cron_string,
            is_custom=is_custom,
            human_readable_cron_string=human_readable_cron_string,
        )

        domino_scheduledjob_api_cron_schedule_dto.additional_properties = d
        return domino_scheduledjob_api_cron_schedule_dto

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
