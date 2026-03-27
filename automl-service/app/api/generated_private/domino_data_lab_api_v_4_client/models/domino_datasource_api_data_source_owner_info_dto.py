from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoDatasourceApiDataSourceOwnerInfoDto")


@_attrs_define
class DominoDatasourceApiDataSourceOwnerInfoDto:
    """
    Attributes:
        owner_name (str):
        owner_email (str):
        is_owner_admin (bool):
    """

    owner_name: str
    owner_email: str
    is_owner_admin: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        owner_name = self.owner_name

        owner_email = self.owner_email

        is_owner_admin = self.is_owner_admin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ownerName": owner_name,
                "ownerEmail": owner_email,
                "isOwnerAdmin": is_owner_admin,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        owner_name = d.pop("ownerName")

        owner_email = d.pop("ownerEmail")

        is_owner_admin = d.pop("isOwnerAdmin")

        domino_datasource_api_data_source_owner_info_dto = cls(
            owner_name=owner_name,
            owner_email=owner_email,
            is_owner_admin=is_owner_admin,
        )

        domino_datasource_api_data_source_owner_info_dto.additional_properties = d
        return domino_datasource_api_data_source_owner_info_dto

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
