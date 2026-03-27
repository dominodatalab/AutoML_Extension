from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_scheduledjob_api_scheduled_job_dto import DominoScheduledjobApiScheduledJobDto


T = TypeVar("T", bound="DominoScheduledjobApiScheduledJobForRequestingUserDto")


@_attrs_define
class DominoScheduledjobApiScheduledJobForRequestingUserDto:
    """
    Attributes:
        scheduled_job (DominoScheduledjobApiScheduledJobDto):
        can_edit (bool):
    """

    scheduled_job: DominoScheduledjobApiScheduledJobDto
    can_edit: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scheduled_job = self.scheduled_job.to_dict()

        can_edit = self.can_edit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scheduledJob": scheduled_job,
                "canEdit": can_edit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_scheduledjob_api_scheduled_job_dto import DominoScheduledjobApiScheduledJobDto

        d = dict(src_dict)
        scheduled_job = DominoScheduledjobApiScheduledJobDto.from_dict(d.pop("scheduledJob"))

        can_edit = d.pop("canEdit")

        domino_scheduledjob_api_scheduled_job_for_requesting_user_dto = cls(
            scheduled_job=scheduled_job,
            can_edit=can_edit,
        )

        domino_scheduledjob_api_scheduled_job_for_requesting_user_dto.additional_properties = d
        return domino_scheduledjob_api_scheduled_job_for_requesting_user_dto

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
