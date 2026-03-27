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


T = TypeVar("T", bound="Organization")


@_attrs_define
class Organization:
    """
    Attributes:
        id (str): Organization identifier
        organization_user_id (str): User id of Organization user
        name (str): Organization name
        members (list[DominoNucleusOrganizationModelsOrganizationMember]): List of the organization members
        default_environment (str | Unset): Default environment used in the organization
        legacy_default_environment (str | Unset): Legacy default environment used in the organization
    """

    id: str
    organization_user_id: str
    name: str
    members: list[DominoNucleusOrganizationModelsOrganizationMember]
    default_environment: str | Unset = UNSET
    legacy_default_environment: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        organization_user_id = self.organization_user_id

        name = self.name

        members = []
        for members_item_data in self.members:
            members_item = members_item_data.to_dict()
            members.append(members_item)

        default_environment = self.default_environment

        legacy_default_environment = self.legacy_default_environment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "organizationUserId": organization_user_id,
                "name": name,
                "members": members,
            }
        )
        if default_environment is not UNSET:
            field_dict["defaultEnvironment"] = default_environment
        if legacy_default_environment is not UNSET:
            field_dict["legacyDefaultEnvironment"] = legacy_default_environment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_nucleus_organization_models_organization_member import (
            DominoNucleusOrganizationModelsOrganizationMember,
        )

        d = dict(src_dict)
        id = d.pop("id")

        organization_user_id = d.pop("organizationUserId")

        name = d.pop("name")

        members = []
        _members = d.pop("members")
        for members_item_data in _members:
            members_item = DominoNucleusOrganizationModelsOrganizationMember.from_dict(members_item_data)

            members.append(members_item)

        default_environment = d.pop("defaultEnvironment", UNSET)

        legacy_default_environment = d.pop("legacyDefaultEnvironment", UNSET)

        organization = cls(
            id=id,
            organization_user_id=organization_user_id,
            name=name,
            members=members,
            default_environment=default_environment,
            legacy_default_environment=legacy_default_environment,
        )

        organization.additional_properties = d
        return organization

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
