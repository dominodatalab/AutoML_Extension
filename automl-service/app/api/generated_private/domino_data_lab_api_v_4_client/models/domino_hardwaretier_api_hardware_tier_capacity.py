from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_hardwaretier_api_hardware_tier_capacity_capacity_level import (
    DominoHardwaretierApiHardwareTierCapacityCapacityLevel,
)

T = TypeVar("T", bound="DominoHardwaretierApiHardwareTierCapacity")


@_attrs_define
class DominoHardwaretierApiHardwareTierCapacity:
    """
    Attributes:
        current_number_of_executors (int):
        maximum_number_of_executors (int):
        number_of_currently_executing_runs (int):
        number_of_queued_runs (int):
        maximum_concurrent_runs (int):
        available_capacity_without_launching (int):
        maximum_available_capacity (int):
        capacity_level (DominoHardwaretierApiHardwareTierCapacityCapacityLevel):
    """

    current_number_of_executors: int
    maximum_number_of_executors: int
    number_of_currently_executing_runs: int
    number_of_queued_runs: int
    maximum_concurrent_runs: int
    available_capacity_without_launching: int
    maximum_available_capacity: int
    capacity_level: DominoHardwaretierApiHardwareTierCapacityCapacityLevel
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_number_of_executors = self.current_number_of_executors

        maximum_number_of_executors = self.maximum_number_of_executors

        number_of_currently_executing_runs = self.number_of_currently_executing_runs

        number_of_queued_runs = self.number_of_queued_runs

        maximum_concurrent_runs = self.maximum_concurrent_runs

        available_capacity_without_launching = self.available_capacity_without_launching

        maximum_available_capacity = self.maximum_available_capacity

        capacity_level = self.capacity_level.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currentNumberOfExecutors": current_number_of_executors,
                "maximumNumberOfExecutors": maximum_number_of_executors,
                "numberOfCurrentlyExecutingRuns": number_of_currently_executing_runs,
                "numberOfQueuedRuns": number_of_queued_runs,
                "maximumConcurrentRuns": maximum_concurrent_runs,
                "availableCapacityWithoutLaunching": available_capacity_without_launching,
                "maximumAvailableCapacity": maximum_available_capacity,
                "capacityLevel": capacity_level,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current_number_of_executors = d.pop("currentNumberOfExecutors")

        maximum_number_of_executors = d.pop("maximumNumberOfExecutors")

        number_of_currently_executing_runs = d.pop("numberOfCurrentlyExecutingRuns")

        number_of_queued_runs = d.pop("numberOfQueuedRuns")

        maximum_concurrent_runs = d.pop("maximumConcurrentRuns")

        available_capacity_without_launching = d.pop("availableCapacityWithoutLaunching")

        maximum_available_capacity = d.pop("maximumAvailableCapacity")

        capacity_level = DominoHardwaretierApiHardwareTierCapacityCapacityLevel(d.pop("capacityLevel"))

        domino_hardwaretier_api_hardware_tier_capacity = cls(
            current_number_of_executors=current_number_of_executors,
            maximum_number_of_executors=maximum_number_of_executors,
            number_of_currently_executing_runs=number_of_currently_executing_runs,
            number_of_queued_runs=number_of_queued_runs,
            maximum_concurrent_runs=maximum_concurrent_runs,
            available_capacity_without_launching=available_capacity_without_launching,
            maximum_available_capacity=maximum_available_capacity,
            capacity_level=capacity_level,
        )

        domino_hardwaretier_api_hardware_tier_capacity.additional_properties = d
        return domino_hardwaretier_api_hardware_tier_capacity

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
