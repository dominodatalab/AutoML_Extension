from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoWorkspacesApiStageTime")


@_attrs_define
class DominoWorkspacesApiStageTime:
    """
    Attributes:
        submission_time (int):
        start_time (int | None | Unset):
        completed_time (int | None | Unset):
    """

    submission_time: int
    start_time: int | None | Unset = UNSET
    completed_time: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        submission_time = self.submission_time

        start_time: int | None | Unset
        if isinstance(self.start_time, Unset):
            start_time = UNSET
        else:
            start_time = self.start_time

        completed_time: int | None | Unset
        if isinstance(self.completed_time, Unset):
            completed_time = UNSET
        else:
            completed_time = self.completed_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "submissionTime": submission_time,
            }
        )
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if completed_time is not UNSET:
            field_dict["completedTime"] = completed_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        submission_time = d.pop("submissionTime")

        def _parse_start_time(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        start_time = _parse_start_time(d.pop("startTime", UNSET))

        def _parse_completed_time(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        completed_time = _parse_completed_time(d.pop("completedTime", UNSET))

        domino_workspaces_api_stage_time = cls(
            submission_time=submission_time,
            start_time=start_time,
            completed_time=completed_time,
        )

        domino_workspaces_api_stage_time.additional_properties = d
        return domino_workspaces_api_stage_time

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
