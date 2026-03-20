from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostAllocationNetworkV2")


@_attrs_define
class CostAllocationNetworkV2:
    """
    Attributes:
        cost (float | Unset):
        cost_adjustment (float | Unset):
        cross_region_cost (float | Unset):
        cross_zone_cost (float | Unset):
        internet_cost (float | Unset):
        receive_bytes (float | Unset):
        transfer_bytes (float | Unset):
    """

    cost: float | Unset = UNSET
    cost_adjustment: float | Unset = UNSET
    cross_region_cost: float | Unset = UNSET
    cross_zone_cost: float | Unset = UNSET
    internet_cost: float | Unset = UNSET
    receive_bytes: float | Unset = UNSET
    transfer_bytes: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cost = self.cost

        cost_adjustment = self.cost_adjustment

        cross_region_cost = self.cross_region_cost

        cross_zone_cost = self.cross_zone_cost

        internet_cost = self.internet_cost

        receive_bytes = self.receive_bytes

        transfer_bytes = self.transfer_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cost is not UNSET:
            field_dict["cost"] = cost
        if cost_adjustment is not UNSET:
            field_dict["costAdjustment"] = cost_adjustment
        if cross_region_cost is not UNSET:
            field_dict["crossRegionCost"] = cross_region_cost
        if cross_zone_cost is not UNSET:
            field_dict["crossZoneCost"] = cross_zone_cost
        if internet_cost is not UNSET:
            field_dict["internetCost"] = internet_cost
        if receive_bytes is not UNSET:
            field_dict["receiveBytes"] = receive_bytes
        if transfer_bytes is not UNSET:
            field_dict["transferBytes"] = transfer_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cost = d.pop("cost", UNSET)

        cost_adjustment = d.pop("costAdjustment", UNSET)

        cross_region_cost = d.pop("crossRegionCost", UNSET)

        cross_zone_cost = d.pop("crossZoneCost", UNSET)

        internet_cost = d.pop("internetCost", UNSET)

        receive_bytes = d.pop("receiveBytes", UNSET)

        transfer_bytes = d.pop("transferBytes", UNSET)

        cost_allocation_network_v2 = cls(
            cost=cost,
            cost_adjustment=cost_adjustment,
            cross_region_cost=cross_region_cost,
            cross_zone_cost=cross_zone_cost,
            internet_cost=internet_cost,
            receive_bytes=receive_bytes,
            transfer_bytes=transfer_bytes,
        )

        cost_allocation_network_v2.additional_properties = d
        return cost_allocation_network_v2

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
