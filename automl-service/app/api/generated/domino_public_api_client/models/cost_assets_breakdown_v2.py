from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostAssetsBreakdownV2")


@_attrs_define
class CostAssetsBreakdownV2:
    """
    Attributes:
        idle (float | Unset):
        other (float | Unset):
        system (float | Unset):
        user (float | Unset):
    """

    idle: float | Unset = UNSET
    other: float | Unset = UNSET
    system: float | Unset = UNSET
    user: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        idle = self.idle

        other = self.other

        system = self.system

        user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if idle is not UNSET:
            field_dict["idle"] = idle
        if other is not UNSET:
            field_dict["other"] = other
        if system is not UNSET:
            field_dict["system"] = system
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        idle = d.pop("idle", UNSET)

        other = d.pop("other", UNSET)

        system = d.pop("system", UNSET)

        user = d.pop("user", UNSET)

        cost_assets_breakdown_v2 = cls(
            idle=idle,
            other=other,
            system=system,
            user=user,
        )

        cost_assets_breakdown_v2.additional_properties = d
        return cost_assets_breakdown_v2

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
