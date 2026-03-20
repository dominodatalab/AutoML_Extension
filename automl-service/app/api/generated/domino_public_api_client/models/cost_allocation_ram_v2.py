from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostAllocationRamV2")


@_attrs_define
class CostAllocationRamV2:
    """
    Attributes:
        byte_hours (float | Unset):
        byte_request_average (float | Unset):
        byte_usage_average (float | Unset):
        bytes_ (float | Unset):
        cost (float | Unset):
        cost_adjustment (float | Unset):
        efficiency (float | Unset):
    """

    byte_hours: float | Unset = UNSET
    byte_request_average: float | Unset = UNSET
    byte_usage_average: float | Unset = UNSET
    bytes_: float | Unset = UNSET
    cost: float | Unset = UNSET
    cost_adjustment: float | Unset = UNSET
    efficiency: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        byte_hours = self.byte_hours

        byte_request_average = self.byte_request_average

        byte_usage_average = self.byte_usage_average

        bytes_ = self.bytes_

        cost = self.cost

        cost_adjustment = self.cost_adjustment

        efficiency = self.efficiency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if byte_hours is not UNSET:
            field_dict["byteHours"] = byte_hours
        if byte_request_average is not UNSET:
            field_dict["byteRequestAverage"] = byte_request_average
        if byte_usage_average is not UNSET:
            field_dict["byteUsageAverage"] = byte_usage_average
        if bytes_ is not UNSET:
            field_dict["bytes"] = bytes_
        if cost is not UNSET:
            field_dict["cost"] = cost
        if cost_adjustment is not UNSET:
            field_dict["costAdjustment"] = cost_adjustment
        if efficiency is not UNSET:
            field_dict["efficiency"] = efficiency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        byte_hours = d.pop("byteHours", UNSET)

        byte_request_average = d.pop("byteRequestAverage", UNSET)

        byte_usage_average = d.pop("byteUsageAverage", UNSET)

        bytes_ = d.pop("bytes", UNSET)

        cost = d.pop("cost", UNSET)

        cost_adjustment = d.pop("costAdjustment", UNSET)

        efficiency = d.pop("efficiency", UNSET)

        cost_allocation_ram_v2 = cls(
            byte_hours=byte_hours,
            byte_request_average=byte_request_average,
            byte_usage_average=byte_usage_average,
            bytes_=bytes_,
            cost=cost,
            cost_adjustment=cost_adjustment,
            efficiency=efficiency,
        )

        cost_allocation_ram_v2.additional_properties = d
        return cost_allocation_ram_v2

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
