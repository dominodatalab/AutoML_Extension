from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HardwareTierGpuConfigurationV1")


@_attrs_define
class HardwareTierGpuConfigurationV1:
    """Gpu configuration for a hardware tier

    Attributes:
        gpu_key (str):
        number_of_gpus (int):
    """

    gpu_key: str
    number_of_gpus: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gpu_key = self.gpu_key

        number_of_gpus = self.number_of_gpus

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gpuKey": gpu_key,
                "numberOfGpus": number_of_gpus,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gpu_key = d.pop("gpuKey")

        number_of_gpus = d.pop("numberOfGpus")

        hardware_tier_gpu_configuration_v1 = cls(
            gpu_key=gpu_key,
            number_of_gpus=number_of_gpus,
        )

        hardware_tier_gpu_configuration_v1.additional_properties = d
        return hardware_tier_gpu_configuration_v1

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
