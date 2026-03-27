from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoProjectManagementWebBulkDeleteProjectGoals")


@_attrs_define
class DominoProjectManagementWebBulkDeleteProjectGoals:
    """
    Attributes:
        goal_ids (list[str]):
    """

    goal_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        goal_ids = self.goal_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "goalIds": goal_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        goal_ids = cast(list[str], d.pop("goalIds"))

        domino_project_management_web_bulk_delete_project_goals = cls(
            goal_ids=goal_ids,
        )

        domino_project_management_web_bulk_delete_project_goals.additional_properties = d
        return domino_project_management_web_bulk_delete_project_goals

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
