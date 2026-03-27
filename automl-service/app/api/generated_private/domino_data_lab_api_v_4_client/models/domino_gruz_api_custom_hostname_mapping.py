from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoGruzApiCustomHostnameMapping")


@_attrs_define
class DominoGruzApiCustomHostnameMapping:
    """
    Attributes:
        hostname (str):
        target_ip (str):
    """

    hostname: str
    target_ip: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hostname = self.hostname

        target_ip = self.target_ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hostname": hostname,
                "targetIp": target_ip,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hostname = d.pop("hostname")

        target_ip = d.pop("targetIp")

        domino_gruz_api_custom_hostname_mapping = cls(
            hostname=hostname,
            target_ip=target_ip,
        )

        domino_gruz_api_custom_hostname_mapping.additional_properties = d
        return domino_gruz_api_custom_hostname_mapping

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
