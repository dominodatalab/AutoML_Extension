from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.vllm_metric_observation_v1 import VllmMetricObservationV1


T = TypeVar("T", bound="VllmMetricsTimeSeriesV1")


@_attrs_define
class VllmMetricsTimeSeriesV1:
    """
    Attributes:
        observations (list[VllmMetricObservationV1]):
    """

    observations: list[VllmMetricObservationV1]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        observations = []
        for observations_item_data in self.observations:
            observations_item = observations_item_data.to_dict()
            observations.append(observations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "observations": observations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vllm_metric_observation_v1 import VllmMetricObservationV1

        d = dict(src_dict)
        observations = []
        _observations = d.pop("observations")
        for observations_item_data in _observations:
            observations_item = VllmMetricObservationV1.from_dict(observations_item_data)

            observations.append(observations_item)

        vllm_metrics_time_series_v1 = cls(
            observations=observations,
        )

        vllm_metrics_time_series_v1.additional_properties = d
        return vllm_metrics_time_series_v1

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
