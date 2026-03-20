from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="StageTimesV1")


@_attrs_define
class StageTimesV1:
    """
    Attributes:
        submission_time (datetime.datetime): When the start job request was submitted. Example:
            2022-03-12T02:13:44.467Z.
        completed_time (datetime.datetime | Unset): When the job completed Example: 2022-03-12T02:16:43.127Z.
        start_time (datetime.datetime | Unset): When the job started Example: 2022-03-12T02:15:44.848Z.
    """

    submission_time: datetime.datetime
    completed_time: datetime.datetime | Unset = UNSET
    start_time: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        submission_time = self.submission_time.isoformat()

        completed_time: str | Unset = UNSET
        if not isinstance(self.completed_time, Unset):
            completed_time = self.completed_time.isoformat()

        start_time: str | Unset = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "submissionTime": submission_time,
            }
        )
        if completed_time is not UNSET:
            field_dict["completedTime"] = completed_time
        if start_time is not UNSET:
            field_dict["startTime"] = start_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        submission_time = isoparse(d.pop("submissionTime"))

        _completed_time = d.pop("completedTime", UNSET)
        completed_time: datetime.datetime | Unset
        if isinstance(_completed_time, Unset):
            completed_time = UNSET
        else:
            completed_time = isoparse(_completed_time)

        _start_time = d.pop("startTime", UNSET)
        start_time: datetime.datetime | Unset
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        stage_times_v1 = cls(
            submission_time=submission_time,
            completed_time=completed_time,
            start_time=start_time,
        )

        stage_times_v1.additional_properties = d
        return stage_times_v1

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
