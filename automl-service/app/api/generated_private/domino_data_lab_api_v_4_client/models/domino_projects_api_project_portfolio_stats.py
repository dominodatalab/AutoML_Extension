from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_projects_api_stage_stat import DominoProjectsApiStageStat
    from ..models.domino_projects_api_status_stat import DominoProjectsApiStatusStat


T = TypeVar("T", bound="DominoProjectsApiProjectPortfolioStats")


@_attrs_define
class DominoProjectsApiProjectPortfolioStats:
    """
    Attributes:
        total_projects (int):
        stage_stats (list[DominoProjectsApiStageStat]):
        statu_stats (list[DominoProjectsApiStatusStat]):
    """

    total_projects: int
    stage_stats: list[DominoProjectsApiStageStat]
    statu_stats: list[DominoProjectsApiStatusStat]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_projects = self.total_projects

        stage_stats = []
        for stage_stats_item_data in self.stage_stats:
            stage_stats_item = stage_stats_item_data.to_dict()
            stage_stats.append(stage_stats_item)

        statu_stats = []
        for statu_stats_item_data in self.statu_stats:
            statu_stats_item = statu_stats_item_data.to_dict()
            statu_stats.append(statu_stats_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalProjects": total_projects,
                "stageStats": stage_stats,
                "statuStats": statu_stats,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_stage_stat import DominoProjectsApiStageStat
        from ..models.domino_projects_api_status_stat import DominoProjectsApiStatusStat

        d = dict(src_dict)
        total_projects = d.pop("totalProjects")

        stage_stats = []
        _stage_stats = d.pop("stageStats")
        for stage_stats_item_data in _stage_stats:
            stage_stats_item = DominoProjectsApiStageStat.from_dict(stage_stats_item_data)

            stage_stats.append(stage_stats_item)

        statu_stats = []
        _statu_stats = d.pop("statuStats")
        for statu_stats_item_data in _statu_stats:
            statu_stats_item = DominoProjectsApiStatusStat.from_dict(statu_stats_item_data)

            statu_stats.append(statu_stats_item)

        domino_projects_api_project_portfolio_stats = cls(
            total_projects=total_projects,
            stage_stats=stage_stats,
            statu_stats=statu_stats,
        )

        domino_projects_api_project_portfolio_stats.additional_properties = d
        return domino_projects_api_project_portfolio_stats

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
