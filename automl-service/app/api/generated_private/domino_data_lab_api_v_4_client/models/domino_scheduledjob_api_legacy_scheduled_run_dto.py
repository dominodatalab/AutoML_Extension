from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_scheduledjob_api_legacy_scheduled_run_dto_launch_behavior import (
    DominoScheduledjobApiLegacyScheduledRunDTOLaunchBehavior,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoScheduledjobApiLegacyScheduledRunDTO")


@_attrs_define
class DominoScheduledjobApiLegacyScheduledRunDTO:
    """
    Attributes:
        id (str):
        scheduling_user_name (str):
        schedule_time (str):
        hardware_tier_name (str):
        launch_behavior (DominoScheduledjobApiLegacyScheduledRunDTOLaunchBehavior):
        project_identity (str):
        title (None | str | Unset):
        emails_to_notify (None | str | Unset):
    """

    id: str
    scheduling_user_name: str
    schedule_time: str
    hardware_tier_name: str
    launch_behavior: DominoScheduledjobApiLegacyScheduledRunDTOLaunchBehavior
    project_identity: str
    title: None | str | Unset = UNSET
    emails_to_notify: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        scheduling_user_name = self.scheduling_user_name

        schedule_time = self.schedule_time

        hardware_tier_name = self.hardware_tier_name

        launch_behavior = self.launch_behavior.value

        project_identity = self.project_identity

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        emails_to_notify: None | str | Unset
        if isinstance(self.emails_to_notify, Unset):
            emails_to_notify = UNSET
        else:
            emails_to_notify = self.emails_to_notify

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "schedulingUserName": scheduling_user_name,
                "scheduleTime": schedule_time,
                "hardwareTierName": hardware_tier_name,
                "launchBehavior": launch_behavior,
                "projectIdentity": project_identity,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if emails_to_notify is not UNSET:
            field_dict["emailsToNotify"] = emails_to_notify

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        scheduling_user_name = d.pop("schedulingUserName")

        schedule_time = d.pop("scheduleTime")

        hardware_tier_name = d.pop("hardwareTierName")

        launch_behavior = DominoScheduledjobApiLegacyScheduledRunDTOLaunchBehavior(d.pop("launchBehavior"))

        project_identity = d.pop("projectIdentity")

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_emails_to_notify(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        emails_to_notify = _parse_emails_to_notify(d.pop("emailsToNotify", UNSET))

        domino_scheduledjob_api_legacy_scheduled_run_dto = cls(
            id=id,
            scheduling_user_name=scheduling_user_name,
            schedule_time=schedule_time,
            hardware_tier_name=hardware_tier_name,
            launch_behavior=launch_behavior,
            project_identity=project_identity,
            title=title,
            emails_to_notify=emails_to_notify,
        )

        domino_scheduledjob_api_legacy_scheduled_run_dto.additional_properties = d
        return domino_scheduledjob_api_legacy_scheduled_run_dto

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
