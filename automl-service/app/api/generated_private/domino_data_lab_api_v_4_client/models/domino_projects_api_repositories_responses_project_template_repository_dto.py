from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_projects_api_repositories_responses_project_template_reference_dto import (
        DominoProjectsApiRepositoriesResponsesProjectTemplateReferenceDTO,
    )


T = TypeVar("T", bound="DominoProjectsApiRepositoriesResponsesProjectTemplateRepositoryDTO")


@_attrs_define
class DominoProjectsApiRepositoriesResponsesProjectTemplateRepositoryDTO:
    """
    Attributes:
        uri (str):
        ref (DominoProjectsApiRepositoriesResponsesProjectTemplateReferenceDTO):
        service_provider (str):
    """

    uri: str
    ref: DominoProjectsApiRepositoriesResponsesProjectTemplateReferenceDTO
    service_provider: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uri = self.uri

        ref = self.ref.to_dict()

        service_provider = self.service_provider

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uri": uri,
                "ref": ref,
                "serviceProvider": service_provider,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_repositories_responses_project_template_reference_dto import (
            DominoProjectsApiRepositoriesResponsesProjectTemplateReferenceDTO,
        )

        d = dict(src_dict)
        uri = d.pop("uri")

        ref = DominoProjectsApiRepositoriesResponsesProjectTemplateReferenceDTO.from_dict(d.pop("ref"))

        service_provider = d.pop("serviceProvider")

        domino_projects_api_repositories_responses_project_template_repository_dto = cls(
            uri=uri,
            ref=ref,
            service_provider=service_provider,
        )

        domino_projects_api_repositories_responses_project_template_repository_dto.additional_properties = d
        return domino_projects_api_repositories_responses_project_template_repository_dto

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
