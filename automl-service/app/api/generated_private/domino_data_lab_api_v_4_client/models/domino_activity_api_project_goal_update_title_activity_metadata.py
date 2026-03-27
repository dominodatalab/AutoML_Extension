from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoActivityApiProjectGoalUpdateTitleActivityMetadata")


@_attrs_define
class DominoActivityApiProjectGoalUpdateTitleActivityMetadata:
    """
    Attributes:
        from_title (str):
        to_title (str):
    """

    from_title: str
    to_title: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_title = self.from_title

        to_title = self.to_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fromTitle": from_title,
                "toTitle": to_title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_title = d.pop("fromTitle")

        to_title = d.pop("toTitle")

        domino_activity_api_project_goal_update_title_activity_metadata = cls(
            from_title=from_title,
            to_title=to_title,
        )

        domino_activity_api_project_goal_update_title_activity_metadata.additional_properties = d
        return domino_activity_api_project_goal_update_title_activity_metadata

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
