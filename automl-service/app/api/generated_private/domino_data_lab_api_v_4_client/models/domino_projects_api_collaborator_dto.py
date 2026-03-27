from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_projects_api_collaborator_dto_project_role import DominoProjectsApiCollaboratorDTOProjectRole

T = TypeVar("T", bound="DominoProjectsApiCollaboratorDTO")


@_attrs_define
class DominoProjectsApiCollaboratorDTO:
    """
    Attributes:
        collaborator_id (str):
        project_role (DominoProjectsApiCollaboratorDTOProjectRole):
    """

    collaborator_id: str
    project_role: DominoProjectsApiCollaboratorDTOProjectRole
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collaborator_id = self.collaborator_id

        project_role = self.project_role.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collaboratorId": collaborator_id,
                "projectRole": project_role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        collaborator_id = d.pop("collaboratorId")

        project_role = DominoProjectsApiCollaboratorDTOProjectRole(d.pop("projectRole"))

        domino_projects_api_collaborator_dto = cls(
            collaborator_id=collaborator_id,
            project_role=project_role,
        )

        domino_projects_api_collaborator_dto.additional_properties = d
        return domino_projects_api_collaborator_dto

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
