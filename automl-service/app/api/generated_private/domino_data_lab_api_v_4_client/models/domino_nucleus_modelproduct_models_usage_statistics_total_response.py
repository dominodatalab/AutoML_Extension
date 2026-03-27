from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_nucleus_modelproduct_models_usage_statistics import (
        DominoNucleusModelproductModelsUsageStatistics,
    )


T = TypeVar("T", bound="DominoNucleusModelproductModelsUsageStatisticsTotalResponse")


@_attrs_define
class DominoNucleusModelproductModelsUsageStatisticsTotalResponse:
    """
    Attributes:
        stats (DominoNucleusModelproductModelsUsageStatistics):
    """

    stats: DominoNucleusModelproductModelsUsageStatistics
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stats = self.stats.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stats": stats,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_nucleus_modelproduct_models_usage_statistics import (
            DominoNucleusModelproductModelsUsageStatistics,
        )

        d = dict(src_dict)
        stats = DominoNucleusModelproductModelsUsageStatistics.from_dict(d.pop("stats"))

        domino_nucleus_modelproduct_models_usage_statistics_total_response = cls(
            stats=stats,
        )

        domino_nucleus_modelproduct_models_usage_statistics_total_response.additional_properties = d
        return domino_nucleus_modelproduct_models_usage_statistics_total_response

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
