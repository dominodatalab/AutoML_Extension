from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_member_v1 import OrganizationMemberV1


T = TypeVar("T", bound="OrganizationV1")


@_attrs_define
class OrganizationV1:
    """
    Attributes:
        id (str): Organization identifier in the users collection. Example: 623132867a0af0281c01a69c.
        members (list[OrganizationMemberV1]): List of the organization members.
        name (str): Organization name. Example: MyOrg.
        default_environment_id (str | Unset): Id of the default environment used in the organization. Example:
            6231327c7a0af0281c01a65f.
    """

    id: str
    members: list[OrganizationMemberV1]
    name: str
    default_environment_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        members = []
        for members_item_data in self.members:
            members_item = members_item_data.to_dict()
            members.append(members_item)

        name = self.name

        default_environment_id = self.default_environment_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "members": members,
                "name": name,
            }
        )
        if default_environment_id is not UNSET:
            field_dict["defaultEnvironmentId"] = default_environment_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_member_v1 import OrganizationMemberV1

        d = dict(src_dict)
        id = d.pop("id")

        members = []
        _members = d.pop("members")
        for members_item_data in _members:
            members_item = OrganizationMemberV1.from_dict(members_item_data)

            members.append(members_item)

        name = d.pop("name")

        default_environment_id = d.pop("defaultEnvironmentId", UNSET)

        organization_v1 = cls(
            id=id,
            members=members,
            name=name,
            default_environment_id=default_environment_id,
        )

        organization_v1.additional_properties = d
        return organization_v1

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
