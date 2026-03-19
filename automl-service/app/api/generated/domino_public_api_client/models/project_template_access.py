from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.project_template_access_visibility import ProjectTemplateAccessVisibility

if TYPE_CHECKING:
    from ..models.project_template_collaborator import ProjectTemplateCollaborator


T = TypeVar("T", bound="ProjectTemplateAccess")


@_attrs_define
class ProjectTemplateAccess:
    """
    Attributes:
        collaborators (list[ProjectTemplateCollaborator]):
        visibility (ProjectTemplateAccessVisibility):
    """

    collaborators: list[ProjectTemplateCollaborator]
    visibility: ProjectTemplateAccessVisibility
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collaborators = []
        for collaborators_item_data in self.collaborators:
            collaborators_item = collaborators_item_data.to_dict()
            collaborators.append(collaborators_item)

        visibility = self.visibility.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collaborators": collaborators,
                "visibility": visibility,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_template_collaborator import ProjectTemplateCollaborator

        d = dict(src_dict)
        collaborators = []
        _collaborators = d.pop("collaborators")
        for collaborators_item_data in _collaborators:
            collaborators_item = ProjectTemplateCollaborator.from_dict(collaborators_item_data)

            collaborators.append(collaborators_item)

        visibility = ProjectTemplateAccessVisibility(d.pop("visibility"))

        project_template_access = cls(
            collaborators=collaborators,
            visibility=visibility,
        )

        project_template_access.additional_properties = d
        return project_template_access

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
