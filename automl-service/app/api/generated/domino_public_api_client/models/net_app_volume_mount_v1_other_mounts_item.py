from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NetAppVolumeMountV1OtherMountsItem")


@_attrs_define
class NetAppVolumeMountV1OtherMountsItem:
    """
    Attributes:
        mount_path (str): Path to mount the volume. Example: /path/to/other/mount.
        read_only (bool): Whether to mount the volume as read only. Example: True.
        sub_path (str | Unset): Path within the volume to mount. The entire volume will be mounted if not specified.
            Example: /other/subPath.
    """

    mount_path: str
    read_only: bool
    sub_path: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mount_path = self.mount_path

        read_only = self.read_only

        sub_path = self.sub_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mountPath": mount_path,
                "readOnly": read_only,
            }
        )
        if sub_path is not UNSET:
            field_dict["subPath"] = sub_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mount_path = d.pop("mountPath")

        read_only = d.pop("readOnly")

        sub_path = d.pop("subPath", UNSET)

        net_app_volume_mount_v1_other_mounts_item = cls(
            mount_path=mount_path,
            read_only=read_only,
            sub_path=sub_path,
        )

        net_app_volume_mount_v1_other_mounts_item.additional_properties = d
        return net_app_volume_mount_v1_other_mounts_item

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
