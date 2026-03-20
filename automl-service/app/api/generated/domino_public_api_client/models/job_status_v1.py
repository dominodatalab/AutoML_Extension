from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="JobStatusV1")


@_attrs_define
class JobStatusV1:
    """
    Attributes:
        execution_status (str): Current status of the job. Example: Succeeded.
        is_archived (bool): Whether a job is archived.
        is_completed (bool): Whether a job is complete. Example: True.
        is_scheduled (bool): Whether a job was started by a scheduled trigger.
    """

    execution_status: str
    is_archived: bool
    is_completed: bool
    is_scheduled: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        execution_status = self.execution_status

        is_archived = self.is_archived

        is_completed = self.is_completed

        is_scheduled = self.is_scheduled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "executionStatus": execution_status,
                "isArchived": is_archived,
                "isCompleted": is_completed,
                "isScheduled": is_scheduled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        execution_status = d.pop("executionStatus")

        is_archived = d.pop("isArchived")

        is_completed = d.pop("isCompleted")

        is_scheduled = d.pop("isScheduled")

        job_status_v1 = cls(
            execution_status=execution_status,
            is_archived=is_archived,
            is_completed=is_completed,
            is_scheduled=is_scheduled,
        )

        job_status_v1.additional_properties = d
        return job_status_v1

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
