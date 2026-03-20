from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.hardware_tier_capacity_v1_capacity_level import HardwareTierCapacityV1CapacityLevel

T = TypeVar("T", bound="HardwareTierCapacityV1")


@_attrs_define
class HardwareTierCapacityV1:
    """Current capacity information for a hardware tier. Note: Not necessary on requests to update a hardware tier.

    Attributes:
        available_capacity_without_launching (int):
        capacity_level (HardwareTierCapacityV1CapacityLevel):
        executing_runs (int):
        max_available_capacity (int):
        max_concurrent_runs (int):
        max_number_of_executors (int):
        number_of_executors (int):
        queued_runs (int):
    """

    available_capacity_without_launching: int
    capacity_level: HardwareTierCapacityV1CapacityLevel
    executing_runs: int
    max_available_capacity: int
    max_concurrent_runs: int
    max_number_of_executors: int
    number_of_executors: int
    queued_runs: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available_capacity_without_launching = self.available_capacity_without_launching

        capacity_level = self.capacity_level.value

        executing_runs = self.executing_runs

        max_available_capacity = self.max_available_capacity

        max_concurrent_runs = self.max_concurrent_runs

        max_number_of_executors = self.max_number_of_executors

        number_of_executors = self.number_of_executors

        queued_runs = self.queued_runs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "availableCapacityWithoutLaunching": available_capacity_without_launching,
                "capacityLevel": capacity_level,
                "executingRuns": executing_runs,
                "maxAvailableCapacity": max_available_capacity,
                "maxConcurrentRuns": max_concurrent_runs,
                "maxNumberOfExecutors": max_number_of_executors,
                "numberOfExecutors": number_of_executors,
                "queuedRuns": queued_runs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        available_capacity_without_launching = d.pop("availableCapacityWithoutLaunching")

        capacity_level = HardwareTierCapacityV1CapacityLevel(d.pop("capacityLevel"))

        executing_runs = d.pop("executingRuns")

        max_available_capacity = d.pop("maxAvailableCapacity")

        max_concurrent_runs = d.pop("maxConcurrentRuns")

        max_number_of_executors = d.pop("maxNumberOfExecutors")

        number_of_executors = d.pop("numberOfExecutors")

        queued_runs = d.pop("queuedRuns")

        hardware_tier_capacity_v1 = cls(
            available_capacity_without_launching=available_capacity_without_launching,
            capacity_level=capacity_level,
            executing_runs=executing_runs,
            max_available_capacity=max_available_capacity,
            max_concurrent_runs=max_concurrent_runs,
            max_number_of_executors=max_number_of_executors,
            number_of_executors=number_of_executors,
            queued_runs=queued_runs,
        )

        hardware_tier_capacity_v1.additional_properties = d
        return hardware_tier_capacity_v1

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
