from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_modelmanager_api_model_version_reproduce_in_workspace_details_status import (
    DominoModelmanagerApiModelVersionReproduceInWorkspaceDetailsStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_modelmanager_api_model_git_repo_commit import DominoModelmanagerApiModelGitRepoCommit


T = TypeVar("T", bound="DominoModelmanagerApiModelVersionReproduceInWorkspaceDetails")


@_attrs_define
class DominoModelmanagerApiModelVersionReproduceInWorkspaceDetails:
    """
    Attributes:
        model_id (str):
        model_version_id (str):
        project_name (str):
        project_owner_name (str):
        project_id (str):
        is_git_based_project (bool):
        dfs_commit_id (str):
        git_repo_commits (list[DominoModelmanagerApiModelGitRepoCommit]):
        can_be_reproduced (bool):
        env_id (str):
        env_name (str):
        env_revision_number (int):
        requested_user_id (str):
        status (DominoModelmanagerApiModelVersionReproduceInWorkspaceDetailsStatus):
        version_number (int | None | Unset):
    """

    model_id: str
    model_version_id: str
    project_name: str
    project_owner_name: str
    project_id: str
    is_git_based_project: bool
    dfs_commit_id: str
    git_repo_commits: list[DominoModelmanagerApiModelGitRepoCommit]
    can_be_reproduced: bool
    env_id: str
    env_name: str
    env_revision_number: int
    requested_user_id: str
    status: DominoModelmanagerApiModelVersionReproduceInWorkspaceDetailsStatus
    version_number: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_id = self.model_id

        model_version_id = self.model_version_id

        project_name = self.project_name

        project_owner_name = self.project_owner_name

        project_id = self.project_id

        is_git_based_project = self.is_git_based_project

        dfs_commit_id = self.dfs_commit_id

        git_repo_commits = []
        for git_repo_commits_item_data in self.git_repo_commits:
            git_repo_commits_item = git_repo_commits_item_data.to_dict()
            git_repo_commits.append(git_repo_commits_item)

        can_be_reproduced = self.can_be_reproduced

        env_id = self.env_id

        env_name = self.env_name

        env_revision_number = self.env_revision_number

        requested_user_id = self.requested_user_id

        status = self.status.value

        version_number: int | None | Unset
        if isinstance(self.version_number, Unset):
            version_number = UNSET
        else:
            version_number = self.version_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modelId": model_id,
                "modelVersionId": model_version_id,
                "projectName": project_name,
                "projectOwnerName": project_owner_name,
                "projectId": project_id,
                "isGitBasedProject": is_git_based_project,
                "dfsCommitId": dfs_commit_id,
                "gitRepoCommits": git_repo_commits,
                "canBeReproduced": can_be_reproduced,
                "envId": env_id,
                "envName": env_name,
                "envRevisionNumber": env_revision_number,
                "requestedUserId": requested_user_id,
                "status": status,
            }
        )
        if version_number is not UNSET:
            field_dict["versionNumber"] = version_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_modelmanager_api_model_git_repo_commit import DominoModelmanagerApiModelGitRepoCommit

        d = dict(src_dict)
        model_id = d.pop("modelId")

        model_version_id = d.pop("modelVersionId")

        project_name = d.pop("projectName")

        project_owner_name = d.pop("projectOwnerName")

        project_id = d.pop("projectId")

        is_git_based_project = d.pop("isGitBasedProject")

        dfs_commit_id = d.pop("dfsCommitId")

        git_repo_commits = []
        _git_repo_commits = d.pop("gitRepoCommits")
        for git_repo_commits_item_data in _git_repo_commits:
            git_repo_commits_item = DominoModelmanagerApiModelGitRepoCommit.from_dict(git_repo_commits_item_data)

            git_repo_commits.append(git_repo_commits_item)

        can_be_reproduced = d.pop("canBeReproduced")

        env_id = d.pop("envId")

        env_name = d.pop("envName")

        env_revision_number = d.pop("envRevisionNumber")

        requested_user_id = d.pop("requestedUserId")

        status = DominoModelmanagerApiModelVersionReproduceInWorkspaceDetailsStatus(d.pop("status"))

        def _parse_version_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        version_number = _parse_version_number(d.pop("versionNumber", UNSET))

        domino_modelmanager_api_model_version_reproduce_in_workspace_details = cls(
            model_id=model_id,
            model_version_id=model_version_id,
            project_name=project_name,
            project_owner_name=project_owner_name,
            project_id=project_id,
            is_git_based_project=is_git_based_project,
            dfs_commit_id=dfs_commit_id,
            git_repo_commits=git_repo_commits,
            can_be_reproduced=can_be_reproduced,
            env_id=env_id,
            env_name=env_name,
            env_revision_number=env_revision_number,
            requested_user_id=requested_user_id,
            status=status,
            version_number=version_number,
        )

        domino_modelmanager_api_model_version_reproduce_in_workspace_details.additional_properties = d
        return domino_modelmanager_api_model_version_reproduce_in_workspace_details

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
