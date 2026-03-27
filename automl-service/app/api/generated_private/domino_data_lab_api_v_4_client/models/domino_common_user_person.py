from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoCommonUserPerson")


@_attrs_define
class DominoCommonUserPerson:
    """
    Attributes:
        last_name (str): Person last name
        first_name (str): Person first name
        avatar_url (str): Url of the person's avatar
        full_name (str): Person full name
        id (str): Person user id
        user_name (str): Person username
        phone_number (None | str | Unset): Person phone number
        idp_id (None | str | Unset):
        company_name (None | str | Unset): Person's company name
        email (None | str | Unset): Person email
    """

    last_name: str
    first_name: str
    avatar_url: str
    full_name: str
    id: str
    user_name: str
    phone_number: None | str | Unset = UNSET
    idp_id: None | str | Unset = UNSET
    company_name: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_name = self.last_name

        first_name = self.first_name

        avatar_url = self.avatar_url

        full_name = self.full_name

        id = self.id

        user_name = self.user_name

        phone_number: None | str | Unset
        if isinstance(self.phone_number, Unset):
            phone_number = UNSET
        else:
            phone_number = self.phone_number

        idp_id: None | str | Unset
        if isinstance(self.idp_id, Unset):
            idp_id = UNSET
        else:
            idp_id = self.idp_id

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lastName": last_name,
                "firstName": first_name,
                "avatarUrl": avatar_url,
                "fullName": full_name,
                "id": id,
                "userName": user_name,
            }
        )
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if idp_id is not UNSET:
            field_dict["idpId"] = idp_id
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        last_name = d.pop("lastName")

        first_name = d.pop("firstName")

        avatar_url = d.pop("avatarUrl")

        full_name = d.pop("fullName")

        id = d.pop("id")

        user_name = d.pop("userName")

        def _parse_phone_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone_number = _parse_phone_number(d.pop("phoneNumber", UNSET))

        def _parse_idp_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        idp_id = _parse_idp_id(d.pop("idpId", UNSET))

        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("companyName", UNSET))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        domino_common_user_person = cls(
            last_name=last_name,
            first_name=first_name,
            avatar_url=avatar_url,
            full_name=full_name,
            id=id,
            user_name=user_name,
            phone_number=phone_number,
            idp_id=idp_id,
            company_name=company_name,
            email=email,
        )

        domino_common_user_person.additional_properties = d
        return domino_common_user_person

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
