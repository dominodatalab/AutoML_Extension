from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_assets_breakdown_v2 import CostAssetsBreakdownV2


T = TypeVar("T", bound="CostAssetsRamV2")


@_attrs_define
class CostAssetsRamV2:
    """
    Attributes:
        breakdown (CostAssetsBreakdownV2 | Unset):
        byte_hours (float | Unset):
        bytes_ (float | Unset):
        cost (float | Unset):
    """

    breakdown: CostAssetsBreakdownV2 | Unset = UNSET
    byte_hours: float | Unset = UNSET
    bytes_: float | Unset = UNSET
    cost: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        breakdown: dict[str, Any] | Unset = UNSET
        if not isinstance(self.breakdown, Unset):
            breakdown = self.breakdown.to_dict()

        byte_hours = self.byte_hours

        bytes_ = self.bytes_

        cost = self.cost

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if breakdown is not UNSET:
            field_dict["breakdown"] = breakdown
        if byte_hours is not UNSET:
            field_dict["byteHours"] = byte_hours
        if bytes_ is not UNSET:
            field_dict["bytes"] = bytes_
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

        byte_hours = d.pop("byteHours", UNSET)

        bytes_ = d.pop("bytes", UNSET)

        cost = d.pop("cost", UNSET)

        cost_assets_ram_v2 = cls(
            breakdown=breakdown,
            byte_hours=byte_hours,
            bytes_=bytes_,
            cost=cost,
        )

        cost_assets_ram_v2.additional_properties = d
        return cost_assets_ram_v2

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
