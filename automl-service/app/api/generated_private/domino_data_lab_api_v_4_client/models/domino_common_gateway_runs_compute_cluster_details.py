from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoCommonGatewayRunsComputeClusterDetails")


@_attrs_define
class DominoCommonGatewayRunsComputeClusterDetails:
    """
    Attributes:
        compute_cluster_type (str):
        average_worker_count (float):
        worker_hardware_tier_id (str):
        worker_hardware_tier_cost_per_minute (float):
        master_hardware_tier_id (None | str | Unset):
        master_hardware_tier_cost_per_minute (float | None | Unset):
    """

    compute_cluster_type: str
    average_worker_count: float
    worker_hardware_tier_id: str
    worker_hardware_tier_cost_per_minute: float
    master_hardware_tier_id: None | str | Unset = UNSET
    master_hardware_tier_cost_per_minute: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        compute_cluster_type = self.compute_cluster_type

        average_worker_count = self.average_worker_count

        worker_hardware_tier_id = self.worker_hardware_tier_id

        worker_hardware_tier_cost_per_minute = self.worker_hardware_tier_cost_per_minute

        master_hardware_tier_id: None | str | Unset
        if isinstance(self.master_hardware_tier_id, Unset):
            master_hardware_tier_id = UNSET
        else:
            master_hardware_tier_id = self.master_hardware_tier_id

        master_hardware_tier_cost_per_minute: float | None | Unset
        if isinstance(self.master_hardware_tier_cost_per_minute, Unset):
            master_hardware_tier_cost_per_minute = UNSET
        else:
            master_hardware_tier_cost_per_minute = self.master_hardware_tier_cost_per_minute

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "computeClusterType": compute_cluster_type,
                "averageWorkerCount": average_worker_count,
                "workerHardwareTierId": worker_hardware_tier_id,
                "workerHardwareTierCostPerMinute": worker_hardware_tier_cost_per_minute,
            }
        )
        if master_hardware_tier_id is not UNSET:
            field_dict["masterHardwareTierId"] = master_hardware_tier_id
        if master_hardware_tier_cost_per_minute is not UNSET:
            field_dict["masterHardwareTierCostPerMinute"] = master_hardware_tier_cost_per_minute

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        compute_cluster_type = d.pop("computeClusterType")

        average_worker_count = d.pop("averageWorkerCount")

        worker_hardware_tier_id = d.pop("workerHardwareTierId")

        worker_hardware_tier_cost_per_minute = d.pop("workerHardwareTierCostPerMinute")

        def _parse_master_hardware_tier_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        master_hardware_tier_id = _parse_master_hardware_tier_id(d.pop("masterHardwareTierId", UNSET))

        def _parse_master_hardware_tier_cost_per_minute(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        master_hardware_tier_cost_per_minute = _parse_master_hardware_tier_cost_per_minute(
            d.pop("masterHardwareTierCostPerMinute", UNSET)
        )

        domino_common_gateway_runs_compute_cluster_details = cls(
            compute_cluster_type=compute_cluster_type,
            average_worker_count=average_worker_count,
            worker_hardware_tier_id=worker_hardware_tier_id,
            worker_hardware_tier_cost_per_minute=worker_hardware_tier_cost_per_minute,
            master_hardware_tier_id=master_hardware_tier_id,
            master_hardware_tier_cost_per_minute=master_hardware_tier_cost_per_minute,
        )

        domino_common_gateway_runs_compute_cluster_details.additional_properties = d
        return domino_common_gateway_runs_compute_cluster_details

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
