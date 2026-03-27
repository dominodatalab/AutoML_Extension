from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_projects_templates_api_models_new_customer_template_dto_type import (
    DominoProjectsTemplatesApiModelsNewCustomerTemplateDtoType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_api_billing_tag import DominoProjectsApiBillingTag
    from ..models.domino_projects_templates_api_models_new_source_project_dto import (
        DominoProjectsTemplatesApiModelsNewSourceProjectDto,
    )
    from ..models.domino_projects_templates_api_models_new_template_definition_dto import (
        DominoProjectsTemplatesApiModelsNewTemplateDefinitionDto,
    )
    from ..models.domino_projects_templates_api_models_template_access_dto import (
        DominoProjectsTemplatesApiModelsTemplateAccessDto,
    )


T = TypeVar("T", bound="DominoProjectsTemplatesApiModelsNewCustomerTemplateDto")


@_attrs_define
class DominoProjectsTemplatesApiModelsNewCustomerTemplateDto:
    """
    Attributes:
        name (str):
        access (DominoProjectsTemplatesApiModelsTemplateAccessDto):
        type_ (DominoProjectsTemplatesApiModelsNewCustomerTemplateDtoType):
        source_project (DominoProjectsTemplatesApiModelsNewSourceProjectDto):
        definition (DominoProjectsTemplatesApiModelsNewTemplateDefinitionDto):
        description (None | str | Unset):
        billing_tag (DominoProjectsApiBillingTag | Unset):
    """

    name: str
    access: DominoProjectsTemplatesApiModelsTemplateAccessDto
    type_: DominoProjectsTemplatesApiModelsNewCustomerTemplateDtoType
    source_project: DominoProjectsTemplatesApiModelsNewSourceProjectDto
    definition: DominoProjectsTemplatesApiModelsNewTemplateDefinitionDto
    description: None | str | Unset = UNSET
    billing_tag: DominoProjectsApiBillingTag | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        access = self.access.to_dict()

        type_ = self.type_.value

        source_project = self.source_project.to_dict()

        definition = self.definition.to_dict()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        billing_tag: dict[str, Any] | Unset = UNSET
        if not isinstance(self.billing_tag, Unset):
            billing_tag = self.billing_tag.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "access": access,
                "type": type_,
                "sourceProject": source_project,
                "definition": definition,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if billing_tag is not UNSET:
            field_dict["billingTag"] = billing_tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_billing_tag import DominoProjectsApiBillingTag
        from ..models.domino_projects_templates_api_models_new_source_project_dto import (
            DominoProjectsTemplatesApiModelsNewSourceProjectDto,
        )
        from ..models.domino_projects_templates_api_models_new_template_definition_dto import (
            DominoProjectsTemplatesApiModelsNewTemplateDefinitionDto,
        )
        from ..models.domino_projects_templates_api_models_template_access_dto import (
            DominoProjectsTemplatesApiModelsTemplateAccessDto,
        )

        d = dict(src_dict)
        name = d.pop("name")

        access = DominoProjectsTemplatesApiModelsTemplateAccessDto.from_dict(d.pop("access"))

        type_ = DominoProjectsTemplatesApiModelsNewCustomerTemplateDtoType(d.pop("type"))

        source_project = DominoProjectsTemplatesApiModelsNewSourceProjectDto.from_dict(d.pop("sourceProject"))

        definition = DominoProjectsTemplatesApiModelsNewTemplateDefinitionDto.from_dict(d.pop("definition"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _billing_tag = d.pop("billingTag", UNSET)
        billing_tag: DominoProjectsApiBillingTag | Unset
        if isinstance(_billing_tag, Unset):
            billing_tag = UNSET
        else:
            billing_tag = DominoProjectsApiBillingTag.from_dict(_billing_tag)

        domino_projects_templates_api_models_new_customer_template_dto = cls(
            name=name,
            access=access,
            type_=type_,
            source_project=source_project,
            definition=definition,
            description=description,
            billing_tag=billing_tag,
        )

        domino_projects_templates_api_models_new_customer_template_dto.additional_properties = d
        return domino_projects_templates_api_models_new_customer_template_dto

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
