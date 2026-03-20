from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostAssetsOverheadV2")


@_attrs_define
class CostAssetsOverheadV2:
    """
    Attributes:
        cpu_overhead_fraction (float | Unset):
        overhead_cost_fraction (float | Unset):
        ram_overhead_fraction (float | Unset):
    """

    cpu_overhead_fraction: float | Unset = UNSET
    overhead_cost_fraction: float | Unset = UNSET
    ram_overhead_fraction: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpu_overhead_fraction = self.cpu_overhead_fraction

        overhead_cost_fraction = self.overhead_cost_fraction

        ram_overhead_fraction = self.ram_overhead_fraction

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpu_overhead_fraction is not UNSET:
            field_dict["CpuOverheadFraction"] = cpu_overhead_fraction
        if overhead_cost_fraction is not UNSET:
            field_dict["OverheadCostFraction"] = overhead_cost_fraction
        if ram_overhead_fraction is not UNSET:
            field_dict["RamOverheadFraction"] = ram_overhead_fraction

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cpu_overhead_fraction = d.pop("CpuOverheadFraction", UNSET)

        overhead_cost_fraction = d.pop("OverheadCostFraction", UNSET)

        ram_overhead_fraction = d.pop("RamOverheadFraction", UNSET)

        cost_assets_overhead_v2 = cls(
            cpu_overhead_fraction=cpu_overhead_fraction,
            overhead_cost_fraction=overhead_cost_fraction,
            ram_overhead_fraction=ram_overhead_fraction,
        )

        cost_assets_overhead_v2.additional_properties = d
        return cost_assets_overhead_v2

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
