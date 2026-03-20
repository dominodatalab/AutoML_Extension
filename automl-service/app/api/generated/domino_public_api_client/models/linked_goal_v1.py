from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkedGoalV1")


@_attrs_define
class LinkedGoalV1:
    """
    Attributes:
        current_stage (str): The stage this goal is currently assigned. Example: Ideation.
        goal_id (str): Id of Goal linked to Job. Example: 62313cfd7a0af0281c01a6a6.
        job_id (str): Id of Job linked to Goal. Example: 62313d207a0af0281c01a6a7.
        project_id (str): Id of project resources belong to. Example: 62313d377a0af0281c01a6a8.
        title (str): Name of goal. Example: MyGoal.
        description (str | Unset): Description of the Goal. Example: Develop a better performing model.
    """

    current_stage: str
    goal_id: str
    job_id: str
    project_id: str
    title: str
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_stage = self.current_stage

        goal_id = self.goal_id

        job_id = self.job_id

        project_id = self.project_id

        title = self.title

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currentStage": current_stage,
                "goalId": goal_id,
                "jobId": job_id,
                "projectId": project_id,
                "title": title,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current_stage = d.pop("currentStage")

        goal_id = d.pop("goalId")

        job_id = d.pop("jobId")

        project_id = d.pop("projectId")

        title = d.pop("title")

        description = d.pop("description", UNSET)

        linked_goal_v1 = cls(
            current_stage=current_stage,
            goal_id=goal_id,
            job_id=job_id,
            project_id=project_id,
            title=title,
            description=description,
        )

        linked_goal_v1.additional_properties = d
        return linked_goal_v1

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
