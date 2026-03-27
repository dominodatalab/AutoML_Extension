from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoProjectsWebRaiseBlockerToProject")


@_attrs_define
class DominoProjectsWebRaiseBlockerToProject:
    """
    Attributes:
        project_id (str):
        blocker_reason (str):
    """

    project_id: str
    blocker_reason: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        blocker_reason = self.blocker_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectId": project_id,
                "blockerReason": blocker_reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = d.pop("projectId")

        blocker_reason = d.pop("blockerReason")

        domino_projects_web_raise_blocker_to_project = cls(
            project_id=project_id,
            blocker_reason=blocker_reason,
        )

        domino_projects_web_raise_blocker_to_project.additional_properties = d
        return domino_projects_web_raise_blocker_to_project

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
