from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.admin_auth_response import AdminAuthResponse


T = TypeVar("T", bound="AdminConfigResponse")


@_attrs_define
class AdminConfigResponse:
    """
    Attributes:
        auth (AdminAuthResponse):
        base_url (str): PPM instance base URL
        id (str): Config ID
        repos (list[str]): Enabled repository types
        created_at (str | Unset): ISO timestamp when the configuration was created
        name (str | Unset): Optional human-readable name for the PPM server
    """

    auth: AdminAuthResponse
    base_url: str
    id: str
    repos: list[str]
    created_at: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth = self.auth.to_dict()

        base_url = self.base_url

        id = self.id

        repos = self.repos

        created_at = self.created_at

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "auth": auth,
                "baseUrl": base_url,
                "id": id,
                "repos": repos,
            }
        )
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.admin_auth_response import AdminAuthResponse

        d = dict(src_dict)
        auth = AdminAuthResponse.from_dict(d.pop("auth"))

        base_url = d.pop("baseUrl")

        id = d.pop("id")

        repos = cast(list[str], d.pop("repos"))

        created_at = d.pop("createdAt", UNSET)

        name = d.pop("name", UNSET)

        admin_config_response = cls(
            auth=auth,
            base_url=base_url,
            id=id,
            repos=repos,
            created_at=created_at,
            name=name,
        )

        admin_config_response.additional_properties = d
        return admin_config_response

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
