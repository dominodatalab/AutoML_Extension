from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_project_management_web_set_assignee_for_goal import (
        DominoProjectManagementWebSetAssigneeForGoal,
    )


T = TypeVar("T", bound="DominoProjectManagementWebBulkEditProjectGoals")


@_attrs_define
class DominoProjectManagementWebBulkEditProjectGoals:
    """
    Attributes:
        goal_ids (list[str]):
        stage_id (None | str | Unset):
        assignee_value (DominoProjectManagementWebSetAssigneeForGoal | Unset):
    """

    goal_ids: list[str]
    stage_id: None | str | Unset = UNSET
    assignee_value: DominoProjectManagementWebSetAssigneeForGoal | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        goal_ids = self.goal_ids

        stage_id: None | str | Unset
        if isinstance(self.stage_id, Unset):
            stage_id = UNSET
        else:
            stage_id = self.stage_id

        assignee_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assignee_value, Unset):
            assignee_value = self.assignee_value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "goalIds": goal_ids,
            }
        )
        if stage_id is not UNSET:
            field_dict["stageId"] = stage_id
        if assignee_value is not UNSET:
            field_dict["assigneeValue"] = assignee_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_project_management_web_set_assignee_for_goal import (
            DominoProjectManagementWebSetAssigneeForGoal,
        )

        d = dict(src_dict)
        goal_ids = cast(list[str], d.pop("goalIds"))

        def _parse_stage_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stage_id = _parse_stage_id(d.pop("stageId", UNSET))

        _assignee_value = d.pop("assigneeValue", UNSET)
        assignee_value: DominoProjectManagementWebSetAssigneeForGoal | Unset
        if isinstance(_assignee_value, Unset):
            assignee_value = UNSET
        else:
            assignee_value = DominoProjectManagementWebSetAssigneeForGoal.from_dict(_assignee_value)

        domino_project_management_web_bulk_edit_project_goals = cls(
            goal_ids=goal_ids,
            stage_id=stage_id,
            assignee_value=assignee_value,
        )

        domino_project_management_web_bulk_edit_project_goals.additional_properties = d
        return domino_project_management_web_bulk_edit_project_goals

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
