from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_projects_api_repositories_responses_browse_commit_author_dto import (
        DominoProjectsApiRepositoriesResponsesBrowseCommitAuthorDTO,
    )


T = TypeVar("T", bound="DominoProjectsApiRepositoriesResponsesBrowseCommitShortDTO")


@_attrs_define
class DominoProjectsApiRepositoriesResponsesBrowseCommitShortDTO:
    """
    Attributes:
        sha (str):
        author (DominoProjectsApiRepositoriesResponsesBrowseCommitAuthorDTO):
        message (str):
    """

    sha: str
    author: DominoProjectsApiRepositoriesResponsesBrowseCommitAuthorDTO
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sha = self.sha

        author = self.author.to_dict()

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sha": sha,
                "author": author,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_repositories_responses_browse_commit_author_dto import (
            DominoProjectsApiRepositoriesResponsesBrowseCommitAuthorDTO,
        )

        d = dict(src_dict)
        sha = d.pop("sha")

        author = DominoProjectsApiRepositoriesResponsesBrowseCommitAuthorDTO.from_dict(d.pop("author"))

        message = d.pop("message")

        domino_projects_api_repositories_responses_browse_commit_short_dto = cls(
            sha=sha,
            author=author,
            message=message,
        )

        domino_projects_api_repositories_responses_browse_commit_short_dto.additional_properties = d
        return domino_projects_api_repositories_responses_browse_commit_short_dto

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
