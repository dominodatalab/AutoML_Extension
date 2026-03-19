from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_allocation_v1_pv_pvs import CostAllocationV1PvPvs


T = TypeVar("T", bound="CostAllocationV1Pv")


@_attrs_define
class CostAllocationV1Pv:
    """
    Attributes:
        pv_byte_hours (float | Unset):
        pv_bytes (float | Unset):
        pv_cost (float | Unset):
        pv_cost_adjustment (float | Unset):
        pvs (CostAllocationV1PvPvs | Unset):
    """

    pv_byte_hours: float | Unset = UNSET
    pv_bytes: float | Unset = UNSET
    pv_cost: float | Unset = UNSET
    pv_cost_adjustment: float | Unset = UNSET
    pvs: CostAllocationV1PvPvs | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pv_byte_hours = self.pv_byte_hours

        pv_bytes = self.pv_bytes

        pv_cost = self.pv_cost

        pv_cost_adjustment = self.pv_cost_adjustment

        pvs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pvs, Unset):
            pvs = self.pvs.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pv_byte_hours is not UNSET:
            field_dict["pvByteHours"] = pv_byte_hours
        if pv_bytes is not UNSET:
            field_dict["pvBytes"] = pv_bytes
        if pv_cost is not UNSET:
            field_dict["pvCost"] = pv_cost
        if pv_cost_adjustment is not UNSET:
            field_dict["pvCostAdjustment"] = pv_cost_adjustment
        if pvs is not UNSET:
            field_dict["pvs"] = pvs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cost_allocation_v1_pv_pvs import CostAllocationV1PvPvs

        d = dict(src_dict)
        pv_byte_hours = d.pop("pvByteHours", UNSET)

        pv_bytes = d.pop("pvBytes", UNSET)

        pv_cost = d.pop("pvCost", UNSET)

        pv_cost_adjustment = d.pop("pvCostAdjustment", UNSET)

        _pvs = d.pop("pvs", UNSET)
        pvs: CostAllocationV1PvPvs | Unset
        if isinstance(_pvs, Unset):
            pvs = UNSET
        else:
            pvs = CostAllocationV1PvPvs.from_dict(_pvs)

        cost_allocation_v1_pv = cls(
            pv_byte_hours=pv_byte_hours,
            pv_bytes=pv_bytes,
            pv_cost=pv_cost,
            pv_cost_adjustment=pv_cost_adjustment,
            pvs=pvs,
        )

        cost_allocation_v1_pv.additional_properties = d
        return cost_allocation_v1_pv

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
