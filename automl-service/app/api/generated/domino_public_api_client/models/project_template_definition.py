from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.project_template_definition_project_type import ProjectTemplateDefinitionProjectType

if TYPE_CHECKING:
    from ..models.project_settings import ProjectSettings
    from ..models.project_template_backing_project import ProjectTemplateBackingProject


T = TypeVar("T", bound="ProjectTemplateDefinition")


@_attrs_define
class ProjectTemplateDefinition:
    """
    Attributes:
        backing_project (ProjectTemplateBackingProject):
        project_type (ProjectTemplateDefinitionProjectType):
        settings (ProjectSettings):
    """

    backing_project: ProjectTemplateBackingProject
    project_type: ProjectTemplateDefinitionProjectType
    settings: ProjectSettings
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backing_project = self.backing_project.to_dict()

        project_type = self.project_type.value

        settings = self.settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "backingProject": backing_project,
                "projectType": project_type,
                "settings": settings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_settings import ProjectSettings
        from ..models.project_template_backing_project import ProjectTemplateBackingProject

        d = dict(src_dict)
        backing_project = ProjectTemplateBackingProject.from_dict(d.pop("backingProject"))

        project_type = ProjectTemplateDefinitionProjectType(d.pop("projectType"))

        settings = ProjectSettings.from_dict(d.pop("settings"))

        project_template_definition = cls(
            backing_project=backing_project,
            project_type=project_type,
            settings=settings,
        )

        project_template_definition.additional_properties = d
        return project_template_definition

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
