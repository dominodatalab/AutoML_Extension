from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoWorkspacesWebAutoSyncFrequencyRequest")


@_attrs_define
class DominoWorkspacesWebAutoSyncFrequencyRequest:
    """
    Attributes:
        project_id (str):
        enable_auto_sync (bool):
        time_in_minutes (int | None | Unset):
    """

    project_id: str
    enable_auto_sync: bool
    time_in_minutes: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        enable_auto_sync = self.enable_auto_sync

        time_in_minutes: int | None | Unset
        if isinstance(self.time_in_minutes, Unset):
            time_in_minutes = UNSET
        else:
            time_in_minutes = self.time_in_minutes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectId": project_id,
                "enableAutoSync": enable_auto_sync,
            }
        )
        if time_in_minutes is not UNSET:
            field_dict["timeInMinutes"] = time_in_minutes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = d.pop("projectId")

        enable_auto_sync = d.pop("enableAutoSync")

        def _parse_time_in_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        time_in_minutes = _parse_time_in_minutes(d.pop("timeInMinutes", UNSET))

        domino_workspaces_web_auto_sync_frequency_request = cls(
            project_id=project_id,
            enable_auto_sync=enable_auto_sync,
            time_in_minutes=time_in_minutes,
        )

        domino_workspaces_web_auto_sync_frequency_request.additional_properties = d
        return domino_workspaces_web_auto_sync_frequency_request

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
