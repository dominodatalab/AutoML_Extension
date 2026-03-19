from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelApiVolume")


@_attrs_define
class ModelApiVolume:
    """
    Attributes:
        mount_path (str): The mount path of the volume.
        name (str): The name of the volume.
        read_only (bool): Whether the volume is read only.
        volume_type (str): The type of volume.
    """

    mount_path: str
    name: str
    read_only: bool
    volume_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mount_path = self.mount_path

        name = self.name

        read_only = self.read_only

        volume_type = self.volume_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mountPath": mount_path,
                "name": name,
                "readOnly": read_only,
                "volumeType": volume_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mount_path = d.pop("mountPath")

        name = d.pop("name")

        read_only = d.pop("readOnly")

        volume_type = d.pop("volumeType")

        model_api_volume = cls(
            mount_path=mount_path,
            name=name,
            read_only=read_only,
            volume_type=volume_type,
        )

        model_api_volume.additional_properties = d
        return model_api_volume

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
