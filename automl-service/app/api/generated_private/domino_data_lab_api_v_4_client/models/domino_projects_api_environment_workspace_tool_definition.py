from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_api_proxy_config import DominoProjectsApiProxyConfig


T = TypeVar("T", bound="DominoProjectsApiEnvironmentWorkspaceToolDefinition")


@_attrs_define
class DominoProjectsApiEnvironmentWorkspaceToolDefinition:
    """
    Attributes:
        id (str):
        name (str):
        title (str):
        start (list[str]):
        icon_url (None | str | Unset):
        proxy_config (DominoProjectsApiProxyConfig | Unset):
        supported_file_extensions (list[str] | None | Unset):
    """

    id: str
    name: str
    title: str
    start: list[str]
    icon_url: None | str | Unset = UNSET
    proxy_config: DominoProjectsApiProxyConfig | Unset = UNSET
    supported_file_extensions: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        title = self.title

        start = self.start

        icon_url: None | str | Unset
        if isinstance(self.icon_url, Unset):
            icon_url = UNSET
        else:
            icon_url = self.icon_url

        proxy_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.proxy_config, Unset):
            proxy_config = self.proxy_config.to_dict()

        supported_file_extensions: list[str] | None | Unset
        if isinstance(self.supported_file_extensions, Unset):
            supported_file_extensions = UNSET
        elif isinstance(self.supported_file_extensions, list):
            supported_file_extensions = self.supported_file_extensions

        else:
            supported_file_extensions = self.supported_file_extensions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "title": title,
                "start": start,
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
        from ..models.domino_projects_api_proxy_config import DominoProjectsApiProxyConfig

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        title = d.pop("title")

        start = cast(list[str], d.pop("start"))

        def _parse_icon_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon_url = _parse_icon_url(d.pop("iconUrl", UNSET))

        _proxy_config = d.pop("proxyConfig", UNSET)
        proxy_config: DominoProjectsApiProxyConfig | Unset
        if isinstance(_proxy_config, Unset):
            proxy_config = UNSET
        else:
            proxy_config = DominoProjectsApiProxyConfig.from_dict(_proxy_config)

        def _parse_supported_file_extensions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                supported_file_extensions_type_0 = cast(list[str], data)

                return supported_file_extensions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        supported_file_extensions = _parse_supported_file_extensions(d.pop("supportedFileExtensions", UNSET))

        domino_projects_api_environment_workspace_tool_definition = cls(
            id=id,
            name=name,
            title=title,
            start=start,
            icon_url=icon_url,
            proxy_config=proxy_config,
            supported_file_extensions=supported_file_extensions,
        )

        domino_projects_api_environment_workspace_tool_definition.additional_properties = d
        return domino_projects_api_environment_workspace_tool_definition

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
