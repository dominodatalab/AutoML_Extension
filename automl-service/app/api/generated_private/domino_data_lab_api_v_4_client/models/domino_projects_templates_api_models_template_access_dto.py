from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_projects_templates_api_models_template_access_dto_visibility import (
    DominoProjectsTemplatesApiModelsTemplateAccessDtoVisibility,
)

if TYPE_CHECKING:
    from ..models.domino_projects_templates_api_models_template_collaborator_dto import (
        DominoProjectsTemplatesApiModelsTemplateCollaboratorDto,
    )


T = TypeVar("T", bound="DominoProjectsTemplatesApiModelsTemplateAccessDto")


@_attrs_define
class DominoProjectsTemplatesApiModelsTemplateAccessDto:
    """
    Attributes:
        visibility (DominoProjectsTemplatesApiModelsTemplateAccessDtoVisibility):
        collaborators (list[DominoProjectsTemplatesApiModelsTemplateCollaboratorDto]):
    """

    visibility: DominoProjectsTemplatesApiModelsTemplateAccessDtoVisibility
    collaborators: list[DominoProjectsTemplatesApiModelsTemplateCollaboratorDto]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        visibility = self.visibility.value

        collaborators = []
        for collaborators_item_data in self.collaborators:
            collaborators_item = collaborators_item_data.to_dict()
            collaborators.append(collaborators_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "visibility": visibility,
                "collaborators": collaborators,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_templates_api_models_template_collaborator_dto import (
            DominoProjectsTemplatesApiModelsTemplateCollaboratorDto,
        )

        d = dict(src_dict)
        visibility = DominoProjectsTemplatesApiModelsTemplateAccessDtoVisibility(d.pop("visibility"))

        collaborators = []
        _collaborators = d.pop("collaborators")
        for collaborators_item_data in _collaborators:
            collaborators_item = DominoProjectsTemplatesApiModelsTemplateCollaboratorDto.from_dict(
                collaborators_item_data
            )

            collaborators.append(collaborators_item)

        domino_projects_templates_api_models_template_access_dto = cls(
            visibility=visibility,
            collaborators=collaborators,
        )

        domino_projects_templates_api_models_template_access_dto.additional_properties = d
        return domino_projects_templates_api_models_template_access_dto

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
