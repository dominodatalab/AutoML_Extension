from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_projects_api_repositories_git_provider_dto import DominoProjectsApiRepositoriesGitProviderDto


T = TypeVar("T", bound="DominoProjectsApiRepositoriesGitProvidersDto")


@_attrs_define
class DominoProjectsApiRepositoriesGitProvidersDto:
    """
    Attributes:
        providers (list[DominoProjectsApiRepositoriesGitProviderDto]):
    """

    providers: list[DominoProjectsApiRepositoriesGitProviderDto]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        providers = []
        for providers_item_data in self.providers:
            providers_item = providers_item_data.to_dict()
            providers.append(providers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "providers": providers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_repositories_git_provider_dto import (
            DominoProjectsApiRepositoriesGitProviderDto,
        )

        d = dict(src_dict)
        providers = []
        _providers = d.pop("providers")
        for providers_item_data in _providers:
            providers_item = DominoProjectsApiRepositoriesGitProviderDto.from_dict(providers_item_data)

            providers.append(providers_item)

        domino_projects_api_repositories_git_providers_dto = cls(
            providers=providers,
        )

        domino_projects_api_repositories_git_providers_dto.additional_properties = d
        return domino_projects_api_repositories_git_providers_dto

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
