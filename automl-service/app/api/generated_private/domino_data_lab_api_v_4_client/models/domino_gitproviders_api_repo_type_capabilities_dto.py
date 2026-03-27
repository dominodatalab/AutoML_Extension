from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoGitprovidersApiRepoTypeCapabilitiesDTO")


@_attrs_define
class DominoGitprovidersApiRepoTypeCapabilitiesDTO:
    """
    Attributes:
        repo_creation_enabled (bool):
        repo_listing_enabled (bool):
        owner_listing_enabled (bool):
    """

    repo_creation_enabled: bool
    repo_listing_enabled: bool
    owner_listing_enabled: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repo_creation_enabled = self.repo_creation_enabled

        repo_listing_enabled = self.repo_listing_enabled

        owner_listing_enabled = self.owner_listing_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repoCreationEnabled": repo_creation_enabled,
                "repoListingEnabled": repo_listing_enabled,
                "ownerListingEnabled": owner_listing_enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        repo_creation_enabled = d.pop("repoCreationEnabled")

        repo_listing_enabled = d.pop("repoListingEnabled")

        owner_listing_enabled = d.pop("ownerListingEnabled")

        domino_gitproviders_api_repo_type_capabilities_dto = cls(
            repo_creation_enabled=repo_creation_enabled,
            repo_listing_enabled=repo_listing_enabled,
            owner_listing_enabled=owner_listing_enabled,
        )

        domino_gitproviders_api_repo_type_capabilities_dto.additional_properties = d
        return domino_gitproviders_api_repo_type_capabilities_dto

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
