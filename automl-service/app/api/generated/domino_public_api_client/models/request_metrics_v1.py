from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.vllm_metrics_time_series_v1 import VllmMetricsTimeSeriesV1


T = TypeVar("T", bound="RequestMetricsV1")


@_attrs_define
class RequestMetricsV1:
    """
    Attributes:
        failed_requests (VllmMetricsTimeSeriesV1):
        successful_requests (VllmMetricsTimeSeriesV1):
        total_error_count (float): Total number of failed requests (non-2xx status codes) across the entire time period
            Example: 25.
        total_requests (float): Total number of requests across the entire time period Example: 1500.
    """

    failed_requests: VllmMetricsTimeSeriesV1
    successful_requests: VllmMetricsTimeSeriesV1
    total_error_count: float
    total_requests: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        failed_requests = self.failed_requests.to_dict()

        successful_requests = self.successful_requests.to_dict()

        total_error_count = self.total_error_count

        total_requests = self.total_requests

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "failedRequests": failed_requests,
                "successfulRequests": successful_requests,
                "totalErrorCount": total_error_count,
                "totalRequests": total_requests,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vllm_metrics_time_series_v1 import VllmMetricsTimeSeriesV1

        d = dict(src_dict)
        failed_requests = VllmMetricsTimeSeriesV1.from_dict(d.pop("failedRequests"))

        successful_requests = VllmMetricsTimeSeriesV1.from_dict(d.pop("successfulRequests"))

        total_error_count = d.pop("totalErrorCount")

        total_requests = d.pop("totalRequests")

        request_metrics_v1 = cls(
            failed_requests=failed_requests,
            successful_requests=successful_requests,
            total_error_count=total_error_count,
            total_requests=total_requests,
        )

        request_metrics_v1.additional_properties = d
        return request_metrics_v1

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
