from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_projects_templates_api_models_project_owner_dto import (
        DominoProjectsTemplatesApiModelsProjectOwnerDto,
    )


T = TypeVar("T", bound="DominoProjectsTemplatesApiModelsBackingProjectDto")


@_attrs_define
class DominoProjectsTemplatesApiModelsBackingProjectDto:
    """
    Attributes:
        id (str):
        name (str):
        owner (DominoProjectsTemplatesApiModelsProjectOwnerDto):
    """

    id: str
    name: str
    owner: DominoProjectsTemplatesApiModelsProjectOwnerDto
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        owner = self.owner.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "owner": owner,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_templates_api_models_project_owner_dto import (
            DominoProjectsTemplatesApiModelsProjectOwnerDto,
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        owner = DominoProjectsTemplatesApiModelsProjectOwnerDto.from_dict(d.pop("owner"))

        domino_projects_templates_api_models_backing_project_dto = cls(
            id=id,
            name=name,
            owner=owner,
        )

        domino_projects_templates_api_models_backing_project_dto.additional_properties = d
        return domino_projects_templates_api_models_backing_project_dto

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
