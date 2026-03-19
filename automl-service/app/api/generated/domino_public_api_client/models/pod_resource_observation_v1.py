from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="PodResourceObservationV1")


@_attrs_define
class PodResourceObservationV1:
    """
    Attributes:
        cpu_usage_percent (float): CPU usage as percentage Example: 45.2.
        gpu_memory_usage_percent (float): GPU memory usage as a percentage of the GPU's total memory Example: 42.7.
        gpu_memory_used_bytes (float): GPU memory usage in bytes Example: 2147483648.0.
        gpu_utilization_percent (float): GPU utilization as percentage Example: 78.5.
        memory_usage_bytes (float): Memory usage in bytes Example: 1073741824.0.
        memory_usage_percent (float): Memory usage as a percentage of the container's memory limit Example: 65.3.
        timestamp (datetime.datetime): Timestamp of the observation Example: 2024-01-15T10:00:00Z.
    """

    cpu_usage_percent: float
    gpu_memory_usage_percent: float
    gpu_memory_used_bytes: float
    gpu_utilization_percent: float
    memory_usage_bytes: float
    memory_usage_percent: float
    timestamp: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpu_usage_percent = self.cpu_usage_percent

        gpu_memory_usage_percent = self.gpu_memory_usage_percent

        gpu_memory_used_bytes = self.gpu_memory_used_bytes

        gpu_utilization_percent = self.gpu_utilization_percent

        memory_usage_bytes = self.memory_usage_bytes

        memory_usage_percent = self.memory_usage_percent

        timestamp = self.timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cpuUsagePercent": cpu_usage_percent,
                "gpuMemoryUsagePercent": gpu_memory_usage_percent,
                "gpuMemoryUsedBytes": gpu_memory_used_bytes,
                "gpuUtilizationPercent": gpu_utilization_percent,
                "memoryUsageBytes": memory_usage_bytes,
                "memoryUsagePercent": memory_usage_percent,
                "timestamp": timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cpu_usage_percent = d.pop("cpuUsagePercent")

        gpu_memory_usage_percent = d.pop("gpuMemoryUsagePercent")

        gpu_memory_used_bytes = d.pop("gpuMemoryUsedBytes")

        gpu_utilization_percent = d.pop("gpuUtilizationPercent")

        memory_usage_bytes = d.pop("memoryUsageBytes")

        memory_usage_percent = d.pop("memoryUsagePercent")

        timestamp = isoparse(d.pop("timestamp"))

        pod_resource_observation_v1 = cls(
            cpu_usage_percent=cpu_usage_percent,
            gpu_memory_usage_percent=gpu_memory_usage_percent,
            gpu_memory_used_bytes=gpu_memory_used_bytes,
            gpu_utilization_percent=gpu_utilization_percent,
            memory_usage_bytes=memory_usage_bytes,
            memory_usage_percent=memory_usage_percent,
            timestamp=timestamp,
        )

        pod_resource_observation_v1.additional_properties = d
        return pod_resource_observation_v1

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
