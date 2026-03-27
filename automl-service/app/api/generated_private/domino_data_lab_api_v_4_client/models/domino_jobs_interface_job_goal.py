from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoJobsInterfaceJobGoal")


@_attrs_define
class DominoJobsInterfaceJobGoal:
    """
    Attributes:
        goal_id (str):
        job_id (str):
        job_number (int):
        project_id (str):
        title (str):
        current_stage (str):
        description (None | str | Unset):
    """

    goal_id: str
    job_id: str
    job_number: int
    project_id: str
    title: str
    current_stage: str
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        goal_id = self.goal_id

        job_id = self.job_id

        job_number = self.job_number

        project_id = self.project_id

        title = self.title

        current_stage = self.current_stage

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "goalId": goal_id,
                "jobId": job_id,
                "jobNumber": job_number,
                "projectId": project_id,
                "title": title,
                "currentStage": current_stage,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        goal_id = d.pop("goalId")

        job_id = d.pop("jobId")

        job_number = d.pop("jobNumber")

        project_id = d.pop("projectId")

        title = d.pop("title")

        current_stage = d.pop("currentStage")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        domino_jobs_interface_job_goal = cls(
            goal_id=goal_id,
            job_id=job_id,
            job_number=job_number,
            project_id=project_id,
            title=title,
            current_stage=current_stage,
            description=description,
        )

        domino_jobs_interface_job_goal.additional_properties = d
        return domino_jobs_interface_job_goal

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
