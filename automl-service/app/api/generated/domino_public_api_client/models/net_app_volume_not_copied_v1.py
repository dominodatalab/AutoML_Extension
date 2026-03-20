from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.net_app_volume_info_v1 import NetAppVolumeInfoV1


T = TypeVar("T", bound="NetAppVolumeNotCopiedV1")


@_attrs_define
class NetAppVolumeNotCopiedV1:
    """
    Attributes:
        error_message (str): error message explaining why volume wasn't copied
        volume_info (NetAppVolumeInfoV1):
    """

    error_message: str
    volume_info: NetAppVolumeInfoV1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_message = self.error_message

        volume_info = self.volume_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "errorMessage": error_message,
                "volumeInfo": volume_info,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.net_app_volume_info_v1 import NetAppVolumeInfoV1

        d = dict(src_dict)
        error_message = d.pop("errorMessage")

        volume_info = NetAppVolumeInfoV1.from_dict(d.pop("volumeInfo"))

        net_app_volume_not_copied_v1 = cls(
            error_message=error_message,
            volume_info=volume_info,
        )

        net_app_volume_not_copied_v1.additional_properties = d
        return net_app_volume_not_copied_v1

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
