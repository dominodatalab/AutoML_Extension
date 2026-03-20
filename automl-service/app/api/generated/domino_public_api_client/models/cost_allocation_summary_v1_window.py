from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostAllocationSummaryV1Window")


@_attrs_define
class CostAllocationSummaryV1Window:
    """
    Attributes:
        end (str | Unset):
        minutes (float | Unset):
        start (str | Unset):
    """

    end: str | Unset = UNSET
    minutes: float | Unset = UNSET
    start: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end = self.end

        minutes = self.minutes

        start = self.start

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end is not UNSET:
            field_dict["end"] = end
        if minutes is not UNSET:
            field_dict["minutes"] = minutes
        if start is not UNSET:
            field_dict["start"] = start

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        end = d.pop("end", UNSET)

        minutes = d.pop("minutes", UNSET)

        start = d.pop("start", UNSET)

        cost_allocation_summary_v1_window = cls(
            end=end,
            minutes=minutes,
            start=start,
        )

        cost_allocation_summary_v1_window.additional_properties = d
        return cost_allocation_summary_v1_window

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
