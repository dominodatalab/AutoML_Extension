from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoWorkspaceApiGitMergeConflictRepository")


@_attrs_define
class DominoWorkspaceApiGitMergeConflictRepository:
    """
    Attributes:
        repo_id (str):
        repo_name (str):
    """

    repo_id: str
    repo_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repo_id = self.repo_id

        repo_name = self.repo_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repoId": repo_id,
                "repoName": repo_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        repo_id = d.pop("repoId")

        repo_name = d.pop("repoName")

        domino_workspace_api_git_merge_conflict_repository = cls(
            repo_id=repo_id,
            repo_name=repo_name,
        )

        domino_workspace_api_git_merge_conflict_repository.additional_properties = d
        return domino_workspace_api_git_merge_conflict_repository

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
