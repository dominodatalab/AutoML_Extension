from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_assets_v1_labels import CostAssetsV1Labels
    from ..models.cost_assets_v1_properties import CostAssetsV1Properties
    from ..models.cost_assets_v1_window import CostAssetsV1Window


T = TypeVar("T", bound="CostAssetsV1")


@_attrs_define
class CostAssetsV1:
    """
    Attributes:
        cpu_cost (float | Unset):
        gpu_cost (float | Unset):
        labels (CostAssetsV1Labels | Unset):
        name (str | Unset):
        properties (CostAssetsV1Properties | Unset):
        ram_cost (float | Unset):
        total_cost (float | Unset):
        type_ (str | Unset):
        window (CostAssetsV1Window | Unset):
    """

    cpu_cost: float | Unset = UNSET
    gpu_cost: float | Unset = UNSET
    labels: CostAssetsV1Labels | Unset = UNSET
    name: str | Unset = UNSET
    properties: CostAssetsV1Properties | Unset = UNSET
    ram_cost: float | Unset = UNSET
    total_cost: float | Unset = UNSET
    type_: str | Unset = UNSET
    window: CostAssetsV1Window | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpu_cost = self.cpu_cost

        gpu_cost = self.gpu_cost

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        name = self.name

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        ram_cost = self.ram_cost

        total_cost = self.total_cost

        type_ = self.type_

        window: dict[str, Any] | Unset = UNSET
        if not isinstance(self.window, Unset):
            window = self.window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpu_cost is not UNSET:
            field_dict["cpuCost"] = cpu_cost
        if gpu_cost is not UNSET:
            field_dict["gpuCost"] = gpu_cost
        if labels is not UNSET:
            field_dict["labels"] = labels
        if name is not UNSET:
            field_dict["name"] = name
        if properties is not UNSET:
            field_dict["properties"] = properties
        if ram_cost is not UNSET:
            field_dict["ramCost"] = ram_cost
        if total_cost is not UNSET:
            field_dict["totalCost"] = total_cost
        if type_ is not UNSET:
            field_dict["type"] = type_
        if window is not UNSET:
            field_dict["window"] = window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cost_assets_v1_labels import CostAssetsV1Labels
        from ..models.cost_assets_v1_properties import CostAssetsV1Properties
        from ..models.cost_assets_v1_window import CostAssetsV1Window

        d = dict(src_dict)
        cpu_cost = d.pop("cpuCost", UNSET)

        gpu_cost = d.pop("gpuCost", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: CostAssetsV1Labels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = CostAssetsV1Labels.from_dict(_labels)

        name = d.pop("name", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: CostAssetsV1Properties | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = CostAssetsV1Properties.from_dict(_properties)

        ram_cost = d.pop("ramCost", UNSET)

        total_cost = d.pop("totalCost", UNSET)

        type_ = d.pop("type", UNSET)

        _window = d.pop("window", UNSET)
        window: CostAssetsV1Window | Unset
        if isinstance(_window, Unset):
            window = UNSET
        else:
            window = CostAssetsV1Window.from_dict(_window)

        cost_assets_v1 = cls(
            cpu_cost=cpu_cost,
            gpu_cost=gpu_cost,
            labels=labels,
            name=name,
            properties=properties,
            ram_cost=ram_cost,
            total_cost=total_cost,
            type_=type_,
            window=window,
        )

        cost_assets_v1.additional_properties = d
        return cost_assets_v1

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
