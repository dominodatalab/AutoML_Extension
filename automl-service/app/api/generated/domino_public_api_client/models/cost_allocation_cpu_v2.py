from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostAllocationCpuV2")


@_attrs_define
class CostAllocationCpuV2:
    """
    Attributes:
        core_hours (float | Unset):
        core_request_average (float | Unset):
        core_usage_average (float | Unset):
        cores (float | Unset):
        cost (float | Unset):
        cost_adjustment (float | Unset):
        efficiency (float | Unset):
    """

    core_hours: float | Unset = UNSET
    core_request_average: float | Unset = UNSET
    core_usage_average: float | Unset = UNSET
    cores: float | Unset = UNSET
    cost: float | Unset = UNSET
    cost_adjustment: float | Unset = UNSET
    efficiency: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        core_hours = self.core_hours

        core_request_average = self.core_request_average

        core_usage_average = self.core_usage_average

        cores = self.cores

        cost = self.cost

        cost_adjustment = self.cost_adjustment

        efficiency = self.efficiency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if core_hours is not UNSET:
            field_dict["coreHours"] = core_hours
        if core_request_average is not UNSET:
            field_dict["coreRequestAverage"] = core_request_average
        if core_usage_average is not UNSET:
            field_dict["coreUsageAverage"] = core_usage_average
        if cores is not UNSET:
            field_dict["cores"] = cores
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
        core_hours = d.pop("coreHours", UNSET)

        core_request_average = d.pop("coreRequestAverage", UNSET)

        core_usage_average = d.pop("coreUsageAverage", UNSET)

        cores = d.pop("cores", UNSET)

        cost = d.pop("cost", UNSET)

        cost_adjustment = d.pop("costAdjustment", UNSET)

        efficiency = d.pop("efficiency", UNSET)

        cost_allocation_cpu_v2 = cls(
            core_hours=core_hours,
            core_request_average=core_request_average,
            core_usage_average=core_usage_average,
            cores=cores,
            cost=cost,
            cost_adjustment=cost_adjustment,
            efficiency=efficiency,
        )

        cost_allocation_cpu_v2.additional_properties = d
        return cost_allocation_cpu_v2

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
