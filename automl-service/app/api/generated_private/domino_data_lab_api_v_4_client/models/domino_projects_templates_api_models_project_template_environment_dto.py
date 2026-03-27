from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_templates_api_models_project_template_env_rev_details_dto import (
        DominoProjectsTemplatesApiModelsProjectTemplateEnvRevDetailsDto,
    )


T = TypeVar("T", bound="DominoProjectsTemplatesApiModelsProjectTemplateEnvironmentDto")


@_attrs_define
class DominoProjectsTemplatesApiModelsProjectTemplateEnvironmentDto:
    """
    Attributes:
        name (str):
        revision_details (DominoProjectsTemplatesApiModelsProjectTemplateEnvRevDetailsDto | Unset):
    """

    name: str
    revision_details: DominoProjectsTemplatesApiModelsProjectTemplateEnvRevDetailsDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        revision_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.revision_details, Unset):
            revision_details = self.revision_details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if revision_details is not UNSET:
            field_dict["revisionDetails"] = revision_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_templates_api_models_project_template_env_rev_details_dto import (
            DominoProjectsTemplatesApiModelsProjectTemplateEnvRevDetailsDto,
        )

        d = dict(src_dict)
        name = d.pop("name")

        _revision_details = d.pop("revisionDetails", UNSET)
        revision_details: DominoProjectsTemplatesApiModelsProjectTemplateEnvRevDetailsDto | Unset
        if isinstance(_revision_details, Unset):
            revision_details = UNSET
        else:
            revision_details = DominoProjectsTemplatesApiModelsProjectTemplateEnvRevDetailsDto.from_dict(
                _revision_details
            )

        domino_projects_templates_api_models_project_template_environment_dto = cls(
            name=name,
            revision_details=revision_details,
        )

        domino_projects_templates_api_models_project_template_environment_dto.additional_properties = d
        return domino_projects_templates_api_models_project_template_environment_dto

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
