from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostAllocationGpuV2")


@_attrs_define
class CostAllocationGpuV2:
    """
    Attributes:
        cost (float | Unset):
        cost_adjustment (float | Unset):
        count (float | Unset):
        hours (float | Unset):
    """

    cost: float | Unset = UNSET
    cost_adjustment: float | Unset = UNSET
    count: float | Unset = UNSET
    hours: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cost = self.cost

        cost_adjustment = self.cost_adjustment

        count = self.count

        hours = self.hours

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cost is not UNSET:
            field_dict["cost"] = cost
        if cost_adjustment is not UNSET:
            field_dict["costAdjustment"] = cost_adjustment
        if count is not UNSET:
            field_dict["count"] = count
        if hours is not UNSET:
            field_dict["hours"] = hours

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cost = d.pop("cost", UNSET)

        cost_adjustment = d.pop("costAdjustment", UNSET)

        count = d.pop("count", UNSET)

        hours = d.pop("hours", UNSET)

        cost_allocation_gpu_v2 = cls(
            cost=cost,
            cost_adjustment=cost_adjustment,
            count=count,
            hours=hours,
        )

        cost_allocation_gpu_v2.additional_properties = d
        return cost_allocation_gpu_v2

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
