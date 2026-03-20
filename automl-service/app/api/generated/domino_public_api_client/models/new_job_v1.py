from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compute_cluster_config_v1 import ComputeClusterConfigV1
    from ..models.git_ref_v1 import GitRefV1


T = TypeVar("T", bound="NewJobV1")


@_attrs_define
class NewJobV1:
    """
    Attributes:
        project_id (str): Id of project to create job in. Example: 623130ad7a0af0281c01a698.
        run_command (str): Command for job to run Example: main.py.
        capacity_type (str | Unset): Optional capacity type within the hardware tier. Example: on-demand.
        commit_id (str | Unset): Git commitId to start job from. Defaults to head commitId for the project. Example:
            960a4c99a4cc38194cbacbcce41caa68ba5369ea.
        compute_cluster (ComputeClusterConfigV1 | Unset):
        environment_id (str | Unset): Id of environment to use when creating job. Defaults to project default
            environment. Example: 623131507a0af0281c01a699.
        environment_revision_spec (str | Unset): Specification describing which environment revision to use. Defaults to
            "ActiveRevision" Example: ActiveRevision | LatestRevision | SomeRevision(623131577a0af0281c01a69a).
        external_volume_mount_ids (list[str] | Unset): Ids of external volumes to be mounted on this job. Example:
            ['6231327c7a0af0281c01a69b', '623132867a0af0281c01a69c'].
        hardware_tier (str | Unset): Hardware tier to use for this job. Defaults to project default hardware tier.
            Example: small-k8s.
        main_repo_git_ref (GitRefV1 | Unset):
        net_app_volume_ids (list[str] | Unset): Ids of NetApp volumes to be mounted on this job. Example:
            ['31c4a22a-5571-4e9b-b7ac-921d241acd00', '31c4a22a-5571-4e9b-b7ac-921d241acd01'].
        snapshot_datasets_on_completion (bool | Unset): Whether to snapshot datasets mounted on the Job when the Job
            completes.
        snapshot_net_app_volumes_on_completion (bool | Unset): Whether to snapshot NetApp volumes mounted on the Job
            when the Job completes.
        title (str | Unset): Name of job to start Example: K-means clustering.
    """

    project_id: str
    run_command: str
    capacity_type: str | Unset = UNSET
    commit_id: str | Unset = UNSET
    compute_cluster: ComputeClusterConfigV1 | Unset = UNSET
    environment_id: str | Unset = UNSET
    environment_revision_spec: str | Unset = UNSET
    external_volume_mount_ids: list[str] | Unset = UNSET
    hardware_tier: str | Unset = UNSET
    main_repo_git_ref: GitRefV1 | Unset = UNSET
    net_app_volume_ids: list[str] | Unset = UNSET
    snapshot_datasets_on_completion: bool | Unset = UNSET
    snapshot_net_app_volumes_on_completion: bool | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        run_command = self.run_command

        capacity_type = self.capacity_type

        commit_id = self.commit_id

        compute_cluster: dict[str, Any] | Unset = UNSET
        if not isinstance(self.compute_cluster, Unset):
            compute_cluster = self.compute_cluster.to_dict()

        environment_id = self.environment_id

        environment_revision_spec = self.environment_revision_spec

        external_volume_mount_ids: list[str] | Unset = UNSET
        if not isinstance(self.external_volume_mount_ids, Unset):
            external_volume_mount_ids = self.external_volume_mount_ids

        hardware_tier = self.hardware_tier

        main_repo_git_ref: dict[str, Any] | Unset = UNSET
        if not isinstance(self.main_repo_git_ref, Unset):
            main_repo_git_ref = self.main_repo_git_ref.to_dict()

        net_app_volume_ids: list[str] | Unset = UNSET
        if not isinstance(self.net_app_volume_ids, Unset):
            net_app_volume_ids = self.net_app_volume_ids

        snapshot_datasets_on_completion = self.snapshot_datasets_on_completion

        snapshot_net_app_volumes_on_completion = self.snapshot_net_app_volumes_on_completion

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectId": project_id,
                "runCommand": run_command,
            }
        )
        if capacity_type is not UNSET:
            field_dict["capacityType"] = capacity_type
        if commit_id is not UNSET:
            field_dict["commitId"] = commit_id
        if compute_cluster is not UNSET:
            field_dict["computeCluster"] = compute_cluster
        if environment_id is not UNSET:
            field_dict["environmentId"] = environment_id
        if environment_revision_spec is not UNSET:
            field_dict["environmentRevisionSpec"] = environment_revision_spec
        if external_volume_mount_ids is not UNSET:
            field_dict["externalVolumeMountIds"] = external_volume_mount_ids
        if hardware_tier is not UNSET:
            field_dict["hardwareTier"] = hardware_tier
        if main_repo_git_ref is not UNSET:
            field_dict["mainRepoGitRef"] = main_repo_git_ref
        if net_app_volume_ids is not UNSET:
            field_dict["netAppVolumeIds"] = net_app_volume_ids
        if snapshot_datasets_on_completion is not UNSET:
            field_dict["snapshotDatasetsOnCompletion"] = snapshot_datasets_on_completion
        if snapshot_net_app_volumes_on_completion is not UNSET:
            field_dict["snapshotNetAppVolumesOnCompletion"] = snapshot_net_app_volumes_on_completion
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compute_cluster_config_v1 import ComputeClusterConfigV1
        from ..models.git_ref_v1 import GitRefV1

        d = dict(src_dict)
        project_id = d.pop("projectId")

        run_command = d.pop("runCommand")

        capacity_type = d.pop("capacityType", UNSET)

        commit_id = d.pop("commitId", UNSET)

        _compute_cluster = d.pop("computeCluster", UNSET)
        compute_cluster: ComputeClusterConfigV1 | Unset
        if isinstance(_compute_cluster, Unset):
            compute_cluster = UNSET
        else:
            compute_cluster = ComputeClusterConfigV1.from_dict(_compute_cluster)

        environment_id = d.pop("environmentId", UNSET)

        environment_revision_spec = d.pop("environmentRevisionSpec", UNSET)

        external_volume_mount_ids = cast(list[str], d.pop("externalVolumeMountIds", UNSET))

        hardware_tier = d.pop("hardwareTier", UNSET)

        _main_repo_git_ref = d.pop("mainRepoGitRef", UNSET)
        main_repo_git_ref: GitRefV1 | Unset
        if isinstance(_main_repo_git_ref, Unset):
            main_repo_git_ref = UNSET
        else:
            main_repo_git_ref = GitRefV1.from_dict(_main_repo_git_ref)

        net_app_volume_ids = cast(list[str], d.pop("netAppVolumeIds", UNSET))

        snapshot_datasets_on_completion = d.pop("snapshotDatasetsOnCompletion", UNSET)

        snapshot_net_app_volumes_on_completion = d.pop("snapshotNetAppVolumesOnCompletion", UNSET)

        title = d.pop("title", UNSET)

        new_job_v1 = cls(
            project_id=project_id,
            run_command=run_command,
            capacity_type=capacity_type,
            commit_id=commit_id,
            compute_cluster=compute_cluster,
            environment_id=environment_id,
            environment_revision_spec=environment_revision_spec,
            external_volume_mount_ids=external_volume_mount_ids,
            hardware_tier=hardware_tier,
            main_repo_git_ref=main_repo_git_ref,
            net_app_volume_ids=net_app_volume_ids,
            snapshot_datasets_on_completion=snapshot_datasets_on_completion,
            snapshot_net_app_volumes_on_completion=snapshot_net_app_volumes_on_completion,
            title=title,
        )

        new_job_v1.additional_properties = d
        return new_job_v1

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
