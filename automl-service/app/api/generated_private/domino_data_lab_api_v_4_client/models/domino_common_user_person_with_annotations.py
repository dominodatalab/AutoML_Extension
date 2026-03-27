from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_common_user_organization_membership import DominoCommonUserOrganizationMembership


T = TypeVar("T", bound="DominoCommonUserPersonWithAnnotations")


@_attrs_define
class DominoCommonUserPersonWithAnnotations:
    """
    Attributes:
        last_name (str): Person last name
        avatar_url (str): Url of the person's avatar
        roles (list[str]):
        full_name (str): Person full name
        user_name (str): Person username
        first_name (str): Person first name
        organizations (list[DominoCommonUserOrganizationMembership]):
        id (str): Person user id
        idp_id (None | str | Unset):
        company_name (None | str | Unset): Person's company name
        phone_number (None | str | Unset): Person phone number
        email (None | str | Unset): Person email
    """

    last_name: str
    avatar_url: str
    roles: list[str]
    full_name: str
    user_name: str
    first_name: str
    organizations: list[DominoCommonUserOrganizationMembership]
    id: str
    idp_id: None | str | Unset = UNSET
    company_name: None | str | Unset = UNSET
    phone_number: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_name = self.last_name

        avatar_url = self.avatar_url

        roles = self.roles

        full_name = self.full_name

        user_name = self.user_name

        first_name = self.first_name

        organizations = []
        for organizations_item_data in self.organizations:
            organizations_item = organizations_item_data.to_dict()
            organizations.append(organizations_item)

        id = self.id

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

        phone_number: None | str | Unset
        if isinstance(self.phone_number, Unset):
            phone_number = UNSET
        else:
            phone_number = self.phone_number

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
                "avatarUrl": avatar_url,
                "roles": roles,
                "fullName": full_name,
                "userName": user_name,
                "firstName": first_name,
                "organizations": organizations,
                "id": id,
            }
        )
        if idp_id is not UNSET:
            field_dict["idpId"] = idp_id
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_common_user_organization_membership import DominoCommonUserOrganizationMembership

        d = dict(src_dict)
        last_name = d.pop("lastName")

        avatar_url = d.pop("avatarUrl")

        roles = cast(list[str], d.pop("roles"))

        full_name = d.pop("fullName")

        user_name = d.pop("userName")

        first_name = d.pop("firstName")

        organizations = []
        _organizations = d.pop("organizations")
        for organizations_item_data in _organizations:
            organizations_item = DominoCommonUserOrganizationMembership.from_dict(organizations_item_data)

            organizations.append(organizations_item)

        id = d.pop("id")

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

        def _parse_phone_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone_number = _parse_phone_number(d.pop("phoneNumber", UNSET))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        domino_common_user_person_with_annotations = cls(
            last_name=last_name,
            avatar_url=avatar_url,
            roles=roles,
            full_name=full_name,
            user_name=user_name,
            first_name=first_name,
            organizations=organizations,
            id=id,
            idp_id=idp_id,
            company_name=company_name,
            phone_number=phone_number,
            email=email,
        )

        domino_common_user_person_with_annotations.additional_properties = d
        return domino_common_user_person_with_annotations

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
