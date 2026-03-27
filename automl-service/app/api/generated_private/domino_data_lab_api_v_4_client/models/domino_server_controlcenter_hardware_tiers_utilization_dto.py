from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoServerControlcenterHardwareTiersUtilizationDTO")


@_attrs_define
class DominoServerControlcenterHardwareTiersUtilizationDTO:
    """TODO describe

    Attributes:
        completed_runs_count (int): How many runs was executed in this hardware tier
        estimated_cost_variation (float): How much the `estimatedCost` changed recently
        average_queue_time_in_seconds (float): TODO describe
        estimated_cost_per_hour (float): TODO describe
        name (str): TODO describe
        cost_efficiency (float): TODO describe
        utilization (float): TODO describe
        id (str): TODO describe
        estimated_cost (float): TODO describe
        utilization_variation (float): How much the `utilization` changed recently
    """

    completed_runs_count: int
    estimated_cost_variation: float
    average_queue_time_in_seconds: float
    estimated_cost_per_hour: float
    name: str
    cost_efficiency: float
    utilization: float
    id: str
    estimated_cost: float
    utilization_variation: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        completed_runs_count = self.completed_runs_count

        estimated_cost_variation = self.estimated_cost_variation

        average_queue_time_in_seconds = self.average_queue_time_in_seconds

        estimated_cost_per_hour = self.estimated_cost_per_hour

        name = self.name

        cost_efficiency = self.cost_efficiency

        utilization = self.utilization

        id = self.id

        estimated_cost = self.estimated_cost

        utilization_variation = self.utilization_variation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "completedRunsCount": completed_runs_count,
                "estimatedCostVariation": estimated_cost_variation,
                "averageQueueTimeInSeconds": average_queue_time_in_seconds,
                "estimatedCostPerHour": estimated_cost_per_hour,
                "name": name,
                "costEfficiency": cost_efficiency,
                "utilization": utilization,
                "id": id,
                "estimatedCost": estimated_cost,
                "utilizationVariation": utilization_variation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        completed_runs_count = d.pop("completedRunsCount")

        estimated_cost_variation = d.pop("estimatedCostVariation")

        average_queue_time_in_seconds = d.pop("averageQueueTimeInSeconds")

        estimated_cost_per_hour = d.pop("estimatedCostPerHour")

        name = d.pop("name")

        cost_efficiency = d.pop("costEfficiency")

        utilization = d.pop("utilization")

        id = d.pop("id")

        estimated_cost = d.pop("estimatedCost")

        utilization_variation = d.pop("utilizationVariation")

        domino_server_controlcenter_hardware_tiers_utilization_dto = cls(
            completed_runs_count=completed_runs_count,
            estimated_cost_variation=estimated_cost_variation,
            average_queue_time_in_seconds=average_queue_time_in_seconds,
            estimated_cost_per_hour=estimated_cost_per_hour,
            name=name,
            cost_efficiency=cost_efficiency,
            utilization=utilization,
            id=id,
            estimated_cost=estimated_cost,
            utilization_variation=utilization_variation,
        )

        domino_server_controlcenter_hardware_tiers_utilization_dto.additional_properties = d
        return domino_server_controlcenter_hardware_tiers_utilization_dto

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
