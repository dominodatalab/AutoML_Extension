from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_activity_api_goal_assignee import DominoActivityApiGoalAssignee
    from ..models.domino_activity_api_project_stage import DominoActivityApiProjectStage


T = TypeVar("T", bound="DominoActivityApiProjectGoalBulkUpdateActivityMetadata")


@_attrs_define
class DominoActivityApiProjectGoalBulkUpdateActivityMetadata:
    """
    Attributes:
        goal_ids (list[str]):
        goal_names (list[str]):
        update_assignee (bool):
        update_stage (bool):
        to_assignee (DominoActivityApiGoalAssignee | Unset):
        to_stage (DominoActivityApiProjectStage | Unset):
    """

    goal_ids: list[str]
    goal_names: list[str]
    update_assignee: bool
    update_stage: bool
    to_assignee: DominoActivityApiGoalAssignee | Unset = UNSET
    to_stage: DominoActivityApiProjectStage | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        goal_ids = self.goal_ids

        goal_names = self.goal_names

        update_assignee = self.update_assignee

        update_stage = self.update_stage

        to_assignee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.to_assignee, Unset):
            to_assignee = self.to_assignee.to_dict()

        to_stage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.to_stage, Unset):
            to_stage = self.to_stage.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "goalIds": goal_ids,
                "goalNames": goal_names,
                "updateAssignee": update_assignee,
                "updateStage": update_stage,
            }
        )
        if to_assignee is not UNSET:
            field_dict["toAssignee"] = to_assignee
        if to_stage is not UNSET:
            field_dict["toStage"] = to_stage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_activity_api_goal_assignee import DominoActivityApiGoalAssignee
        from ..models.domino_activity_api_project_stage import DominoActivityApiProjectStage

        d = dict(src_dict)
        goal_ids = cast(list[str], d.pop("goalIds"))

        goal_names = cast(list[str], d.pop("goalNames"))

        update_assignee = d.pop("updateAssignee")

        update_stage = d.pop("updateStage")

        _to_assignee = d.pop("toAssignee", UNSET)
        to_assignee: DominoActivityApiGoalAssignee | Unset
        if isinstance(_to_assignee, Unset):
            to_assignee = UNSET
        else:
            to_assignee = DominoActivityApiGoalAssignee.from_dict(_to_assignee)

        _to_stage = d.pop("toStage", UNSET)
        to_stage: DominoActivityApiProjectStage | Unset
        if isinstance(_to_stage, Unset):
            to_stage = UNSET
        else:
            to_stage = DominoActivityApiProjectStage.from_dict(_to_stage)

        domino_activity_api_project_goal_bulk_update_activity_metadata = cls(
            goal_ids=goal_ids,
            goal_names=goal_names,
            update_assignee=update_assignee,
            update_stage=update_stage,
            to_assignee=to_assignee,
            to_stage=to_stage,
        )

        domino_activity_api_project_goal_bulk_update_activity_metadata.additional_properties = d
        return domino_activity_api_project_goal_bulk_update_activity_metadata

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
