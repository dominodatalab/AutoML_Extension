from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoProjectManagementWebLinkFileToGoalRequest")


@_attrs_define
class DominoProjectManagementWebLinkFileToGoalRequest:
    """
    Attributes:
        file_name (str):
        commit_id (str):
        project_id (str):
        goal_id (str):
    """

    file_name: str
    commit_id: str
    project_id: str
    goal_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_name = self.file_name

        commit_id = self.commit_id

        project_id = self.project_id

        goal_id = self.goal_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fileName": file_name,
                "commitId": commit_id,
                "projectId": project_id,
                "goalId": goal_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_name = d.pop("fileName")

        commit_id = d.pop("commitId")

        project_id = d.pop("projectId")

        goal_id = d.pop("goalId")

        domino_project_management_web_link_file_to_goal_request = cls(
            file_name=file_name,
            commit_id=commit_id,
            project_id=project_id,
            goal_id=goal_id,
        )

        domino_project_management_web_link_file_to_goal_request.additional_properties = d
        return domino_project_management_web_link_file_to_goal_request

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
