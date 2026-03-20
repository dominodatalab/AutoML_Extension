from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_allocation_v1_labels import CostAllocationV1Labels
    from ..models.cost_allocation_v1_pv import CostAllocationV1Pv
    from ..models.cost_allocation_v1_window import CostAllocationV1Window


T = TypeVar("T", bound="CostAllocationV1")


@_attrs_define
class CostAllocationV1:
    """
    Attributes:
        cpu_core_hours (float | Unset):
        cpu_core_request_average (float | Unset):
        cpu_core_usage_average (float | Unset):
        cpu_cores (float | Unset):
        cpu_cost (float | Unset):
        cpu_cost_adjustment (float | Unset):
        cpu_efficincy (float | Unset):
        discount (float | Unset):
        gpu_cost (float | Unset):
        gpu_cost_adjustment (float | Unset):
        gpu_count (float | Unset):
        gpu_hours (float | Unset):
        labels (CostAllocationV1Labels | Unset):
        load_balancer_cost (float | Unset):
        load_balancer_cost_adjustment (float | Unset):
        name (str | Unset):
        node_type (str | Unset):
        pv (CostAllocationV1Pv | Unset):
        ram_cost (float | Unset):
        ram_cost_adjustment (float | Unset):
        total_cost (float | Unset):
        window (CostAllocationV1Window | Unset):
    """

    cpu_core_hours: float | Unset = UNSET
    cpu_core_request_average: float | Unset = UNSET
    cpu_core_usage_average: float | Unset = UNSET
    cpu_cores: float | Unset = UNSET
    cpu_cost: float | Unset = UNSET
    cpu_cost_adjustment: float | Unset = UNSET
    cpu_efficincy: float | Unset = UNSET
    discount: float | Unset = UNSET
    gpu_cost: float | Unset = UNSET
    gpu_cost_adjustment: float | Unset = UNSET
    gpu_count: float | Unset = UNSET
    gpu_hours: float | Unset = UNSET
    labels: CostAllocationV1Labels | Unset = UNSET
    load_balancer_cost: float | Unset = UNSET
    load_balancer_cost_adjustment: float | Unset = UNSET
    name: str | Unset = UNSET
    node_type: str | Unset = UNSET
    pv: CostAllocationV1Pv | Unset = UNSET
    ram_cost: float | Unset = UNSET
    ram_cost_adjustment: float | Unset = UNSET
    total_cost: float | Unset = UNSET
    window: CostAllocationV1Window | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpu_core_hours = self.cpu_core_hours

        cpu_core_request_average = self.cpu_core_request_average

        cpu_core_usage_average = self.cpu_core_usage_average

        cpu_cores = self.cpu_cores

        cpu_cost = self.cpu_cost

        cpu_cost_adjustment = self.cpu_cost_adjustment

        cpu_efficincy = self.cpu_efficincy

        discount = self.discount

        gpu_cost = self.gpu_cost

        gpu_cost_adjustment = self.gpu_cost_adjustment

        gpu_count = self.gpu_count

        gpu_hours = self.gpu_hours

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        load_balancer_cost = self.load_balancer_cost

        load_balancer_cost_adjustment = self.load_balancer_cost_adjustment

        name = self.name

        node_type = self.node_type

        pv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pv, Unset):
            pv = self.pv.to_dict()

        ram_cost = self.ram_cost

        ram_cost_adjustment = self.ram_cost_adjustment

        total_cost = self.total_cost

        window: dict[str, Any] | Unset = UNSET
        if not isinstance(self.window, Unset):
            window = self.window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpu_core_hours is not UNSET:
            field_dict["cpuCoreHours"] = cpu_core_hours
        if cpu_core_request_average is not UNSET:
            field_dict["cpuCoreRequestAverage"] = cpu_core_request_average
        if cpu_core_usage_average is not UNSET:
            field_dict["cpuCoreUsageAverage"] = cpu_core_usage_average
        if cpu_cores is not UNSET:
            field_dict["cpuCores"] = cpu_cores
        if cpu_cost is not UNSET:
            field_dict["cpuCost"] = cpu_cost
        if cpu_cost_adjustment is not UNSET:
            field_dict["cpuCostAdjustment"] = cpu_cost_adjustment
        if cpu_efficincy is not UNSET:
            field_dict["cpuEfficincy"] = cpu_efficincy
        if discount is not UNSET:
            field_dict["discount"] = discount
        if gpu_cost is not UNSET:
            field_dict["gpuCost"] = gpu_cost
        if gpu_cost_adjustment is not UNSET:
            field_dict["gpuCostAdjustment"] = gpu_cost_adjustment
        if gpu_count is not UNSET:
            field_dict["gpuCount"] = gpu_count
        if gpu_hours is not UNSET:
            field_dict["gpuHours"] = gpu_hours
        if labels is not UNSET:
            field_dict["labels"] = labels
        if load_balancer_cost is not UNSET:
            field_dict["loadBalancerCost"] = load_balancer_cost
        if load_balancer_cost_adjustment is not UNSET:
            field_dict["loadBalancerCostAdjustment"] = load_balancer_cost_adjustment
        if name is not UNSET:
            field_dict["name"] = name
        if node_type is not UNSET:
            field_dict["nodeType"] = node_type
        if pv is not UNSET:
            field_dict["pv"] = pv
        if ram_cost is not UNSET:
            field_dict["ramCost"] = ram_cost
        if ram_cost_adjustment is not UNSET:
            field_dict["ramCostAdjustment"] = ram_cost_adjustment
        if total_cost is not UNSET:
            field_dict["totalCost"] = total_cost
        if window is not UNSET:
            field_dict["window"] = window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cost_allocation_v1_labels import CostAllocationV1Labels
        from ..models.cost_allocation_v1_pv import CostAllocationV1Pv
        from ..models.cost_allocation_v1_window import CostAllocationV1Window

        d = dict(src_dict)
        cpu_core_hours = d.pop("cpuCoreHours", UNSET)

        cpu_core_request_average = d.pop("cpuCoreRequestAverage", UNSET)

        cpu_core_usage_average = d.pop("cpuCoreUsageAverage", UNSET)

        cpu_cores = d.pop("cpuCores", UNSET)

        cpu_cost = d.pop("cpuCost", UNSET)

        cpu_cost_adjustment = d.pop("cpuCostAdjustment", UNSET)

        cpu_efficincy = d.pop("cpuEfficincy", UNSET)

        discount = d.pop("discount", UNSET)

        gpu_cost = d.pop("gpuCost", UNSET)

        gpu_cost_adjustment = d.pop("gpuCostAdjustment", UNSET)

        gpu_count = d.pop("gpuCount", UNSET)

        gpu_hours = d.pop("gpuHours", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: CostAllocationV1Labels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = CostAllocationV1Labels.from_dict(_labels)

        load_balancer_cost = d.pop("loadBalancerCost", UNSET)

        load_balancer_cost_adjustment = d.pop("loadBalancerCostAdjustment", UNSET)

        name = d.pop("name", UNSET)

        node_type = d.pop("nodeType", UNSET)

        _pv = d.pop("pv", UNSET)
        pv: CostAllocationV1Pv | Unset
        if isinstance(_pv, Unset):
            pv = UNSET
        else:
            pv = CostAllocationV1Pv.from_dict(_pv)

        ram_cost = d.pop("ramCost", UNSET)

        ram_cost_adjustment = d.pop("ramCostAdjustment", UNSET)

        total_cost = d.pop("totalCost", UNSET)

        _window = d.pop("window", UNSET)
        window: CostAllocationV1Window | Unset
        if isinstance(_window, Unset):
            window = UNSET
        else:
            window = CostAllocationV1Window.from_dict(_window)

        cost_allocation_v1 = cls(
            cpu_core_hours=cpu_core_hours,
            cpu_core_request_average=cpu_core_request_average,
            cpu_core_usage_average=cpu_core_usage_average,
            cpu_cores=cpu_cores,
            cpu_cost=cpu_cost,
            cpu_cost_adjustment=cpu_cost_adjustment,
            cpu_efficincy=cpu_efficincy,
            discount=discount,
            gpu_cost=gpu_cost,
            gpu_cost_adjustment=gpu_cost_adjustment,
            gpu_count=gpu_count,
            gpu_hours=gpu_hours,
            labels=labels,
            load_balancer_cost=load_balancer_cost,
            load_balancer_cost_adjustment=load_balancer_cost_adjustment,
            name=name,
            node_type=node_type,
            pv=pv,
            ram_cost=ram_cost,
            ram_cost_adjustment=ram_cost_adjustment,
            total_cost=total_cost,
            window=window,
        )

        cost_allocation_v1.additional_properties = d
        return cost_allocation_v1

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
