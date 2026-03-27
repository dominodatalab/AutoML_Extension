from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_activity_api_project_goal_file_link_activity_metadata_action import (
    DominoActivityApiProjectGoalFileLinkActivityMetadataAction,
)

T = TypeVar("T", bound="DominoActivityApiProjectGoalFileLinkActivityMetadata")


@_attrs_define
class DominoActivityApiProjectGoalFileLinkActivityMetadata:
    """
    Attributes:
        action (DominoActivityApiProjectGoalFileLinkActivityMetadataAction):
        file_name (str):
        commit_id (str):
        project_goal_title (str):
    """

    action: DominoActivityApiProjectGoalFileLinkActivityMetadataAction
    file_name: str
    commit_id: str
    project_goal_title: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        file_name = self.file_name

        commit_id = self.commit_id

        project_goal_title = self.project_goal_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "fileName": file_name,
                "commitId": commit_id,
                "projectGoalTitle": project_goal_title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = DominoActivityApiProjectGoalFileLinkActivityMetadataAction(d.pop("action"))

        file_name = d.pop("fileName")

        commit_id = d.pop("commitId")

        project_goal_title = d.pop("projectGoalTitle")

        domino_activity_api_project_goal_file_link_activity_metadata = cls(
            action=action,
            file_name=file_name,
            commit_id=commit_id,
            project_goal_title=project_goal_title,
        )

        domino_activity_api_project_goal_file_link_activity_metadata.additional_properties = d
        return domino_activity_api_project_goal_file_link_activity_metadata

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
