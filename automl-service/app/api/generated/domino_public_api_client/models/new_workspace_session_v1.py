from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewWorkspaceSessionV1")


@_attrs_define
class NewWorkspaceSessionV1:
    """
    Attributes:
        external_volume_mounts (list[str]):
        net_app_volume_mounts (list[str] | Unset):
    """

    external_volume_mounts: list[str]
    net_app_volume_mounts: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_volume_mounts = self.external_volume_mounts

        net_app_volume_mounts: list[str] | Unset = UNSET
        if not isinstance(self.net_app_volume_mounts, Unset):
            net_app_volume_mounts = self.net_app_volume_mounts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "externalVolumeMounts": external_volume_mounts,
            }
        )
        if net_app_volume_mounts is not UNSET:
            field_dict["netAppVolumeMounts"] = net_app_volume_mounts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        external_volume_mounts = cast(list[str], d.pop("externalVolumeMounts"))

        net_app_volume_mounts = cast(list[str], d.pop("netAppVolumeMounts", UNSET))

        new_workspace_session_v1 = cls(
            external_volume_mounts=external_volume_mounts,
            net_app_volume_mounts=net_app_volume_mounts,
        )

        new_workspace_session_v1.additional_properties = d
        return new_workspace_session_v1

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
