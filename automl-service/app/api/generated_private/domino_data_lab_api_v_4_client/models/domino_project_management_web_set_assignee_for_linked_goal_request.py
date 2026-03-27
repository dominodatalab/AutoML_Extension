from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_project_management_web_assignee_for_linked_goal import (
        DominoProjectManagementWebAssigneeForLinkedGoal,
    )


T = TypeVar("T", bound="DominoProjectManagementWebSetAssigneeForLinkedGoalRequest")


@_attrs_define
class DominoProjectManagementWebSetAssigneeForLinkedGoalRequest:
    """
    Attributes:
        goal_id (str):
        jira_user_data (DominoProjectManagementWebAssigneeForLinkedGoal | Unset):
    """

    goal_id: str
    jira_user_data: DominoProjectManagementWebAssigneeForLinkedGoal | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        goal_id = self.goal_id

        jira_user_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.jira_user_data, Unset):
            jira_user_data = self.jira_user_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "goalId": goal_id,
            }
        )
        if jira_user_data is not UNSET:
            field_dict["jiraUserData"] = jira_user_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_project_management_web_assignee_for_linked_goal import (
            DominoProjectManagementWebAssigneeForLinkedGoal,
        )

        d = dict(src_dict)
        goal_id = d.pop("goalId")

        _jira_user_data = d.pop("jiraUserData", UNSET)
        jira_user_data: DominoProjectManagementWebAssigneeForLinkedGoal | Unset
        if isinstance(_jira_user_data, Unset):
            jira_user_data = UNSET
        else:
            jira_user_data = DominoProjectManagementWebAssigneeForLinkedGoal.from_dict(_jira_user_data)

        domino_project_management_web_set_assignee_for_linked_goal_request = cls(
            goal_id=goal_id,
            jira_user_data=jira_user_data,
        )

        domino_project_management_web_set_assignee_for_linked_goal_request.additional_properties = d
        return domino_project_management_web_set_assignee_for_linked_goal_request

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
