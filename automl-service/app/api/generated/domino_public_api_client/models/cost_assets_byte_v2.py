from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_assets_breakdown_v2 import CostAssetsBreakdownV2


T = TypeVar("T", bound="CostAssetsByteV2")


@_attrs_define
class CostAssetsByteV2:
    """
    Attributes:
        breakdown (CostAssetsBreakdownV2 | Unset):
        count (float | Unset):
        hours (float | Unset):
        hours_used (float | None | Unset):
        usage_max (float | Unset):
    """

    breakdown: CostAssetsBreakdownV2 | Unset = UNSET
    count: float | Unset = UNSET
    hours: float | Unset = UNSET
    hours_used: float | None | Unset = UNSET
    usage_max: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        breakdown: dict[str, Any] | Unset = UNSET
        if not isinstance(self.breakdown, Unset):
            breakdown = self.breakdown.to_dict()

        count = self.count

        hours = self.hours

        hours_used: float | None | Unset
        if isinstance(self.hours_used, Unset):
            hours_used = UNSET
        else:
            hours_used = self.hours_used

        usage_max = self.usage_max

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if breakdown is not UNSET:
            field_dict["breakdown"] = breakdown
        if count is not UNSET:
            field_dict["count"] = count
        if hours is not UNSET:
            field_dict["hours"] = hours
        if hours_used is not UNSET:
            field_dict["hoursUsed"] = hours_used
        if usage_max is not UNSET:
            field_dict["usageMax"] = usage_max

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

        count = d.pop("count", UNSET)

        hours = d.pop("hours", UNSET)

        def _parse_hours_used(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        hours_used = _parse_hours_used(d.pop("hoursUsed", UNSET))

        usage_max = d.pop("usageMax", UNSET)

        cost_assets_byte_v2 = cls(
            breakdown=breakdown,
            count=count,
            hours=hours,
            hours_used=hours_used,
            usage_max=usage_max,
        )

        cost_assets_byte_v2.additional_properties = d
        return cost_assets_byte_v2

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
