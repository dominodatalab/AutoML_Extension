from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminConfigPatchRequest")


@_attrs_define
class AdminConfigPatchRequest:
    """Partial PPM admin configuration (all fields optional)

    Attributes:
        base_url (str | Unset): PPM instance base URL
        name (str | Unset): Optional human-readable name for the PPM server
        repos (list[str] | Unset): Enabled repository types
        token (str | Unset): Authentication token for PPM
    """

    base_url: str | Unset = UNSET
    name: str | Unset = UNSET
    repos: list[str] | Unset = UNSET
    token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_url = self.base_url

        name = self.name

        repos: list[str] | Unset = UNSET
        if not isinstance(self.repos, Unset):
            repos = self.repos

        token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_url is not UNSET:
            field_dict["baseUrl"] = base_url
        if name is not UNSET:
            field_dict["name"] = name
        if repos is not UNSET:
            field_dict["repos"] = repos
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base_url = d.pop("baseUrl", UNSET)

        name = d.pop("name", UNSET)

        repos = cast(list[str], d.pop("repos", UNSET))

        token = d.pop("token", UNSET)

        admin_config_patch_request = cls(
            base_url=base_url,
            name=name,
            repos=repos,
            token=token,
        )

        admin_config_patch_request.additional_properties = d
        return admin_config_patch_request

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
