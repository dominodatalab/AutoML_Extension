from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoDatasetrwApiDatasetRwCopyTimeEstimateDto")


@_attrs_define
class DominoDatasetrwApiDatasetRwCopyTimeEstimateDto:
    """
    Attributes:
        is_less_than_minutes_estimate (bool):
        minutes_estimate (int):
    """

    is_less_than_minutes_estimate: bool
    minutes_estimate: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_less_than_minutes_estimate = self.is_less_than_minutes_estimate

        minutes_estimate = self.minutes_estimate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isLessThanMinutesEstimate": is_less_than_minutes_estimate,
                "minutesEstimate": minutes_estimate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_less_than_minutes_estimate = d.pop("isLessThanMinutesEstimate")

        minutes_estimate = d.pop("minutesEstimate")

        domino_datasetrw_api_dataset_rw_copy_time_estimate_dto = cls(
            is_less_than_minutes_estimate=is_less_than_minutes_estimate,
            minutes_estimate=minutes_estimate,
        )

        domino_datasetrw_api_dataset_rw_copy_time_estimate_dto.additional_properties = d
        return domino_datasetrw_api_dataset_rw_copy_time_estimate_dto

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
