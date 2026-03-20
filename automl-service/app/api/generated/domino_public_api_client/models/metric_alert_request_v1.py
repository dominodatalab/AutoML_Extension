from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.target_range_v1 import TargetRangeV1


T = TypeVar("T", bound="MetricAlertRequestV1")


@_attrs_define
class MetricAlertRequestV1:
    """
    Attributes:
        metric (str): Name of the metric to send alert for
        model_monitoring_id (str): ID of the monitored model to send metric alerts for
        target_range (TargetRangeV1):
        value (float): Value of the metric
        description (str | Unset): Optional text to append to the metric alert message
    """

    metric: str
    model_monitoring_id: str
    target_range: TargetRangeV1
    value: float
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metric = self.metric

        model_monitoring_id = self.model_monitoring_id

        target_range = self.target_range.to_dict()

        value = self.value

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metric": metric,
                "modelMonitoringId": model_monitoring_id,
                "targetRange": target_range,
                "value": value,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.target_range_v1 import TargetRangeV1

        d = dict(src_dict)
        metric = d.pop("metric")

        model_monitoring_id = d.pop("modelMonitoringId")

        target_range = TargetRangeV1.from_dict(d.pop("targetRange"))

        value = d.pop("value")

        description = d.pop("description", UNSET)

        metric_alert_request_v1 = cls(
            metric=metric,
            model_monitoring_id=model_monitoring_id,
            target_range=target_range,
            value=value,
            description=description,
        )

        metric_alert_request_v1.additional_properties = d
        return metric_alert_request_v1

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
