from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostAssetsStorageV2")


@_attrs_define
class CostAssetsStorageV2:
    """
    Attributes:
        claim_name (str | Unset):
        claim_namespace (str | Unset):
        class_ (str | Unset):
        node_type (str | Unset):
        pool (str | Unset):
        volume_name (str | Unset):
    """

    claim_name: str | Unset = UNSET
    claim_namespace: str | Unset = UNSET
    class_: str | Unset = UNSET
    node_type: str | Unset = UNSET
    pool: str | Unset = UNSET
    volume_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        claim_name = self.claim_name

        claim_namespace = self.claim_namespace

        class_ = self.class_

        node_type = self.node_type

        pool = self.pool

        volume_name = self.volume_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if claim_name is not UNSET:
            field_dict["claimName"] = claim_name
        if claim_namespace is not UNSET:
            field_dict["claimNamespace"] = claim_namespace
        if class_ is not UNSET:
            field_dict["class"] = class_
        if node_type is not UNSET:
            field_dict["nodeType"] = node_type
        if pool is not UNSET:
            field_dict["pool"] = pool
        if volume_name is not UNSET:
            field_dict["volumeName"] = volume_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        claim_name = d.pop("claimName", UNSET)

        claim_namespace = d.pop("claimNamespace", UNSET)

        class_ = d.pop("class", UNSET)

        node_type = d.pop("nodeType", UNSET)

        pool = d.pop("pool", UNSET)

        volume_name = d.pop("volumeName", UNSET)

        cost_assets_storage_v2 = cls(
            claim_name=claim_name,
            claim_namespace=claim_namespace,
            class_=class_,
            node_type=node_type,
            pool=pool,
            volume_name=volume_name,
        )

        cost_assets_storage_v2.additional_properties = d
        return cost_assets_storage_v2

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
