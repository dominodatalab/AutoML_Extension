from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoNucleusUserUpdatePinnedProjects")


@_attrs_define
class DominoNucleusUserUpdatePinnedProjects:
    """
    Attributes:
        project_id (str):
        is_pinned (bool):
    """

    project_id: str
    is_pinned: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        is_pinned = self.is_pinned

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectId": project_id,
                "isPinned": is_pinned,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = d.pop("projectId")

        is_pinned = d.pop("isPinned")

        domino_nucleus_user_update_pinned_projects = cls(
            project_id=project_id,
            is_pinned=is_pinned,
        )

        domino_nucleus_user_update_pinned_projects.additional_properties = d
        return domino_nucleus_user_update_pinned_projects

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
