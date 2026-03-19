from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.environment_owner_type_v1 import EnvironmentOwnerTypeV1

T = TypeVar("T", bound="EnvironmentOwnerV1")


@_attrs_define
class EnvironmentOwnerV1:
    """
    Attributes:
        id (str): Id of owner of an environment. Example: 6231327c7a0af0281c01a69b.
        owner_type (EnvironmentOwnerTypeV1): Type of owner for an Environment. Environments can either be owned by a
            normal user or by an Organization.
        username (str): Username of owner of an environment. Example: OrgOwner.
    """

    id: str
    owner_type: EnvironmentOwnerTypeV1
    username: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        owner_type = self.owner_type.value

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "ownerType": owner_type,
                "username": username,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        owner_type = EnvironmentOwnerTypeV1(d.pop("ownerType"))

        username = d.pop("username")

        environment_owner_v1 = cls(
            id=id,
            owner_type=owner_type,
            username=username,
        )

        environment_owner_v1.additional_properties = d
        return environment_owner_v1

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
