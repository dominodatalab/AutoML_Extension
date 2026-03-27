from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoModelmanagerWebUnlinkmodelFromGoal")


@_attrs_define
class DominoModelmanagerWebUnlinkmodelFromGoal:
    """
    Attributes:
        model_id (str):
        model_version (int):
        project_id (str):
        goal_id (str):
    """

    model_id: str
    model_version: int
    project_id: str
    goal_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_id = self.model_id

        model_version = self.model_version

        project_id = self.project_id

        goal_id = self.goal_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modelId": model_id,
                "modelVersion": model_version,
                "projectId": project_id,
                "goalId": goal_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model_id = d.pop("modelId")

        model_version = d.pop("modelVersion")

        project_id = d.pop("projectId")

        goal_id = d.pop("goalId")

        domino_modelmanager_web_unlinkmodel_from_goal = cls(
            model_id=model_id,
            model_version=model_version,
            project_id=project_id,
            goal_id=goal_id,
        )

        domino_modelmanager_web_unlinkmodel_from_goal.additional_properties = d
        return domino_modelmanager_web_unlinkmodel_from_goal

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
