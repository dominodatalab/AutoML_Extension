from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostAllocationV1PvPvsAdditionalProperty")


@_attrs_define
class CostAllocationV1PvPvsAdditionalProperty:
    """
    Attributes:
        byte_hours (float | Unset):
        cost (float | Unset):
    """

    byte_hours: float | Unset = UNSET
    cost: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        byte_hours = self.byte_hours

        cost = self.cost

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if byte_hours is not UNSET:
            field_dict["byteHours"] = byte_hours
        if cost is not UNSET:
            field_dict["cost"] = cost

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        byte_hours = d.pop("byteHours", UNSET)

        cost = d.pop("cost", UNSET)

        cost_allocation_v1_pv_pvs_additional_property = cls(
            byte_hours=byte_hours,
            cost=cost,
        )

        cost_allocation_v1_pv_pvs_additional_property.additional_properties = d
        return cost_allocation_v1_pv_pvs_additional_property

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
