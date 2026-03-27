from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoWorkspacesApiWorkspaceAutoSync")


@_attrs_define
class DominoWorkspacesApiWorkspaceAutoSync:
    """
    Attributes:
        enable (bool):
        sync_frequency_in_minutes (int | None | Unset):
    """

    enable: bool
    sync_frequency_in_minutes: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        sync_frequency_in_minutes: int | None | Unset
        if isinstance(self.sync_frequency_in_minutes, Unset):
            sync_frequency_in_minutes = UNSET
        else:
            sync_frequency_in_minutes = self.sync_frequency_in_minutes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
            }
        )
        if sync_frequency_in_minutes is not UNSET:
            field_dict["syncFrequencyInMinutes"] = sync_frequency_in_minutes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable = d.pop("enable")

        def _parse_sync_frequency_in_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sync_frequency_in_minutes = _parse_sync_frequency_in_minutes(d.pop("syncFrequencyInMinutes", UNSET))

        domino_workspaces_api_workspace_auto_sync = cls(
            enable=enable,
            sync_frequency_in_minutes=sync_frequency_in_minutes,
        )

        domino_workspaces_api_workspace_auto_sync.additional_properties = d
        return domino_workspaces_api_workspace_auto_sync

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
