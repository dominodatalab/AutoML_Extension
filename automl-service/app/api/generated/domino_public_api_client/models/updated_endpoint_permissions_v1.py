from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdatedEndpointPermissionsV1")


@_attrs_define
class UpdatedEndpointPermissionsV1:
    """
    Attributes:
        is_everyone_allowed (bool | Unset): If the endpoint is accessible by everyone
        user_ids (list[str] | Unset): User IDs that can access this endpoint
    """

    is_everyone_allowed: bool | Unset = UNSET
    user_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_everyone_allowed = self.is_everyone_allowed

        user_ids: list[str] | Unset = UNSET
        if not isinstance(self.user_ids, Unset):
            user_ids = self.user_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_everyone_allowed is not UNSET:
            field_dict["isEveryoneAllowed"] = is_everyone_allowed
        if user_ids is not UNSET:
            field_dict["userIds"] = user_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_everyone_allowed = d.pop("isEveryoneAllowed", UNSET)

        user_ids = cast(list[str], d.pop("userIds", UNSET))

        updated_endpoint_permissions_v1 = cls(
            is_everyone_allowed=is_everyone_allowed,
            user_ids=user_ids,
        )

        updated_endpoint_permissions_v1.additional_properties = d
        return updated_endpoint_permissions_v1

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
