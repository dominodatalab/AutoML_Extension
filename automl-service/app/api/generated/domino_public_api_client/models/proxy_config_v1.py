from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProxyConfigV1")


@_attrs_define
class ProxyConfigV1:
    """
    Attributes:
        internal_path (str): Path to find workspace at. Used internally. Example:
            /{{ownerUsername}}/{{projectName}}/{{sessionPathComponent}}/{{runId}}/{{#if
            pathToOpen}}tree/{{pathToOpen}}{{/if}}.
        port (int): Port to run this tool on. Example: 8888.
        require_subdomain (bool | Unset): Whether workspace requires subdomains. Subdomain workspaces only work if
            deployment is configured to support subdomains. Defaults to false.
        rewrite (bool | Unset): If url rewriting is necessary for routing. Defaults to false
    """

    internal_path: str
    port: int
    require_subdomain: bool | Unset = UNSET
    rewrite: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        internal_path = self.internal_path

        port = self.port

        require_subdomain = self.require_subdomain

        rewrite = self.rewrite

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "internalPath": internal_path,
                "port": port,
            }
        )
        if require_subdomain is not UNSET:
            field_dict["requireSubdomain"] = require_subdomain
        if rewrite is not UNSET:
            field_dict["rewrite"] = rewrite

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        internal_path = d.pop("internalPath")

        port = d.pop("port")

        require_subdomain = d.pop("requireSubdomain", UNSET)

        rewrite = d.pop("rewrite", UNSET)

        proxy_config_v1 = cls(
            internal_path=internal_path,
            port=port,
            require_subdomain=require_subdomain,
            rewrite=rewrite,
        )

        proxy_config_v1.additional_properties = d
        return proxy_config_v1

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
