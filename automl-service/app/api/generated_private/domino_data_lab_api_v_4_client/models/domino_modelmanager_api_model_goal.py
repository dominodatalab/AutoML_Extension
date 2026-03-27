from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoModelmanagerApiModelGoal")


@_attrs_define
class DominoModelmanagerApiModelGoal:
    """
    Attributes:
        model_version_id (str):
        goal_id (str):
        project_id (str):
        model_version (int):
        model_id (str):
    """

    model_version_id: str
    goal_id: str
    project_id: str
    model_version: int
    model_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_version_id = self.model_version_id

        goal_id = self.goal_id

        project_id = self.project_id

        model_version = self.model_version

        model_id = self.model_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modelVersionId": model_version_id,
                "goalId": goal_id,
                "projectId": project_id,
                "modelVersion": model_version,
                "modelId": model_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model_version_id = d.pop("modelVersionId")

        goal_id = d.pop("goalId")

        project_id = d.pop("projectId")

        model_version = d.pop("modelVersion")

        model_id = d.pop("modelId")

        domino_modelmanager_api_model_goal = cls(
            model_version_id=model_version_id,
            goal_id=goal_id,
            project_id=project_id,
            model_version=model_version,
            model_id=model_id,
        )

        domino_modelmanager_api_model_goal.additional_properties = d
        return domino_modelmanager_api_model_goal

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
