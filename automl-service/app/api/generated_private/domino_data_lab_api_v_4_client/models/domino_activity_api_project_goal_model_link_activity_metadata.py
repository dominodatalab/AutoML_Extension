from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_activity_api_project_goal_model_link_activity_metadata_action import (
    DominoActivityApiProjectGoalModelLinkActivityMetadataAction,
)

T = TypeVar("T", bound="DominoActivityApiProjectGoalModelLinkActivityMetadata")


@_attrs_define
class DominoActivityApiProjectGoalModelLinkActivityMetadata:
    """
    Attributes:
        action (DominoActivityApiProjectGoalModelLinkActivityMetadataAction):
        model_id (str):
        model_version (int):
        model_version_id (str):
        project_goal_title (str):
        name (str):
    """

    action: DominoActivityApiProjectGoalModelLinkActivityMetadataAction
    model_id: str
    model_version: int
    model_version_id: str
    project_goal_title: str
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        model_id = self.model_id

        model_version = self.model_version

        model_version_id = self.model_version_id

        project_goal_title = self.project_goal_title

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "modelId": model_id,
                "modelVersion": model_version,
                "modelVersionId": model_version_id,
                "projectGoalTitle": project_goal_title,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = DominoActivityApiProjectGoalModelLinkActivityMetadataAction(d.pop("action"))

        model_id = d.pop("modelId")

        model_version = d.pop("modelVersion")

        model_version_id = d.pop("modelVersionId")

        project_goal_title = d.pop("projectGoalTitle")

        name = d.pop("name")

        domino_activity_api_project_goal_model_link_activity_metadata = cls(
            action=action,
            model_id=model_id,
            model_version=model_version,
            model_version_id=model_version_id,
            project_goal_title=project_goal_title,
            name=name,
        )

        domino_activity_api_project_goal_model_link_activity_metadata.additional_properties = d
        return domino_activity_api_project_goal_model_link_activity_metadata

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
