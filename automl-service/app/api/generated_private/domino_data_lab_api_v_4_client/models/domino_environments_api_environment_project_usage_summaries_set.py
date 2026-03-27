from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_environments_api_env_project_pagination import DominoEnvironmentsApiEnvProjectPagination
    from ..models.domino_environments_api_environment_project_usage_summary import (
        DominoEnvironmentsApiEnvironmentProjectUsageSummary,
    )


T = TypeVar("T", bound="DominoEnvironmentsApiEnvironmentProjectUsageSummariesSet")


@_attrs_define
class DominoEnvironmentsApiEnvironmentProjectUsageSummariesSet:
    """
    Attributes:
        summaries (list[DominoEnvironmentsApiEnvironmentProjectUsageSummary]):
        total_count (int):
        pagination (DominoEnvironmentsApiEnvProjectPagination):
    """

    summaries: list[DominoEnvironmentsApiEnvironmentProjectUsageSummary]
    total_count: int
    pagination: DominoEnvironmentsApiEnvProjectPagination
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        summaries = []
        for summaries_item_data in self.summaries:
            summaries_item = summaries_item_data.to_dict()
            summaries.append(summaries_item)

        total_count = self.total_count

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "summaries": summaries,
                "totalCount": total_count,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_environments_api_env_project_pagination import DominoEnvironmentsApiEnvProjectPagination
        from ..models.domino_environments_api_environment_project_usage_summary import (
            DominoEnvironmentsApiEnvironmentProjectUsageSummary,
        )

        d = dict(src_dict)
        summaries = []
        _summaries = d.pop("summaries")
        for summaries_item_data in _summaries:
            summaries_item = DominoEnvironmentsApiEnvironmentProjectUsageSummary.from_dict(summaries_item_data)

            summaries.append(summaries_item)

        total_count = d.pop("totalCount")

        pagination = DominoEnvironmentsApiEnvProjectPagination.from_dict(d.pop("pagination"))

        domino_environments_api_environment_project_usage_summaries_set = cls(
            summaries=summaries,
            total_count=total_count,
            pagination=pagination,
        )

        domino_environments_api_environment_project_usage_summaries_set.additional_properties = d
        return domino_environments_api_environment_project_usage_summaries_set

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
