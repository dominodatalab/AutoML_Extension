from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostAssetsV1Properties")


@_attrs_define
class CostAssetsV1Properties:
    """
    Attributes:
        category (str | Unset):
        cluster (str | Unset):
        provider (str | Unset):
        provider_id (str | Unset):
        service (str | Unset):
    """

    category: str | Unset = UNSET
    cluster: str | Unset = UNSET
    provider: str | Unset = UNSET
    provider_id: str | Unset = UNSET
    service: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        cluster = self.cluster

        provider = self.provider

        provider_id = self.provider_id

        service = self.service

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if provider is not UNSET:
            field_dict["provider"] = provider
        if provider_id is not UNSET:
            field_dict["providerId"] = provider_id
        if service is not UNSET:
            field_dict["service"] = service

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category", UNSET)

        cluster = d.pop("cluster", UNSET)

        provider = d.pop("provider", UNSET)

        provider_id = d.pop("providerId", UNSET)

        service = d.pop("service", UNSET)

        cost_assets_v1_properties = cls(
            category=category,
            cluster=cluster,
            provider=provider,
            provider_id=provider_id,
            service=service,
        )

        cost_assets_v1_properties.additional_properties = d
        return cost_assets_v1_properties

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
