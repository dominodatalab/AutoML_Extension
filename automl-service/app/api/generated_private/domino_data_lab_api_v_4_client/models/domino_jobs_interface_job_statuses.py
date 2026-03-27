from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoJobsInterfaceJobStatuses")


@_attrs_define
class DominoJobsInterfaceJobStatuses:
    """
    Attributes:
        is_completed (bool):
        is_archived (bool):
        is_scheduled (bool):
        execution_status (str):
    """

    is_completed: bool
    is_archived: bool
    is_scheduled: bool
    execution_status: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_completed = self.is_completed

        is_archived = self.is_archived

        is_scheduled = self.is_scheduled

        execution_status = self.execution_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isCompleted": is_completed,
                "isArchived": is_archived,
                "isScheduled": is_scheduled,
                "executionStatus": execution_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_completed = d.pop("isCompleted")

        is_archived = d.pop("isArchived")

        is_scheduled = d.pop("isScheduled")

        execution_status = d.pop("executionStatus")

        domino_jobs_interface_job_statuses = cls(
            is_completed=is_completed,
            is_archived=is_archived,
            is_scheduled=is_scheduled,
            execution_status=execution_status,
        )

        domino_jobs_interface_job_statuses.additional_properties = d
        return domino_jobs_interface_job_statuses

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
