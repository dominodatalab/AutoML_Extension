from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_templates_api_models_named_link import DominoProjectsTemplatesApiModelsNamedLink
    from ..models.domino_projects_templates_api_models_project_template_size_dto import (
        DominoProjectsTemplatesApiModelsProjectTemplateSizeDto,
    )


T = TypeVar("T", bound="DominoProjectsTemplatesApiModelsProjectHubModelDto")


@_attrs_define
class DominoProjectsTemplatesApiModelsProjectHubModelDto:
    """
    Attributes:
        name (str):
        link (str):
        size (DominoProjectsTemplatesApiModelsProjectTemplateSizeDto | Unset):
        source (DominoProjectsTemplatesApiModelsNamedLink | Unset):
    """

    name: str
    link: str
    size: DominoProjectsTemplatesApiModelsProjectTemplateSizeDto | Unset = UNSET
    source: DominoProjectsTemplatesApiModelsNamedLink | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        link = self.link

        size: dict[str, Any] | Unset = UNSET
        if not isinstance(self.size, Unset):
            size = self.size.to_dict()

        source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "link": link,
            }
        )
        if size is not UNSET:
            field_dict["size"] = size
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_templates_api_models_named_link import DominoProjectsTemplatesApiModelsNamedLink
        from ..models.domino_projects_templates_api_models_project_template_size_dto import (
            DominoProjectsTemplatesApiModelsProjectTemplateSizeDto,
        )

        d = dict(src_dict)
        name = d.pop("name")

        link = d.pop("link")

        _size = d.pop("size", UNSET)
        size: DominoProjectsTemplatesApiModelsProjectTemplateSizeDto | Unset
        if isinstance(_size, Unset):
            size = UNSET
        else:
            size = DominoProjectsTemplatesApiModelsProjectTemplateSizeDto.from_dict(_size)

        _source = d.pop("source", UNSET)
        source: DominoProjectsTemplatesApiModelsNamedLink | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = DominoProjectsTemplatesApiModelsNamedLink.from_dict(_source)

        domino_projects_templates_api_models_project_hub_model_dto = cls(
            name=name,
            link=link,
            size=size,
            source=source,
        )

        domino_projects_templates_api_models_project_hub_model_dto.additional_properties = d
        return domino_projects_templates_api_models_project_hub_model_dto

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
