from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_activity_api_schedule_job_activity_meta_data_action import (
    DominoActivityApiScheduleJobActivityMetaDataAction,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoActivityApiScheduleJobActivityMetaData")


@_attrs_define
class DominoActivityApiScheduleJobActivityMetaData:
    """
    Attributes:
        action (DominoActivityApiScheduleJobActivityMetaDataAction):
        command_to_run (str):
        cron_schedule (str):
        title (None | str | Unset):
    """

    action: DominoActivityApiScheduleJobActivityMetaDataAction
    command_to_run: str
    cron_schedule: str
    title: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        command_to_run = self.command_to_run

        cron_schedule = self.cron_schedule

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "commandToRun": command_to_run,
                "cronSchedule": cron_schedule,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = DominoActivityApiScheduleJobActivityMetaDataAction(d.pop("action"))

        command_to_run = d.pop("commandToRun")

        cron_schedule = d.pop("cronSchedule")

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        domino_activity_api_schedule_job_activity_meta_data = cls(
            action=action,
            command_to_run=command_to_run,
            cron_schedule=cron_schedule,
            title=title,
        )

        domino_activity_api_schedule_job_activity_meta_data.additional_properties = d
        return domino_activity_api_schedule_job_activity_meta_data

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
