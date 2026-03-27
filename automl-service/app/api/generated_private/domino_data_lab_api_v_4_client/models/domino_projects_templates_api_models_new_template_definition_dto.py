from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_projects_templates_api_models_new_settings_dto import (
        DominoProjectsTemplatesApiModelsNewSettingsDto,
    )


T = TypeVar("T", bound="DominoProjectsTemplatesApiModelsNewTemplateDefinitionDto")


@_attrs_define
class DominoProjectsTemplatesApiModelsNewTemplateDefinitionDto:
    """
    Attributes:
        settings (DominoProjectsTemplatesApiModelsNewSettingsDto):
    """

    settings: DominoProjectsTemplatesApiModelsNewSettingsDto
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        settings = self.settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "settings": settings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_templates_api_models_new_settings_dto import (
            DominoProjectsTemplatesApiModelsNewSettingsDto,
        )

        d = dict(src_dict)
        settings = DominoProjectsTemplatesApiModelsNewSettingsDto.from_dict(d.pop("settings"))

        domino_projects_templates_api_models_new_template_definition_dto = cls(
            settings=settings,
        )

        domino_projects_templates_api_models_new_template_definition_dto.additional_properties = d
        return domino_projects_templates_api_models_new_template_definition_dto

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
