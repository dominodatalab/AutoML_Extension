from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_nucleus_organization_models_organization_member_role import (
    DominoNucleusOrganizationModelsOrganizationMemberRole,
)

T = TypeVar("T", bound="DominoNucleusOrganizationModelsOrganizationMember")


@_attrs_define
class DominoNucleusOrganizationModelsOrganizationMember:
    """
    Attributes:
        id (str):
        role (DominoNucleusOrganizationModelsOrganizationMemberRole):
    """

    id: str
    role: DominoNucleusOrganizationModelsOrganizationMemberRole
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        role = self.role.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        role = DominoNucleusOrganizationModelsOrganizationMemberRole(d.pop("role"))

        domino_nucleus_organization_models_organization_member = cls(
            id=id,
            role=role,
        )

        domino_nucleus_organization_models_organization_member.additional_properties = d
        return domino_nucleus_organization_models_organization_member

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
