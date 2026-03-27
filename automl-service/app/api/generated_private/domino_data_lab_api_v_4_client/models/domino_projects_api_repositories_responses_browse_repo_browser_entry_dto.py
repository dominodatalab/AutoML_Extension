from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_projects_api_repositories_responses_browse_repo_browser_entry_dto_kind import (
    DominoProjectsApiRepositoriesResponsesBrowseRepoBrowserEntryDTOKind,
)

if TYPE_CHECKING:
    from ..models.domino_projects_api_repositories_responses_browse_commit_short_dto import (
        DominoProjectsApiRepositoriesResponsesBrowseCommitShortDTO,
    )


T = TypeVar("T", bound="DominoProjectsApiRepositoriesResponsesBrowseRepoBrowserEntryDTO")


@_attrs_define
class DominoProjectsApiRepositoriesResponsesBrowseRepoBrowserEntryDTO:
    """
    Attributes:
        kind (DominoProjectsApiRepositoriesResponsesBrowseRepoBrowserEntryDTOKind):
        sha (str):
        name (str):
        path (str):
        modified (DominoProjectsApiRepositoriesResponsesBrowseCommitShortDTO):
    """

    kind: DominoProjectsApiRepositoriesResponsesBrowseRepoBrowserEntryDTOKind
    sha: str
    name: str
    path: str
    modified: DominoProjectsApiRepositoriesResponsesBrowseCommitShortDTO
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        sha = self.sha

        name = self.name

        path = self.path

        modified = self.modified.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "sha": sha,
                "name": name,
                "path": path,
                "modified": modified,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_repositories_responses_browse_commit_short_dto import (
            DominoProjectsApiRepositoriesResponsesBrowseCommitShortDTO,
        )

        d = dict(src_dict)
        kind = DominoProjectsApiRepositoriesResponsesBrowseRepoBrowserEntryDTOKind(d.pop("kind"))

        sha = d.pop("sha")

        name = d.pop("name")

        path = d.pop("path")

        modified = DominoProjectsApiRepositoriesResponsesBrowseCommitShortDTO.from_dict(d.pop("modified"))

        domino_projects_api_repositories_responses_browse_repo_browser_entry_dto = cls(
            kind=kind,
            sha=sha,
            name=name,
            path=path,
            modified=modified,
        )

        domino_projects_api_repositories_responses_browse_repo_browser_entry_dto.additional_properties = d
        return domino_projects_api_repositories_responses_browse_repo_browser_entry_dto

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
