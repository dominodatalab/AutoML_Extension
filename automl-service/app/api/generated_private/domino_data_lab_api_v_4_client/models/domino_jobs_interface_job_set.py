from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_jobs_interface_job import DominoJobsInterfaceJob
    from ..models.domino_jobs_interface_job_pagination import DominoJobsInterfaceJobPagination


T = TypeVar("T", bound="DominoJobsInterfaceJobSet")


@_attrs_define
class DominoJobsInterfaceJobSet:
    """
    Attributes:
        jobs (list[DominoJobsInterfaceJob]):
        total_count (int):
        pagination (DominoJobsInterfaceJobPagination):
        domino_stat_columns (list[str]):
    """

    jobs: list[DominoJobsInterfaceJob]
    total_count: int
    pagination: DominoJobsInterfaceJobPagination
    domino_stat_columns: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        jobs = []
        for jobs_item_data in self.jobs:
            jobs_item = jobs_item_data.to_dict()
            jobs.append(jobs_item)

        total_count = self.total_count

        pagination = self.pagination.to_dict()

        domino_stat_columns = self.domino_stat_columns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jobs": jobs,
                "totalCount": total_count,
                "pagination": pagination,
                "dominoStatColumns": domino_stat_columns,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_jobs_interface_job import DominoJobsInterfaceJob
        from ..models.domino_jobs_interface_job_pagination import DominoJobsInterfaceJobPagination

        d = dict(src_dict)
        jobs = []
        _jobs = d.pop("jobs")
        for jobs_item_data in _jobs:
            jobs_item = DominoJobsInterfaceJob.from_dict(jobs_item_data)

            jobs.append(jobs_item)

        total_count = d.pop("totalCount")

        pagination = DominoJobsInterfaceJobPagination.from_dict(d.pop("pagination"))

        domino_stat_columns = cast(list[str], d.pop("dominoStatColumns"))

        domino_jobs_interface_job_set = cls(
            jobs=jobs,
            total_count=total_count,
            pagination=pagination,
            domino_stat_columns=domino_stat_columns,
        )

        domino_jobs_interface_job_set.additional_properties = d
        return domino_jobs_interface_job_set

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
