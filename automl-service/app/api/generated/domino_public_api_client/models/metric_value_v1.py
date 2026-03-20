from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.metric_tag_v1 import MetricTagV1


T = TypeVar("T", bound="MetricValueV1")


@_attrs_define
class MetricValueV1:
    """
    Attributes:
        reference_timestamp (str): Timestamp associated with the metric log entry
        tags (list[MetricTagV1]): List of tags associated with the metric
        value (float): Value of the metric
    """

    reference_timestamp: str
    tags: list[MetricTagV1]
    value: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reference_timestamp = self.reference_timestamp

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.to_dict()
            tags.append(tags_item)

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "referenceTimestamp": reference_timestamp,
                "tags": tags,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metric_tag_v1 import MetricTagV1

        d = dict(src_dict)
        reference_timestamp = d.pop("referenceTimestamp")

        tags = []
        _tags = d.pop("tags")
        for tags_item_data in _tags:
            tags_item = MetricTagV1.from_dict(tags_item_data)

            tags.append(tags_item)

        value = d.pop("value")

        metric_value_v1 = cls(
            reference_timestamp=reference_timestamp,
            tags=tags,
            value=value,
        )

        metric_value_v1.additional_properties = d
        return metric_value_v1

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
