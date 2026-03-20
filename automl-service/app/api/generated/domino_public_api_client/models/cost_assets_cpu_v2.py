from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_assets_breakdown_v2 import CostAssetsBreakdownV2


T = TypeVar("T", bound="CostAssetsCpuV2")


@_attrs_define
class CostAssetsCpuV2:
    """
    Attributes:
        breakdown (CostAssetsBreakdownV2 | Unset):
        core_hours (float | Unset):
        cores (float | Unset):
        cost (float | Unset):
    """

    breakdown: CostAssetsBreakdownV2 | Unset = UNSET
    core_hours: float | Unset = UNSET
    cores: float | Unset = UNSET
    cost: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        breakdown: dict[str, Any] | Unset = UNSET
        if not isinstance(self.breakdown, Unset):
            breakdown = self.breakdown.to_dict()

        core_hours = self.core_hours

        cores = self.cores

        cost = self.cost

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if breakdown is not UNSET:
            field_dict["breakdown"] = breakdown
        if core_hours is not UNSET:
            field_dict["coreHours"] = core_hours
        if cores is not UNSET:
            field_dict["cores"] = cores
        if cost is not UNSET:
            field_dict["cost"] = cost

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cost_assets_breakdown_v2 import CostAssetsBreakdownV2

        d = dict(src_dict)
        _breakdown = d.pop("breakdown", UNSET)
        breakdown: CostAssetsBreakdownV2 | Unset
        if isinstance(_breakdown, Unset):
            breakdown = UNSET
        else:
            breakdown = CostAssetsBreakdownV2.from_dict(_breakdown)

        core_hours = d.pop("coreHours", UNSET)

        cores = d.pop("cores", UNSET)

        cost = d.pop("cost", UNSET)

        cost_assets_cpu_v2 = cls(
            breakdown=breakdown,
            core_hours=core_hours,
            cores=cores,
            cost=cost,
        )

        cost_assets_cpu_v2.additional_properties = d
        return cost_assets_cpu_v2

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
