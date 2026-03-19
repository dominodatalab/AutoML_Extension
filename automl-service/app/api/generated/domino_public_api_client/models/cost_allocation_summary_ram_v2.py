from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostAllocationSummaryRamV2")


@_attrs_define
class CostAllocationSummaryRamV2:
    """
    Attributes:
        byte_request_average (float | Unset):
        byte_usage_average (float | Unset):
        cost (float | Unset):
    """

    byte_request_average: float | Unset = UNSET
    byte_usage_average: float | Unset = UNSET
    cost: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        byte_request_average = self.byte_request_average

        byte_usage_average = self.byte_usage_average

        cost = self.cost

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if byte_request_average is not UNSET:
            field_dict["byteRequestAverage"] = byte_request_average
        if byte_usage_average is not UNSET:
            field_dict["byteUsageAverage"] = byte_usage_average
        if cost is not UNSET:
            field_dict["cost"] = cost

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        byte_request_average = d.pop("byteRequestAverage", UNSET)

        byte_usage_average = d.pop("byteUsageAverage", UNSET)

        cost = d.pop("cost", UNSET)

        cost_allocation_summary_ram_v2 = cls(
            byte_request_average=byte_request_average,
            byte_usage_average=byte_usage_average,
            cost=cost,
        )

        cost_allocation_summary_ram_v2.additional_properties = d
        return cost_allocation_summary_ram_v2

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
