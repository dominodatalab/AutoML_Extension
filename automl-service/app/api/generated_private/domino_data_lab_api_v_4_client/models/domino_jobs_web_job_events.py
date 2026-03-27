from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_jobs_web_job_status_change_socket_event import DominoJobsWebJobStatusChangeSocketEvent
    from ..models.domino_jobs_web_jobs_usage_socket_event import DominoJobsWebJobsUsageSocketEvent


T = TypeVar("T", bound="DominoJobsWebJobEvents")


@_attrs_define
class DominoJobsWebJobEvents:
    """
    Attributes:
        jobs_usage_event (DominoJobsWebJobsUsageSocketEvent):
        job_status_change_event (DominoJobsWebJobStatusChangeSocketEvent):
    """

    jobs_usage_event: DominoJobsWebJobsUsageSocketEvent
    job_status_change_event: DominoJobsWebJobStatusChangeSocketEvent
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        jobs_usage_event = self.jobs_usage_event.to_dict()

        job_status_change_event = self.job_status_change_event.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jobsUsageEvent": jobs_usage_event,
                "jobStatusChangeEvent": job_status_change_event,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_jobs_web_job_status_change_socket_event import DominoJobsWebJobStatusChangeSocketEvent
        from ..models.domino_jobs_web_jobs_usage_socket_event import DominoJobsWebJobsUsageSocketEvent

        d = dict(src_dict)
        jobs_usage_event = DominoJobsWebJobsUsageSocketEvent.from_dict(d.pop("jobsUsageEvent"))

        job_status_change_event = DominoJobsWebJobStatusChangeSocketEvent.from_dict(d.pop("jobStatusChangeEvent"))

        domino_jobs_web_job_events = cls(
            jobs_usage_event=jobs_usage_event,
            job_status_change_event=job_status_change_event,
        )

        domino_jobs_web_job_events.additional_properties = d
        return domino_jobs_web_job_events

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
