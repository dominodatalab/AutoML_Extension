from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoCommonUserPersonDTO")


@_attrs_define
class DominoCommonUserPersonDTO:
    """
    Attributes:
        first_name (str):
        last_name (str):
        full_name (str):
        user_name (str):
        avatar_url (str):
        id (str):
        email (None | str | Unset):
        company_name (None | str | Unset):
        phone_number (None | str | Unset):
        idp_id (None | str | Unset):
    """

    first_name: str
    last_name: str
    full_name: str
    user_name: str
    avatar_url: str
    id: str
    email: None | str | Unset = UNSET
    company_name: None | str | Unset = UNSET
    phone_number: None | str | Unset = UNSET
    idp_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_name = self.first_name

        last_name = self.last_name

        full_name = self.full_name

        user_name = self.user_name

        avatar_url = self.avatar_url

        id = self.id

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "firstName": first_name,
                "lastName": last_name,
                "fullName": full_name,
                "userName": user_name,
                "avatarUrl": avatar_url,
                "id": id,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if idp_id is not UNSET:
            field_dict["idpId"] = idp_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        full_name = d.pop("fullName")

        user_name = d.pop("userName")

        avatar_url = d.pop("avatarUrl")

        id = d.pop("id")

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("companyName", UNSET))

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

        domino_common_user_person_dto = cls(
            first_name=first_name,
            last_name=last_name,
            full_name=full_name,
            user_name=user_name,
            avatar_url=avatar_url,
            id=id,
            email=email,
            company_name=company_name,
            phone_number=phone_number,
            idp_id=idp_id,
        )

        domino_common_user_person_dto.additional_properties = d
        return domino_common_user_person_dto

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
