from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoProjectsTemplatesApiModelsGitRepositoryDto")


@_attrs_define
class DominoProjectsTemplatesApiModelsGitRepositoryDto:
    """
    Attributes:
        id (str):
        uri (str):
        provider_name (str):
    """

    id: str
    uri: str
    provider_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uri = self.uri

        provider_name = self.provider_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "uri": uri,
                "providerName": provider_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        uri = d.pop("uri")

        provider_name = d.pop("providerName")

        domino_projects_templates_api_models_git_repository_dto = cls(
            id=id,
            uri=uri,
            provider_name=provider_name,
        )

        domino_projects_templates_api_models_git_repository_dto.additional_properties = d
        return domino_projects_templates_api_models_git_repository_dto

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
