from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoWorkspacesApiWorkspaceTag")


@_attrs_define
class DominoWorkspacesApiWorkspaceTag:
    """
    Attributes:
        tag_id (str):
        name (str):
        created_by (str):
        created_at (int):
        project_id (str):
    """

    tag_id: str
    name: str
    created_by: str
    created_at: int
    project_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tag_id = self.tag_id

        name = self.name

        created_by = self.created_by

        created_at = self.created_at

        project_id = self.project_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tagId": tag_id,
                "name": name,
                "createdBy": created_by,
                "createdAt": created_at,
                "projectId": project_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tag_id = d.pop("tagId")

        name = d.pop("name")

        created_by = d.pop("createdBy")

        created_at = d.pop("createdAt")

        project_id = d.pop("projectId")

        domino_workspaces_api_workspace_tag = cls(
            tag_id=tag_id,
            name=name,
            created_by=created_by,
            created_at=created_at,
            project_id=project_id,
        )

        domino_workspaces_api_workspace_tag.additional_properties = d
        return domino_workspaces_api_workspace_tag

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
