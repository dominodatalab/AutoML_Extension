from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="JobUsageV1")


@_attrs_define
class JobUsageV1:
    """
    Attributes:
        cpu_percentage (float): Max cpu usage for a job as a percentage of the total available cpu. Example: 5.
        memory_gi_b (float): Max memory usage for a job in GiB. Example: 0.73.
    """

    cpu_percentage: float
    memory_gi_b: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpu_percentage = self.cpu_percentage

        memory_gi_b = self.memory_gi_b

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cpuPercentage": cpu_percentage,
                "memoryGiB": memory_gi_b,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cpu_percentage = d.pop("cpuPercentage")

        memory_gi_b = d.pop("memoryGiB")

        job_usage_v1 = cls(
            cpu_percentage=cpu_percentage,
            memory_gi_b=memory_gi_b,
        )

        job_usage_v1.additional_properties = d
        return job_usage_v1

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
