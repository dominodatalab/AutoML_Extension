from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_workspaces_api_dependent_dataset_mount import DominoWorkspacesApiDependentDatasetMount
    from ..models.domino_workspaces_api_dependent_external_volume_mount import (
        DominoWorkspacesApiDependentExternalVolumeMount,
    )
    from ..models.domino_workspaces_api_dependent_project import DominoWorkspacesApiDependentProject
    from ..models.domino_workspaces_api_dependent_repository import DominoWorkspacesApiDependentRepository
    from ..models.domino_workspaces_api_domino_stats import DominoWorkspacesApiDominoStats
    from ..models.domino_workspaces_api_queued_workspace_history_details import (
        DominoWorkspacesApiQueuedWorkspaceHistoryDetails,
    )
    from ..models.domino_workspaces_api_stage_time import DominoWorkspacesApiStageTime
    from ..models.domino_workspaces_api_workspace_auto_sync import DominoWorkspacesApiWorkspaceAutoSync
    from ..models.domino_workspaces_api_workspace_resource_usage import DominoWorkspacesApiWorkspaceResourceUsage
    from ..models.domino_workspaces_api_workspace_started_by import DominoWorkspacesApiWorkspaceStartedBy
    from ..models.domino_workspaces_api_workspace_tag import DominoWorkspacesApiWorkspaceTag


T = TypeVar("T", bound="DominoWorkspacesApiWorkspace")


@_attrs_define
class DominoWorkspacesApiWorkspace:
    """
    Attributes:
        id (str):
        project_id (str):
        title (str):
        definition_title (str):
        stage_time (DominoWorkspacesApiStageTime):
        number (int):
        is_completed (bool):
        is_archived (bool):
        queued_workspace_history_details (DominoWorkspacesApiQueuedWorkspaceHistoryDetails):
        tags (list[DominoWorkspacesApiWorkspaceTag]):
        comments_count (int):
        status (str):
        input_commit_id (str):
        domino_stats (list[DominoWorkspacesApiDominoStats]):
        dependent_repositories (list[DominoWorkspacesApiDependentRepository]):
        dependent_dataset_mounts (list[DominoWorkspacesApiDependentDatasetMount]):
        dependent_projects (list[DominoWorkspacesApiDependentProject]):
        is_restartable (bool):
        dependent_external_volume_mounts (list[DominoWorkspacesApiDependentExternalVolumeMount]):
        started_by (DominoWorkspacesApiWorkspaceStartedBy | Unset):
        usage (DominoWorkspacesApiWorkspaceResourceUsage | Unset):
        output_commit_id (None | str | Unset):
        auto_sync_settings (DominoWorkspacesApiWorkspaceAutoSync | Unset):
    """

    id: str
    project_id: str
    title: str
    definition_title: str
    stage_time: DominoWorkspacesApiStageTime
    number: int
    is_completed: bool
    is_archived: bool
    queued_workspace_history_details: DominoWorkspacesApiQueuedWorkspaceHistoryDetails
    tags: list[DominoWorkspacesApiWorkspaceTag]
    comments_count: int
    status: str
    input_commit_id: str
    domino_stats: list[DominoWorkspacesApiDominoStats]
    dependent_repositories: list[DominoWorkspacesApiDependentRepository]
    dependent_dataset_mounts: list[DominoWorkspacesApiDependentDatasetMount]
    dependent_projects: list[DominoWorkspacesApiDependentProject]
    is_restartable: bool
    dependent_external_volume_mounts: list[DominoWorkspacesApiDependentExternalVolumeMount]
    started_by: DominoWorkspacesApiWorkspaceStartedBy | Unset = UNSET
    usage: DominoWorkspacesApiWorkspaceResourceUsage | Unset = UNSET
    output_commit_id: None | str | Unset = UNSET
    auto_sync_settings: DominoWorkspacesApiWorkspaceAutoSync | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        project_id = self.project_id

        title = self.title

        definition_title = self.definition_title

        stage_time = self.stage_time.to_dict()

        number = self.number

        is_completed = self.is_completed

        is_archived = self.is_archived

        queued_workspace_history_details = self.queued_workspace_history_details.to_dict()

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.to_dict()
            tags.append(tags_item)

        comments_count = self.comments_count

        status = self.status

        input_commit_id = self.input_commit_id

        domino_stats = []
        for domino_stats_item_data in self.domino_stats:
            domino_stats_item = domino_stats_item_data.to_dict()
            domino_stats.append(domino_stats_item)

        dependent_repositories = []
        for dependent_repositories_item_data in self.dependent_repositories:
            dependent_repositories_item = dependent_repositories_item_data.to_dict()
            dependent_repositories.append(dependent_repositories_item)

        dependent_dataset_mounts = []
        for dependent_dataset_mounts_item_data in self.dependent_dataset_mounts:
            dependent_dataset_mounts_item = dependent_dataset_mounts_item_data.to_dict()
            dependent_dataset_mounts.append(dependent_dataset_mounts_item)

        dependent_projects = []
        for dependent_projects_item_data in self.dependent_projects:
            dependent_projects_item = dependent_projects_item_data.to_dict()
            dependent_projects.append(dependent_projects_item)

        is_restartable = self.is_restartable

        dependent_external_volume_mounts = []
        for dependent_external_volume_mounts_item_data in self.dependent_external_volume_mounts:
            dependent_external_volume_mounts_item = dependent_external_volume_mounts_item_data.to_dict()
            dependent_external_volume_mounts.append(dependent_external_volume_mounts_item)

        started_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.started_by, Unset):
            started_by = self.started_by.to_dict()

        usage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.usage, Unset):
            usage = self.usage.to_dict()

        output_commit_id: None | str | Unset
        if isinstance(self.output_commit_id, Unset):
            output_commit_id = UNSET
        else:
            output_commit_id = self.output_commit_id

        auto_sync_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auto_sync_settings, Unset):
            auto_sync_settings = self.auto_sync_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "projectId": project_id,
                "title": title,
                "definitionTitle": definition_title,
                "stageTime": stage_time,
                "number": number,
                "isCompleted": is_completed,
                "isArchived": is_archived,
                "queuedWorkspaceHistoryDetails": queued_workspace_history_details,
                "tags": tags,
                "commentsCount": comments_count,
                "status": status,
                "inputCommitId": input_commit_id,
                "dominoStats": domino_stats,
                "dependentRepositories": dependent_repositories,
                "dependentDatasetMounts": dependent_dataset_mounts,
                "dependentProjects": dependent_projects,
                "isRestartable": is_restartable,
                "dependentExternalVolumeMounts": dependent_external_volume_mounts,
            }
        )
        if started_by is not UNSET:
            field_dict["startedBy"] = started_by
        if usage is not UNSET:
            field_dict["usage"] = usage
        if output_commit_id is not UNSET:
            field_dict["outputCommitId"] = output_commit_id
        if auto_sync_settings is not UNSET:
            field_dict["autoSyncSettings"] = auto_sync_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_workspaces_api_dependent_dataset_mount import DominoWorkspacesApiDependentDatasetMount
        from ..models.domino_workspaces_api_dependent_external_volume_mount import (
            DominoWorkspacesApiDependentExternalVolumeMount,
        )
        from ..models.domino_workspaces_api_dependent_project import DominoWorkspacesApiDependentProject
        from ..models.domino_workspaces_api_dependent_repository import DominoWorkspacesApiDependentRepository
        from ..models.domino_workspaces_api_domino_stats import DominoWorkspacesApiDominoStats
        from ..models.domino_workspaces_api_queued_workspace_history_details import (
            DominoWorkspacesApiQueuedWorkspaceHistoryDetails,
        )
        from ..models.domino_workspaces_api_stage_time import DominoWorkspacesApiStageTime
        from ..models.domino_workspaces_api_workspace_auto_sync import DominoWorkspacesApiWorkspaceAutoSync
        from ..models.domino_workspaces_api_workspace_resource_usage import DominoWorkspacesApiWorkspaceResourceUsage
        from ..models.domino_workspaces_api_workspace_started_by import DominoWorkspacesApiWorkspaceStartedBy
        from ..models.domino_workspaces_api_workspace_tag import DominoWorkspacesApiWorkspaceTag

        d = dict(src_dict)
        id = d.pop("id")

        project_id = d.pop("projectId")

        title = d.pop("title")

        definition_title = d.pop("definitionTitle")

        stage_time = DominoWorkspacesApiStageTime.from_dict(d.pop("stageTime"))

        number = d.pop("number")

        is_completed = d.pop("isCompleted")

        is_archived = d.pop("isArchived")

        queued_workspace_history_details = DominoWorkspacesApiQueuedWorkspaceHistoryDetails.from_dict(
            d.pop("queuedWorkspaceHistoryDetails")
        )

        tags = []
        _tags = d.pop("tags")
        for tags_item_data in _tags:
            tags_item = DominoWorkspacesApiWorkspaceTag.from_dict(tags_item_data)

            tags.append(tags_item)

        comments_count = d.pop("commentsCount")

        status = d.pop("status")

        input_commit_id = d.pop("inputCommitId")

        domino_stats = []
        _domino_stats = d.pop("dominoStats")
        for domino_stats_item_data in _domino_stats:
            domino_stats_item = DominoWorkspacesApiDominoStats.from_dict(domino_stats_item_data)

            domino_stats.append(domino_stats_item)

        dependent_repositories = []
        _dependent_repositories = d.pop("dependentRepositories")
        for dependent_repositories_item_data in _dependent_repositories:
            dependent_repositories_item = DominoWorkspacesApiDependentRepository.from_dict(
                dependent_repositories_item_data
            )

            dependent_repositories.append(dependent_repositories_item)

        dependent_dataset_mounts = []
        _dependent_dataset_mounts = d.pop("dependentDatasetMounts")
        for dependent_dataset_mounts_item_data in _dependent_dataset_mounts:
            dependent_dataset_mounts_item = DominoWorkspacesApiDependentDatasetMount.from_dict(
                dependent_dataset_mounts_item_data
            )

            dependent_dataset_mounts.append(dependent_dataset_mounts_item)

        dependent_projects = []
        _dependent_projects = d.pop("dependentProjects")
        for dependent_projects_item_data in _dependent_projects:
            dependent_projects_item = DominoWorkspacesApiDependentProject.from_dict(dependent_projects_item_data)

            dependent_projects.append(dependent_projects_item)

        is_restartable = d.pop("isRestartable")

        dependent_external_volume_mounts = []
        _dependent_external_volume_mounts = d.pop("dependentExternalVolumeMounts")
        for dependent_external_volume_mounts_item_data in _dependent_external_volume_mounts:
            dependent_external_volume_mounts_item = DominoWorkspacesApiDependentExternalVolumeMount.from_dict(
                dependent_external_volume_mounts_item_data
            )

            dependent_external_volume_mounts.append(dependent_external_volume_mounts_item)

        _started_by = d.pop("startedBy", UNSET)
        started_by: DominoWorkspacesApiWorkspaceStartedBy | Unset
        if isinstance(_started_by, Unset):
            started_by = UNSET
        else:
            started_by = DominoWorkspacesApiWorkspaceStartedBy.from_dict(_started_by)

        _usage = d.pop("usage", UNSET)
        usage: DominoWorkspacesApiWorkspaceResourceUsage | Unset
        if isinstance(_usage, Unset):
            usage = UNSET
        else:
            usage = DominoWorkspacesApiWorkspaceResourceUsage.from_dict(_usage)

        def _parse_output_commit_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        output_commit_id = _parse_output_commit_id(d.pop("outputCommitId", UNSET))

        _auto_sync_settings = d.pop("autoSyncSettings", UNSET)
        auto_sync_settings: DominoWorkspacesApiWorkspaceAutoSync | Unset
        if isinstance(_auto_sync_settings, Unset):
            auto_sync_settings = UNSET
        else:
            auto_sync_settings = DominoWorkspacesApiWorkspaceAutoSync.from_dict(_auto_sync_settings)

        domino_workspaces_api_workspace = cls(
            id=id,
            project_id=project_id,
            title=title,
            definition_title=definition_title,
            stage_time=stage_time,
            number=number,
            is_completed=is_completed,
            is_archived=is_archived,
            queued_workspace_history_details=queued_workspace_history_details,
            tags=tags,
            comments_count=comments_count,
            status=status,
            input_commit_id=input_commit_id,
            domino_stats=domino_stats,
            dependent_repositories=dependent_repositories,
            dependent_dataset_mounts=dependent_dataset_mounts,
            dependent_projects=dependent_projects,
            is_restartable=is_restartable,
            dependent_external_volume_mounts=dependent_external_volume_mounts,
            started_by=started_by,
            usage=usage,
            output_commit_id=output_commit_id,
            auto_sync_settings=auto_sync_settings,
        )

        domino_workspaces_api_workspace.additional_properties = d
        return domino_workspaces_api_workspace

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
