from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelEndpointConfigurationV1")


@_attrs_define
class ModelEndpointConfigurationV1:
    """
    Attributes:
        max_number_of_sequences (int | Unset): The maximum number of sequences (requests) processed in parallel Example:
            256.
        served_model_name (str | Unset): The name used when calling the endpoint Example: my-model.
        tensor_parallelism (int | Unset): The number of GPUs used to split the model for faster inference Example: 1.
        vllm_arguments (str | Unset): The arguments passed to the vLLM binary Example: --max-model-length 4095 --gpu-
            memory-utilization 0.90.
    """

    max_number_of_sequences: int | Unset = UNSET
    served_model_name: str | Unset = UNSET
    tensor_parallelism: int | Unset = UNSET
    vllm_arguments: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_number_of_sequences = self.max_number_of_sequences

        served_model_name = self.served_model_name

        tensor_parallelism = self.tensor_parallelism

        vllm_arguments = self.vllm_arguments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_number_of_sequences is not UNSET:
            field_dict["maxNumberOfSequences"] = max_number_of_sequences
        if served_model_name is not UNSET:
            field_dict["servedModelName"] = served_model_name
        if tensor_parallelism is not UNSET:
            field_dict["tensorParallelism"] = tensor_parallelism
        if vllm_arguments is not UNSET:
            field_dict["vllmArguments"] = vllm_arguments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_number_of_sequences = d.pop("maxNumberOfSequences", UNSET)

        served_model_name = d.pop("servedModelName", UNSET)

        tensor_parallelism = d.pop("tensorParallelism", UNSET)

        vllm_arguments = d.pop("vllmArguments", UNSET)

        model_endpoint_configuration_v1 = cls(
            max_number_of_sequences=max_number_of_sequences,
            served_model_name=served_model_name,
            tensor_parallelism=tensor_parallelism,
            vllm_arguments=vllm_arguments,
        )

        model_endpoint_configuration_v1.additional_properties = d
        return model_endpoint_configuration_v1

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
