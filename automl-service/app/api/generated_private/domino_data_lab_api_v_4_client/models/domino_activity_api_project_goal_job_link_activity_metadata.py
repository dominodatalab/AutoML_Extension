from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_activity_api_project_goal_job_link_activity_metadata_action import (
    DominoActivityApiProjectGoalJobLinkActivityMetadataAction,
)

T = TypeVar("T", bound="DominoActivityApiProjectGoalJobLinkActivityMetadata")


@_attrs_define
class DominoActivityApiProjectGoalJobLinkActivityMetadata:
    """
    Attributes:
        action (DominoActivityApiProjectGoalJobLinkActivityMetadataAction):
        job_number (int):
        job_id (str):
        project_goal_title (str):
    """

    action: DominoActivityApiProjectGoalJobLinkActivityMetadataAction
    job_number: int
    job_id: str
    project_goal_title: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        job_number = self.job_number

        job_id = self.job_id

        project_goal_title = self.project_goal_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "jobNumber": job_number,
                "jobId": job_id,
                "projectGoalTitle": project_goal_title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = DominoActivityApiProjectGoalJobLinkActivityMetadataAction(d.pop("action"))

        job_number = d.pop("jobNumber")

        job_id = d.pop("jobId")

        project_goal_title = d.pop("projectGoalTitle")

        domino_activity_api_project_goal_job_link_activity_metadata = cls(
            action=action,
            job_number=job_number,
            job_id=job_id,
            project_goal_title=project_goal_title,
        )

        domino_activity_api_project_goal_job_link_activity_metadata.additional_properties = d
        return domino_activity_api_project_goal_job_link_activity_metadata

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
