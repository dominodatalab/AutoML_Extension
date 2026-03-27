from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoGruzApiHttpProxyConfig")


@_attrs_define
class DominoGruzApiHttpProxyConfig:
    """
    Attributes:
        port (int):
        internal_path (str):
        rewrite (bool):
        require_subdomain (bool):
    """

    port: int
    internal_path: str
    rewrite: bool
    require_subdomain: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        internal_path = self.internal_path

        rewrite = self.rewrite

        require_subdomain = self.require_subdomain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "port": port,
                "internalPath": internal_path,
                "rewrite": rewrite,
                "requireSubdomain": require_subdomain,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        port = d.pop("port")

        internal_path = d.pop("internalPath")

        rewrite = d.pop("rewrite")

        require_subdomain = d.pop("requireSubdomain")

        domino_gruz_api_http_proxy_config = cls(
            port=port,
            internal_path=internal_path,
            rewrite=rewrite,
            require_subdomain=require_subdomain,
        )

        domino_gruz_api_http_proxy_config.additional_properties = d
        return domino_gruz_api_http_proxy_config

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
