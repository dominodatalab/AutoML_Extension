from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.commit_details_v1 import CommitDetailsV1
    from ..models.compute_cluster_config_v1 import ComputeClusterConfigV1
    from ..models.dataset_mount_v1 import DatasetMountV1
    from ..models.domino_stats_v1 import DominoStatsV1
    from ..models.external_volume_mount_v1 import ExternalVolumeMountV1
    from ..models.git_ref_v1 import GitRefV1
    from ..models.job_status_v1 import JobStatusV1
    from ..models.job_usage_v1 import JobUsageV1
    from ..models.mounted_git_repo_v1 import MountedGitRepoV1
    from ..models.mounted_project_v1 import MountedProjectV1
    from ..models.net_app_volume_mount_v1 import NetAppVolumeMountV1
    from ..models.stage_times_v1 import StageTimesV1


T = TypeVar("T", bound="JobV1")


@_attrs_define
class JobV1:
    """
    Attributes:
        commit_details (CommitDetailsV1):
        dataset_mounts (list[DatasetMountV1]):
        domino_stats (list[DominoStatsV1]):
        external_volume_mounts (list[ExternalVolumeMountV1]):
        git_repos (list[MountedGitRepoV1]):
        id (str):
        net_app_volume_mounts (list[NetAppVolumeMountV1]):
        number (int):
        projects (list[MountedProjectV1]):
        run_command (str):
        stage_times (StageTimesV1):
        status (JobStatusV1):
        compute_cluster (ComputeClusterConfigV1 | Unset):
        main_repo_git_ref (GitRefV1 | Unset):
        run_launcher_id (str | Unset):
        started_by_id (str | Unset):
        title (str | Unset):
        usage (JobUsageV1 | Unset):
    """

    commit_details: CommitDetailsV1
    dataset_mounts: list[DatasetMountV1]
    domino_stats: list[DominoStatsV1]
    external_volume_mounts: list[ExternalVolumeMountV1]
    git_repos: list[MountedGitRepoV1]
    id: str
    net_app_volume_mounts: list[NetAppVolumeMountV1]
    number: int
    projects: list[MountedProjectV1]
    run_command: str
    stage_times: StageTimesV1
    status: JobStatusV1
    compute_cluster: ComputeClusterConfigV1 | Unset = UNSET
    main_repo_git_ref: GitRefV1 | Unset = UNSET
    run_launcher_id: str | Unset = UNSET
    started_by_id: str | Unset = UNSET
    title: str | Unset = UNSET
    usage: JobUsageV1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        commit_details = self.commit_details.to_dict()

        dataset_mounts = []
        for dataset_mounts_item_data in self.dataset_mounts:
            dataset_mounts_item = dataset_mounts_item_data.to_dict()
            dataset_mounts.append(dataset_mounts_item)

        domino_stats = []
        for domino_stats_item_data in self.domino_stats:
            domino_stats_item = domino_stats_item_data.to_dict()
            domino_stats.append(domino_stats_item)

        external_volume_mounts = []
        for external_volume_mounts_item_data in self.external_volume_mounts:
            external_volume_mounts_item = external_volume_mounts_item_data.to_dict()
            external_volume_mounts.append(external_volume_mounts_item)

        git_repos = []
        for git_repos_item_data in self.git_repos:
            git_repos_item = git_repos_item_data.to_dict()
            git_repos.append(git_repos_item)

        id = self.id

        net_app_volume_mounts = []
        for net_app_volume_mounts_item_data in self.net_app_volume_mounts:
            net_app_volume_mounts_item = net_app_volume_mounts_item_data.to_dict()
            net_app_volume_mounts.append(net_app_volume_mounts_item)

        number = self.number

        projects = []
        for projects_item_data in self.projects:
            projects_item = projects_item_data.to_dict()
            projects.append(projects_item)

        run_command = self.run_command

        stage_times = self.stage_times.to_dict()

        status = self.status.to_dict()

        compute_cluster: dict[str, Any] | Unset = UNSET
        if not isinstance(self.compute_cluster, Unset):
            compute_cluster = self.compute_cluster.to_dict()

        main_repo_git_ref: dict[str, Any] | Unset = UNSET
        if not isinstance(self.main_repo_git_ref, Unset):
            main_repo_git_ref = self.main_repo_git_ref.to_dict()

        run_launcher_id = self.run_launcher_id

        started_by_id = self.started_by_id

        title = self.title

        usage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.usage, Unset):
            usage = self.usage.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commitDetails": commit_details,
                "datasetMounts": dataset_mounts,
                "dominoStats": domino_stats,
                "externalVolumeMounts": external_volume_mounts,
                "gitRepos": git_repos,
                "id": id,
                "netAppVolumeMounts": net_app_volume_mounts,
                "number": number,
                "projects": projects,
                "runCommand": run_command,
                "stageTimes": stage_times,
                "status": status,
            }
        )
        if compute_cluster is not UNSET:
            field_dict["computeCluster"] = compute_cluster
        if main_repo_git_ref is not UNSET:
            field_dict["mainRepoGitRef"] = main_repo_git_ref
        if run_launcher_id is not UNSET:
            field_dict["runLauncherId"] = run_launcher_id
        if started_by_id is not UNSET:
            field_dict["startedById"] = started_by_id
        if title is not UNSET:
            field_dict["title"] = title
        if usage is not UNSET:
            field_dict["usage"] = usage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.commit_details_v1 import CommitDetailsV1
        from ..models.compute_cluster_config_v1 import ComputeClusterConfigV1
        from ..models.dataset_mount_v1 import DatasetMountV1
        from ..models.domino_stats_v1 import DominoStatsV1
        from ..models.external_volume_mount_v1 import ExternalVolumeMountV1
        from ..models.git_ref_v1 import GitRefV1
        from ..models.job_status_v1 import JobStatusV1
        from ..models.job_usage_v1 import JobUsageV1
        from ..models.mounted_git_repo_v1 import MountedGitRepoV1
        from ..models.mounted_project_v1 import MountedProjectV1
        from ..models.net_app_volume_mount_v1 import NetAppVolumeMountV1
        from ..models.stage_times_v1 import StageTimesV1

        d = dict(src_dict)
        commit_details = CommitDetailsV1.from_dict(d.pop("commitDetails"))

        dataset_mounts = []
        _dataset_mounts = d.pop("datasetMounts")
        for dataset_mounts_item_data in _dataset_mounts:
            dataset_mounts_item = DatasetMountV1.from_dict(dataset_mounts_item_data)

            dataset_mounts.append(dataset_mounts_item)

        domino_stats = []
        _domino_stats = d.pop("dominoStats")
        for domino_stats_item_data in _domino_stats:
            domino_stats_item = DominoStatsV1.from_dict(domino_stats_item_data)

            domino_stats.append(domino_stats_item)

        external_volume_mounts = []
        _external_volume_mounts = d.pop("externalVolumeMounts")
        for external_volume_mounts_item_data in _external_volume_mounts:
            external_volume_mounts_item = ExternalVolumeMountV1.from_dict(external_volume_mounts_item_data)

            external_volume_mounts.append(external_volume_mounts_item)

        git_repos = []
        _git_repos = d.pop("gitRepos")
        for git_repos_item_data in _git_repos:
            git_repos_item = MountedGitRepoV1.from_dict(git_repos_item_data)

            git_repos.append(git_repos_item)

        id = d.pop("id")

        net_app_volume_mounts = []
        _net_app_volume_mounts = d.pop("netAppVolumeMounts")
        for net_app_volume_mounts_item_data in _net_app_volume_mounts:
            net_app_volume_mounts_item = NetAppVolumeMountV1.from_dict(net_app_volume_mounts_item_data)

            net_app_volume_mounts.append(net_app_volume_mounts_item)

        number = d.pop("number")

        projects = []
        _projects = d.pop("projects")
        for projects_item_data in _projects:
            projects_item = MountedProjectV1.from_dict(projects_item_data)

            projects.append(projects_item)

        run_command = d.pop("runCommand")

        stage_times = StageTimesV1.from_dict(d.pop("stageTimes"))

        status = JobStatusV1.from_dict(d.pop("status"))

        _compute_cluster = d.pop("computeCluster", UNSET)
        compute_cluster: ComputeClusterConfigV1 | Unset
        if isinstance(_compute_cluster, Unset):
            compute_cluster = UNSET
        else:
            compute_cluster = ComputeClusterConfigV1.from_dict(_compute_cluster)

        _main_repo_git_ref = d.pop("mainRepoGitRef", UNSET)
        main_repo_git_ref: GitRefV1 | Unset
        if isinstance(_main_repo_git_ref, Unset):
            main_repo_git_ref = UNSET
        else:
            main_repo_git_ref = GitRefV1.from_dict(_main_repo_git_ref)

        run_launcher_id = d.pop("runLauncherId", UNSET)

        started_by_id = d.pop("startedById", UNSET)

        title = d.pop("title", UNSET)

        _usage = d.pop("usage", UNSET)
        usage: JobUsageV1 | Unset
        if isinstance(_usage, Unset):
            usage = UNSET
        else:
            usage = JobUsageV1.from_dict(_usage)

        job_v1 = cls(
            commit_details=commit_details,
            dataset_mounts=dataset_mounts,
            domino_stats=domino_stats,
            external_volume_mounts=external_volume_mounts,
            git_repos=git_repos,
            id=id,
            net_app_volume_mounts=net_app_volume_mounts,
            number=number,
            projects=projects,
            run_command=run_command,
            stage_times=stage_times,
            status=status,
            compute_cluster=compute_cluster,
            main_repo_git_ref=main_repo_git_ref,
            run_launcher_id=run_launcher_id,
            started_by_id=started_by_id,
            title=title,
            usage=usage,
        )

        job_v1.additional_properties = d
        return job_v1

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
