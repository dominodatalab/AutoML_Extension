from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_projects_api_copied_git_repo_metadata_visibility import (
    DominoProjectsApiCopiedGitRepoMetadataVisibility,
)

T = TypeVar("T", bound="DominoProjectsApiCopiedGitRepoMetadata")


@_attrs_define
class DominoProjectsApiCopiedGitRepoMetadata:
    """
    Attributes:
        repo_name (str):
        owner_name (str):
        visibility (DominoProjectsApiCopiedGitRepoMetadataVisibility):
    """

    repo_name: str
    owner_name: str
    visibility: DominoProjectsApiCopiedGitRepoMetadataVisibility
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repo_name = self.repo_name

        owner_name = self.owner_name

        visibility = self.visibility.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repoName": repo_name,
                "ownerName": owner_name,
                "visibility": visibility,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        repo_name = d.pop("repoName")

        owner_name = d.pop("ownerName")

        visibility = DominoProjectsApiCopiedGitRepoMetadataVisibility(d.pop("visibility"))

        domino_projects_api_copied_git_repo_metadata = cls(
            repo_name=repo_name,
            owner_name=owner_name,
            visibility=visibility,
        )

        domino_projects_api_copied_git_repo_metadata.additional_properties = d
        return domino_projects_api_copied_git_repo_metadata

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
