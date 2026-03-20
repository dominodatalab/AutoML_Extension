from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.organization_role_v1 import OrganizationRoleV1

T = TypeVar("T", bound="OrganizationMemberV1")


@_attrs_define
class OrganizationMemberV1:
    """
    Attributes:
        organization_role (OrganizationRoleV1): Role of member in the organization.
        user_id (str): Id of the user in the org. Example: 6234c9542bc6731e3471ade8.
    """

    organization_role: OrganizationRoleV1
    user_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization_role = self.organization_role.value

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organizationRole": organization_role,
                "userId": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        organization_role = OrganizationRoleV1(d.pop("organizationRole"))

        user_id = d.pop("userId")

        organization_member_v1 = cls(
            organization_role=organization_role,
            user_id=user_id,
        )

        organization_member_v1.additional_properties = d
        return organization_member_v1

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
