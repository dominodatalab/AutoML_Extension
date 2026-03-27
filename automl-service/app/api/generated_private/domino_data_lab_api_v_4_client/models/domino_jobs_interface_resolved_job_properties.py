from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

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
    from ..models.domino_projects_api_repositories_reference_dto import DominoProjectsApiRepositoriesReferenceDTO


T = TypeVar("T", bound="DominoJobsInterfaceResolvedJobProperties")


@_attrs_define
class DominoJobsInterfaceResolvedJobProperties:
    """
    Attributes:
        commit_id (str):
        hardware_tier_id (DominoHardwaretierApiHardwareTierIdentifier):
        dataset_snapshots (list[DominoDatasetrwApiDatasetSnapshotRefDto]):
        net_app_volume_snapshots (list[DominoJobsInterfaceNetAppVolumeSnapshotRefDto]):
        environment_id (str):
        environment_revision_spec (Any):
        external_volume_mount_ids (list[str]):
        net_app_volume_ids (list[str]):
        volume_size_gi_b (float):
        main_repo_git_ref (DominoProjectsApiRepositoriesReferenceDTO | Unset):
        compute_cluster_properties (DominoJobsInterfaceComputeClusterConfigSpecWithSpecificRevisionDto | Unset):
    """

    commit_id: str
    hardware_tier_id: DominoHardwaretierApiHardwareTierIdentifier
    dataset_snapshots: list[DominoDatasetrwApiDatasetSnapshotRefDto]
    net_app_volume_snapshots: list[DominoJobsInterfaceNetAppVolumeSnapshotRefDto]
    environment_id: str
    environment_revision_spec: Any
    external_volume_mount_ids: list[str]
    net_app_volume_ids: list[str]
    volume_size_gi_b: float
    main_repo_git_ref: DominoProjectsApiRepositoriesReferenceDTO | Unset = UNSET
    compute_cluster_properties: DominoJobsInterfaceComputeClusterConfigSpecWithSpecificRevisionDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        commit_id = self.commit_id

        hardware_tier_id = self.hardware_tier_id.to_dict()

        dataset_snapshots = []
        for dataset_snapshots_item_data in self.dataset_snapshots:
            dataset_snapshots_item = dataset_snapshots_item_data.to_dict()
            dataset_snapshots.append(dataset_snapshots_item)

        net_app_volume_snapshots = []
        for net_app_volume_snapshots_item_data in self.net_app_volume_snapshots:
            net_app_volume_snapshots_item = net_app_volume_snapshots_item_data.to_dict()
            net_app_volume_snapshots.append(net_app_volume_snapshots_item)

        environment_id = self.environment_id

        environment_revision_spec = self.environment_revision_spec

        external_volume_mount_ids = self.external_volume_mount_ids

        net_app_volume_ids = self.net_app_volume_ids

        volume_size_gi_b = self.volume_size_gi_b

        main_repo_git_ref: dict[str, Any] | Unset = UNSET
        if not isinstance(self.main_repo_git_ref, Unset):
            main_repo_git_ref = self.main_repo_git_ref.to_dict()

        compute_cluster_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.compute_cluster_properties, Unset):
            compute_cluster_properties = self.compute_cluster_properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commitId": commit_id,
                "hardwareTierId": hardware_tier_id,
                "datasetSnapshots": dataset_snapshots,
                "netAppVolumeSnapshots": net_app_volume_snapshots,
                "environmentId": environment_id,
                "environmentRevisionSpec": environment_revision_spec,
                "externalVolumeMountIds": external_volume_mount_ids,
                "netAppVolumeIds": net_app_volume_ids,
                "volumeSizeGiB": volume_size_gi_b,
            }
        )
        if main_repo_git_ref is not UNSET:
            field_dict["mainRepoGitRef"] = main_repo_git_ref
        if compute_cluster_properties is not UNSET:
            field_dict["computeClusterProperties"] = compute_cluster_properties

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
        from ..models.domino_projects_api_repositories_reference_dto import DominoProjectsApiRepositoriesReferenceDTO

        d = dict(src_dict)
        commit_id = d.pop("commitId")

        hardware_tier_id = DominoHardwaretierApiHardwareTierIdentifier.from_dict(d.pop("hardwareTierId"))

        dataset_snapshots = []
        _dataset_snapshots = d.pop("datasetSnapshots")
        for dataset_snapshots_item_data in _dataset_snapshots:
            dataset_snapshots_item = DominoDatasetrwApiDatasetSnapshotRefDto.from_dict(dataset_snapshots_item_data)

            dataset_snapshots.append(dataset_snapshots_item)

        net_app_volume_snapshots = []
        _net_app_volume_snapshots = d.pop("netAppVolumeSnapshots")
        for net_app_volume_snapshots_item_data in _net_app_volume_snapshots:
            net_app_volume_snapshots_item = DominoJobsInterfaceNetAppVolumeSnapshotRefDto.from_dict(
                net_app_volume_snapshots_item_data
            )

            net_app_volume_snapshots.append(net_app_volume_snapshots_item)

        environment_id = d.pop("environmentId")

        environment_revision_spec = d.pop("environmentRevisionSpec")

        external_volume_mount_ids = cast(list[str], d.pop("externalVolumeMountIds"))

        net_app_volume_ids = cast(list[str], d.pop("netAppVolumeIds"))

        volume_size_gi_b = d.pop("volumeSizeGiB")

        _main_repo_git_ref = d.pop("mainRepoGitRef", UNSET)
        main_repo_git_ref: DominoProjectsApiRepositoriesReferenceDTO | Unset
        if isinstance(_main_repo_git_ref, Unset):
            main_repo_git_ref = UNSET
        else:
            main_repo_git_ref = DominoProjectsApiRepositoriesReferenceDTO.from_dict(_main_repo_git_ref)

        _compute_cluster_properties = d.pop("computeClusterProperties", UNSET)
        compute_cluster_properties: DominoJobsInterfaceComputeClusterConfigSpecWithSpecificRevisionDto | Unset
        if isinstance(_compute_cluster_properties, Unset):
            compute_cluster_properties = UNSET
        else:
            compute_cluster_properties = DominoJobsInterfaceComputeClusterConfigSpecWithSpecificRevisionDto.from_dict(
                _compute_cluster_properties
            )

        domino_jobs_interface_resolved_job_properties = cls(
            commit_id=commit_id,
            hardware_tier_id=hardware_tier_id,
            dataset_snapshots=dataset_snapshots,
            net_app_volume_snapshots=net_app_volume_snapshots,
            environment_id=environment_id,
            environment_revision_spec=environment_revision_spec,
            external_volume_mount_ids=external_volume_mount_ids,
            net_app_volume_ids=net_app_volume_ids,
            volume_size_gi_b=volume_size_gi_b,
            main_repo_git_ref=main_repo_git_ref,
            compute_cluster_properties=compute_cluster_properties,
        )

        domino_jobs_interface_resolved_job_properties.additional_properties = d
        return domino_jobs_interface_resolved_job_properties

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
