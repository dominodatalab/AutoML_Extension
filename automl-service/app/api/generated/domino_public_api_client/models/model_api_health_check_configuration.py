from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelApiHealthCheckConfiguration")


@_attrs_define
class ModelApiHealthCheckConfiguration:
    """
    Attributes:
        failure_threshold (int): The threshold of health check failures for the Model API.
        initial_delay_seconds (int): The initial delay of the health check for the Model API.
        period_seconds (int): The health check period for the Model API.
        timeout_seconds (int): The health check timeout for the Model API.
    """

    failure_threshold: int
    initial_delay_seconds: int
    period_seconds: int
    timeout_seconds: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        failure_threshold = self.failure_threshold

        initial_delay_seconds = self.initial_delay_seconds

        period_seconds = self.period_seconds

        timeout_seconds = self.timeout_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "failureThreshold": failure_threshold,
                "initialDelaySeconds": initial_delay_seconds,
                "periodSeconds": period_seconds,
                "timeoutSeconds": timeout_seconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        failure_threshold = d.pop("failureThreshold")

        initial_delay_seconds = d.pop("initialDelaySeconds")

        period_seconds = d.pop("periodSeconds")

        timeout_seconds = d.pop("timeoutSeconds")

        model_api_health_check_configuration = cls(
            failure_threshold=failure_threshold,
            initial_delay_seconds=initial_delay_seconds,
            period_seconds=period_seconds,
            timeout_seconds=timeout_seconds,
        )

        model_api_health_check_configuration.additional_properties = d
        return model_api_health_check_configuration

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
