from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_dataplane_data_plane_dto import DominoDataplaneDataPlaneDto
    from ..models.domino_jobs_interface_abnormal_status import DominoJobsInterfaceAbnormalStatus
    from ..models.domino_jobs_interface_commit_details import DominoJobsInterfaceCommitDetails
    from ..models.domino_jobs_interface_compute_cluster_config_spec_dto import (
        DominoJobsInterfaceComputeClusterConfigSpecDto,
    )
    from ..models.domino_jobs_interface_dependent_dataset_mount import DominoJobsInterfaceDependentDatasetMount
    from ..models.domino_jobs_interface_dependent_external_volume_mount import (
        DominoJobsInterfaceDependentExternalVolumeMount,
    )
    from ..models.domino_jobs_interface_dependent_net_app_volume_mount import (
        DominoJobsInterfaceDependentNetAppVolumeMount,
    )
    from ..models.domino_jobs_interface_dependent_project import DominoJobsInterfaceDependentProject
    from ..models.domino_jobs_interface_dependent_repository import DominoJobsInterfaceDependentRepository
    from ..models.domino_jobs_interface_domino_stats import DominoJobsInterfaceDominoStats
    from ..models.domino_jobs_interface_job_started_by import DominoJobsInterfaceJobStartedBy
    from ..models.domino_jobs_interface_job_statuses import DominoJobsInterfaceJobStatuses
    from ..models.domino_jobs_interface_job_usage_in_job import DominoJobsInterfaceJobUsageInJob
    from ..models.domino_jobs_interface_queued_job_history_details import DominoJobsInterfaceQueuedJobHistoryDetails
    from ..models.domino_jobs_interface_stage_time import DominoJobsInterfaceStageTime
    from ..models.domino_jobs_interface_tag_application import DominoJobsInterfaceTagApplication
    from ..models.domino_jobs_interface_workflow_details import DominoJobsInterfaceWorkflowDetails
    from ..models.domino_projects_api_repositories_reference_dto import DominoProjectsApiRepositoriesReferenceDTO


T = TypeVar("T", bound="DominoJobsInterfaceJob")


@_attrs_define
class DominoJobsInterfaceJob:
    """
    Attributes:
        number (int):
        id (str):
        stage_time (DominoJobsInterfaceStageTime):
        tags (list[DominoJobsInterfaceTagApplication]):
        job_run_command (str):
        comments_count (int):
        project_id (str):
        commit_details (DominoJobsInterfaceCommitDetails):
        domino_stats (list[DominoJobsInterfaceDominoStats]):
        statuses (DominoJobsInterfaceJobStatuses):
        dependent_repositories (list[DominoJobsInterfaceDependentRepository]):
        dependent_dataset_mounts (list[DominoJobsInterfaceDependentDatasetMount]):
        dependent_projects (list[DominoJobsInterfaceDependentProject]):
        suggest_datasets (bool):
        goal_ids (list[str]):
        dependent_external_volume_mounts (list[DominoJobsInterfaceDependentExternalVolumeMount]):
        dependent_net_app_volume_mounts (list[DominoJobsInterfaceDependentNetAppVolumeMount]):
        snapshot_datasets_on_completion (bool):
        snapshot_net_app_volumes_on_completion (bool):
        queued_job_history_details (DominoJobsInterfaceQueuedJobHistoryDetails | Unset):
        usage (DominoJobsInterfaceJobUsageInJob | Unset):
        started_by (DominoJobsInterfaceJobStartedBy | Unset):
        title (None | str | Unset):
        main_repo_git_ref (DominoProjectsApiRepositoriesReferenceDTO | Unset):
        run_launcher_id (None | str | Unset):
        compute_cluster (DominoJobsInterfaceComputeClusterConfigSpecDto | Unset):
        data_plane (DominoDataplaneDataPlaneDto | Unset):
        workflow_details (DominoJobsInterfaceWorkflowDetails | Unset):
        abnormal_status (DominoJobsInterfaceAbnormalStatus | Unset):
    """

    number: int
    id: str
    stage_time: DominoJobsInterfaceStageTime
    tags: list[DominoJobsInterfaceTagApplication]
    job_run_command: str
    comments_count: int
    project_id: str
    commit_details: DominoJobsInterfaceCommitDetails
    domino_stats: list[DominoJobsInterfaceDominoStats]
    statuses: DominoJobsInterfaceJobStatuses
    dependent_repositories: list[DominoJobsInterfaceDependentRepository]
    dependent_dataset_mounts: list[DominoJobsInterfaceDependentDatasetMount]
    dependent_projects: list[DominoJobsInterfaceDependentProject]
    suggest_datasets: bool
    goal_ids: list[str]
    dependent_external_volume_mounts: list[DominoJobsInterfaceDependentExternalVolumeMount]
    dependent_net_app_volume_mounts: list[DominoJobsInterfaceDependentNetAppVolumeMount]
    snapshot_datasets_on_completion: bool
    snapshot_net_app_volumes_on_completion: bool
    queued_job_history_details: DominoJobsInterfaceQueuedJobHistoryDetails | Unset = UNSET
    usage: DominoJobsInterfaceJobUsageInJob | Unset = UNSET
    started_by: DominoJobsInterfaceJobStartedBy | Unset = UNSET
    title: None | str | Unset = UNSET
    main_repo_git_ref: DominoProjectsApiRepositoriesReferenceDTO | Unset = UNSET
    run_launcher_id: None | str | Unset = UNSET
    compute_cluster: DominoJobsInterfaceComputeClusterConfigSpecDto | Unset = UNSET
    data_plane: DominoDataplaneDataPlaneDto | Unset = UNSET
    workflow_details: DominoJobsInterfaceWorkflowDetails | Unset = UNSET
    abnormal_status: DominoJobsInterfaceAbnormalStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        number = self.number

        id = self.id

        stage_time = self.stage_time.to_dict()

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.to_dict()
            tags.append(tags_item)

        job_run_command = self.job_run_command

        comments_count = self.comments_count

        project_id = self.project_id

        commit_details = self.commit_details.to_dict()

        domino_stats = []
        for domino_stats_item_data in self.domino_stats:
            domino_stats_item = domino_stats_item_data.to_dict()
            domino_stats.append(domino_stats_item)

        statuses = self.statuses.to_dict()

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

        suggest_datasets = self.suggest_datasets

        goal_ids = self.goal_ids

        dependent_external_volume_mounts = []
        for dependent_external_volume_mounts_item_data in self.dependent_external_volume_mounts:
            dependent_external_volume_mounts_item = dependent_external_volume_mounts_item_data.to_dict()
            dependent_external_volume_mounts.append(dependent_external_volume_mounts_item)

        dependent_net_app_volume_mounts = []
        for dependent_net_app_volume_mounts_item_data in self.dependent_net_app_volume_mounts:
            dependent_net_app_volume_mounts_item = dependent_net_app_volume_mounts_item_data.to_dict()
            dependent_net_app_volume_mounts.append(dependent_net_app_volume_mounts_item)

        snapshot_datasets_on_completion = self.snapshot_datasets_on_completion

        snapshot_net_app_volumes_on_completion = self.snapshot_net_app_volumes_on_completion

        queued_job_history_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.queued_job_history_details, Unset):
            queued_job_history_details = self.queued_job_history_details.to_dict()

        usage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.usage, Unset):
            usage = self.usage.to_dict()

        started_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.started_by, Unset):
            started_by = self.started_by.to_dict()

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        main_repo_git_ref: dict[str, Any] | Unset = UNSET
        if not isinstance(self.main_repo_git_ref, Unset):
            main_repo_git_ref = self.main_repo_git_ref.to_dict()

        run_launcher_id: None | str | Unset
        if isinstance(self.run_launcher_id, Unset):
            run_launcher_id = UNSET
        else:
            run_launcher_id = self.run_launcher_id

        compute_cluster: dict[str, Any] | Unset = UNSET
        if not isinstance(self.compute_cluster, Unset):
            compute_cluster = self.compute_cluster.to_dict()

        data_plane: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_plane, Unset):
            data_plane = self.data_plane.to_dict()

        workflow_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workflow_details, Unset):
            workflow_details = self.workflow_details.to_dict()

        abnormal_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.abnormal_status, Unset):
            abnormal_status = self.abnormal_status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "number": number,
                "id": id,
                "stageTime": stage_time,
                "tags": tags,
                "jobRunCommand": job_run_command,
                "commentsCount": comments_count,
                "projectId": project_id,
                "commitDetails": commit_details,
                "dominoStats": domino_stats,
                "statuses": statuses,
                "dependentRepositories": dependent_repositories,
                "dependentDatasetMounts": dependent_dataset_mounts,
                "dependentProjects": dependent_projects,
                "suggestDatasets": suggest_datasets,
                "goalIds": goal_ids,
                "dependentExternalVolumeMounts": dependent_external_volume_mounts,
                "dependentNetAppVolumeMounts": dependent_net_app_volume_mounts,
                "snapshotDatasetsOnCompletion": snapshot_datasets_on_completion,
                "snapshotNetAppVolumesOnCompletion": snapshot_net_app_volumes_on_completion,
            }
        )
        if queued_job_history_details is not UNSET:
            field_dict["queuedJobHistoryDetails"] = queued_job_history_details
        if usage is not UNSET:
            field_dict["usage"] = usage
        if started_by is not UNSET:
            field_dict["startedBy"] = started_by
        if title is not UNSET:
            field_dict["title"] = title
        if main_repo_git_ref is not UNSET:
            field_dict["mainRepoGitRef"] = main_repo_git_ref
        if run_launcher_id is not UNSET:
            field_dict["runLauncherId"] = run_launcher_id
        if compute_cluster is not UNSET:
            field_dict["computeCluster"] = compute_cluster
        if data_plane is not UNSET:
            field_dict["dataPlane"] = data_plane
        if workflow_details is not UNSET:
            field_dict["workflowDetails"] = workflow_details
        if abnormal_status is not UNSET:
            field_dict["abnormalStatus"] = abnormal_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_dataplane_data_plane_dto import DominoDataplaneDataPlaneDto
        from ..models.domino_jobs_interface_abnormal_status import DominoJobsInterfaceAbnormalStatus
        from ..models.domino_jobs_interface_commit_details import DominoJobsInterfaceCommitDetails
        from ..models.domino_jobs_interface_compute_cluster_config_spec_dto import (
            DominoJobsInterfaceComputeClusterConfigSpecDto,
        )
        from ..models.domino_jobs_interface_dependent_dataset_mount import DominoJobsInterfaceDependentDatasetMount
        from ..models.domino_jobs_interface_dependent_external_volume_mount import (
            DominoJobsInterfaceDependentExternalVolumeMount,
        )
        from ..models.domino_jobs_interface_dependent_net_app_volume_mount import (
            DominoJobsInterfaceDependentNetAppVolumeMount,
        )
        from ..models.domino_jobs_interface_dependent_project import DominoJobsInterfaceDependentProject
        from ..models.domino_jobs_interface_dependent_repository import DominoJobsInterfaceDependentRepository
        from ..models.domino_jobs_interface_domino_stats import DominoJobsInterfaceDominoStats
        from ..models.domino_jobs_interface_job_started_by import DominoJobsInterfaceJobStartedBy
        from ..models.domino_jobs_interface_job_statuses import DominoJobsInterfaceJobStatuses
        from ..models.domino_jobs_interface_job_usage_in_job import DominoJobsInterfaceJobUsageInJob
        from ..models.domino_jobs_interface_queued_job_history_details import DominoJobsInterfaceQueuedJobHistoryDetails
        from ..models.domino_jobs_interface_stage_time import DominoJobsInterfaceStageTime
        from ..models.domino_jobs_interface_tag_application import DominoJobsInterfaceTagApplication
        from ..models.domino_jobs_interface_workflow_details import DominoJobsInterfaceWorkflowDetails
        from ..models.domino_projects_api_repositories_reference_dto import DominoProjectsApiRepositoriesReferenceDTO

        d = dict(src_dict)
        number = d.pop("number")

        id = d.pop("id")

        stage_time = DominoJobsInterfaceStageTime.from_dict(d.pop("stageTime"))

        tags = []
        _tags = d.pop("tags")
        for tags_item_data in _tags:
            tags_item = DominoJobsInterfaceTagApplication.from_dict(tags_item_data)

            tags.append(tags_item)

        job_run_command = d.pop("jobRunCommand")

        comments_count = d.pop("commentsCount")

        project_id = d.pop("projectId")

        commit_details = DominoJobsInterfaceCommitDetails.from_dict(d.pop("commitDetails"))

        domino_stats = []
        _domino_stats = d.pop("dominoStats")
        for domino_stats_item_data in _domino_stats:
            domino_stats_item = DominoJobsInterfaceDominoStats.from_dict(domino_stats_item_data)

            domino_stats.append(domino_stats_item)

        statuses = DominoJobsInterfaceJobStatuses.from_dict(d.pop("statuses"))

        dependent_repositories = []
        _dependent_repositories = d.pop("dependentRepositories")
        for dependent_repositories_item_data in _dependent_repositories:
            dependent_repositories_item = DominoJobsInterfaceDependentRepository.from_dict(
                dependent_repositories_item_data
            )

            dependent_repositories.append(dependent_repositories_item)

        dependent_dataset_mounts = []
        _dependent_dataset_mounts = d.pop("dependentDatasetMounts")
        for dependent_dataset_mounts_item_data in _dependent_dataset_mounts:
            dependent_dataset_mounts_item = DominoJobsInterfaceDependentDatasetMount.from_dict(
                dependent_dataset_mounts_item_data
            )

            dependent_dataset_mounts.append(dependent_dataset_mounts_item)

        dependent_projects = []
        _dependent_projects = d.pop("dependentProjects")
        for dependent_projects_item_data in _dependent_projects:
            dependent_projects_item = DominoJobsInterfaceDependentProject.from_dict(dependent_projects_item_data)

            dependent_projects.append(dependent_projects_item)

        suggest_datasets = d.pop("suggestDatasets")

        goal_ids = cast(list[str], d.pop("goalIds"))

        dependent_external_volume_mounts = []
        _dependent_external_volume_mounts = d.pop("dependentExternalVolumeMounts")
        for dependent_external_volume_mounts_item_data in _dependent_external_volume_mounts:
            dependent_external_volume_mounts_item = DominoJobsInterfaceDependentExternalVolumeMount.from_dict(
                dependent_external_volume_mounts_item_data
            )

            dependent_external_volume_mounts.append(dependent_external_volume_mounts_item)

        dependent_net_app_volume_mounts = []
        _dependent_net_app_volume_mounts = d.pop("dependentNetAppVolumeMounts")
        for dependent_net_app_volume_mounts_item_data in _dependent_net_app_volume_mounts:
            dependent_net_app_volume_mounts_item = DominoJobsInterfaceDependentNetAppVolumeMount.from_dict(
                dependent_net_app_volume_mounts_item_data
            )

            dependent_net_app_volume_mounts.append(dependent_net_app_volume_mounts_item)

        snapshot_datasets_on_completion = d.pop("snapshotDatasetsOnCompletion")

        snapshot_net_app_volumes_on_completion = d.pop("snapshotNetAppVolumesOnCompletion")

        _queued_job_history_details = d.pop("queuedJobHistoryDetails", UNSET)
        queued_job_history_details: DominoJobsInterfaceQueuedJobHistoryDetails | Unset
        if isinstance(_queued_job_history_details, Unset):
            queued_job_history_details = UNSET
        else:
            queued_job_history_details = DominoJobsInterfaceQueuedJobHistoryDetails.from_dict(
                _queued_job_history_details
            )

        _usage = d.pop("usage", UNSET)
        usage: DominoJobsInterfaceJobUsageInJob | Unset
        if isinstance(_usage, Unset):
            usage = UNSET
        else:
            usage = DominoJobsInterfaceJobUsageInJob.from_dict(_usage)

        _started_by = d.pop("startedBy", UNSET)
        started_by: DominoJobsInterfaceJobStartedBy | Unset
        if isinstance(_started_by, Unset):
            started_by = UNSET
        else:
            started_by = DominoJobsInterfaceJobStartedBy.from_dict(_started_by)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        _main_repo_git_ref = d.pop("mainRepoGitRef", UNSET)
        main_repo_git_ref: DominoProjectsApiRepositoriesReferenceDTO | Unset
        if isinstance(_main_repo_git_ref, Unset):
            main_repo_git_ref = UNSET
        else:
            main_repo_git_ref = DominoProjectsApiRepositoriesReferenceDTO.from_dict(_main_repo_git_ref)

        def _parse_run_launcher_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        run_launcher_id = _parse_run_launcher_id(d.pop("runLauncherId", UNSET))

        _compute_cluster = d.pop("computeCluster", UNSET)
        compute_cluster: DominoJobsInterfaceComputeClusterConfigSpecDto | Unset
        if isinstance(_compute_cluster, Unset):
            compute_cluster = UNSET
        else:
            compute_cluster = DominoJobsInterfaceComputeClusterConfigSpecDto.from_dict(_compute_cluster)

        _data_plane = d.pop("dataPlane", UNSET)
        data_plane: DominoDataplaneDataPlaneDto | Unset
        if isinstance(_data_plane, Unset):
            data_plane = UNSET
        else:
            data_plane = DominoDataplaneDataPlaneDto.from_dict(_data_plane)

        _workflow_details = d.pop("workflowDetails", UNSET)
        workflow_details: DominoJobsInterfaceWorkflowDetails | Unset
        if isinstance(_workflow_details, Unset):
            workflow_details = UNSET
        else:
            workflow_details = DominoJobsInterfaceWorkflowDetails.from_dict(_workflow_details)

        _abnormal_status = d.pop("abnormalStatus", UNSET)
        abnormal_status: DominoJobsInterfaceAbnormalStatus | Unset
        if isinstance(_abnormal_status, Unset):
            abnormal_status = UNSET
        else:
            abnormal_status = DominoJobsInterfaceAbnormalStatus.from_dict(_abnormal_status)

        domino_jobs_interface_job = cls(
            number=number,
            id=id,
            stage_time=stage_time,
            tags=tags,
            job_run_command=job_run_command,
            comments_count=comments_count,
            project_id=project_id,
            commit_details=commit_details,
            domino_stats=domino_stats,
            statuses=statuses,
            dependent_repositories=dependent_repositories,
            dependent_dataset_mounts=dependent_dataset_mounts,
            dependent_projects=dependent_projects,
            suggest_datasets=suggest_datasets,
            goal_ids=goal_ids,
            dependent_external_volume_mounts=dependent_external_volume_mounts,
            dependent_net_app_volume_mounts=dependent_net_app_volume_mounts,
            snapshot_datasets_on_completion=snapshot_datasets_on_completion,
            snapshot_net_app_volumes_on_completion=snapshot_net_app_volumes_on_completion,
            queued_job_history_details=queued_job_history_details,
            usage=usage,
            started_by=started_by,
            title=title,
            main_repo_git_ref=main_repo_git_ref,
            run_launcher_id=run_launcher_id,
            compute_cluster=compute_cluster,
            data_plane=data_plane,
            workflow_details=workflow_details,
            abnormal_status=abnormal_status,
        )

        domino_jobs_interface_job.additional_properties = d
        return domino_jobs_interface_job

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
