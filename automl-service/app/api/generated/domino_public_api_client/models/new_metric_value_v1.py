from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metric_tag_v1 import MetricTagV1


T = TypeVar("T", bound="NewMetricValueV1")


@_attrs_define
class NewMetricValueV1:
    """
    Attributes:
        metric (str): Name of the metric to log values for
        model_monitoring_id (str): ID of the monitored model to log metric values for
        reference_timestamp (str): Timestamp to associate the metric log entry with. Timestamp should follow the RFC3339
            format with timezone e.g. 2013-07-01T17:55:13-07:00
        value (float): Value of the metric
        tags (list[MetricTagV1] | Unset): List of tags associated with the metric
    """

    metric: str
    model_monitoring_id: str
    reference_timestamp: str
    value: float
    tags: list[MetricTagV1] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metric = self.metric

        model_monitoring_id = self.model_monitoring_id

        reference_timestamp = self.reference_timestamp

        value = self.value

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metric": metric,
                "modelMonitoringId": model_monitoring_id,
                "referenceTimestamp": reference_timestamp,
                "value": value,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metric_tag_v1 import MetricTagV1

        d = dict(src_dict)
        metric = d.pop("metric")

        model_monitoring_id = d.pop("modelMonitoringId")

        reference_timestamp = d.pop("referenceTimestamp")

        value = d.pop("value")

        _tags = d.pop("tags", UNSET)
        tags: list[MetricTagV1] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = MetricTagV1.from_dict(tags_item_data)

                tags.append(tags_item)

        new_metric_value_v1 = cls(
            metric=metric,
            model_monitoring_id=model_monitoring_id,
            reference_timestamp=reference_timestamp,
            value=value,
            tags=tags,
        )

        new_metric_value_v1.additional_properties = d
        return new_metric_value_v1

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
