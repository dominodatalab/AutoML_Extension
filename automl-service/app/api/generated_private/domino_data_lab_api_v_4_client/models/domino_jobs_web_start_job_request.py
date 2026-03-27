from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_jobs_web_start_job_request_capacity_type import DominoJobsWebStartJobRequestCapacityType
from ..models.domino_jobs_web_start_job_request_environment_revision_spec_type_0 import (
    DominoJobsWebStartJobRequestEnvironmentRevisionSpecType0,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_jobs_interface_compute_cluster_config_spec_dto import (
        DominoJobsInterfaceComputeClusterConfigSpecDto,
    )
    from ..models.domino_jobs_web_start_job_request_environment_revision_spec_type_1 import (
        DominoJobsWebStartJobRequestEnvironmentRevisionSpecType1,
    )
    from ..models.domino_projects_api_on_demand_spark_cluster_properties_spec import (
        DominoProjectsApiOnDemandSparkClusterPropertiesSpec,
    )
    from ..models.domino_projects_api_repositories_reference_dto import DominoProjectsApiRepositoriesReferenceDTO


T = TypeVar("T", bound="DominoJobsWebStartJobRequest")


@_attrs_define
class DominoJobsWebStartJobRequest:
    """
    Attributes:
        project_id (str):
        command_to_run (str):
        commit_id (None | str | Unset):
        main_repo_git_ref (DominoProjectsApiRepositoriesReferenceDTO | Unset):
        capacity_type (DominoJobsWebStartJobRequestCapacityType | Unset):
        override_hardware_tier_id (None | str | Unset):
        on_demand_spark_cluster_properties (DominoProjectsApiOnDemandSparkClusterPropertiesSpec | Unset):
        compute_cluster_properties (DominoJobsInterfaceComputeClusterConfigSpecDto | Unset):
        environment_id (None | str | Unset):
        environment_revision_spec (DominoJobsWebStartJobRequestEnvironmentRevisionSpecType0 |
            DominoJobsWebStartJobRequestEnvironmentRevisionSpecType1 | None | Unset):
        external_volume_mounts (list[str] | None | Unset):
        net_app_volume_ids (list[str] | None | Unset):
        override_volume_size_gi_b (float | None | Unset):
        title (None | str | Unset):
        snapshot_datasets_on_completion (bool | None | Unset):
        snapshot_net_app_volumes_on_completion (bool | None | Unset):
    """

    project_id: str
    command_to_run: str
    commit_id: None | str | Unset = UNSET
    main_repo_git_ref: DominoProjectsApiRepositoriesReferenceDTO | Unset = UNSET
    capacity_type: DominoJobsWebStartJobRequestCapacityType | Unset = UNSET
    override_hardware_tier_id: None | str | Unset = UNSET
    on_demand_spark_cluster_properties: DominoProjectsApiOnDemandSparkClusterPropertiesSpec | Unset = UNSET
    compute_cluster_properties: DominoJobsInterfaceComputeClusterConfigSpecDto | Unset = UNSET
    environment_id: None | str | Unset = UNSET
    environment_revision_spec: (
        DominoJobsWebStartJobRequestEnvironmentRevisionSpecType0
        | DominoJobsWebStartJobRequestEnvironmentRevisionSpecType1
        | None
        | Unset
    ) = UNSET
    external_volume_mounts: list[str] | None | Unset = UNSET
    net_app_volume_ids: list[str] | None | Unset = UNSET
    override_volume_size_gi_b: float | None | Unset = UNSET
    title: None | str | Unset = UNSET
    snapshot_datasets_on_completion: bool | None | Unset = UNSET
    snapshot_net_app_volumes_on_completion: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.domino_jobs_web_start_job_request_environment_revision_spec_type_1 import (
            DominoJobsWebStartJobRequestEnvironmentRevisionSpecType1,
        )

        project_id = self.project_id

        command_to_run = self.command_to_run

        commit_id: None | str | Unset
        if isinstance(self.commit_id, Unset):
            commit_id = UNSET
        else:
            commit_id = self.commit_id

        main_repo_git_ref: dict[str, Any] | Unset = UNSET
        if not isinstance(self.main_repo_git_ref, Unset):
            main_repo_git_ref = self.main_repo_git_ref.to_dict()

        capacity_type: str | Unset = UNSET
        if not isinstance(self.capacity_type, Unset):
            capacity_type = self.capacity_type.value

        override_hardware_tier_id: None | str | Unset
        if isinstance(self.override_hardware_tier_id, Unset):
            override_hardware_tier_id = UNSET
        else:
            override_hardware_tier_id = self.override_hardware_tier_id

        on_demand_spark_cluster_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.on_demand_spark_cluster_properties, Unset):
            on_demand_spark_cluster_properties = self.on_demand_spark_cluster_properties.to_dict()

        compute_cluster_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.compute_cluster_properties, Unset):
            compute_cluster_properties = self.compute_cluster_properties.to_dict()

        environment_id: None | str | Unset
        if isinstance(self.environment_id, Unset):
            environment_id = UNSET
        else:
            environment_id = self.environment_id

        environment_revision_spec: dict[str, Any] | None | str | Unset
        if isinstance(self.environment_revision_spec, Unset):
            environment_revision_spec = UNSET
        elif isinstance(self.environment_revision_spec, DominoJobsWebStartJobRequestEnvironmentRevisionSpecType0):
            environment_revision_spec = self.environment_revision_spec.value
        elif isinstance(self.environment_revision_spec, DominoJobsWebStartJobRequestEnvironmentRevisionSpecType1):
            environment_revision_spec = self.environment_revision_spec.to_dict()
        else:
            environment_revision_spec = self.environment_revision_spec

        external_volume_mounts: list[str] | None | Unset
        if isinstance(self.external_volume_mounts, Unset):
            external_volume_mounts = UNSET
        elif isinstance(self.external_volume_mounts, list):
            external_volume_mounts = self.external_volume_mounts

        else:
            external_volume_mounts = self.external_volume_mounts

        net_app_volume_ids: list[str] | None | Unset
        if isinstance(self.net_app_volume_ids, Unset):
            net_app_volume_ids = UNSET
        elif isinstance(self.net_app_volume_ids, list):
            net_app_volume_ids = self.net_app_volume_ids

        else:
            net_app_volume_ids = self.net_app_volume_ids

        override_volume_size_gi_b: float | None | Unset
        if isinstance(self.override_volume_size_gi_b, Unset):
            override_volume_size_gi_b = UNSET
        else:
            override_volume_size_gi_b = self.override_volume_size_gi_b

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        snapshot_datasets_on_completion: bool | None | Unset
        if isinstance(self.snapshot_datasets_on_completion, Unset):
            snapshot_datasets_on_completion = UNSET
        else:
            snapshot_datasets_on_completion = self.snapshot_datasets_on_completion

        snapshot_net_app_volumes_on_completion: bool | None | Unset
        if isinstance(self.snapshot_net_app_volumes_on_completion, Unset):
            snapshot_net_app_volumes_on_completion = UNSET
        else:
            snapshot_net_app_volumes_on_completion = self.snapshot_net_app_volumes_on_completion

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectId": project_id,
                "commandToRun": command_to_run,
            }
        )
        if commit_id is not UNSET:
            field_dict["commitId"] = commit_id
        if main_repo_git_ref is not UNSET:
            field_dict["mainRepoGitRef"] = main_repo_git_ref
        if capacity_type is not UNSET:
            field_dict["capacityType"] = capacity_type
        if override_hardware_tier_id is not UNSET:
            field_dict["overrideHardwareTierId"] = override_hardware_tier_id
        if on_demand_spark_cluster_properties is not UNSET:
            field_dict["onDemandSparkClusterProperties"] = on_demand_spark_cluster_properties
        if compute_cluster_properties is not UNSET:
            field_dict["computeClusterProperties"] = compute_cluster_properties
        if environment_id is not UNSET:
            field_dict["environmentId"] = environment_id
        if environment_revision_spec is not UNSET:
            field_dict["environmentRevisionSpec"] = environment_revision_spec
        if external_volume_mounts is not UNSET:
            field_dict["externalVolumeMounts"] = external_volume_mounts
        if net_app_volume_ids is not UNSET:
            field_dict["netAppVolumeIds"] = net_app_volume_ids
        if override_volume_size_gi_b is not UNSET:
            field_dict["overrideVolumeSizeGiB"] = override_volume_size_gi_b
        if title is not UNSET:
            field_dict["title"] = title
        if snapshot_datasets_on_completion is not UNSET:
            field_dict["snapshotDatasetsOnCompletion"] = snapshot_datasets_on_completion
        if snapshot_net_app_volumes_on_completion is not UNSET:
            field_dict["snapshotNetAppVolumesOnCompletion"] = snapshot_net_app_volumes_on_completion

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_jobs_interface_compute_cluster_config_spec_dto import (
            DominoJobsInterfaceComputeClusterConfigSpecDto,
        )
        from ..models.domino_jobs_web_start_job_request_environment_revision_spec_type_1 import (
            DominoJobsWebStartJobRequestEnvironmentRevisionSpecType1,
        )
        from ..models.domino_projects_api_on_demand_spark_cluster_properties_spec import (
            DominoProjectsApiOnDemandSparkClusterPropertiesSpec,
        )
        from ..models.domino_projects_api_repositories_reference_dto import DominoProjectsApiRepositoriesReferenceDTO

        d = dict(src_dict)
        project_id = d.pop("projectId")

        command_to_run = d.pop("commandToRun")

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

        _capacity_type = d.pop("capacityType", UNSET)
        capacity_type: DominoJobsWebStartJobRequestCapacityType | Unset
        if isinstance(_capacity_type, Unset):
            capacity_type = UNSET
        else:
            capacity_type = DominoJobsWebStartJobRequestCapacityType(_capacity_type)

        def _parse_override_hardware_tier_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        override_hardware_tier_id = _parse_override_hardware_tier_id(d.pop("overrideHardwareTierId", UNSET))

        _on_demand_spark_cluster_properties = d.pop("onDemandSparkClusterProperties", UNSET)
        on_demand_spark_cluster_properties: DominoProjectsApiOnDemandSparkClusterPropertiesSpec | Unset
        if isinstance(_on_demand_spark_cluster_properties, Unset):
            on_demand_spark_cluster_properties = UNSET
        else:
            on_demand_spark_cluster_properties = DominoProjectsApiOnDemandSparkClusterPropertiesSpec.from_dict(
                _on_demand_spark_cluster_properties
            )

        _compute_cluster_properties = d.pop("computeClusterProperties", UNSET)
        compute_cluster_properties: DominoJobsInterfaceComputeClusterConfigSpecDto | Unset
        if isinstance(_compute_cluster_properties, Unset):
            compute_cluster_properties = UNSET
        else:
            compute_cluster_properties = DominoJobsInterfaceComputeClusterConfigSpecDto.from_dict(
                _compute_cluster_properties
            )

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
            DominoJobsWebStartJobRequestEnvironmentRevisionSpecType0
            | DominoJobsWebStartJobRequestEnvironmentRevisionSpecType1
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
                environment_revision_spec_type_0 = DominoJobsWebStartJobRequestEnvironmentRevisionSpecType0(data)

                return environment_revision_spec_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                environment_revision_spec_type_1 = DominoJobsWebStartJobRequestEnvironmentRevisionSpecType1.from_dict(
                    data
                )

                return environment_revision_spec_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                DominoJobsWebStartJobRequestEnvironmentRevisionSpecType0
                | DominoJobsWebStartJobRequestEnvironmentRevisionSpecType1
                | None
                | Unset,
                data,
            )

        environment_revision_spec = _parse_environment_revision_spec(d.pop("environmentRevisionSpec", UNSET))

        def _parse_external_volume_mounts(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                external_volume_mounts_type_0 = cast(list[str], data)

                return external_volume_mounts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        external_volume_mounts = _parse_external_volume_mounts(d.pop("externalVolumeMounts", UNSET))

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

        def _parse_override_volume_size_gi_b(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        override_volume_size_gi_b = _parse_override_volume_size_gi_b(d.pop("overrideVolumeSizeGiB", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_snapshot_datasets_on_completion(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        snapshot_datasets_on_completion = _parse_snapshot_datasets_on_completion(
            d.pop("snapshotDatasetsOnCompletion", UNSET)
        )

        def _parse_snapshot_net_app_volumes_on_completion(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        snapshot_net_app_volumes_on_completion = _parse_snapshot_net_app_volumes_on_completion(
            d.pop("snapshotNetAppVolumesOnCompletion", UNSET)
        )

        domino_jobs_web_start_job_request = cls(
            project_id=project_id,
            command_to_run=command_to_run,
            commit_id=commit_id,
            main_repo_git_ref=main_repo_git_ref,
            capacity_type=capacity_type,
            override_hardware_tier_id=override_hardware_tier_id,
            on_demand_spark_cluster_properties=on_demand_spark_cluster_properties,
            compute_cluster_properties=compute_cluster_properties,
            environment_id=environment_id,
            environment_revision_spec=environment_revision_spec,
            external_volume_mounts=external_volume_mounts,
            net_app_volume_ids=net_app_volume_ids,
            override_volume_size_gi_b=override_volume_size_gi_b,
            title=title,
            snapshot_datasets_on_completion=snapshot_datasets_on_completion,
            snapshot_net_app_volumes_on_completion=snapshot_net_app_volumes_on_completion,
        )

        domino_jobs_web_start_job_request.additional_properties = d
        return domino_jobs_web_start_job_request

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
