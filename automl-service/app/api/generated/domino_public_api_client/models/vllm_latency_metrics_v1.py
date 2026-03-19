from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.vllm_metrics_time_series_v1 import VllmMetricsTimeSeriesV1


T = TypeVar("T", bound="VllmLatencyMetricsV1")


@_attrs_define
class VllmLatencyMetricsV1:
    """
    Attributes:
        average_end_to_end_latency (float): Average end-to-end latency across the entire queried time period in seconds
            Example: 1.234.
        average_time_per_output_token (float): Average time per output token across the entire queried time period in
            seconds Example: 0.056.
        average_time_to_first_token (float): Average time to first token across the entire queried time period in
            seconds Example: 0.245.
        end_to_end_latency (VllmMetricsTimeSeriesV1):
        time_per_output_token (VllmMetricsTimeSeriesV1):
        time_to_first_token (VllmMetricsTimeSeriesV1):
    """

    average_end_to_end_latency: float
    average_time_per_output_token: float
    average_time_to_first_token: float
    end_to_end_latency: VllmMetricsTimeSeriesV1
    time_per_output_token: VllmMetricsTimeSeriesV1
    time_to_first_token: VllmMetricsTimeSeriesV1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        average_end_to_end_latency = self.average_end_to_end_latency

        average_time_per_output_token = self.average_time_per_output_token

        average_time_to_first_token = self.average_time_to_first_token

        end_to_end_latency = self.end_to_end_latency.to_dict()

        time_per_output_token = self.time_per_output_token.to_dict()

        time_to_first_token = self.time_to_first_token.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "averageEndToEndLatency": average_end_to_end_latency,
                "averageTimePerOutputToken": average_time_per_output_token,
                "averageTimeToFirstToken": average_time_to_first_token,
                "endToEndLatency": end_to_end_latency,
                "timePerOutputToken": time_per_output_token,
                "timeToFirstToken": time_to_first_token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vllm_metrics_time_series_v1 import VllmMetricsTimeSeriesV1

        d = dict(src_dict)
        average_end_to_end_latency = d.pop("averageEndToEndLatency")

        average_time_per_output_token = d.pop("averageTimePerOutputToken")

        average_time_to_first_token = d.pop("averageTimeToFirstToken")

        end_to_end_latency = VllmMetricsTimeSeriesV1.from_dict(d.pop("endToEndLatency"))

        time_per_output_token = VllmMetricsTimeSeriesV1.from_dict(d.pop("timePerOutputToken"))

        time_to_first_token = VllmMetricsTimeSeriesV1.from_dict(d.pop("timeToFirstToken"))

        vllm_latency_metrics_v1 = cls(
            average_end_to_end_latency=average_end_to_end_latency,
            average_time_per_output_token=average_time_per_output_token,
            average_time_to_first_token=average_time_to_first_token,
            end_to_end_latency=end_to_end_latency,
            time_per_output_token=time_per_output_token,
            time_to_first_token=time_to_first_token,
        )

        vllm_latency_metrics_v1.additional_properties = d
        return vllm_latency_metrics_v1

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
