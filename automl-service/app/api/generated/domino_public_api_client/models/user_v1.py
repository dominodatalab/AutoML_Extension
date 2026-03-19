from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserV1")


@_attrs_define
class UserV1:
    """
    Attributes:
        avatar_url (str):
        first_name (str):
        full_name (str):
        id (str):
        last_name (str):
        user_name (str):
        company_name (str | Unset):
        email (str | Unset):
        phone_number (str | Unset):
        roles (list[str] | Unset):
    """

    avatar_url: str
    first_name: str
    full_name: str
    id: str
    last_name: str
    user_name: str
    company_name: str | Unset = UNSET
    email: str | Unset = UNSET
    phone_number: str | Unset = UNSET
    roles: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar_url = self.avatar_url

        first_name = self.first_name

        full_name = self.full_name

        id = self.id

        last_name = self.last_name

        user_name = self.user_name

        company_name = self.company_name

        email = self.email

        phone_number = self.phone_number

        roles: list[str] | Unset = UNSET
        if not isinstance(self.roles, Unset):
            roles = self.roles

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "avatarUrl": avatar_url,
                "firstName": first_name,
                "fullName": full_name,
                "id": id,
                "lastName": last_name,
                "userName": user_name,
            }
        )
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if email is not UNSET:
            field_dict["email"] = email
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if roles is not UNSET:
            field_dict["roles"] = roles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avatar_url = d.pop("avatarUrl")

        first_name = d.pop("firstName")

        full_name = d.pop("fullName")

        id = d.pop("id")

        last_name = d.pop("lastName")

        user_name = d.pop("userName")

        company_name = d.pop("companyName", UNSET)

        email = d.pop("email", UNSET)

        phone_number = d.pop("phoneNumber", UNSET)

        roles = cast(list[str], d.pop("roles", UNSET))

        user_v1 = cls(
            avatar_url=avatar_url,
            first_name=first_name,
            full_name=full_name,
            id=id,
            last_name=last_name,
            user_name=user_name,
            company_name=company_name,
            email=email,
            phone_number=phone_number,
            roles=roles,
        )

        user_v1.additional_properties = d
        return user_v1

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
