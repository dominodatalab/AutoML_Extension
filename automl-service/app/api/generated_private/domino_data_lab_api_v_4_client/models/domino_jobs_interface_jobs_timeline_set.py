from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_jobs_interface_jobs_timeline_record import DominoJobsInterfaceJobsTimelineRecord


T = TypeVar("T", bound="DominoJobsInterfaceJobsTimelineSet")


@_attrs_define
class DominoJobsInterfaceJobsTimelineSet:
    """
    Attributes:
        jobs_timeline (list[DominoJobsInterfaceJobsTimelineRecord]):
        domino_stat_columns (list[str]):
    """

    jobs_timeline: list[DominoJobsInterfaceJobsTimelineRecord]
    domino_stat_columns: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        jobs_timeline = []
        for jobs_timeline_item_data in self.jobs_timeline:
            jobs_timeline_item = jobs_timeline_item_data.to_dict()
            jobs_timeline.append(jobs_timeline_item)

        domino_stat_columns = self.domino_stat_columns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jobsTimeline": jobs_timeline,
                "dominoStatColumns": domino_stat_columns,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_jobs_interface_jobs_timeline_record import DominoJobsInterfaceJobsTimelineRecord

        d = dict(src_dict)
        jobs_timeline = []
        _jobs_timeline = d.pop("jobsTimeline")
        for jobs_timeline_item_data in _jobs_timeline:
            jobs_timeline_item = DominoJobsInterfaceJobsTimelineRecord.from_dict(jobs_timeline_item_data)

            jobs_timeline.append(jobs_timeline_item)

        domino_stat_columns = cast(list[str], d.pop("dominoStatColumns"))

        domino_jobs_interface_jobs_timeline_set = cls(
            jobs_timeline=jobs_timeline,
            domino_stat_columns=domino_stat_columns,
        )

        domino_jobs_interface_jobs_timeline_set.additional_properties = d
        return domino_jobs_interface_jobs_timeline_set

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
