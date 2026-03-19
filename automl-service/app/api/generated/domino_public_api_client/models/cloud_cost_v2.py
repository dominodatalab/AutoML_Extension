from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cloud_cost_details_v2 import CloudCostDetailsV2
    from ..models.cost_key_v2 import CostKeyV2
    from ..models.cost_time_window_v2 import CostTimeWindowV2


T = TypeVar("T", bound="CloudCostV2")


@_attrs_define
class CloudCostV2:
    """
    Attributes:
        amortized_cost (CloudCostDetailsV2 | Unset):
        amortized_net_cost (CloudCostDetailsV2 | Unset):
        invoiced_cost (CloudCostDetailsV2 | Unset):
        key (CostKeyV2 | Unset):
        list_cost (CloudCostDetailsV2 | Unset):
        net_cost (CloudCostDetailsV2 | Unset):
        window (CostTimeWindowV2 | Unset):
    """

    amortized_cost: CloudCostDetailsV2 | Unset = UNSET
    amortized_net_cost: CloudCostDetailsV2 | Unset = UNSET
    invoiced_cost: CloudCostDetailsV2 | Unset = UNSET
    key: CostKeyV2 | Unset = UNSET
    list_cost: CloudCostDetailsV2 | Unset = UNSET
    net_cost: CloudCostDetailsV2 | Unset = UNSET
    window: CostTimeWindowV2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amortized_cost: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amortized_cost, Unset):
            amortized_cost = self.amortized_cost.to_dict()

        amortized_net_cost: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amortized_net_cost, Unset):
            amortized_net_cost = self.amortized_net_cost.to_dict()

        invoiced_cost: dict[str, Any] | Unset = UNSET
        if not isinstance(self.invoiced_cost, Unset):
            invoiced_cost = self.invoiced_cost.to_dict()

        key: dict[str, Any] | Unset = UNSET
        if not isinstance(self.key, Unset):
            key = self.key.to_dict()

        list_cost: dict[str, Any] | Unset = UNSET
        if not isinstance(self.list_cost, Unset):
            list_cost = self.list_cost.to_dict()

        net_cost: dict[str, Any] | Unset = UNSET
        if not isinstance(self.net_cost, Unset):
            net_cost = self.net_cost.to_dict()

        window: dict[str, Any] | Unset = UNSET
        if not isinstance(self.window, Unset):
            window = self.window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amortized_cost is not UNSET:
            field_dict["amortizedCost"] = amortized_cost
        if amortized_net_cost is not UNSET:
            field_dict["amortizedNetCost"] = amortized_net_cost
        if invoiced_cost is not UNSET:
            field_dict["invoicedCost"] = invoiced_cost
        if key is not UNSET:
            field_dict["key"] = key
        if list_cost is not UNSET:
            field_dict["listCost"] = list_cost
        if net_cost is not UNSET:
            field_dict["netCost"] = net_cost
        if window is not UNSET:
            field_dict["window"] = window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cloud_cost_details_v2 import CloudCostDetailsV2
        from ..models.cost_key_v2 import CostKeyV2
        from ..models.cost_time_window_v2 import CostTimeWindowV2

        d = dict(src_dict)
        _amortized_cost = d.pop("amortizedCost", UNSET)
        amortized_cost: CloudCostDetailsV2 | Unset
        if isinstance(_amortized_cost, Unset):
            amortized_cost = UNSET
        else:
            amortized_cost = CloudCostDetailsV2.from_dict(_amortized_cost)

        _amortized_net_cost = d.pop("amortizedNetCost", UNSET)
        amortized_net_cost: CloudCostDetailsV2 | Unset
        if isinstance(_amortized_net_cost, Unset):
            amortized_net_cost = UNSET
        else:
            amortized_net_cost = CloudCostDetailsV2.from_dict(_amortized_net_cost)

        _invoiced_cost = d.pop("invoicedCost", UNSET)
        invoiced_cost: CloudCostDetailsV2 | Unset
        if isinstance(_invoiced_cost, Unset):
            invoiced_cost = UNSET
        else:
            invoiced_cost = CloudCostDetailsV2.from_dict(_invoiced_cost)

        _key = d.pop("key", UNSET)
        key: CostKeyV2 | Unset
        if isinstance(_key, Unset):
            key = UNSET
        else:
            key = CostKeyV2.from_dict(_key)

        _list_cost = d.pop("listCost", UNSET)
        list_cost: CloudCostDetailsV2 | Unset
        if isinstance(_list_cost, Unset):
            list_cost = UNSET
        else:
            list_cost = CloudCostDetailsV2.from_dict(_list_cost)

        _net_cost = d.pop("netCost", UNSET)
        net_cost: CloudCostDetailsV2 | Unset
        if isinstance(_net_cost, Unset):
            net_cost = UNSET
        else:
            net_cost = CloudCostDetailsV2.from_dict(_net_cost)

        _window = d.pop("window", UNSET)
        window: CostTimeWindowV2 | Unset
        if isinstance(_window, Unset):
            window = UNSET
        else:
            window = CostTimeWindowV2.from_dict(_window)

        cloud_cost_v2 = cls(
            amortized_cost=amortized_cost,
            amortized_net_cost=amortized_net_cost,
            invoiced_cost=invoiced_cost,
            key=key,
            list_cost=list_cost,
            net_cost=net_cost,
            window=window,
        )

        cloud_cost_v2.additional_properties = d
        return cloud_cost_v2

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
