from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.proxy_config_v1 import ProxyConfigV1


T = TypeVar("T", bound="EnvironmentToolV1")


@_attrs_define
class EnvironmentToolV1:
    """
    Attributes:
        name (str): Name of environment tool Example: Jupyter.
        start_scripts (list[str]):
        title (str): Title of environment tool. Example: Jupyter.
        icon_url (str | Unset): Url to pull icon image from Example: /assets/images/workspace-logos/Jupyter.svg.
        proxy_config (ProxyConfigV1 | Unset):
        supported_file_extensions (list[str] | Unset):
    """

    name: str
    start_scripts: list[str]
    title: str
    icon_url: str | Unset = UNSET
    proxy_config: ProxyConfigV1 | Unset = UNSET
    supported_file_extensions: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        start_scripts = self.start_scripts

        title = self.title

        icon_url = self.icon_url

        proxy_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.proxy_config, Unset):
            proxy_config = self.proxy_config.to_dict()

        supported_file_extensions: list[str] | Unset = UNSET
        if not isinstance(self.supported_file_extensions, Unset):
            supported_file_extensions = self.supported_file_extensions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "startScripts": start_scripts,
                "title": title,
            }
        )
        if icon_url is not UNSET:
            field_dict["iconUrl"] = icon_url
        if proxy_config is not UNSET:
            field_dict["proxyConfig"] = proxy_config
        if supported_file_extensions is not UNSET:
            field_dict["supportedFileExtensions"] = supported_file_extensions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.proxy_config_v1 import ProxyConfigV1

        d = dict(src_dict)
        name = d.pop("name")

        start_scripts = cast(list[str], d.pop("startScripts"))

        title = d.pop("title")

        icon_url = d.pop("iconUrl", UNSET)

        _proxy_config = d.pop("proxyConfig", UNSET)
        proxy_config: ProxyConfigV1 | Unset
        if isinstance(_proxy_config, Unset):
            proxy_config = UNSET
        else:
            proxy_config = ProxyConfigV1.from_dict(_proxy_config)

        supported_file_extensions = cast(list[str], d.pop("supportedFileExtensions", UNSET))

        environment_tool_v1 = cls(
            name=name,
            start_scripts=start_scripts,
            title=title,
            icon_url=icon_url,
            proxy_config=proxy_config,
            supported_file_extensions=supported_file_extensions,
        )

        environment_tool_v1.additional_properties = d
        return environment_tool_v1

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
