from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_allocation_cpu_v2 import CostAllocationCpuV2
    from ..models.cost_allocation_gpu_v2 import CostAllocationGpuV2
    from ..models.cost_allocation_load_balancer_v2 import CostAllocationLoadBalancerV2
    from ..models.cost_allocation_network_v2 import CostAllocationNetworkV2
    from ..models.cost_allocation_pv_v2 import CostAllocationPvV2
    from ..models.cost_allocation_ram_v2 import CostAllocationRamV2
    from ..models.cost_key_v2 import CostKeyV2
    from ..models.cost_labels_v2 import CostLabelsV2
    from ..models.cost_properties_v2 import CostPropertiesV2
    from ..models.cost_time_window_v2 import CostTimeWindowV2


T = TypeVar("T", bound="CostAllocationV2")


@_attrs_define
class CostAllocationV2:
    """
    Attributes:
        allocation_properties (CostPropertiesV2 | Unset):
        cpu (CostAllocationCpuV2 | Unset):
        end (str | Unset):
        external_cost (float | Unset):
        gpu (CostAllocationGpuV2 | Unset):
        key (CostKeyV2 | Unset):
        labels (CostLabelsV2 | Unset):
        load_balancer (CostAllocationLoadBalancerV2 | Unset):
        minutes (float | Unset):
        network (CostAllocationNetworkV2 | Unset):
        pv (CostAllocationPvV2 | Unset):
        ram (CostAllocationRamV2 | Unset):
        shared_cost (float | Unset):
        start (str | Unset):
        total_cost (float | Unset):
        total_efficiency (float | Unset):
        window (CostTimeWindowV2 | Unset):
    """

    allocation_properties: CostPropertiesV2 | Unset = UNSET
    cpu: CostAllocationCpuV2 | Unset = UNSET
    end: str | Unset = UNSET
    external_cost: float | Unset = UNSET
    gpu: CostAllocationGpuV2 | Unset = UNSET
    key: CostKeyV2 | Unset = UNSET
    labels: CostLabelsV2 | Unset = UNSET
    load_balancer: CostAllocationLoadBalancerV2 | Unset = UNSET
    minutes: float | Unset = UNSET
    network: CostAllocationNetworkV2 | Unset = UNSET
    pv: CostAllocationPvV2 | Unset = UNSET
    ram: CostAllocationRamV2 | Unset = UNSET
    shared_cost: float | Unset = UNSET
    start: str | Unset = UNSET
    total_cost: float | Unset = UNSET
    total_efficiency: float | Unset = UNSET
    window: CostTimeWindowV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allocation_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.allocation_properties, Unset):
            allocation_properties = self.allocation_properties.to_dict()

        cpu: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cpu, Unset):
            cpu = self.cpu.to_dict()

        end = self.end

        external_cost = self.external_cost

        gpu: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gpu, Unset):
            gpu = self.gpu.to_dict()

        key: dict[str, Any] | Unset = UNSET
        if not isinstance(self.key, Unset):
            key = self.key.to_dict()

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        load_balancer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.load_balancer, Unset):
            load_balancer = self.load_balancer.to_dict()

        minutes = self.minutes

        network: dict[str, Any] | Unset = UNSET
        if not isinstance(self.network, Unset):
            network = self.network.to_dict()

        pv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pv, Unset):
            pv = self.pv.to_dict()

        ram: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ram, Unset):
            ram = self.ram.to_dict()

        shared_cost = self.shared_cost

        start = self.start

        total_cost = self.total_cost

        total_efficiency = self.total_efficiency

        window: dict[str, Any] | Unset = UNSET
        if not isinstance(self.window, Unset):
            window = self.window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allocation_properties is not UNSET:
            field_dict["allocationProperties"] = allocation_properties
        if cpu is not UNSET:
            field_dict["cpu"] = cpu
        if end is not UNSET:
            field_dict["end"] = end
        if external_cost is not UNSET:
            field_dict["externalCost"] = external_cost
        if gpu is not UNSET:
            field_dict["gpu"] = gpu
        if key is not UNSET:
            field_dict["key"] = key
        if labels is not UNSET:
            field_dict["labels"] = labels
        if load_balancer is not UNSET:
            field_dict["loadBalancer"] = load_balancer
        if minutes is not UNSET:
            field_dict["minutes"] = minutes
        if network is not UNSET:
            field_dict["network"] = network
        if pv is not UNSET:
            field_dict["pv"] = pv
        if ram is not UNSET:
            field_dict["ram"] = ram
        if shared_cost is not UNSET:
            field_dict["sharedCost"] = shared_cost
        if start is not UNSET:
            field_dict["start"] = start
        if total_cost is not UNSET:
            field_dict["totalCost"] = total_cost
        if total_efficiency is not UNSET:
            field_dict["totalEfficiency"] = total_efficiency
        if window is not UNSET:
            field_dict["window"] = window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cost_allocation_cpu_v2 import CostAllocationCpuV2
        from ..models.cost_allocation_gpu_v2 import CostAllocationGpuV2
        from ..models.cost_allocation_load_balancer_v2 import CostAllocationLoadBalancerV2
        from ..models.cost_allocation_network_v2 import CostAllocationNetworkV2
        from ..models.cost_allocation_pv_v2 import CostAllocationPvV2
        from ..models.cost_allocation_ram_v2 import CostAllocationRamV2
        from ..models.cost_key_v2 import CostKeyV2
        from ..models.cost_labels_v2 import CostLabelsV2
        from ..models.cost_properties_v2 import CostPropertiesV2
        from ..models.cost_time_window_v2 import CostTimeWindowV2

        d = dict(src_dict)
        _allocation_properties = d.pop("allocationProperties", UNSET)
        allocation_properties: CostPropertiesV2 | Unset
        if isinstance(_allocation_properties, Unset):
            allocation_properties = UNSET
        else:
            allocation_properties = CostPropertiesV2.from_dict(_allocation_properties)

        _cpu = d.pop("cpu", UNSET)
        cpu: CostAllocationCpuV2 | Unset
        if isinstance(_cpu, Unset):
            cpu = UNSET
        else:
            cpu = CostAllocationCpuV2.from_dict(_cpu)

        end = d.pop("end", UNSET)

        external_cost = d.pop("externalCost", UNSET)

        _gpu = d.pop("gpu", UNSET)
        gpu: CostAllocationGpuV2 | Unset
        if isinstance(_gpu, Unset):
            gpu = UNSET
        else:
            gpu = CostAllocationGpuV2.from_dict(_gpu)

        _key = d.pop("key", UNSET)
        key: CostKeyV2 | Unset
        if isinstance(_key, Unset):
            key = UNSET
        else:
            key = CostKeyV2.from_dict(_key)

        _labels = d.pop("labels", UNSET)
        labels: CostLabelsV2 | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = CostLabelsV2.from_dict(_labels)

        _load_balancer = d.pop("loadBalancer", UNSET)
        load_balancer: CostAllocationLoadBalancerV2 | Unset
        if isinstance(_load_balancer, Unset):
            load_balancer = UNSET
        else:
            load_balancer = CostAllocationLoadBalancerV2.from_dict(_load_balancer)

        minutes = d.pop("minutes", UNSET)

        _network = d.pop("network", UNSET)
        network: CostAllocationNetworkV2 | Unset
        if isinstance(_network, Unset):
            network = UNSET
        else:
            network = CostAllocationNetworkV2.from_dict(_network)

        _pv = d.pop("pv", UNSET)
        pv: CostAllocationPvV2 | Unset
        if isinstance(_pv, Unset):
            pv = UNSET
        else:
            pv = CostAllocationPvV2.from_dict(_pv)

        _ram = d.pop("ram", UNSET)
        ram: CostAllocationRamV2 | Unset
        if isinstance(_ram, Unset):
            ram = UNSET
        else:
            ram = CostAllocationRamV2.from_dict(_ram)

        shared_cost = d.pop("sharedCost", UNSET)

        start = d.pop("start", UNSET)

        total_cost = d.pop("totalCost", UNSET)

        total_efficiency = d.pop("totalEfficiency", UNSET)

        _window = d.pop("window", UNSET)
        window: CostTimeWindowV2 | Unset
        if isinstance(_window, Unset):
            window = UNSET
        else:
            window = CostTimeWindowV2.from_dict(_window)

        cost_allocation_v2 = cls(
            allocation_properties=allocation_properties,
            cpu=cpu,
            end=end,
            external_cost=external_cost,
            gpu=gpu,
            key=key,
            labels=labels,
            load_balancer=load_balancer,
            minutes=minutes,
            network=network,
            pv=pv,
            ram=ram,
            shared_cost=shared_cost,
            start=start,
            total_cost=total_cost,
            total_efficiency=total_efficiency,
            window=window,
        )

        cost_allocation_v2.additional_properties = d
        return cost_allocation_v2

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
