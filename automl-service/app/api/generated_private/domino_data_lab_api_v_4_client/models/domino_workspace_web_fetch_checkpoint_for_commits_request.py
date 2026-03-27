from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_provenance_api_provenance_git_repo_commit import DominoProvenanceApiProvenanceGitRepoCommit


T = TypeVar("T", bound="DominoWorkspaceWebFetchCheckpointForCommitsRequest")


@_attrs_define
class DominoWorkspaceWebFetchCheckpointForCommitsRequest:
    """
    Attributes:
        dfs_commit_id (str):
        git_repo_commits (list[DominoProvenanceApiProvenanceGitRepoCommit]):
    """

    dfs_commit_id: str
    git_repo_commits: list[DominoProvenanceApiProvenanceGitRepoCommit]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dfs_commit_id = self.dfs_commit_id

        git_repo_commits = []
        for git_repo_commits_item_data in self.git_repo_commits:
            git_repo_commits_item = git_repo_commits_item_data.to_dict()
            git_repo_commits.append(git_repo_commits_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dfsCommitId": dfs_commit_id,
                "gitRepoCommits": git_repo_commits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_provenance_api_provenance_git_repo_commit import DominoProvenanceApiProvenanceGitRepoCommit

        d = dict(src_dict)
        dfs_commit_id = d.pop("dfsCommitId")

        git_repo_commits = []
        _git_repo_commits = d.pop("gitRepoCommits")
        for git_repo_commits_item_data in _git_repo_commits:
            git_repo_commits_item = DominoProvenanceApiProvenanceGitRepoCommit.from_dict(git_repo_commits_item_data)

            git_repo_commits.append(git_repo_commits_item)

        domino_workspace_web_fetch_checkpoint_for_commits_request = cls(
            dfs_commit_id=dfs_commit_id,
            git_repo_commits=git_repo_commits,
        )

        domino_workspace_web_fetch_checkpoint_for_commits_request.additional_properties = d
        return domino_workspace_web_fetch_checkpoint_for_commits_request

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
