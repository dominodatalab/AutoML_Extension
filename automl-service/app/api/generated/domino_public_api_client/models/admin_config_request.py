from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.admin_auth_request import AdminAuthRequest


T = TypeVar("T", bound="AdminConfigRequest")


@_attrs_define
class AdminConfigRequest:
    """
    Attributes:
        auth (AdminAuthRequest):
        base_url (str): PPM instance base URL
        repos (list[str]): Enabled repository types
        id (str | Unset): Config ID (auto-generated if not provided)
        name (str | Unset): Optional human-readable name for the PPM server
    """

    auth: AdminAuthRequest
    base_url: str
    repos: list[str]
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth = self.auth.to_dict()

        base_url = self.base_url

        repos = self.repos

        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "auth": auth,
                "baseUrl": base_url,
                "repos": repos,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.admin_auth_request import AdminAuthRequest

        d = dict(src_dict)
        auth = AdminAuthRequest.from_dict(d.pop("auth"))

        base_url = d.pop("baseUrl")

        repos = cast(list[str], d.pop("repos"))

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        admin_config_request = cls(
            auth=auth,
            base_url=base_url,
            repos=repos,
            id=id,
            name=name,
        )

        admin_config_request.additional_properties = d
        return admin_config_request

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
