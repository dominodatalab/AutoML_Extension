from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_workspace_api_git_commit_repo import DominoWorkspaceApiGitCommitRepo


T = TypeVar("T", bound="DominoWorkspaceApiGitCommitRequest")


@_attrs_define
class DominoWorkspaceApiGitCommitRequest:
    """
    Attributes:
        project_id (str):
        repos (list[DominoWorkspaceApiGitCommitRepo]):
    """

    project_id: str
    repos: list[DominoWorkspaceApiGitCommitRepo]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        repos = []
        for repos_item_data in self.repos:
            repos_item = repos_item_data.to_dict()
            repos.append(repos_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectId": project_id,
                "repos": repos,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_workspace_api_git_commit_repo import DominoWorkspaceApiGitCommitRepo

        d = dict(src_dict)
        project_id = d.pop("projectId")

        repos = []
        _repos = d.pop("repos")
        for repos_item_data in _repos:
            repos_item = DominoWorkspaceApiGitCommitRepo.from_dict(repos_item_data)

            repos.append(repos_item)

        domino_workspace_api_git_commit_request = cls(
            project_id=project_id,
            repos=repos,
        )

        domino_workspace_api_git_commit_request.additional_properties = d
        return domino_workspace_api_git_commit_request

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
