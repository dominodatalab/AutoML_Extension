from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_organizations_api_organization_member_dto_role import (
    DominoOrganizationsApiOrganizationMemberDTORole,
)

T = TypeVar("T", bound="DominoOrganizationsApiOrganizationMemberDTO")


@_attrs_define
class DominoOrganizationsApiOrganizationMemberDTO:
    """
    Attributes:
        id (str):
        role (DominoOrganizationsApiOrganizationMemberDTORole):
    """

    id: str
    role: DominoOrganizationsApiOrganizationMemberDTORole
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

        role = DominoOrganizationsApiOrganizationMemberDTORole(d.pop("role"))

        domino_organizations_api_organization_member_dto = cls(
            id=id,
            role=role,
        )

        domino_organizations_api_organization_member_dto.additional_properties = d
        return domino_organizations_api_organization_member_dto

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
