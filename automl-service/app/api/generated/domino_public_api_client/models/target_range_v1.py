from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.target_range_v1_condition import TargetRangeV1Condition
from ..types import UNSET, Unset

T = TypeVar("T", bound="TargetRangeV1")


@_attrs_define
class TargetRangeV1:
    """
    Attributes:
        condition (TargetRangeV1Condition): Condition to evaluate metric value against upperLimit/lowerLimit
        lower_limit (float | Unset): Lower limit in the target range for a metric; lowerLimit, upperLimit, or both must
            be provided
        upper_limit (float | Unset): Upper limit in the target range for a metric; lowerLimit, upperLimit, or both must
            be provided
    """

    condition: TargetRangeV1Condition
    lower_limit: float | Unset = UNSET
    upper_limit: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        condition = self.condition.value

        lower_limit = self.lower_limit

        upper_limit = self.upper_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "condition": condition,
            }
        )
        if lower_limit is not UNSET:
            field_dict["lowerLimit"] = lower_limit
        if upper_limit is not UNSET:
            field_dict["upperLimit"] = upper_limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        condition = TargetRangeV1Condition(d.pop("condition"))

        lower_limit = d.pop("lowerLimit", UNSET)

        upper_limit = d.pop("upperLimit", UNSET)

        target_range_v1 = cls(
            condition=condition,
            lower_limit=lower_limit,
            upper_limit=upper_limit,
        )

        target_range_v1.additional_properties = d
        return target_range_v1

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
