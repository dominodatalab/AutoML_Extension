from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_allocation_pv_v2_pvs import CostAllocationPvV2Pvs


T = TypeVar("T", bound="CostAllocationPvV2")


@_attrs_define
class CostAllocationPvV2:
    """
    Attributes:
        byte_hours (float | Unset):
        bytes_ (float | Unset):
        cost (float | Unset):
        cost_adjustment (float | Unset):
        pvs (CostAllocationPvV2Pvs | Unset):
    """

    byte_hours: float | Unset = UNSET
    bytes_: float | Unset = UNSET
    cost: float | Unset = UNSET
    cost_adjustment: float | Unset = UNSET
    pvs: CostAllocationPvV2Pvs | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        byte_hours = self.byte_hours

        bytes_ = self.bytes_

        cost = self.cost

        cost_adjustment = self.cost_adjustment

        pvs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pvs, Unset):
            pvs = self.pvs.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if byte_hours is not UNSET:
            field_dict["byteHours"] = byte_hours
        if bytes_ is not UNSET:
            field_dict["bytes"] = bytes_
        if cost is not UNSET:
            field_dict["cost"] = cost
        if cost_adjustment is not UNSET:
            field_dict["costAdjustment"] = cost_adjustment
        if pvs is not UNSET:
            field_dict["pvs"] = pvs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cost_allocation_pv_v2_pvs import CostAllocationPvV2Pvs

        d = dict(src_dict)
        byte_hours = d.pop("byteHours", UNSET)

        bytes_ = d.pop("bytes", UNSET)

        cost = d.pop("cost", UNSET)

        cost_adjustment = d.pop("costAdjustment", UNSET)

        _pvs = d.pop("pvs", UNSET)
        pvs: CostAllocationPvV2Pvs | Unset
        if isinstance(_pvs, Unset):
            pvs = UNSET
        else:
            pvs = CostAllocationPvV2Pvs.from_dict(_pvs)

        cost_allocation_pv_v2 = cls(
            byte_hours=byte_hours,
            bytes_=bytes_,
            cost=cost,
            cost_adjustment=cost_adjustment,
            pvs=pvs,
        )

        cost_allocation_pv_v2.additional_properties = d
        return cost_allocation_pv_v2

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
