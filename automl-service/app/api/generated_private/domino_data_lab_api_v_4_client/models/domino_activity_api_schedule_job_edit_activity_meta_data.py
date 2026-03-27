from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_activity_api_schedule_job_edit_activity_meta_data_action import (
    DominoActivityApiScheduleJobEditActivityMetaDataAction,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoActivityApiScheduleJobEditActivityMetaData")


@_attrs_define
class DominoActivityApiScheduleJobEditActivityMetaData:
    """
    Attributes:
        action (DominoActivityApiScheduleJobEditActivityMetaDataAction):
        from_command_to_run (str):
        from_cron_schedule (str):
        to_command_to_run (str):
        to_cron_schedule (str):
        from_title (None | str | Unset):
        to_title (None | str | Unset):
    """

    action: DominoActivityApiScheduleJobEditActivityMetaDataAction
    from_command_to_run: str
    from_cron_schedule: str
    to_command_to_run: str
    to_cron_schedule: str
    from_title: None | str | Unset = UNSET
    to_title: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        from_command_to_run = self.from_command_to_run

        from_cron_schedule = self.from_cron_schedule

        to_command_to_run = self.to_command_to_run

        to_cron_schedule = self.to_cron_schedule

        from_title: None | str | Unset
        if isinstance(self.from_title, Unset):
            from_title = UNSET
        else:
            from_title = self.from_title

        to_title: None | str | Unset
        if isinstance(self.to_title, Unset):
            to_title = UNSET
        else:
            to_title = self.to_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "fromCommandToRun": from_command_to_run,
                "fromCronSchedule": from_cron_schedule,
                "toCommandToRun": to_command_to_run,
                "toCronSchedule": to_cron_schedule,
            }
        )
        if from_title is not UNSET:
            field_dict["fromTitle"] = from_title
        if to_title is not UNSET:
            field_dict["toTitle"] = to_title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = DominoActivityApiScheduleJobEditActivityMetaDataAction(d.pop("action"))

        from_command_to_run = d.pop("fromCommandToRun")

        from_cron_schedule = d.pop("fromCronSchedule")

        to_command_to_run = d.pop("toCommandToRun")

        to_cron_schedule = d.pop("toCronSchedule")

        def _parse_from_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_title = _parse_from_title(d.pop("fromTitle", UNSET))

        def _parse_to_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        to_title = _parse_to_title(d.pop("toTitle", UNSET))

        domino_activity_api_schedule_job_edit_activity_meta_data = cls(
            action=action,
            from_command_to_run=from_command_to_run,
            from_cron_schedule=from_cron_schedule,
            to_command_to_run=to_command_to_run,
            to_cron_schedule=to_cron_schedule,
            from_title=from_title,
            to_title=to_title,
        )

        domino_activity_api_schedule_job_edit_activity_meta_data.additional_properties = d
        return domino_activity_api_schedule_job_edit_activity_meta_data

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
