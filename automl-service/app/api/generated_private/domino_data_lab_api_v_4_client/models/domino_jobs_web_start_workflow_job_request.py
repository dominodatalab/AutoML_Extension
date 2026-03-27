from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_jobs_web_start_workflow_job_request_capacity_type import (
    DominoJobsWebStartWorkflowJobRequestCapacityType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_datasetrw_api_dataset_snapshot_ref_dto import DominoDatasetrwApiDatasetSnapshotRefDto
    from ..models.domino_hardwaretier_api_hardware_tier_identifier import DominoHardwaretierApiHardwareTierIdentifier
    from ..models.domino_jobs_interface_compute_cluster_config_spec_with_specific_revision_dto import (
        DominoJobsInterfaceComputeClusterConfigSpecWithSpecificRevisionDto,
    )
    from ..models.domino_jobs_interface_net_app_volume_snapshot_ref_dto import (
        DominoJobsInterfaceNetAppVolumeSnapshotRefDto,
    )
    from ..models.domino_jobs_interface_workflow_config import DominoJobsInterfaceWorkflowConfig
    from ..models.domino_projects_api_repositories_reference_dto import DominoProjectsApiRepositoriesReferenceDTO


T = TypeVar("T", bound="DominoJobsWebStartWorkflowJobRequest")


@_attrs_define
class DominoJobsWebStartWorkflowJobRequest:
    """
    Attributes:
        project_id (str):
        command_to_run (str):
        commit_id (str):
        hardware_tier_id (DominoHardwaretierApiHardwareTierIdentifier):
        dataset_snapshots (list[DominoDatasetrwApiDatasetSnapshotRefDto]):
        environment_id (str):
        environment_revision_spec (Any):
        external_volume_mount_ids (list[str]):
        volume_size_gi_b (float):
        workflow_config (DominoJobsInterfaceWorkflowConfig):
        title (None | str | Unset):
        main_repo_git_ref (DominoProjectsApiRepositoriesReferenceDTO | Unset):
        capacity_type (DominoJobsWebStartWorkflowJobRequestCapacityType | Unset):
        compute_cluster_properties (DominoJobsInterfaceComputeClusterConfigSpecWithSpecificRevisionDto | Unset):
        net_app_volume_snapshots (list[DominoJobsInterfaceNetAppVolumeSnapshotRefDto] | None | Unset):
    """

    project_id: str
    command_to_run: str
    commit_id: str
    hardware_tier_id: DominoHardwaretierApiHardwareTierIdentifier
    dataset_snapshots: list[DominoDatasetrwApiDatasetSnapshotRefDto]
    environment_id: str
    environment_revision_spec: Any
    external_volume_mount_ids: list[str]
    volume_size_gi_b: float
    workflow_config: DominoJobsInterfaceWorkflowConfig
    title: None | str | Unset = UNSET
    main_repo_git_ref: DominoProjectsApiRepositoriesReferenceDTO | Unset = UNSET
    capacity_type: DominoJobsWebStartWorkflowJobRequestCapacityType | Unset = UNSET
    compute_cluster_properties: DominoJobsInterfaceComputeClusterConfigSpecWithSpecificRevisionDto | Unset = UNSET
    net_app_volume_snapshots: list[DominoJobsInterfaceNetAppVolumeSnapshotRefDto] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        command_to_run = self.command_to_run

        commit_id = self.commit_id

        hardware_tier_id = self.hardware_tier_id.to_dict()

        dataset_snapshots = []
        for dataset_snapshots_item_data in self.dataset_snapshots:
            dataset_snapshots_item = dataset_snapshots_item_data.to_dict()
            dataset_snapshots.append(dataset_snapshots_item)

        environment_id = self.environment_id

        environment_revision_spec = self.environment_revision_spec

        external_volume_mount_ids = self.external_volume_mount_ids

        volume_size_gi_b = self.volume_size_gi_b

        workflow_config = self.workflow_config.to_dict()

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        main_repo_git_ref: dict[str, Any] | Unset = UNSET
        if not isinstance(self.main_repo_git_ref, Unset):
            main_repo_git_ref = self.main_repo_git_ref.to_dict()

        capacity_type: str | Unset = UNSET
        if not isinstance(self.capacity_type, Unset):
            capacity_type = self.capacity_type.value

        compute_cluster_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.compute_cluster_properties, Unset):
            compute_cluster_properties = self.compute_cluster_properties.to_dict()

        net_app_volume_snapshots: list[dict[str, Any]] | None | Unset
        if isinstance(self.net_app_volume_snapshots, Unset):
            net_app_volume_snapshots = UNSET
        elif isinstance(self.net_app_volume_snapshots, list):
            net_app_volume_snapshots = []
            for net_app_volume_snapshots_type_0_item_data in self.net_app_volume_snapshots:
                net_app_volume_snapshots_type_0_item = net_app_volume_snapshots_type_0_item_data.to_dict()
                net_app_volume_snapshots.append(net_app_volume_snapshots_type_0_item)

        else:
            net_app_volume_snapshots = self.net_app_volume_snapshots

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectId": project_id,
                "commandToRun": command_to_run,
                "commitId": commit_id,
                "hardwareTierId": hardware_tier_id,
                "datasetSnapshots": dataset_snapshots,
                "environmentId": environment_id,
                "environmentRevisionSpec": environment_revision_spec,
                "externalVolumeMountIds": external_volume_mount_ids,
                "volumeSizeGiB": volume_size_gi_b,
                "workflowConfig": workflow_config,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if main_repo_git_ref is not UNSET:
            field_dict["mainRepoGitRef"] = main_repo_git_ref
        if capacity_type is not UNSET:
            field_dict["capacityType"] = capacity_type
        if compute_cluster_properties is not UNSET:
            field_dict["computeClusterProperties"] = compute_cluster_properties
        if net_app_volume_snapshots is not UNSET:
            field_dict["netAppVolumeSnapshots"] = net_app_volume_snapshots

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_datasetrw_api_dataset_snapshot_ref_dto import DominoDatasetrwApiDatasetSnapshotRefDto
        from ..models.domino_hardwaretier_api_hardware_tier_identifier import (
            DominoHardwaretierApiHardwareTierIdentifier,
        )
        from ..models.domino_jobs_interface_compute_cluster_config_spec_with_specific_revision_dto import (
            DominoJobsInterfaceComputeClusterConfigSpecWithSpecificRevisionDto,
        )
        from ..models.domino_jobs_interface_net_app_volume_snapshot_ref_dto import (
            DominoJobsInterfaceNetAppVolumeSnapshotRefDto,
        )
        from ..models.domino_jobs_interface_workflow_config import DominoJobsInterfaceWorkflowConfig
        from ..models.domino_projects_api_repositories_reference_dto import DominoProjectsApiRepositoriesReferenceDTO

        d = dict(src_dict)
        project_id = d.pop("projectId")

        command_to_run = d.pop("commandToRun")

        commit_id = d.pop("commitId")

        hardware_tier_id = DominoHardwaretierApiHardwareTierIdentifier.from_dict(d.pop("hardwareTierId"))

        dataset_snapshots = []
        _dataset_snapshots = d.pop("datasetSnapshots")
        for dataset_snapshots_item_data in _dataset_snapshots:
            dataset_snapshots_item = DominoDatasetrwApiDatasetSnapshotRefDto.from_dict(dataset_snapshots_item_data)

            dataset_snapshots.append(dataset_snapshots_item)

        environment_id = d.pop("environmentId")

        environment_revision_spec = d.pop("environmentRevisionSpec")

        external_volume_mount_ids = cast(list[str], d.pop("externalVolumeMountIds"))

        volume_size_gi_b = d.pop("volumeSizeGiB")

        workflow_config = DominoJobsInterfaceWorkflowConfig.from_dict(d.pop("workflowConfig"))

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

        _capacity_type = d.pop("capacityType", UNSET)
        capacity_type: DominoJobsWebStartWorkflowJobRequestCapacityType | Unset
        if isinstance(_capacity_type, Unset):
            capacity_type = UNSET
        else:
            capacity_type = DominoJobsWebStartWorkflowJobRequestCapacityType(_capacity_type)

        _compute_cluster_properties = d.pop("computeClusterProperties", UNSET)
        compute_cluster_properties: DominoJobsInterfaceComputeClusterConfigSpecWithSpecificRevisionDto | Unset
        if isinstance(_compute_cluster_properties, Unset):
            compute_cluster_properties = UNSET
        else:
            compute_cluster_properties = DominoJobsInterfaceComputeClusterConfigSpecWithSpecificRevisionDto.from_dict(
                _compute_cluster_properties
            )

        def _parse_net_app_volume_snapshots(
            data: object,
        ) -> list[DominoJobsInterfaceNetAppVolumeSnapshotRefDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                net_app_volume_snapshots_type_0 = []
                _net_app_volume_snapshots_type_0 = data
                for net_app_volume_snapshots_type_0_item_data in _net_app_volume_snapshots_type_0:
                    net_app_volume_snapshots_type_0_item = DominoJobsInterfaceNetAppVolumeSnapshotRefDto.from_dict(
                        net_app_volume_snapshots_type_0_item_data
                    )

                    net_app_volume_snapshots_type_0.append(net_app_volume_snapshots_type_0_item)

                return net_app_volume_snapshots_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DominoJobsInterfaceNetAppVolumeSnapshotRefDto] | None | Unset, data)

        net_app_volume_snapshots = _parse_net_app_volume_snapshots(d.pop("netAppVolumeSnapshots", UNSET))

        domino_jobs_web_start_workflow_job_request = cls(
            project_id=project_id,
            command_to_run=command_to_run,
            commit_id=commit_id,
            hardware_tier_id=hardware_tier_id,
            dataset_snapshots=dataset_snapshots,
            environment_id=environment_id,
            environment_revision_spec=environment_revision_spec,
            external_volume_mount_ids=external_volume_mount_ids,
            volume_size_gi_b=volume_size_gi_b,
            workflow_config=workflow_config,
            title=title,
            main_repo_git_ref=main_repo_git_ref,
            capacity_type=capacity_type,
            compute_cluster_properties=compute_cluster_properties,
            net_app_volume_snapshots=net_app_volume_snapshots,
        )

        domino_jobs_web_start_workflow_job_request.additional_properties = d
        return domino_jobs_web_start_workflow_job_request

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
