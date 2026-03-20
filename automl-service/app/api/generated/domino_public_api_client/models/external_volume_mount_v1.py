from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalVolumeMountV1")


@_attrs_define
class ExternalVolumeMountV1:
    """
    Attributes:
        mount_path (str): Path to mount the external volume at. Example: /path/to/my/volume.
        name (str): Name of external volume to mount. Example: MyExternalVolume.
        read_only (bool): Whether to mount the volume as read only.
        sub_path (str | Unset): Path within the external volume to mount. The entire volume will be mounted if not
            specified. Example: /mypath.
    """

    mount_path: str
    name: str
    read_only: bool
    sub_path: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mount_path = self.mount_path

        name = self.name

        read_only = self.read_only

        sub_path = self.sub_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mountPath": mount_path,
                "name": name,
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

        name = d.pop("name")

        read_only = d.pop("readOnly")

        sub_path = d.pop("subPath", UNSET)

        external_volume_mount_v1 = cls(
            mount_path=mount_path,
            name=name,
            read_only=read_only,
            sub_path=sub_path,
        )

        external_volume_mount_v1.additional_properties = d
        return external_volume_mount_v1

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
