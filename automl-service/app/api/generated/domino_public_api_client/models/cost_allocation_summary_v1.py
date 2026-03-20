from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_allocation_summary_v1_window import CostAllocationSummaryV1Window


T = TypeVar("T", bound="CostAllocationSummaryV1")


@_attrs_define
class CostAllocationSummaryV1:
    """
    Attributes:
        cpu_core_request_average (float | Unset):
        cpu_core_usage_average (float | Unset):
        cpu_cost (float | Unset):
        gpu_cost (float | Unset):
        load_balancer_cost (float | Unset):
        name (str | Unset):
        network_cost (float | Unset):
        pv_cost (float | Unset):
        ram_cost (float | Unset):
        total_cost (float | Unset):
        window (CostAllocationSummaryV1Window | Unset):
    """

    cpu_core_request_average: float | Unset = UNSET
    cpu_core_usage_average: float | Unset = UNSET
    cpu_cost: float | Unset = UNSET
    gpu_cost: float | Unset = UNSET
    load_balancer_cost: float | Unset = UNSET
    name: str | Unset = UNSET
    network_cost: float | Unset = UNSET
    pv_cost: float | Unset = UNSET
    ram_cost: float | Unset = UNSET
    total_cost: float | Unset = UNSET
    window: CostAllocationSummaryV1Window | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpu_core_request_average = self.cpu_core_request_average

        cpu_core_usage_average = self.cpu_core_usage_average

        cpu_cost = self.cpu_cost

        gpu_cost = self.gpu_cost

        load_balancer_cost = self.load_balancer_cost

        name = self.name

        network_cost = self.network_cost

        pv_cost = self.pv_cost

        ram_cost = self.ram_cost

        total_cost = self.total_cost

        window: dict[str, Any] | Unset = UNSET
        if not isinstance(self.window, Unset):
            window = self.window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpu_core_request_average is not UNSET:
            field_dict["cpuCoreRequestAverage"] = cpu_core_request_average
        if cpu_core_usage_average is not UNSET:
            field_dict["cpuCoreUsageAverage"] = cpu_core_usage_average
        if cpu_cost is not UNSET:
            field_dict["cpuCost"] = cpu_cost
        if gpu_cost is not UNSET:
            field_dict["gpuCost"] = gpu_cost
        if load_balancer_cost is not UNSET:
            field_dict["loadBalancerCost"] = load_balancer_cost
        if name is not UNSET:
            field_dict["name"] = name
        if network_cost is not UNSET:
            field_dict["networkCost"] = network_cost
        if pv_cost is not UNSET:
            field_dict["pvCost"] = pv_cost
        if ram_cost is not UNSET:
            field_dict["ramCost"] = ram_cost
        if total_cost is not UNSET:
            field_dict["totalCost"] = total_cost
        if window is not UNSET:
            field_dict["window"] = window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cost_allocation_summary_v1_window import CostAllocationSummaryV1Window

        d = dict(src_dict)
        cpu_core_request_average = d.pop("cpuCoreRequestAverage", UNSET)

        cpu_core_usage_average = d.pop("cpuCoreUsageAverage", UNSET)

        cpu_cost = d.pop("cpuCost", UNSET)

        gpu_cost = d.pop("gpuCost", UNSET)

        load_balancer_cost = d.pop("loadBalancerCost", UNSET)

        name = d.pop("name", UNSET)

        network_cost = d.pop("networkCost", UNSET)

        pv_cost = d.pop("pvCost", UNSET)

        ram_cost = d.pop("ramCost", UNSET)

        total_cost = d.pop("totalCost", UNSET)

        _window = d.pop("window", UNSET)
        window: CostAllocationSummaryV1Window | Unset
        if isinstance(_window, Unset):
            window = UNSET
        else:
            window = CostAllocationSummaryV1Window.from_dict(_window)

        cost_allocation_summary_v1 = cls(
            cpu_core_request_average=cpu_core_request_average,
            cpu_core_usage_average=cpu_core_usage_average,
            cpu_cost=cpu_cost,
            gpu_cost=gpu_cost,
            load_balancer_cost=load_balancer_cost,
            name=name,
            network_cost=network_cost,
            pv_cost=pv_cost,
            ram_cost=ram_cost,
            total_cost=total_cost,
            window=window,
        )

        cost_allocation_summary_v1.additional_properties = d
        return cost_allocation_summary_v1

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
