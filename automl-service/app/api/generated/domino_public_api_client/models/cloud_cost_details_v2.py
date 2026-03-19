from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudCostDetailsV2")


@_attrs_define
class CloudCostDetailsV2:
    """
    Attributes:
        cost (float | Unset):
        kubernetes_percent (float | Unset):
    """

    cost: float | Unset = UNSET
    kubernetes_percent: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cost = self.cost

        kubernetes_percent = self.kubernetes_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cost is not UNSET:
            field_dict["cost"] = cost
        if kubernetes_percent is not UNSET:
            field_dict["kubernetesPercent"] = kubernetes_percent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cost = d.pop("cost", UNSET)

        kubernetes_percent = d.pop("kubernetesPercent", UNSET)

        cloud_cost_details_v2 = cls(
            cost=cost,
            kubernetes_percent=kubernetes_percent,
        )

        cloud_cost_details_v2.additional_properties = d
        return cloud_cost_details_v2

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
