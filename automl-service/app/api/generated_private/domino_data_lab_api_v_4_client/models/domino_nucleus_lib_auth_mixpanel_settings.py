from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoNucleusLibAuthMixpanelSettings")


@_attrs_define
class DominoNucleusLibAuthMixpanelSettings:
    """
    Attributes:
        frontend_client_enabled (bool):
        backend_client_enabled (bool):
        token (str):
    """

    frontend_client_enabled: bool
    backend_client_enabled: bool
    token: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        frontend_client_enabled = self.frontend_client_enabled

        backend_client_enabled = self.backend_client_enabled

        token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "frontendClientEnabled": frontend_client_enabled,
                "backendClientEnabled": backend_client_enabled,
                "token": token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        frontend_client_enabled = d.pop("frontendClientEnabled")

        backend_client_enabled = d.pop("backendClientEnabled")

        token = d.pop("token")

        domino_nucleus_lib_auth_mixpanel_settings = cls(
            frontend_client_enabled=frontend_client_enabled,
            backend_client_enabled=backend_client_enabled,
            token=token,
        )

        domino_nucleus_lib_auth_mixpanel_settings.additional_properties = d
        return domino_nucleus_lib_auth_mixpanel_settings

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
