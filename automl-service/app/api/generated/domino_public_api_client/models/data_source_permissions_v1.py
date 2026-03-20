from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DataSourcePermissionsV1")


@_attrs_define
class DataSourcePermissionsV1:
    """
    Attributes:
        is_everyone (bool): If the Data Source is accessible by everyone
        user_and_organization_ids (list[str]): User and Organization IDs that can access this Data Source
    """

    is_everyone: bool
    user_and_organization_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_everyone = self.is_everyone

        user_and_organization_ids = self.user_and_organization_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isEveryone": is_everyone,
                "userAndOrganizationIds": user_and_organization_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_everyone = d.pop("isEveryone")

        user_and_organization_ids = cast(list[str], d.pop("userAndOrganizationIds"))

        data_source_permissions_v1 = cls(
            is_everyone=is_everyone,
            user_and_organization_ids=user_and_organization_ids,
        )

        data_source_permissions_v1.additional_properties = d
        return data_source_permissions_v1

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
