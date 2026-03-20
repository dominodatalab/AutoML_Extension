from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="RegisteredModelVersionExperimentRunMetricV1")


@_attrs_define
class RegisteredModelVersionExperimentRunMetricV1:
    """
    Attributes:
        key (str): Key identifying this metric.
        timestamp (datetime.datetime): The timestamp at which this metric was recorded. Example:
            2022-03-12T02:13:44.467Z.
        value (float): Value associated with this metric.
    """

    key: str
    timestamp: datetime.datetime
    value: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        timestamp = self.timestamp.isoformat()

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "timestamp": timestamp,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        timestamp = isoparse(d.pop("timestamp"))

        value = d.pop("value")

        registered_model_version_experiment_run_metric_v1 = cls(
            key=key,
            timestamp=timestamp,
            value=value,
        )

        registered_model_version_experiment_run_metric_v1.additional_properties = d
        return registered_model_version_experiment_run_metric_v1

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
