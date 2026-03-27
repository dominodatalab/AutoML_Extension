from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_projects_templates_api_models_environment_dto import (
        DominoProjectsTemplatesApiModelsEnvironmentDto,
    )


T = TypeVar("T", bound="DominoProjectsTemplatesApiModelsEnvironmentRevisionDto")


@_attrs_define
class DominoProjectsTemplatesApiModelsEnvironmentRevisionDto:
    """
    Attributes:
        id (str):
        environment (DominoProjectsTemplatesApiModelsEnvironmentDto):
    """

    id: str
    environment: DominoProjectsTemplatesApiModelsEnvironmentDto
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        environment = self.environment.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "environment": environment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_templates_api_models_environment_dto import (
            DominoProjectsTemplatesApiModelsEnvironmentDto,
        )

        d = dict(src_dict)
        id = d.pop("id")

        environment = DominoProjectsTemplatesApiModelsEnvironmentDto.from_dict(d.pop("environment"))

        domino_projects_templates_api_models_environment_revision_dto = cls(
            id=id,
            environment=environment,
        )

        domino_projects_templates_api_models_environment_revision_dto.additional_properties = d
        return domino_projects_templates_api_models_environment_revision_dto

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
