from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoHardwaretierApiHardwareTierGpuConfigurationDto")


@_attrs_define
class DominoHardwaretierApiHardwareTierGpuConfigurationDto:
    """
    Attributes:
        number_of_gpus (int):
        gpu_key (str):
    """

    number_of_gpus: int
    gpu_key: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        number_of_gpus = self.number_of_gpus

        gpu_key = self.gpu_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "numberOfGpus": number_of_gpus,
                "gpuKey": gpu_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        number_of_gpus = d.pop("numberOfGpus")

        gpu_key = d.pop("gpuKey")

        domino_hardwaretier_api_hardware_tier_gpu_configuration_dto = cls(
            number_of_gpus=number_of_gpus,
            gpu_key=gpu_key,
        )

        domino_hardwaretier_api_hardware_tier_gpu_configuration_dto.additional_properties = d
        return domino_hardwaretier_api_hardware_tier_gpu_configuration_dto

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
