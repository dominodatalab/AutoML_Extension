from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.vllm_metrics_time_series_v1 import VllmMetricsTimeSeriesV1


T = TypeVar("T", bound="VllmTokenMetricsV1")


@_attrs_define
class VllmTokenMetricsV1:
    """
    Attributes:
        generation_tokens_total (VllmMetricsTimeSeriesV1):
        prompt_tokens_total (VllmMetricsTimeSeriesV1):
        total_generation_tokens (float): Total number of generation tokens produced across the entire queried time
            period Example: 8500.
        total_prompt_tokens (float): Total number of prompt tokens processed across the entire queried time period
            Example: 15000.
    """

    generation_tokens_total: VllmMetricsTimeSeriesV1
    prompt_tokens_total: VllmMetricsTimeSeriesV1
    total_generation_tokens: float
    total_prompt_tokens: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        generation_tokens_total = self.generation_tokens_total.to_dict()

        prompt_tokens_total = self.prompt_tokens_total.to_dict()

        total_generation_tokens = self.total_generation_tokens

        total_prompt_tokens = self.total_prompt_tokens

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "generationTokensTotal": generation_tokens_total,
                "promptTokensTotal": prompt_tokens_total,
                "totalGenerationTokens": total_generation_tokens,
                "totalPromptTokens": total_prompt_tokens,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vllm_metrics_time_series_v1 import VllmMetricsTimeSeriesV1

        d = dict(src_dict)
        generation_tokens_total = VllmMetricsTimeSeriesV1.from_dict(d.pop("generationTokensTotal"))

        prompt_tokens_total = VllmMetricsTimeSeriesV1.from_dict(d.pop("promptTokensTotal"))

        total_generation_tokens = d.pop("totalGenerationTokens")

        total_prompt_tokens = d.pop("totalPromptTokens")

        vllm_token_metrics_v1 = cls(
            generation_tokens_total=generation_tokens_total,
            prompt_tokens_total=prompt_tokens_total,
            total_generation_tokens=total_generation_tokens,
            total_prompt_tokens=total_prompt_tokens,
        )

        vllm_token_metrics_v1.additional_properties = d
        return vllm_token_metrics_v1

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
