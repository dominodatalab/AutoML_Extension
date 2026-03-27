from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoNucleusModelproductModelsUsageStatisticsRecorded")


@_attrs_define
class DominoNucleusModelproductModelsUsageStatisticsRecorded:
    """
    Attributes:
        product_id (str):
        timestamp_in_sec (int):
    """

    product_id: str
    timestamp_in_sec: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        timestamp_in_sec = self.timestamp_in_sec

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "productId": product_id,
                "timestampInSec": timestamp_in_sec,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_id = d.pop("productId")

        timestamp_in_sec = d.pop("timestampInSec")

        domino_nucleus_modelproduct_models_usage_statistics_recorded = cls(
            product_id=product_id,
            timestamp_in_sec=timestamp_in_sec,
        )

        domino_nucleus_modelproduct_models_usage_statistics_recorded.additional_properties = d
        return domino_nucleus_modelproduct_models_usage_statistics_recorded

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
