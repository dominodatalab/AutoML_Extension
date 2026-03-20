from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.registered_model_version_experiment_run_metric_v1 import RegisteredModelVersionExperimentRunMetricV1
    from ..models.registered_model_version_experiment_run_param_v1 import RegisteredModelVersionExperimentRunParamV1


T = TypeVar("T", bound="RegisteredModelVersionExperimentRunInfoV1")


@_attrs_define
class RegisteredModelVersionExperimentRunInfoV1:
    """
    Attributes:
        metrics (list[RegisteredModelVersionExperimentRunMetricV1]): Run metrics.
        params (list[RegisteredModelVersionExperimentRunParamV1]): Run parameters.
        run_url (str): The snapshotId of the dataset
    """

    metrics: list[RegisteredModelVersionExperimentRunMetricV1]
    params: list[RegisteredModelVersionExperimentRunParamV1]
    run_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metrics = []
        for metrics_item_data in self.metrics:
            metrics_item = metrics_item_data.to_dict()
            metrics.append(metrics_item)

        params = []
        for params_item_data in self.params:
            params_item = params_item_data.to_dict()
            params.append(params_item)

        run_url = self.run_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metrics": metrics,
                "params": params,
                "runUrl": run_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.registered_model_version_experiment_run_metric_v1 import (
            RegisteredModelVersionExperimentRunMetricV1,
        )
        from ..models.registered_model_version_experiment_run_param_v1 import RegisteredModelVersionExperimentRunParamV1

        d = dict(src_dict)
        metrics = []
        _metrics = d.pop("metrics")
        for metrics_item_data in _metrics:
            metrics_item = RegisteredModelVersionExperimentRunMetricV1.from_dict(metrics_item_data)

            metrics.append(metrics_item)

        params = []
        _params = d.pop("params")
        for params_item_data in _params:
            params_item = RegisteredModelVersionExperimentRunParamV1.from_dict(params_item_data)

            params.append(params_item)

        run_url = d.pop("runUrl")

        registered_model_version_experiment_run_info_v1 = cls(
            metrics=metrics,
            params=params,
            run_url=run_url,
        )

        registered_model_version_experiment_run_info_v1.additional_properties = d
        return registered_model_version_experiment_run_info_v1

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
