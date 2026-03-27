from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_jobs_web_resolve_default_job_properties_request_environment_revision_spec_type_0 import (
    DominoJobsWebResolveDefaultJobPropertiesRequestEnvironmentRevisionSpecType0,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_datasetrw_api_dataset_snapshot_ref_dto import DominoDatasetrwApiDatasetSnapshotRefDto
    from ..models.domino_hardwaretier_api_hardware_tier_identifier import DominoHardwaretierApiHardwareTierIdentifier
    from ..models.domino_jobs_interface_compute_cluster_config_spec_dto import (
        DominoJobsInterfaceComputeClusterConfigSpecDto,
    )
    from ..models.domino_jobs_interface_net_app_volume_snapshot_ref_dto import (
        DominoJobsInterfaceNetAppVolumeSnapshotRefDto,
    )
    from ..models.domino_jobs_web_resolve_default_job_properties_request_environment_revision_spec_type_1 import (
        DominoJobsWebResolveDefaultJobPropertiesRequestEnvironmentRevisionSpecType1,
    )
    from ..models.domino_projects_api_repositories_reference_dto import DominoProjectsApiRepositoriesReferenceDTO


T = TypeVar("T", bound="DominoJobsWebResolveDefaultJobPropertiesRequest")


@_attrs_define
class DominoJobsWebResolveDefaultJobPropertiesRequest:
    """
    Attributes:
        commit_id (None | str | Unset):
        main_repo_git_ref (DominoProjectsApiRepositoriesReferenceDTO | Unset):
        hardware_tier_id (DominoHardwaretierApiHardwareTierIdentifier | Unset):
        compute_cluster_properties (DominoJobsInterfaceComputeClusterConfigSpecDto | Unset):
        dataset_snapshots (list[DominoDatasetrwApiDatasetSnapshotRefDto] | None | Unset):
        net_app_volume_snapshots (list[DominoJobsInterfaceNetAppVolumeSnapshotRefDto] | None | Unset):
        environment_id (None | str | Unset):
        environment_revision_spec (DominoJobsWebResolveDefaultJobPropertiesRequestEnvironmentRevisionSpecType0 |
            DominoJobsWebResolveDefaultJobPropertiesRequestEnvironmentRevisionSpecType1 | None | Unset):
        external_volume_mount_ids (list[str] | None | Unset):
        net_app_volume_ids (list[str] | None | Unset):
        volume_size_gi_b (float | None | Unset):
    """

    commit_id: None | str | Unset = UNSET
    main_repo_git_ref: DominoProjectsApiRepositoriesReferenceDTO | Unset = UNSET
    hardware_tier_id: DominoHardwaretierApiHardwareTierIdentifier | Unset = UNSET
    compute_cluster_properties: DominoJobsInterfaceComputeClusterConfigSpecDto | Unset = UNSET
    dataset_snapshots: list[DominoDatasetrwApiDatasetSnapshotRefDto] | None | Unset = UNSET
    net_app_volume_snapshots: list[DominoJobsInterfaceNetAppVolumeSnapshotRefDto] | None | Unset = UNSET
    environment_id: None | str | Unset = UNSET
    environment_revision_spec: (
        DominoJobsWebResolveDefaultJobPropertiesRequestEnvironmentRevisionSpecType0
        | DominoJobsWebResolveDefaultJobPropertiesRequestEnvironmentRevisionSpecType1
        | None
        | Unset
    ) = UNSET
    external_volume_mount_ids: list[str] | None | Unset = UNSET
    net_app_volume_ids: list[str] | None | Unset = UNSET
    volume_size_gi_b: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.domino_jobs_web_resolve_default_job_properties_request_environment_revision_spec_type_1 import (
            DominoJobsWebResolveDefaultJobPropertiesRequestEnvironmentRevisionSpecType1,
        )

        commit_id: None | str | Unset
        if isinstance(self.commit_id, Unset):
            commit_id = UNSET
        else:
            commit_id = self.commit_id

        main_repo_git_ref: dict[str, Any] | Unset = UNSET
        if not isinstance(self.main_repo_git_ref, Unset):
            main_repo_git_ref = self.main_repo_git_ref.to_dict()

        hardware_tier_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hardware_tier_id, Unset):
            hardware_tier_id = self.hardware_tier_id.to_dict()

        compute_cluster_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.compute_cluster_properties, Unset):
            compute_cluster_properties = self.compute_cluster_properties.to_dict()

        dataset_snapshots: list[dict[str, Any]] | None | Unset
        if isinstance(self.dataset_snapshots, Unset):
            dataset_snapshots = UNSET
        elif isinstance(self.dataset_snapshots, list):
            dataset_snapshots = []
            for dataset_snapshots_type_0_item_data in self.dataset_snapshots:
                dataset_snapshots_type_0_item = dataset_snapshots_type_0_item_data.to_dict()
                dataset_snapshots.append(dataset_snapshots_type_0_item)

        else:
            dataset_snapshots = self.dataset_snapshots

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

        environment_id: None | str | Unset
        if isinstance(self.environment_id, Unset):
            environment_id = UNSET
        else:
            environment_id = self.environment_id

        environment_revision_spec: dict[str, Any] | None | str | Unset
        if isinstance(self.environment_revision_spec, Unset):
            environment_revision_spec = UNSET
        elif isinstance(
            self.environment_revision_spec, DominoJobsWebResolveDefaultJobPropertiesRequestEnvironmentRevisionSpecType0
        ):
            environment_revision_spec = self.environment_revision_spec.value
        elif isinstance(
            self.environment_revision_spec, DominoJobsWebResolveDefaultJobPropertiesRequestEnvironmentRevisionSpecType1
        ):
            environment_revision_spec = self.environment_revision_spec.to_dict()
        else:
            environment_revision_spec = self.environment_revision_spec

        external_volume_mount_ids: list[str] | None | Unset
        if isinstance(self.external_volume_mount_ids, Unset):
            external_volume_mount_ids = UNSET
        elif isinstance(self.external_volume_mount_ids, list):
            external_volume_mount_ids = self.external_volume_mount_ids

        else:
            external_volume_mount_ids = self.external_volume_mount_ids

        net_app_volume_ids: list[str] | None | Unset
        if isinstance(self.net_app_volume_ids, Unset):
            net_app_volume_ids = UNSET
        elif isinstance(self.net_app_volume_ids, list):
            net_app_volume_ids = self.net_app_volume_ids

        else:
            net_app_volume_ids = self.net_app_volume_ids

        volume_size_gi_b: float | None | Unset
        if isinstance(self.volume_size_gi_b, Unset):
            volume_size_gi_b = UNSET
        else:
            volume_size_gi_b = self.volume_size_gi_b

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if commit_id is not UNSET:
            field_dict["commitId"] = commit_id
        if main_repo_git_ref is not UNSET:
            field_dict["mainRepoGitRef"] = main_repo_git_ref
        if hardware_tier_id is not UNSET:
            field_dict["hardwareTierId"] = hardware_tier_id
        if compute_cluster_properties is not UNSET:
            field_dict["computeClusterProperties"] = compute_cluster_properties
        if dataset_snapshots is not UNSET:
            field_dict["datasetSnapshots"] = dataset_snapshots
        if net_app_volume_snapshots is not UNSET:
            field_dict["netAppVolumeSnapshots"] = net_app_volume_snapshots
        if environment_id is not UNSET:
            field_dict["environmentId"] = environment_id
        if environment_revision_spec is not UNSET:
            field_dict["environmentRevisionSpec"] = environment_revision_spec
        if external_volume_mount_ids is not UNSET:
            field_dict["externalVolumeMountIds"] = external_volume_mount_ids
        if net_app_volume_ids is not UNSET:
            field_dict["netAppVolumeIds"] = net_app_volume_ids
        if volume_size_gi_b is not UNSET:
            field_dict["volumeSizeGiB"] = volume_size_gi_b

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_datasetrw_api_dataset_snapshot_ref_dto import DominoDatasetrwApiDatasetSnapshotRefDto
        from ..models.domino_hardwaretier_api_hardware_tier_identifier import (
            DominoHardwaretierApiHardwareTierIdentifier,
        )
        from ..models.domino_jobs_interface_compute_cluster_config_spec_dto import (
            DominoJobsInterfaceComputeClusterConfigSpecDto,
        )
        from ..models.domino_jobs_interface_net_app_volume_snapshot_ref_dto import (
            DominoJobsInterfaceNetAppVolumeSnapshotRefDto,
        )
        from ..models.domino_jobs_web_resolve_default_job_properties_request_environment_revision_spec_type_1 import (
            DominoJobsWebResolveDefaultJobPropertiesRequestEnvironmentRevisionSpecType1,
        )
        from ..models.domino_projects_api_repositories_reference_dto import DominoProjectsApiRepositoriesReferenceDTO

        d = dict(src_dict)

        def _parse_commit_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commit_id = _parse_commit_id(d.pop("commitId", UNSET))

        _main_repo_git_ref = d.pop("mainRepoGitRef", UNSET)
        main_repo_git_ref: DominoProjectsApiRepositoriesReferenceDTO | Unset
        if isinstance(_main_repo_git_ref, Unset):
            main_repo_git_ref = UNSET
        else:
            main_repo_git_ref = DominoProjectsApiRepositoriesReferenceDTO.from_dict(_main_repo_git_ref)

        _hardware_tier_id = d.pop("hardwareTierId", UNSET)
        hardware_tier_id: DominoHardwaretierApiHardwareTierIdentifier | Unset
        if isinstance(_hardware_tier_id, Unset):
            hardware_tier_id = UNSET
        else:
            hardware_tier_id = DominoHardwaretierApiHardwareTierIdentifier.from_dict(_hardware_tier_id)

        _compute_cluster_properties = d.pop("computeClusterProperties", UNSET)
        compute_cluster_properties: DominoJobsInterfaceComputeClusterConfigSpecDto | Unset
        if isinstance(_compute_cluster_properties, Unset):
            compute_cluster_properties = UNSET
        else:
            compute_cluster_properties = DominoJobsInterfaceComputeClusterConfigSpecDto.from_dict(
                _compute_cluster_properties
            )

        def _parse_dataset_snapshots(data: object) -> list[DominoDatasetrwApiDatasetSnapshotRefDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                dataset_snapshots_type_0 = []
                _dataset_snapshots_type_0 = data
                for dataset_snapshots_type_0_item_data in _dataset_snapshots_type_0:
                    dataset_snapshots_type_0_item = DominoDatasetrwApiDatasetSnapshotRefDto.from_dict(
                        dataset_snapshots_type_0_item_data
                    )

                    dataset_snapshots_type_0.append(dataset_snapshots_type_0_item)

                return dataset_snapshots_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DominoDatasetrwApiDatasetSnapshotRefDto] | None | Unset, data)

        dataset_snapshots = _parse_dataset_snapshots(d.pop("datasetSnapshots", UNSET))

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

        def _parse_environment_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        environment_id = _parse_environment_id(d.pop("environmentId", UNSET))

        def _parse_environment_revision_spec(
            data: object,
        ) -> (
            DominoJobsWebResolveDefaultJobPropertiesRequestEnvironmentRevisionSpecType0
            | DominoJobsWebResolveDefaultJobPropertiesRequestEnvironmentRevisionSpecType1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                environment_revision_spec_type_0 = (
                    DominoJobsWebResolveDefaultJobPropertiesRequestEnvironmentRevisionSpecType0(data)
                )

                return environment_revision_spec_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                environment_revision_spec_type_1 = (
                    DominoJobsWebResolveDefaultJobPropertiesRequestEnvironmentRevisionSpecType1.from_dict(data)
                )

                return environment_revision_spec_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                DominoJobsWebResolveDefaultJobPropertiesRequestEnvironmentRevisionSpecType0
                | DominoJobsWebResolveDefaultJobPropertiesRequestEnvironmentRevisionSpecType1
                | None
                | Unset,
                data,
            )

        environment_revision_spec = _parse_environment_revision_spec(d.pop("environmentRevisionSpec", UNSET))

        def _parse_external_volume_mount_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                external_volume_mount_ids_type_0 = cast(list[str], data)

                return external_volume_mount_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        external_volume_mount_ids = _parse_external_volume_mount_ids(d.pop("externalVolumeMountIds", UNSET))

        def _parse_net_app_volume_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                net_app_volume_ids_type_0 = cast(list[str], data)

                return net_app_volume_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        net_app_volume_ids = _parse_net_app_volume_ids(d.pop("netAppVolumeIds", UNSET))

        def _parse_volume_size_gi_b(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        volume_size_gi_b = _parse_volume_size_gi_b(d.pop("volumeSizeGiB", UNSET))

        domino_jobs_web_resolve_default_job_properties_request = cls(
            commit_id=commit_id,
            main_repo_git_ref=main_repo_git_ref,
            hardware_tier_id=hardware_tier_id,
            compute_cluster_properties=compute_cluster_properties,
            dataset_snapshots=dataset_snapshots,
            net_app_volume_snapshots=net_app_volume_snapshots,
            environment_id=environment_id,
            environment_revision_spec=environment_revision_spec,
            external_volume_mount_ids=external_volume_mount_ids,
            net_app_volume_ids=net_app_volume_ids,
            volume_size_gi_b=volume_size_gi_b,
        )

        domino_jobs_web_resolve_default_job_properties_request.additional_properties = d
        return domino_jobs_web_resolve_default_job_properties_request

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
