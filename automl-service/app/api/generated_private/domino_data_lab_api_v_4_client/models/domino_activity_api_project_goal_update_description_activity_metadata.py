from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoActivityApiProjectGoalUpdateDescriptionActivityMetadata")


@_attrs_define
class DominoActivityApiProjectGoalUpdateDescriptionActivityMetadata:
    """
    Attributes:
        project_goal_title (str):
        from_description (None | str | Unset):
        to_description (None | str | Unset):
    """

    project_goal_title: str
    from_description: None | str | Unset = UNSET
    to_description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_goal_title = self.project_goal_title

        from_description: None | str | Unset
        if isinstance(self.from_description, Unset):
            from_description = UNSET
        else:
            from_description = self.from_description

        to_description: None | str | Unset
        if isinstance(self.to_description, Unset):
            to_description = UNSET
        else:
            to_description = self.to_description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectGoalTitle": project_goal_title,
            }
        )
        if from_description is not UNSET:
            field_dict["fromDescription"] = from_description
        if to_description is not UNSET:
            field_dict["toDescription"] = to_description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_goal_title = d.pop("projectGoalTitle")

        def _parse_from_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_description = _parse_from_description(d.pop("fromDescription", UNSET))

        def _parse_to_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        to_description = _parse_to_description(d.pop("toDescription", UNSET))

        domino_activity_api_project_goal_update_description_activity_metadata = cls(
            project_goal_title=project_goal_title,
            from_description=from_description,
            to_description=to_description,
        )

        domino_activity_api_project_goal_update_description_activity_metadata.additional_properties = d
        return domino_activity_api_project_goal_update_description_activity_metadata

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
