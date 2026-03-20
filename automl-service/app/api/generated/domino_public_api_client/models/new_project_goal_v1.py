from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewProjectGoalV1")


@_attrs_define
class NewProjectGoalV1:
    """
    Attributes:
        title (str): Title of the goal Example: MyGoal.
        assignee_id (str | Unset): Optional id of the user the goal will be assigned to
        description (str | Unset): An optional description of the goal
        stage_id (str | Unset): Optional id of the stage the goal will be set to
    """

    title: str
    assignee_id: str | Unset = UNSET
    description: str | Unset = UNSET
    stage_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        assignee_id = self.assignee_id

        description = self.description

        stage_id = self.stage_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if assignee_id is not UNSET:
            field_dict["assigneeId"] = assignee_id
        if description is not UNSET:
            field_dict["description"] = description
        if stage_id is not UNSET:
            field_dict["stageId"] = stage_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        assignee_id = d.pop("assigneeId", UNSET)

        description = d.pop("description", UNSET)

        stage_id = d.pop("stageId", UNSET)

        new_project_goal_v1 = cls(
            title=title,
            assignee_id=assignee_id,
            description=description,
            stage_id=stage_id,
        )

        new_project_goal_v1.additional_properties = d
        return new_project_goal_v1

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
