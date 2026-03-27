from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.run_utilization import RunUtilization


T = TypeVar("T", bound="GetRunsPerDayResponse200")


@_attrs_define
class GetRunsPerDayResponse200:
    """
    Attributes:
        runs (list[RunUtilization] | Unset):
        max_load_period_in_months (float | Unset):
    """

    runs: list[RunUtilization] | Unset = UNSET
    max_load_period_in_months: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        runs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.runs, Unset):
            runs = []
            for runs_item_data in self.runs:
                runs_item = runs_item_data.to_dict()
                runs.append(runs_item)

        max_load_period_in_months = self.max_load_period_in_months

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if runs is not UNSET:
            field_dict["runs"] = runs
        if max_load_period_in_months is not UNSET:
            field_dict["maxLoadPeriodInMonths"] = max_load_period_in_months

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_utilization import RunUtilization

        d = dict(src_dict)
        _runs = d.pop("runs", UNSET)
        runs: list[RunUtilization] | Unset = UNSET
        if _runs is not UNSET:
            runs = []
            for runs_item_data in _runs:
                runs_item = RunUtilization.from_dict(runs_item_data)

                runs.append(runs_item)

        max_load_period_in_months = d.pop("maxLoadPeriodInMonths", UNSET)

        get_runs_per_day_response_200 = cls(
            runs=runs,
            max_load_period_in_months=max_load_period_in_months,
        )

        get_runs_per_day_response_200.additional_properties = d
        return get_runs_per_day_response_200

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
