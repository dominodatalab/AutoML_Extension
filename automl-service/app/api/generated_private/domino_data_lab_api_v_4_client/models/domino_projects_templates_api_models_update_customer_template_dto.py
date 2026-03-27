from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_projects_templates_api_models_update_customer_template_dto_visibility import (
    DominoProjectsTemplatesApiModelsUpdateCustomerTemplateDtoVisibility,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_templates_api_models_template_collaborator_dto import (
        DominoProjectsTemplatesApiModelsTemplateCollaboratorDto,
    )


T = TypeVar("T", bound="DominoProjectsTemplatesApiModelsUpdateCustomerTemplateDto")


@_attrs_define
class DominoProjectsTemplatesApiModelsUpdateCustomerTemplateDto:
    """
    Attributes:
        name (None | str | Unset):
        description (None | str | Unset):
        visibility (DominoProjectsTemplatesApiModelsUpdateCustomerTemplateDtoVisibility | Unset):
        collaborators (list[DominoProjectsTemplatesApiModelsTemplateCollaboratorDto] | None | Unset):
        tags (list[str] | None | Unset):
        is_company_official (bool | None | Unset):
    """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    visibility: DominoProjectsTemplatesApiModelsUpdateCustomerTemplateDtoVisibility | Unset = UNSET
    collaborators: list[DominoProjectsTemplatesApiModelsTemplateCollaboratorDto] | None | Unset = UNSET
    tags: list[str] | None | Unset = UNSET
    is_company_official: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        collaborators: list[dict[str, Any]] | None | Unset
        if isinstance(self.collaborators, Unset):
            collaborators = UNSET
        elif isinstance(self.collaborators, list):
            collaborators = []
            for collaborators_type_0_item_data in self.collaborators:
                collaborators_type_0_item = collaborators_type_0_item_data.to_dict()
                collaborators.append(collaborators_type_0_item)

        else:
            collaborators = self.collaborators

        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        is_company_official: bool | None | Unset
        if isinstance(self.is_company_official, Unset):
            is_company_official = UNSET
        else:
            is_company_official = self.is_company_official

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if collaborators is not UNSET:
            field_dict["collaborators"] = collaborators
        if tags is not UNSET:
            field_dict["tags"] = tags
        if is_company_official is not UNSET:
            field_dict["isCompanyOfficial"] = is_company_official

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_templates_api_models_template_collaborator_dto import (
            DominoProjectsTemplatesApiModelsTemplateCollaboratorDto,
        )

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _visibility = d.pop("visibility", UNSET)
        visibility: DominoProjectsTemplatesApiModelsUpdateCustomerTemplateDtoVisibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = DominoProjectsTemplatesApiModelsUpdateCustomerTemplateDtoVisibility(_visibility)

        def _parse_collaborators(
            data: object,
        ) -> list[DominoProjectsTemplatesApiModelsTemplateCollaboratorDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                collaborators_type_0 = []
                _collaborators_type_0 = data
                for collaborators_type_0_item_data in _collaborators_type_0:
                    collaborators_type_0_item = DominoProjectsTemplatesApiModelsTemplateCollaboratorDto.from_dict(
                        collaborators_type_0_item_data
                    )

                    collaborators_type_0.append(collaborators_type_0_item)

                return collaborators_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DominoProjectsTemplatesApiModelsTemplateCollaboratorDto] | None | Unset, data)

        collaborators = _parse_collaborators(d.pop("collaborators", UNSET))

        def _parse_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_is_company_official(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_company_official = _parse_is_company_official(d.pop("isCompanyOfficial", UNSET))

        domino_projects_templates_api_models_update_customer_template_dto = cls(
            name=name,
            description=description,
            visibility=visibility,
            collaborators=collaborators,
            tags=tags,
            is_company_official=is_company_official,
        )

        domino_projects_templates_api_models_update_customer_template_dto.additional_properties = d
        return domino_projects_templates_api_models_update_customer_template_dto

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
