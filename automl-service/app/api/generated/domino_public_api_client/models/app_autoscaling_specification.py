from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppAutoscalingSpecification")


@_attrs_define
class AppAutoscalingSpecification:
    """
    Attributes:
        enabled (bool):
        max_replicas (int | Unset):
        min_replicas (int | Unset):
        scale_down_stabilization_window_seconds (int | Unset):
        scale_up_stabilization_window_seconds (int | Unset):
        target_cpu_avg_utilization_pct (int | Unset):
        target_memory_avg_utilization_pct (int | Unset):
        use_session_affinity (bool | Unset):
    """

    enabled: bool
    max_replicas: int | Unset = UNSET
    min_replicas: int | Unset = UNSET
    scale_down_stabilization_window_seconds: int | Unset = UNSET
    scale_up_stabilization_window_seconds: int | Unset = UNSET
    target_cpu_avg_utilization_pct: int | Unset = UNSET
    target_memory_avg_utilization_pct: int | Unset = UNSET
    use_session_affinity: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        max_replicas = self.max_replicas

        min_replicas = self.min_replicas

        scale_down_stabilization_window_seconds = self.scale_down_stabilization_window_seconds

        scale_up_stabilization_window_seconds = self.scale_up_stabilization_window_seconds

        target_cpu_avg_utilization_pct = self.target_cpu_avg_utilization_pct

        target_memory_avg_utilization_pct = self.target_memory_avg_utilization_pct

        use_session_affinity = self.use_session_affinity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
            }
        )
        if max_replicas is not UNSET:
            field_dict["maxReplicas"] = max_replicas
        if min_replicas is not UNSET:
            field_dict["minReplicas"] = min_replicas
        if scale_down_stabilization_window_seconds is not UNSET:
            field_dict["scaleDownStabilizationWindowSeconds"] = scale_down_stabilization_window_seconds
        if scale_up_stabilization_window_seconds is not UNSET:
            field_dict["scaleUpStabilizationWindowSeconds"] = scale_up_stabilization_window_seconds
        if target_cpu_avg_utilization_pct is not UNSET:
            field_dict["targetCpuAvgUtilizationPct"] = target_cpu_avg_utilization_pct
        if target_memory_avg_utilization_pct is not UNSET:
            field_dict["targetMemoryAvgUtilizationPct"] = target_memory_avg_utilization_pct
        if use_session_affinity is not UNSET:
            field_dict["useSessionAffinity"] = use_session_affinity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        max_replicas = d.pop("maxReplicas", UNSET)

        min_replicas = d.pop("minReplicas", UNSET)

        scale_down_stabilization_window_seconds = d.pop("scaleDownStabilizationWindowSeconds", UNSET)

        scale_up_stabilization_window_seconds = d.pop("scaleUpStabilizationWindowSeconds", UNSET)

        target_cpu_avg_utilization_pct = d.pop("targetCpuAvgUtilizationPct", UNSET)

        target_memory_avg_utilization_pct = d.pop("targetMemoryAvgUtilizationPct", UNSET)

        use_session_affinity = d.pop("useSessionAffinity", UNSET)

        app_autoscaling_specification = cls(
            enabled=enabled,
            max_replicas=max_replicas,
            min_replicas=min_replicas,
            scale_down_stabilization_window_seconds=scale_down_stabilization_window_seconds,
            scale_up_stabilization_window_seconds=scale_up_stabilization_window_seconds,
            target_cpu_avg_utilization_pct=target_cpu_avg_utilization_pct,
            target_memory_avg_utilization_pct=target_memory_avg_utilization_pct,
            use_session_affinity=use_session_affinity,
        )

        app_autoscaling_specification.additional_properties = d
        return app_autoscaling_specification

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
