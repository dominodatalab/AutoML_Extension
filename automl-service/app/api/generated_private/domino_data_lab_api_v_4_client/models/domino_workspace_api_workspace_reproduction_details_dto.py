from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_workspace_api_workspace_reproduction_details_dto_workspace_reproduction_type import (
    DominoWorkspaceApiWorkspaceReproductionDetailsDtoWorkspaceReproductionType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_workspace_api_workspace_initial_git_commit_dto import (
        DominoWorkspaceApiWorkspaceInitialGitCommitDto,
    )


T = TypeVar("T", bound="DominoWorkspaceApiWorkspaceReproductionDetailsDto")


@_attrs_define
class DominoWorkspaceApiWorkspaceReproductionDetailsDto:
    """
    Attributes:
        dfs_commit (str):
        suggested_branch_name (str):
        workspace_reproduction_type (DominoWorkspaceApiWorkspaceReproductionDetailsDtoWorkspaceReproductionType):
        git_repo_commits (list[DominoWorkspaceApiWorkspaceInitialGitCommitDto] | None | Unset):
    """

    dfs_commit: str
    suggested_branch_name: str
    workspace_reproduction_type: DominoWorkspaceApiWorkspaceReproductionDetailsDtoWorkspaceReproductionType
    git_repo_commits: list[DominoWorkspaceApiWorkspaceInitialGitCommitDto] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dfs_commit = self.dfs_commit

        suggested_branch_name = self.suggested_branch_name

        workspace_reproduction_type = self.workspace_reproduction_type.value

        git_repo_commits: list[dict[str, Any]] | None | Unset
        if isinstance(self.git_repo_commits, Unset):
            git_repo_commits = UNSET
        elif isinstance(self.git_repo_commits, list):
            git_repo_commits = []
            for git_repo_commits_type_0_item_data in self.git_repo_commits:
                git_repo_commits_type_0_item = git_repo_commits_type_0_item_data.to_dict()
                git_repo_commits.append(git_repo_commits_type_0_item)

        else:
            git_repo_commits = self.git_repo_commits

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dfsCommit": dfs_commit,
                "suggestedBranchName": suggested_branch_name,
                "workspaceReproductionType": workspace_reproduction_type,
            }
        )
        if git_repo_commits is not UNSET:
            field_dict["gitRepoCommits"] = git_repo_commits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_workspace_api_workspace_initial_git_commit_dto import (
            DominoWorkspaceApiWorkspaceInitialGitCommitDto,
        )

        d = dict(src_dict)
        dfs_commit = d.pop("dfsCommit")

        suggested_branch_name = d.pop("suggestedBranchName")

        workspace_reproduction_type = DominoWorkspaceApiWorkspaceReproductionDetailsDtoWorkspaceReproductionType(
            d.pop("workspaceReproductionType")
        )

        def _parse_git_repo_commits(
            data: object,
        ) -> list[DominoWorkspaceApiWorkspaceInitialGitCommitDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                git_repo_commits_type_0 = []
                _git_repo_commits_type_0 = data
                for git_repo_commits_type_0_item_data in _git_repo_commits_type_0:
                    git_repo_commits_type_0_item = DominoWorkspaceApiWorkspaceInitialGitCommitDto.from_dict(
                        git_repo_commits_type_0_item_data
                    )

                    git_repo_commits_type_0.append(git_repo_commits_type_0_item)

                return git_repo_commits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DominoWorkspaceApiWorkspaceInitialGitCommitDto] | None | Unset, data)

        git_repo_commits = _parse_git_repo_commits(d.pop("gitRepoCommits", UNSET))

        domino_workspace_api_workspace_reproduction_details_dto = cls(
            dfs_commit=dfs_commit,
            suggested_branch_name=suggested_branch_name,
            workspace_reproduction_type=workspace_reproduction_type,
            git_repo_commits=git_repo_commits,
        )

        domino_workspace_api_workspace_reproduction_details_dto.additional_properties = d
        return domino_workspace_api_workspace_reproduction_details_dto

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
