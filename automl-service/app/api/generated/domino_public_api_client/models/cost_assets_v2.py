from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_assets_byte_v2 import CostAssetsByteV2
    from ..models.cost_assets_cpu_v2 import CostAssetsCpuV2
    from ..models.cost_assets_gpu_v2 import CostAssetsGpuV2
    from ..models.cost_assets_labels_v2 import CostAssetsLabelsV2
    from ..models.cost_assets_overhead_v2 import CostAssetsOverheadV2
    from ..models.cost_assets_ram_v2 import CostAssetsRamV2
    from ..models.cost_assets_storage_v2 import CostAssetsStorageV2
    from ..models.cost_key_v2 import CostKeyV2
    from ..models.cost_properties_v2 import CostPropertiesV2
    from ..models.cost_time_window_v2 import CostTimeWindowV2


T = TypeVar("T", bound="CostAssetsV2")


@_attrs_define
class CostAssetsV2:
    """
    Attributes:
        adjustment (float | Unset):
        asset_properties (CostPropertiesV2 | Unset):
        asset_type (str | Unset):
        byte (CostAssetsByteV2 | Unset):
        cpu (CostAssetsCpuV2 | Unset):
        discount (float | Unset):
        end (str | Unset):
        gpu (CostAssetsGpuV2 | Unset):
        key (CostKeyV2 | Unset):
        labels (CostAssetsLabelsV2 | Unset):
        minutes (float | Unset):
        overhead (CostAssetsOverheadV2 | Unset):
        preemptible (float | Unset):
        ram (CostAssetsRamV2 | Unset):
        start (str | Unset):
        storage (CostAssetsStorageV2 | Unset):
        total_cost (float | Unset):
        window (CostTimeWindowV2 | Unset):
    """

    adjustment: float | Unset = UNSET
    asset_properties: CostPropertiesV2 | Unset = UNSET
    asset_type: str | Unset = UNSET
    byte: CostAssetsByteV2 | Unset = UNSET
    cpu: CostAssetsCpuV2 | Unset = UNSET
    discount: float | Unset = UNSET
    end: str | Unset = UNSET
    gpu: CostAssetsGpuV2 | Unset = UNSET
    key: CostKeyV2 | Unset = UNSET
    labels: CostAssetsLabelsV2 | Unset = UNSET
    minutes: float | Unset = UNSET
    overhead: CostAssetsOverheadV2 | Unset = UNSET
    preemptible: float | Unset = UNSET
    ram: CostAssetsRamV2 | Unset = UNSET
    start: str | Unset = UNSET
    storage: CostAssetsStorageV2 | Unset = UNSET
    total_cost: float | Unset = UNSET
    window: CostTimeWindowV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        adjustment = self.adjustment

        asset_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.asset_properties, Unset):
            asset_properties = self.asset_properties.to_dict()

        asset_type = self.asset_type

        byte: dict[str, Any] | Unset = UNSET
        if not isinstance(self.byte, Unset):
            byte = self.byte.to_dict()

        cpu: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cpu, Unset):
            cpu = self.cpu.to_dict()

        discount = self.discount

        end = self.end

        gpu: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gpu, Unset):
            gpu = self.gpu.to_dict()

        key: dict[str, Any] | Unset = UNSET
        if not isinstance(self.key, Unset):
            key = self.key.to_dict()

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        minutes = self.minutes

        overhead: dict[str, Any] | Unset = UNSET
        if not isinstance(self.overhead, Unset):
            overhead = self.overhead.to_dict()

        preemptible = self.preemptible

        ram: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ram, Unset):
            ram = self.ram.to_dict()

        start = self.start

        storage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storage, Unset):
            storage = self.storage.to_dict()

        total_cost = self.total_cost

        window: dict[str, Any] | Unset = UNSET
        if not isinstance(self.window, Unset):
            window = self.window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if adjustment is not UNSET:
            field_dict["adjustment"] = adjustment
        if asset_properties is not UNSET:
            field_dict["assetProperties"] = asset_properties
        if asset_type is not UNSET:
            field_dict["assetType"] = asset_type
        if byte is not UNSET:
            field_dict["byte"] = byte
        if cpu is not UNSET:
            field_dict["cpu"] = cpu
        if discount is not UNSET:
            field_dict["discount"] = discount
        if end is not UNSET:
            field_dict["end"] = end
        if gpu is not UNSET:
            field_dict["gpu"] = gpu
        if key is not UNSET:
            field_dict["key"] = key
        if labels is not UNSET:
            field_dict["labels"] = labels
        if minutes is not UNSET:
            field_dict["minutes"] = minutes
        if overhead is not UNSET:
            field_dict["overhead"] = overhead
        if preemptible is not UNSET:
            field_dict["preemptible"] = preemptible
        if ram is not UNSET:
            field_dict["ram"] = ram
        if start is not UNSET:
            field_dict["start"] = start
        if storage is not UNSET:
            field_dict["storage"] = storage
        if total_cost is not UNSET:
            field_dict["totalCost"] = total_cost
        if window is not UNSET:
            field_dict["window"] = window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cost_assets_byte_v2 import CostAssetsByteV2
        from ..models.cost_assets_cpu_v2 import CostAssetsCpuV2
        from ..models.cost_assets_gpu_v2 import CostAssetsGpuV2
        from ..models.cost_assets_labels_v2 import CostAssetsLabelsV2
        from ..models.cost_assets_overhead_v2 import CostAssetsOverheadV2
        from ..models.cost_assets_ram_v2 import CostAssetsRamV2
        from ..models.cost_assets_storage_v2 import CostAssetsStorageV2
        from ..models.cost_key_v2 import CostKeyV2
        from ..models.cost_properties_v2 import CostPropertiesV2
        from ..models.cost_time_window_v2 import CostTimeWindowV2

        d = dict(src_dict)
        adjustment = d.pop("adjustment", UNSET)

        _asset_properties = d.pop("assetProperties", UNSET)
        asset_properties: CostPropertiesV2 | Unset
        if isinstance(_asset_properties, Unset):
            asset_properties = UNSET
        else:
            asset_properties = CostPropertiesV2.from_dict(_asset_properties)

        asset_type = d.pop("assetType", UNSET)

        _byte = d.pop("byte", UNSET)
        byte: CostAssetsByteV2 | Unset
        if isinstance(_byte, Unset):
            byte = UNSET
        else:
            byte = CostAssetsByteV2.from_dict(_byte)

        _cpu = d.pop("cpu", UNSET)
        cpu: CostAssetsCpuV2 | Unset
        if isinstance(_cpu, Unset):
            cpu = UNSET
        else:
            cpu = CostAssetsCpuV2.from_dict(_cpu)

        discount = d.pop("discount", UNSET)

        end = d.pop("end", UNSET)

        _gpu = d.pop("gpu", UNSET)
        gpu: CostAssetsGpuV2 | Unset
        if isinstance(_gpu, Unset):
            gpu = UNSET
        else:
            gpu = CostAssetsGpuV2.from_dict(_gpu)

        _key = d.pop("key", UNSET)
        key: CostKeyV2 | Unset
        if isinstance(_key, Unset):
            key = UNSET
        else:
            key = CostKeyV2.from_dict(_key)

        _labels = d.pop("labels", UNSET)
        labels: CostAssetsLabelsV2 | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = CostAssetsLabelsV2.from_dict(_labels)

        minutes = d.pop("minutes", UNSET)

        _overhead = d.pop("overhead", UNSET)
        overhead: CostAssetsOverheadV2 | Unset
        if isinstance(_overhead, Unset):
            overhead = UNSET
        else:
            overhead = CostAssetsOverheadV2.from_dict(_overhead)

        preemptible = d.pop("preemptible", UNSET)

        _ram = d.pop("ram", UNSET)
        ram: CostAssetsRamV2 | Unset
        if isinstance(_ram, Unset):
            ram = UNSET
        else:
            ram = CostAssetsRamV2.from_dict(_ram)

        start = d.pop("start", UNSET)

        _storage = d.pop("storage", UNSET)
        storage: CostAssetsStorageV2 | Unset
        if isinstance(_storage, Unset):
            storage = UNSET
        else:
            storage = CostAssetsStorageV2.from_dict(_storage)

        total_cost = d.pop("totalCost", UNSET)

        _window = d.pop("window", UNSET)
        window: CostTimeWindowV2 | Unset
        if isinstance(_window, Unset):
            window = UNSET
        else:
            window = CostTimeWindowV2.from_dict(_window)

        cost_assets_v2 = cls(
            adjustment=adjustment,
            asset_properties=asset_properties,
            asset_type=asset_type,
            byte=byte,
            cpu=cpu,
            discount=discount,
            end=end,
            gpu=gpu,
            key=key,
            labels=labels,
            minutes=minutes,
            overhead=overhead,
            preemptible=preemptible,
            ram=ram,
            start=start,
            storage=storage,
            total_cost=total_cost,
            window=window,
        )

        cost_assets_v2.additional_properties = d
        return cost_assets_v2

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
