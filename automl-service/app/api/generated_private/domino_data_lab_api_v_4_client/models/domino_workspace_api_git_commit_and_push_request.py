from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_provenance_api_sync_operation_info import DominoProvenanceApiSyncOperationInfo
    from ..models.domino_workspace_api_git_commit_repo import DominoWorkspaceApiGitCommitRepo


T = TypeVar("T", bound="DominoWorkspaceApiGitCommitAndPushRequest")


@_attrs_define
class DominoWorkspaceApiGitCommitAndPushRequest:
    """
    Attributes:
        project_id (str):
        repos (list[DominoWorkspaceApiGitCommitRepo]):
        sync_operation_info (DominoProvenanceApiSyncOperationInfo | Unset):
        push_only (bool | None | Unset):
    """

    project_id: str
    repos: list[DominoWorkspaceApiGitCommitRepo]
    sync_operation_info: DominoProvenanceApiSyncOperationInfo | Unset = UNSET
    push_only: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        repos = []
        for repos_item_data in self.repos:
            repos_item = repos_item_data.to_dict()
            repos.append(repos_item)

        sync_operation_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sync_operation_info, Unset):
            sync_operation_info = self.sync_operation_info.to_dict()

        push_only: bool | None | Unset
        if isinstance(self.push_only, Unset):
            push_only = UNSET
        else:
            push_only = self.push_only

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectId": project_id,
                "repos": repos,
            }
        )
        if sync_operation_info is not UNSET:
            field_dict["syncOperationInfo"] = sync_operation_info
        if push_only is not UNSET:
            field_dict["pushOnly"] = push_only

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_provenance_api_sync_operation_info import DominoProvenanceApiSyncOperationInfo
        from ..models.domino_workspace_api_git_commit_repo import DominoWorkspaceApiGitCommitRepo

        d = dict(src_dict)
        project_id = d.pop("projectId")

        repos = []
        _repos = d.pop("repos")
        for repos_item_data in _repos:
            repos_item = DominoWorkspaceApiGitCommitRepo.from_dict(repos_item_data)

            repos.append(repos_item)

        _sync_operation_info = d.pop("syncOperationInfo", UNSET)
        sync_operation_info: DominoProvenanceApiSyncOperationInfo | Unset
        if isinstance(_sync_operation_info, Unset):
            sync_operation_info = UNSET
        else:
            sync_operation_info = DominoProvenanceApiSyncOperationInfo.from_dict(_sync_operation_info)

        def _parse_push_only(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        push_only = _parse_push_only(d.pop("pushOnly", UNSET))

        domino_workspace_api_git_commit_and_push_request = cls(
            project_id=project_id,
            repos=repos,
            sync_operation_info=sync_operation_info,
            push_only=push_only,
        )

        domino_workspace_api_git_commit_and_push_request.additional_properties = d
        return domino_workspace_api_git_commit_and_push_request

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
