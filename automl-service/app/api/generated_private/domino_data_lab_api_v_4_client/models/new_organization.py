from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_nucleus_organization_models_organization_member import (
        DominoNucleusOrganizationModelsOrganizationMember,
    )


T = TypeVar("T", bound="NewOrganization")


@_attrs_define
class NewOrganization:
    """
    Attributes:
        name (str | Unset): Organization name
        email (str | Unset): Organization email used to create the organization user
        members (list[DominoNucleusOrganizationModelsOrganizationMember] | Unset): List of members the organization
            should have
    """

    name: str | Unset = UNSET
    email: str | Unset = UNSET
    members: list[DominoNucleusOrganizationModelsOrganizationMember] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        email = self.email

        members: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()
                members.append(members_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if members is not UNSET:
            field_dict["members"] = members

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_nucleus_organization_models_organization_member import (
            DominoNucleusOrganizationModelsOrganizationMember,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        _members = d.pop("members", UNSET)
        members: list[DominoNucleusOrganizationModelsOrganizationMember] | Unset = UNSET
        if _members is not UNSET:
            members = []
            for members_item_data in _members:
                members_item = DominoNucleusOrganizationModelsOrganizationMember.from_dict(members_item_data)

                members.append(members_item)

        new_organization = cls(
            name=name,
            email=email,
            members=members,
        )

        new_organization.additional_properties = d
        return new_organization

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
