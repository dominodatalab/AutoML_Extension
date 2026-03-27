from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_projects_templates_api_models_dependency_template_dto_kind import (
    DominoProjectsTemplatesApiModelsDependencyTemplateDtoKind,
)

T = TypeVar("T", bound="DominoProjectsTemplatesApiModelsDependencyTemplateDto")


@_attrs_define
class DominoProjectsTemplatesApiModelsDependencyTemplateDto:
    """
    Attributes:
        template_name (str):
        template_id (str):
        revision_id (str):
        kind (DominoProjectsTemplatesApiModelsDependencyTemplateDtoKind):
    """

    template_name: str
    template_id: str
    revision_id: str
    kind: DominoProjectsTemplatesApiModelsDependencyTemplateDtoKind
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template_name = self.template_name

        template_id = self.template_id

        revision_id = self.revision_id

        kind = self.kind.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "templateName": template_name,
                "templateId": template_id,
                "revisionId": revision_id,
                "kind": kind,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        template_name = d.pop("templateName")

        template_id = d.pop("templateId")

        revision_id = d.pop("revisionId")

        kind = DominoProjectsTemplatesApiModelsDependencyTemplateDtoKind(d.pop("kind"))

        domino_projects_templates_api_models_dependency_template_dto = cls(
            template_name=template_name,
            template_id=template_id,
            revision_id=revision_id,
            kind=kind,
        )

        domino_projects_templates_api_models_dependency_template_dto.additional_properties = d
        return domino_projects_templates_api_models_dependency_template_dto

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
