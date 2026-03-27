from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoProjectsWebCreateProjectGoal")


@_attrs_define
class DominoProjectsWebCreateProjectGoal:
    """
    Attributes:
        title (str):
        description (None | str | Unset):
        stage_id (None | str | Unset):
        assignee_id (None | str | Unset):
    """

    title: str
    description: None | str | Unset = UNSET
    stage_id: None | str | Unset = UNSET
    assignee_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        stage_id: None | str | Unset
        if isinstance(self.stage_id, Unset):
            stage_id = UNSET
        else:
            stage_id = self.stage_id

        assignee_id: None | str | Unset
        if isinstance(self.assignee_id, Unset):
            assignee_id = UNSET
        else:
            assignee_id = self.assignee_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if stage_id is not UNSET:
            field_dict["stageId"] = stage_id
        if assignee_id is not UNSET:
            field_dict["assigneeId"] = assignee_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_stage_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stage_id = _parse_stage_id(d.pop("stageId", UNSET))

        def _parse_assignee_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assignee_id = _parse_assignee_id(d.pop("assigneeId", UNSET))

        domino_projects_web_create_project_goal = cls(
            title=title,
            description=description,
            stage_id=stage_id,
            assignee_id=assignee_id,
        )

        domino_projects_web_create_project_goal.additional_properties = d
        return domino_projects_web_create_project_goal

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
