from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_jobs_interface_jobs_timeline_diagnostic_stat_record import (
        DominoJobsInterfaceJobsTimelineDiagnosticStatRecord,
    )


T = TypeVar("T", bound="DominoJobsInterfaceJobsTimelineRecord")


@_attrs_define
class DominoJobsInterfaceJobsTimelineRecord:
    """
    Attributes:
        job_number (int):
        job_id (str):
        job_start_time (int):
        job_title (str):
        job_status (str):
        diagnostic_stats (list[DominoJobsInterfaceJobsTimelineDiagnosticStatRecord]):
    """

    job_number: int
    job_id: str
    job_start_time: int
    job_title: str
    job_status: str
    diagnostic_stats: list[DominoJobsInterfaceJobsTimelineDiagnosticStatRecord]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_number = self.job_number

        job_id = self.job_id

        job_start_time = self.job_start_time

        job_title = self.job_title

        job_status = self.job_status

        diagnostic_stats = []
        for diagnostic_stats_item_data in self.diagnostic_stats:
            diagnostic_stats_item = diagnostic_stats_item_data.to_dict()
            diagnostic_stats.append(diagnostic_stats_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jobNumber": job_number,
                "jobId": job_id,
                "jobStartTime": job_start_time,
                "jobTitle": job_title,
                "jobStatus": job_status,
                "diagnosticStats": diagnostic_stats,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_jobs_interface_jobs_timeline_diagnostic_stat_record import (
            DominoJobsInterfaceJobsTimelineDiagnosticStatRecord,
        )

        d = dict(src_dict)
        job_number = d.pop("jobNumber")

        job_id = d.pop("jobId")

        job_start_time = d.pop("jobStartTime")

        job_title = d.pop("jobTitle")

        job_status = d.pop("jobStatus")

        diagnostic_stats = []
        _diagnostic_stats = d.pop("diagnosticStats")
        for diagnostic_stats_item_data in _diagnostic_stats:
            diagnostic_stats_item = DominoJobsInterfaceJobsTimelineDiagnosticStatRecord.from_dict(
                diagnostic_stats_item_data
            )

            diagnostic_stats.append(diagnostic_stats_item)

        domino_jobs_interface_jobs_timeline_record = cls(
            job_number=job_number,
            job_id=job_id,
            job_start_time=job_start_time,
            job_title=job_title,
            job_status=job_status,
            diagnostic_stats=diagnostic_stats,
        )

        domino_jobs_interface_jobs_timeline_record.additional_properties = d
        return domino_jobs_interface_jobs_timeline_record

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
