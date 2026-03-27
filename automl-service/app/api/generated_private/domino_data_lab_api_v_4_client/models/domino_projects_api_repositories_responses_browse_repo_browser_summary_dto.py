from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_api_repositories_responses_browse_repo_branch_summary_dto import (
        DominoProjectsApiRepositoriesResponsesBrowseRepoBranchSummaryDTO,
    )
    from ..models.domino_projects_api_repositories_responses_browse_repo_directory_summary_dto import (
        DominoProjectsApiRepositoriesResponsesBrowseRepoDirectorySummaryDTO,
    )


T = TypeVar("T", bound="DominoProjectsApiRepositoriesResponsesBrowseRepoBrowserSummaryDTO")


@_attrs_define
class DominoProjectsApiRepositoriesResponsesBrowseRepoBrowserSummaryDTO:
    """
    Attributes:
        ref (DominoProjectsApiRepositoriesResponsesBrowseRepoBranchSummaryDTO):
        dir_ (DominoProjectsApiRepositoriesResponsesBrowseRepoDirectorySummaryDTO | Unset):
    """

    ref: DominoProjectsApiRepositoriesResponsesBrowseRepoBranchSummaryDTO
    dir_: DominoProjectsApiRepositoriesResponsesBrowseRepoDirectorySummaryDTO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ref = self.ref.to_dict()

        dir_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dir_, Unset):
            dir_ = self.dir_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ref": ref,
            }
        )
        if dir_ is not UNSET:
            field_dict["dir"] = dir_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_repositories_responses_browse_repo_branch_summary_dto import (
            DominoProjectsApiRepositoriesResponsesBrowseRepoBranchSummaryDTO,
        )
        from ..models.domino_projects_api_repositories_responses_browse_repo_directory_summary_dto import (
            DominoProjectsApiRepositoriesResponsesBrowseRepoDirectorySummaryDTO,
        )

        d = dict(src_dict)
        ref = DominoProjectsApiRepositoriesResponsesBrowseRepoBranchSummaryDTO.from_dict(d.pop("ref"))

        _dir_ = d.pop("dir", UNSET)
        dir_: DominoProjectsApiRepositoriesResponsesBrowseRepoDirectorySummaryDTO | Unset
        if isinstance(_dir_, Unset):
            dir_ = UNSET
        else:
            dir_ = DominoProjectsApiRepositoriesResponsesBrowseRepoDirectorySummaryDTO.from_dict(_dir_)

        domino_projects_api_repositories_responses_browse_repo_browser_summary_dto = cls(
            ref=ref,
            dir_=dir_,
        )

        domino_projects_api_repositories_responses_browse_repo_browser_summary_dto.additional_properties = d
        return domino_projects_api_repositories_responses_browse_repo_browser_summary_dto

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
