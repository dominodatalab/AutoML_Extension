from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_projects_templates_api_models_new_source_project_dto_included_item import (
    DominoProjectsTemplatesApiModelsNewSourceProjectDtoIncludedItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_templates_api_models_template_backing_git_code_spec_dto import (
        DominoProjectsTemplatesApiModelsTemplateBackingGitCodeSpecDto,
    )


T = TypeVar("T", bound="DominoProjectsTemplatesApiModelsNewSourceProjectDto")


@_attrs_define
class DominoProjectsTemplatesApiModelsNewSourceProjectDto:
    """
    Attributes:
        id (str):
        included (list[DominoProjectsTemplatesApiModelsNewSourceProjectDtoIncludedItem]):
        git_provider_code_spec (DominoProjectsTemplatesApiModelsTemplateBackingGitCodeSpecDto | Unset):
    """

    id: str
    included: list[DominoProjectsTemplatesApiModelsNewSourceProjectDtoIncludedItem]
    git_provider_code_spec: DominoProjectsTemplatesApiModelsTemplateBackingGitCodeSpecDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        included = []
        for included_item_data in self.included:
            included_item = included_item_data.value
            included.append(included_item)

        git_provider_code_spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.git_provider_code_spec, Unset):
            git_provider_code_spec = self.git_provider_code_spec.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "included": included,
            }
        )
        if git_provider_code_spec is not UNSET:
            field_dict["gitProviderCodeSpec"] = git_provider_code_spec

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_templates_api_models_template_backing_git_code_spec_dto import (
            DominoProjectsTemplatesApiModelsTemplateBackingGitCodeSpecDto,
        )

        d = dict(src_dict)
        id = d.pop("id")

        included = []
        _included = d.pop("included")
        for included_item_data in _included:
            included_item = DominoProjectsTemplatesApiModelsNewSourceProjectDtoIncludedItem(included_item_data)

            included.append(included_item)

        _git_provider_code_spec = d.pop("gitProviderCodeSpec", UNSET)
        git_provider_code_spec: DominoProjectsTemplatesApiModelsTemplateBackingGitCodeSpecDto | Unset
        if isinstance(_git_provider_code_spec, Unset):
            git_provider_code_spec = UNSET
        else:
            git_provider_code_spec = DominoProjectsTemplatesApiModelsTemplateBackingGitCodeSpecDto.from_dict(
                _git_provider_code_spec
            )

        domino_projects_templates_api_models_new_source_project_dto = cls(
            id=id,
            included=included,
            git_provider_code_spec=git_provider_code_spec,
        )

        domino_projects_templates_api_models_new_source_project_dto.additional_properties = d
        return domino_projects_templates_api_models_new_source_project_dto

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
