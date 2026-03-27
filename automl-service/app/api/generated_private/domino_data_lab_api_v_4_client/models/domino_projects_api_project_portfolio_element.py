from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_api_project_asset_count import DominoProjectsApiProjectAssetCount
    from ..models.domino_projects_api_project_stage import DominoProjectsApiProjectStage
    from ..models.domino_projects_api_project_stakeholder import DominoProjectsApiProjectStakeholder
    from ..models.domino_projects_api_project_status import DominoProjectsApiProjectStatus


T = TypeVar("T", bound="DominoProjectsApiProjectPortfolioElement")


@_attrs_define
class DominoProjectsApiProjectPortfolioElement:
    """
    Attributes:
        project_id (str):
        project_name (str):
        status (DominoProjectsApiProjectStatus):
        stage (DominoProjectsApiProjectStage):
        created_on (int):
        collaborators (list[DominoProjectsApiProjectStakeholder]):
        owner (DominoProjectsApiProjectStakeholder):
        assets (list[DominoProjectsApiProjectAssetCount]):
        cost_per_minute (float):
        duration (int):
        total_goals_count (int):
        completed_goals_count (int):
        last_activity (int | None | Unset):
    """

    project_id: str
    project_name: str
    status: DominoProjectsApiProjectStatus
    stage: DominoProjectsApiProjectStage
    created_on: int
    collaborators: list[DominoProjectsApiProjectStakeholder]
    owner: DominoProjectsApiProjectStakeholder
    assets: list[DominoProjectsApiProjectAssetCount]
    cost_per_minute: float
    duration: int
    total_goals_count: int
    completed_goals_count: int
    last_activity: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        project_name = self.project_name

        status = self.status.to_dict()

        stage = self.stage.to_dict()

        created_on = self.created_on

        collaborators = []
        for collaborators_item_data in self.collaborators:
            collaborators_item = collaborators_item_data.to_dict()
            collaborators.append(collaborators_item)

        owner = self.owner.to_dict()

        assets = []
        for assets_item_data in self.assets:
            assets_item = assets_item_data.to_dict()
            assets.append(assets_item)

        cost_per_minute = self.cost_per_minute

        duration = self.duration

        total_goals_count = self.total_goals_count

        completed_goals_count = self.completed_goals_count

        last_activity: int | None | Unset
        if isinstance(self.last_activity, Unset):
            last_activity = UNSET
        else:
            last_activity = self.last_activity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectId": project_id,
                "projectName": project_name,
                "status": status,
                "stage": stage,
                "createdOn": created_on,
                "collaborators": collaborators,
                "owner": owner,
                "assets": assets,
                "costPerMinute": cost_per_minute,
                "duration": duration,
                "totalGoalsCount": total_goals_count,
                "completedGoalsCount": completed_goals_count,
            }
        )
        if last_activity is not UNSET:
            field_dict["lastActivity"] = last_activity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_project_asset_count import DominoProjectsApiProjectAssetCount
        from ..models.domino_projects_api_project_stage import DominoProjectsApiProjectStage
        from ..models.domino_projects_api_project_stakeholder import DominoProjectsApiProjectStakeholder
        from ..models.domino_projects_api_project_status import DominoProjectsApiProjectStatus

        d = dict(src_dict)
        project_id = d.pop("projectId")

        project_name = d.pop("projectName")

        status = DominoProjectsApiProjectStatus.from_dict(d.pop("status"))

        stage = DominoProjectsApiProjectStage.from_dict(d.pop("stage"))

        created_on = d.pop("createdOn")

        collaborators = []
        _collaborators = d.pop("collaborators")
        for collaborators_item_data in _collaborators:
            collaborators_item = DominoProjectsApiProjectStakeholder.from_dict(collaborators_item_data)

            collaborators.append(collaborators_item)

        owner = DominoProjectsApiProjectStakeholder.from_dict(d.pop("owner"))

        assets = []
        _assets = d.pop("assets")
        for assets_item_data in _assets:
            assets_item = DominoProjectsApiProjectAssetCount.from_dict(assets_item_data)

            assets.append(assets_item)

        cost_per_minute = d.pop("costPerMinute")

        duration = d.pop("duration")

        total_goals_count = d.pop("totalGoalsCount")

        completed_goals_count = d.pop("completedGoalsCount")

        def _parse_last_activity(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_activity = _parse_last_activity(d.pop("lastActivity", UNSET))

        domino_projects_api_project_portfolio_element = cls(
            project_id=project_id,
            project_name=project_name,
            status=status,
            stage=stage,
            created_on=created_on,
            collaborators=collaborators,
            owner=owner,
            assets=assets,
            cost_per_minute=cost_per_minute,
            duration=duration,
            total_goals_count=total_goals_count,
            completed_goals_count=completed_goals_count,
            last_activity=last_activity,
        )

        domino_projects_api_project_portfolio_element.additional_properties = d
        return domino_projects_api_project_portfolio_element

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
