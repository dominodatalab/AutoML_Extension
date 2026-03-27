from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_nucleus_modelproduct_models_usage_statistics_users import (
        DominoNucleusModelproductModelsUsageStatisticsUsers,
    )


T = TypeVar("T", bound="DominoNucleusModelproductModelsUsageStatistics")


@_attrs_define
class DominoNucleusModelproductModelsUsageStatistics:
    """
    Attributes:
        count (int):
        users (DominoNucleusModelproductModelsUsageStatisticsUsers):
    """

    count: int
    users: DominoNucleusModelproductModelsUsageStatisticsUsers
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        users = self.users.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "users": users,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_nucleus_modelproduct_models_usage_statistics_users import (
            DominoNucleusModelproductModelsUsageStatisticsUsers,
        )

        d = dict(src_dict)
        count = d.pop("count")

        users = DominoNucleusModelproductModelsUsageStatisticsUsers.from_dict(d.pop("users"))

        domino_nucleus_modelproduct_models_usage_statistics = cls(
            count=count,
            users=users,
        )

        domino_nucleus_modelproduct_models_usage_statistics.additional_properties = d
        return domino_nucleus_modelproduct_models_usage_statistics

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
