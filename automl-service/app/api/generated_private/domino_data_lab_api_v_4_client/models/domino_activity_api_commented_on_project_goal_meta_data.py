from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoActivityApiCommentedOnProjectGoalMetaData")


@_attrs_define
class DominoActivityApiCommentedOnProjectGoalMetaData:
    """
    Attributes:
        goal_id (str):
        title (str):
        is_archived (bool):
    """

    goal_id: str
    title: str
    is_archived: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        goal_id = self.goal_id

        title = self.title

        is_archived = self.is_archived

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "goalId": goal_id,
                "title": title,
                "isArchived": is_archived,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        goal_id = d.pop("goalId")

        title = d.pop("title")

        is_archived = d.pop("isArchived")

        domino_activity_api_commented_on_project_goal_meta_data = cls(
            goal_id=goal_id,
            title=title,
            is_archived=is_archived,
        )

        domino_activity_api_commented_on_project_goal_meta_data.additional_properties = d
        return domino_activity_api_commented_on_project_goal_meta_data

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
