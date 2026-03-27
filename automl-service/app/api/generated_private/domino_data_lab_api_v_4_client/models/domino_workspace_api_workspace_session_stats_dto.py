from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoWorkspaceApiWorkspaceSessionStatsDto")


@_attrs_define
class DominoWorkspaceApiWorkspaceSessionStatsDto:
    """
    Attributes:
        run_time_sec (int):
        last_start_time (int | None | Unset):
        last_end_time (int | None | Unset):
    """

    run_time_sec: int
    last_start_time: int | None | Unset = UNSET
    last_end_time: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run_time_sec = self.run_time_sec

        last_start_time: int | None | Unset
        if isinstance(self.last_start_time, Unset):
            last_start_time = UNSET
        else:
            last_start_time = self.last_start_time

        last_end_time: int | None | Unset
        if isinstance(self.last_end_time, Unset):
            last_end_time = UNSET
        else:
            last_end_time = self.last_end_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "runTimeSec": run_time_sec,
            }
        )
        if last_start_time is not UNSET:
            field_dict["lastStartTime"] = last_start_time
        if last_end_time is not UNSET:
            field_dict["lastEndTime"] = last_end_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        run_time_sec = d.pop("runTimeSec")

        def _parse_last_start_time(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_start_time = _parse_last_start_time(d.pop("lastStartTime", UNSET))

        def _parse_last_end_time(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_end_time = _parse_last_end_time(d.pop("lastEndTime", UNSET))

        domino_workspace_api_workspace_session_stats_dto = cls(
            run_time_sec=run_time_sec,
            last_start_time=last_start_time,
            last_end_time=last_end_time,
        )

        domino_workspace_api_workspace_session_stats_dto.additional_properties = d
        return domino_workspace_api_workspace_session_stats_dto

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
