from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoWorkspacesApiWorkspaceGoal")


@_attrs_define
class DominoWorkspacesApiWorkspaceGoal:
    """
    Attributes:
        goal_id (str):
        workspace_id (str):
        workspace_number (int):
        project_id (str):
    """

    goal_id: str
    workspace_id: str
    workspace_number: int
    project_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        goal_id = self.goal_id

        workspace_id = self.workspace_id

        workspace_number = self.workspace_number

        project_id = self.project_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "goalId": goal_id,
                "workspaceId": workspace_id,
                "workspaceNumber": workspace_number,
                "projectId": project_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        goal_id = d.pop("goalId")

        workspace_id = d.pop("workspaceId")

        workspace_number = d.pop("workspaceNumber")

        project_id = d.pop("projectId")

        domino_workspaces_api_workspace_goal = cls(
            goal_id=goal_id,
            workspace_id=workspace_id,
            workspace_number=workspace_number,
            project_id=project_id,
        )

        domino_workspaces_api_workspace_goal.additional_properties = d
        return domino_workspaces_api_workspace_goal

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
