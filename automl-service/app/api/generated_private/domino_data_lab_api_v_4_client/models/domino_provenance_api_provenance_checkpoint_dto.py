from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_computecluster_api_compute_cluster_config import DominoComputeclusterApiComputeClusterConfig
    from ..models.domino_hardwaretier_api_hardware_tier_identifier import DominoHardwaretierApiHardwareTierIdentifier
    from ..models.domino_provenance_api_provenance_checkpoint_dto_attributes import (
        DominoProvenanceApiProvenanceCheckpointDtoAttributes,
    )
    from ..models.domino_provenance_api_provenance_commit import DominoProvenanceApiProvenanceCommit
    from ..models.domino_provenance_api_provenance_environment_details import (
        DominoProvenanceApiProvenanceEnvironmentDetails,
    )
    from ..models.domino_provenance_api_provenance_environment_variables_map import (
        DominoProvenanceApiProvenanceEnvironmentVariablesMap,
    )
    from ..models.domino_provenance_api_provenance_git_repo_dto import DominoProvenanceApiProvenanceGitRepoDto
    from ..models.domino_provenance_api_provenance_imported_project import DominoProvenanceApiProvenanceImportedProject
    from ..models.information import Information


T = TypeVar("T", bound="DominoProvenanceApiProvenanceCheckpointDto")


@_attrs_define
class DominoProvenanceApiProvenanceCheckpointDto:
    """
    Attributes:
        id (str):
        project_id (str):
        execution_id (str):
        execution_name (str):
        created_at (datetime.datetime):
        execution_start (datetime.datetime):
        environment_details (DominoProvenanceApiProvenanceEnvironmentDetails):
        commit_message (str):
        dfs_commit (DominoProvenanceApiProvenanceCommit):
        dfs_branch (str):
        git_repo_commits (list[DominoProvenanceApiProvenanceGitRepoDto]):
        imported_projects (list[DominoProvenanceApiProvenanceImportedProject]):
        hardware_tier_id (DominoHardwaretierApiHardwareTierIdentifier):
        hardware_tier_name (str):
        volume_size (Information):
        environment_variables (DominoProvenanceApiProvenanceEnvironmentVariablesMap):
        isolate_output_commits (bool):
        attributes (DominoProvenanceApiProvenanceCheckpointDtoAttributes):
        main_git_branch (None | str | Unset):
        compute_cluster_config (DominoComputeclusterApiComputeClusterConfig | Unset):
    """

    id: str
    project_id: str
    execution_id: str
    execution_name: str
    created_at: datetime.datetime
    execution_start: datetime.datetime
    environment_details: DominoProvenanceApiProvenanceEnvironmentDetails
    commit_message: str
    dfs_commit: DominoProvenanceApiProvenanceCommit
    dfs_branch: str
    git_repo_commits: list[DominoProvenanceApiProvenanceGitRepoDto]
    imported_projects: list[DominoProvenanceApiProvenanceImportedProject]
    hardware_tier_id: DominoHardwaretierApiHardwareTierIdentifier
    hardware_tier_name: str
    volume_size: Information
    environment_variables: DominoProvenanceApiProvenanceEnvironmentVariablesMap
    isolate_output_commits: bool
    attributes: DominoProvenanceApiProvenanceCheckpointDtoAttributes
    main_git_branch: None | str | Unset = UNSET
    compute_cluster_config: DominoComputeclusterApiComputeClusterConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        project_id = self.project_id

        execution_id = self.execution_id

        execution_name = self.execution_name

        created_at = self.created_at.isoformat()

        execution_start = self.execution_start.isoformat()

        environment_details = self.environment_details.to_dict()

        commit_message = self.commit_message

        dfs_commit = self.dfs_commit.to_dict()

        dfs_branch = self.dfs_branch

        git_repo_commits = []
        for git_repo_commits_item_data in self.git_repo_commits:
            git_repo_commits_item = git_repo_commits_item_data.to_dict()
            git_repo_commits.append(git_repo_commits_item)

        imported_projects = []
        for imported_projects_item_data in self.imported_projects:
            imported_projects_item = imported_projects_item_data.to_dict()
            imported_projects.append(imported_projects_item)

        hardware_tier_id = self.hardware_tier_id.to_dict()

        hardware_tier_name = self.hardware_tier_name

        volume_size = self.volume_size.to_dict()

        environment_variables = self.environment_variables.to_dict()

        isolate_output_commits = self.isolate_output_commits

        attributes = self.attributes.to_dict()

        main_git_branch: None | str | Unset
        if isinstance(self.main_git_branch, Unset):
            main_git_branch = UNSET
        else:
            main_git_branch = self.main_git_branch

        compute_cluster_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.compute_cluster_config, Unset):
            compute_cluster_config = self.compute_cluster_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "projectId": project_id,
                "executionId": execution_id,
                "executionName": execution_name,
                "createdAt": created_at,
                "executionStart": execution_start,
                "environmentDetails": environment_details,
                "commitMessage": commit_message,
                "dfsCommit": dfs_commit,
                "dfsBranch": dfs_branch,
                "gitRepoCommits": git_repo_commits,
                "importedProjects": imported_projects,
                "hardwareTierId": hardware_tier_id,
                "hardwareTierName": hardware_tier_name,
                "volumeSize": volume_size,
                "environmentVariables": environment_variables,
                "isolateOutputCommits": isolate_output_commits,
                "attributes": attributes,
            }
        )
        if main_git_branch is not UNSET:
            field_dict["mainGitBranch"] = main_git_branch
        if compute_cluster_config is not UNSET:
            field_dict["computeClusterConfig"] = compute_cluster_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_computecluster_api_compute_cluster_config import (
            DominoComputeclusterApiComputeClusterConfig,
        )
        from ..models.domino_hardwaretier_api_hardware_tier_identifier import (
            DominoHardwaretierApiHardwareTierIdentifier,
        )
        from ..models.domino_provenance_api_provenance_checkpoint_dto_attributes import (
            DominoProvenanceApiProvenanceCheckpointDtoAttributes,
        )
        from ..models.domino_provenance_api_provenance_commit import DominoProvenanceApiProvenanceCommit
        from ..models.domino_provenance_api_provenance_environment_details import (
            DominoProvenanceApiProvenanceEnvironmentDetails,
        )
        from ..models.domino_provenance_api_provenance_environment_variables_map import (
            DominoProvenanceApiProvenanceEnvironmentVariablesMap,
        )
        from ..models.domino_provenance_api_provenance_git_repo_dto import DominoProvenanceApiProvenanceGitRepoDto
        from ..models.domino_provenance_api_provenance_imported_project import (
            DominoProvenanceApiProvenanceImportedProject,
        )
        from ..models.information import Information

        d = dict(src_dict)
        id = d.pop("id")

        project_id = d.pop("projectId")

        execution_id = d.pop("executionId")

        execution_name = d.pop("executionName")

        created_at = isoparse(d.pop("createdAt"))

        execution_start = isoparse(d.pop("executionStart"))

        environment_details = DominoProvenanceApiProvenanceEnvironmentDetails.from_dict(d.pop("environmentDetails"))

        commit_message = d.pop("commitMessage")

        dfs_commit = DominoProvenanceApiProvenanceCommit.from_dict(d.pop("dfsCommit"))

        dfs_branch = d.pop("dfsBranch")

        git_repo_commits = []
        _git_repo_commits = d.pop("gitRepoCommits")
        for git_repo_commits_item_data in _git_repo_commits:
            git_repo_commits_item = DominoProvenanceApiProvenanceGitRepoDto.from_dict(git_repo_commits_item_data)

            git_repo_commits.append(git_repo_commits_item)

        imported_projects = []
        _imported_projects = d.pop("importedProjects")
        for imported_projects_item_data in _imported_projects:
            imported_projects_item = DominoProvenanceApiProvenanceImportedProject.from_dict(imported_projects_item_data)

            imported_projects.append(imported_projects_item)

        hardware_tier_id = DominoHardwaretierApiHardwareTierIdentifier.from_dict(d.pop("hardwareTierId"))

        hardware_tier_name = d.pop("hardwareTierName")

        volume_size = Information.from_dict(d.pop("volumeSize"))

        environment_variables = DominoProvenanceApiProvenanceEnvironmentVariablesMap.from_dict(
            d.pop("environmentVariables")
        )

        isolate_output_commits = d.pop("isolateOutputCommits")

        attributes = DominoProvenanceApiProvenanceCheckpointDtoAttributes.from_dict(d.pop("attributes"))

        def _parse_main_git_branch(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        main_git_branch = _parse_main_git_branch(d.pop("mainGitBranch", UNSET))

        _compute_cluster_config = d.pop("computeClusterConfig", UNSET)
        compute_cluster_config: DominoComputeclusterApiComputeClusterConfig | Unset
        if isinstance(_compute_cluster_config, Unset):
            compute_cluster_config = UNSET
        else:
            compute_cluster_config = DominoComputeclusterApiComputeClusterConfig.from_dict(_compute_cluster_config)

        domino_provenance_api_provenance_checkpoint_dto = cls(
            id=id,
            project_id=project_id,
            execution_id=execution_id,
            execution_name=execution_name,
            created_at=created_at,
            execution_start=execution_start,
            environment_details=environment_details,
            commit_message=commit_message,
            dfs_commit=dfs_commit,
            dfs_branch=dfs_branch,
            git_repo_commits=git_repo_commits,
            imported_projects=imported_projects,
            hardware_tier_id=hardware_tier_id,
            hardware_tier_name=hardware_tier_name,
            volume_size=volume_size,
            environment_variables=environment_variables,
            isolate_output_commits=isolate_output_commits,
            attributes=attributes,
            main_git_branch=main_git_branch,
            compute_cluster_config=compute_cluster_config,
        )

        domino_provenance_api_provenance_checkpoint_dto.additional_properties = d
        return domino_provenance_api_provenance_checkpoint_dto

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
