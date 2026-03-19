from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostAssetsLabelsV2")


@_attrs_define
class CostAssetsLabelsV2:
    """
    Attributes:
        instance (str | Unset):
        job (str | Unset):
        label_dominodatalab_com_domino_node (str | Unset):
        label_dominodatalab_com_node_pool (str | Unset):
    """

    instance: str | Unset = UNSET
    job: str | Unset = UNSET
    label_dominodatalab_com_domino_node: str | Unset = UNSET
    label_dominodatalab_com_node_pool: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance = self.instance

        job = self.job

        label_dominodatalab_com_domino_node = self.label_dominodatalab_com_domino_node

        label_dominodatalab_com_node_pool = self.label_dominodatalab_com_node_pool

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance is not UNSET:
            field_dict["instance"] = instance
        if job is not UNSET:
            field_dict["job"] = job
        if label_dominodatalab_com_domino_node is not UNSET:
            field_dict["label_dominodatalab_com_domino_node"] = label_dominodatalab_com_domino_node
        if label_dominodatalab_com_node_pool is not UNSET:
            field_dict["label_dominodatalab_com_node_pool"] = label_dominodatalab_com_node_pool

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        instance = d.pop("instance", UNSET)

        job = d.pop("job", UNSET)

        label_dominodatalab_com_domino_node = d.pop("label_dominodatalab_com_domino_node", UNSET)

        label_dominodatalab_com_node_pool = d.pop("label_dominodatalab_com_node_pool", UNSET)

        cost_assets_labels_v2 = cls(
            instance=instance,
            job=job,
            label_dominodatalab_com_domino_node=label_dominodatalab_com_domino_node,
            label_dominodatalab_com_node_pool=label_dominodatalab_com_node_pool,
        )

        cost_assets_labels_v2.additional_properties = d
        return cost_assets_labels_v2

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
