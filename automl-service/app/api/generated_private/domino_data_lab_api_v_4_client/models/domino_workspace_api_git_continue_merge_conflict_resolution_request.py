from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_workspace_api_git_merge_conflict_repository import DominoWorkspaceApiGitMergeConflictRepository


T = TypeVar("T", bound="DominoWorkspaceApiGitContinueMergeConflictResolutionRequest")


@_attrs_define
class DominoWorkspaceApiGitContinueMergeConflictResolutionRequest:
    """
    Attributes:
        repository (DominoWorkspaceApiGitMergeConflictRepository):
        should_commit_and_push (bool):
    """

    repository: DominoWorkspaceApiGitMergeConflictRepository
    should_commit_and_push: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repository = self.repository.to_dict()

        should_commit_and_push = self.should_commit_and_push

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repository": repository,
                "shouldCommitAndPush": should_commit_and_push,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_workspace_api_git_merge_conflict_repository import (
            DominoWorkspaceApiGitMergeConflictRepository,
        )

        d = dict(src_dict)
        repository = DominoWorkspaceApiGitMergeConflictRepository.from_dict(d.pop("repository"))

        should_commit_and_push = d.pop("shouldCommitAndPush")

        domino_workspace_api_git_continue_merge_conflict_resolution_request = cls(
            repository=repository,
            should_commit_and_push=should_commit_and_push,
        )

        domino_workspace_api_git_continue_merge_conflict_resolution_request.additional_properties = d
        return domino_workspace_api_git_continue_merge_conflict_resolution_request

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
