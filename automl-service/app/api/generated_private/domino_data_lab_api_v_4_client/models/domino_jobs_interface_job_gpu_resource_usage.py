from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoJobsInterfaceJobGpuResourceUsage")


@_attrs_define
class DominoJobsInterfaceJobGpuResourceUsage:
    """
    Attributes:
        timestamp (int):
        gpu (float):
        memory (float):
        number (int):
        driver_version (str):
        device (str):
        model_name (str):
        pod (str):
    """

    timestamp: int
    gpu: float
    memory: float
    number: int
    driver_version: str
    device: str
    model_name: str
    pod: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        gpu = self.gpu

        memory = self.memory

        number = self.number

        driver_version = self.driver_version

        device = self.device

        model_name = self.model_name

        pod = self.pod

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "gpu": gpu,
                "memory": memory,
                "number": number,
                "driverVersion": driver_version,
                "device": device,
                "modelName": model_name,
                "pod": pod,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamp = d.pop("timestamp")

        gpu = d.pop("gpu")

        memory = d.pop("memory")

        number = d.pop("number")

        driver_version = d.pop("driverVersion")

        device = d.pop("device")

        model_name = d.pop("modelName")

        pod = d.pop("pod")

        domino_jobs_interface_job_gpu_resource_usage = cls(
            timestamp=timestamp,
            gpu=gpu,
            memory=memory,
            number=number,
            driver_version=driver_version,
            device=device,
            model_name=model_name,
            pod=pod,
        )

        domino_jobs_interface_job_gpu_resource_usage.additional_properties = d
        return domino_jobs_interface_job_gpu_resource_usage

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
