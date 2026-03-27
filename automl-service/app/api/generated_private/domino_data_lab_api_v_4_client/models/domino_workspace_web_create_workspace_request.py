from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_workspace_web_create_workspace_request_capacity_type import (
    DominoWorkspaceWebCreateWorkspaceRequestCapacityType,
)
from ..models.domino_workspace_web_create_workspace_request_environment_revision_spec_type_0 import (
    DominoWorkspaceWebCreateWorkspaceRequestEnvironmentRevisionSpecType0,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_hardwaretier_api_hardware_tier_identifier import DominoHardwaretierApiHardwareTierIdentifier
    from ..models.domino_projects_api_repositories_reference_dto import DominoProjectsApiRepositoriesReferenceDTO
    from ..models.domino_workspace_api_compute_cluster_config_dto import DominoWorkspaceApiComputeClusterConfigDto
    from ..models.domino_workspace_api_ssh_config_dto import DominoWorkspaceApiSshConfigDto
    from ..models.domino_workspace_api_workspace_cluster_config_dto import DominoWorkspaceApiWorkspaceClusterConfigDto
    from ..models.domino_workspace_api_workspace_persistence_config_dto import (
        DominoWorkspaceApiWorkspacePersistenceConfigDto,
    )
    from ..models.domino_workspace_api_workspace_reproduction_details_dto import (
        DominoWorkspaceApiWorkspaceReproductionDetailsDto,
    )
    from ..models.domino_workspace_web_create_workspace_request_environment_revision_spec_type_1 import (
        DominoWorkspaceWebCreateWorkspaceRequestEnvironmentRevisionSpecType1,
    )


T = TypeVar("T", bound="DominoWorkspaceWebCreateWorkspaceRequest")


@_attrs_define
class DominoWorkspaceWebCreateWorkspaceRequest:
    """
    Attributes:
        name (str):
        environment_id (str):
        hardware_tier_id (DominoHardwaretierApiHardwareTierIdentifier):
        tools (list[str]):
        external_volume_mounts (list[str]):
        environment_revision_spec (DominoWorkspaceWebCreateWorkspaceRequestEnvironmentRevisionSpecType0 |
            DominoWorkspaceWebCreateWorkspaceRequestEnvironmentRevisionSpecType1 | None | Unset):
        capacity_type (DominoWorkspaceWebCreateWorkspaceRequestCapacityType | Unset):
        cluster_config (DominoWorkspaceApiWorkspaceClusterConfigDto | Unset):
        compute_cluster_config (DominoWorkspaceApiComputeClusterConfigDto | Unset):
        net_app_volume_ids (list[str] | None | Unset):
        override_main_git_repo_ref (DominoProjectsApiRepositoriesReferenceDTO | Unset):
        workspace_reproduction_details (DominoWorkspaceApiWorkspaceReproductionDetailsDto | Unset):
        override_volume_size_gi_b (float | None | Unset):
        ssh (DominoWorkspaceApiSshConfigDto | Unset):
        persistence (DominoWorkspaceApiWorkspacePersistenceConfigDto | Unset):
    """

    name: str
    environment_id: str
    hardware_tier_id: DominoHardwaretierApiHardwareTierIdentifier
    tools: list[str]
    external_volume_mounts: list[str]
    environment_revision_spec: (
        DominoWorkspaceWebCreateWorkspaceRequestEnvironmentRevisionSpecType0
        | DominoWorkspaceWebCreateWorkspaceRequestEnvironmentRevisionSpecType1
        | None
        | Unset
    ) = UNSET
    capacity_type: DominoWorkspaceWebCreateWorkspaceRequestCapacityType | Unset = UNSET
    cluster_config: DominoWorkspaceApiWorkspaceClusterConfigDto | Unset = UNSET
    compute_cluster_config: DominoWorkspaceApiComputeClusterConfigDto | Unset = UNSET
    net_app_volume_ids: list[str] | None | Unset = UNSET
    override_main_git_repo_ref: DominoProjectsApiRepositoriesReferenceDTO | Unset = UNSET
    workspace_reproduction_details: DominoWorkspaceApiWorkspaceReproductionDetailsDto | Unset = UNSET
    override_volume_size_gi_b: float | None | Unset = UNSET
    ssh: DominoWorkspaceApiSshConfigDto | Unset = UNSET
    persistence: DominoWorkspaceApiWorkspacePersistenceConfigDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.domino_workspace_web_create_workspace_request_environment_revision_spec_type_1 import (
            DominoWorkspaceWebCreateWorkspaceRequestEnvironmentRevisionSpecType1,
        )

        name = self.name

        environment_id = self.environment_id

        hardware_tier_id = self.hardware_tier_id.to_dict()

        tools = self.tools

        external_volume_mounts = self.external_volume_mounts

        environment_revision_spec: dict[str, Any] | None | str | Unset
        if isinstance(self.environment_revision_spec, Unset):
            environment_revision_spec = UNSET
        elif isinstance(
            self.environment_revision_spec, DominoWorkspaceWebCreateWorkspaceRequestEnvironmentRevisionSpecType0
        ):
            environment_revision_spec = self.environment_revision_spec.value
        elif isinstance(
            self.environment_revision_spec, DominoWorkspaceWebCreateWorkspaceRequestEnvironmentRevisionSpecType1
        ):
            environment_revision_spec = self.environment_revision_spec.to_dict()
        else:
            environment_revision_spec = self.environment_revision_spec

        capacity_type: str | Unset = UNSET
        if not isinstance(self.capacity_type, Unset):
            capacity_type = self.capacity_type.value

        cluster_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cluster_config, Unset):
            cluster_config = self.cluster_config.to_dict()

        compute_cluster_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.compute_cluster_config, Unset):
            compute_cluster_config = self.compute_cluster_config.to_dict()

        net_app_volume_ids: list[str] | None | Unset
        if isinstance(self.net_app_volume_ids, Unset):
            net_app_volume_ids = UNSET
        elif isinstance(self.net_app_volume_ids, list):
            net_app_volume_ids = self.net_app_volume_ids

        else:
            net_app_volume_ids = self.net_app_volume_ids

        override_main_git_repo_ref: dict[str, Any] | Unset = UNSET
        if not isinstance(self.override_main_git_repo_ref, Unset):
            override_main_git_repo_ref = self.override_main_git_repo_ref.to_dict()

        workspace_reproduction_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workspace_reproduction_details, Unset):
            workspace_reproduction_details = self.workspace_reproduction_details.to_dict()

        override_volume_size_gi_b: float | None | Unset
        if isinstance(self.override_volume_size_gi_b, Unset):
            override_volume_size_gi_b = UNSET
        else:
            override_volume_size_gi_b = self.override_volume_size_gi_b

        ssh: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ssh, Unset):
            ssh = self.ssh.to_dict()

        persistence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.persistence, Unset):
            persistence = self.persistence.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "environmentId": environment_id,
                "hardwareTierId": hardware_tier_id,
                "tools": tools,
                "externalVolumeMounts": external_volume_mounts,
            }
        )
        if environment_revision_spec is not UNSET:
            field_dict["environmentRevisionSpec"] = environment_revision_spec
        if capacity_type is not UNSET:
            field_dict["capacityType"] = capacity_type
        if cluster_config is not UNSET:
            field_dict["clusterConfig"] = cluster_config
        if compute_cluster_config is not UNSET:
            field_dict["computeClusterConfig"] = compute_cluster_config
        if net_app_volume_ids is not UNSET:
            field_dict["netAppVolumeIds"] = net_app_volume_ids
        if override_main_git_repo_ref is not UNSET:
            field_dict["overrideMainGitRepoRef"] = override_main_git_repo_ref
        if workspace_reproduction_details is not UNSET:
            field_dict["workspaceReproductionDetails"] = workspace_reproduction_details
        if override_volume_size_gi_b is not UNSET:
            field_dict["overrideVolumeSizeGiB"] = override_volume_size_gi_b
        if ssh is not UNSET:
            field_dict["ssh"] = ssh
        if persistence is not UNSET:
            field_dict["persistence"] = persistence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_hardwaretier_api_hardware_tier_identifier import (
            DominoHardwaretierApiHardwareTierIdentifier,
        )
        from ..models.domino_projects_api_repositories_reference_dto import DominoProjectsApiRepositoriesReferenceDTO
        from ..models.domino_workspace_api_compute_cluster_config_dto import DominoWorkspaceApiComputeClusterConfigDto
        from ..models.domino_workspace_api_ssh_config_dto import DominoWorkspaceApiSshConfigDto
        from ..models.domino_workspace_api_workspace_cluster_config_dto import (
            DominoWorkspaceApiWorkspaceClusterConfigDto,
        )
        from ..models.domino_workspace_api_workspace_persistence_config_dto import (
            DominoWorkspaceApiWorkspacePersistenceConfigDto,
        )
        from ..models.domino_workspace_api_workspace_reproduction_details_dto import (
            DominoWorkspaceApiWorkspaceReproductionDetailsDto,
        )
        from ..models.domino_workspace_web_create_workspace_request_environment_revision_spec_type_1 import (
            DominoWorkspaceWebCreateWorkspaceRequestEnvironmentRevisionSpecType1,
        )

        d = dict(src_dict)
        name = d.pop("name")

        environment_id = d.pop("environmentId")

        hardware_tier_id = DominoHardwaretierApiHardwareTierIdentifier.from_dict(d.pop("hardwareTierId"))

        tools = cast(list[str], d.pop("tools"))

        external_volume_mounts = cast(list[str], d.pop("externalVolumeMounts"))

        def _parse_environment_revision_spec(
            data: object,
        ) -> (
            DominoWorkspaceWebCreateWorkspaceRequestEnvironmentRevisionSpecType0
            | DominoWorkspaceWebCreateWorkspaceRequestEnvironmentRevisionSpecType1
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
                environment_revision_spec_type_0 = DominoWorkspaceWebCreateWorkspaceRequestEnvironmentRevisionSpecType0(
                    data
                )

                return environment_revision_spec_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                environment_revision_spec_type_1 = (
                    DominoWorkspaceWebCreateWorkspaceRequestEnvironmentRevisionSpecType1.from_dict(data)
                )

                return environment_revision_spec_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                DominoWorkspaceWebCreateWorkspaceRequestEnvironmentRevisionSpecType0
                | DominoWorkspaceWebCreateWorkspaceRequestEnvironmentRevisionSpecType1
                | None
                | Unset,
                data,
            )

        environment_revision_spec = _parse_environment_revision_spec(d.pop("environmentRevisionSpec", UNSET))

        _capacity_type = d.pop("capacityType", UNSET)
        capacity_type: DominoWorkspaceWebCreateWorkspaceRequestCapacityType | Unset
        if isinstance(_capacity_type, Unset):
            capacity_type = UNSET
        else:
            capacity_type = DominoWorkspaceWebCreateWorkspaceRequestCapacityType(_capacity_type)

        _cluster_config = d.pop("clusterConfig", UNSET)
        cluster_config: DominoWorkspaceApiWorkspaceClusterConfigDto | Unset
        if isinstance(_cluster_config, Unset):
            cluster_config = UNSET
        else:
            cluster_config = DominoWorkspaceApiWorkspaceClusterConfigDto.from_dict(_cluster_config)

        _compute_cluster_config = d.pop("computeClusterConfig", UNSET)
        compute_cluster_config: DominoWorkspaceApiComputeClusterConfigDto | Unset
        if isinstance(_compute_cluster_config, Unset):
            compute_cluster_config = UNSET
        else:
            compute_cluster_config = DominoWorkspaceApiComputeClusterConfigDto.from_dict(_compute_cluster_config)

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

        _override_main_git_repo_ref = d.pop("overrideMainGitRepoRef", UNSET)
        override_main_git_repo_ref: DominoProjectsApiRepositoriesReferenceDTO | Unset
        if isinstance(_override_main_git_repo_ref, Unset):
            override_main_git_repo_ref = UNSET
        else:
            override_main_git_repo_ref = DominoProjectsApiRepositoriesReferenceDTO.from_dict(
                _override_main_git_repo_ref
            )

        _workspace_reproduction_details = d.pop("workspaceReproductionDetails", UNSET)
        workspace_reproduction_details: DominoWorkspaceApiWorkspaceReproductionDetailsDto | Unset
        if isinstance(_workspace_reproduction_details, Unset):
            workspace_reproduction_details = UNSET
        else:
            workspace_reproduction_details = DominoWorkspaceApiWorkspaceReproductionDetailsDto.from_dict(
                _workspace_reproduction_details
            )

        def _parse_override_volume_size_gi_b(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        override_volume_size_gi_b = _parse_override_volume_size_gi_b(d.pop("overrideVolumeSizeGiB", UNSET))

        _ssh = d.pop("ssh", UNSET)
        ssh: DominoWorkspaceApiSshConfigDto | Unset
        if isinstance(_ssh, Unset):
            ssh = UNSET
        else:
            ssh = DominoWorkspaceApiSshConfigDto.from_dict(_ssh)

        _persistence = d.pop("persistence", UNSET)
        persistence: DominoWorkspaceApiWorkspacePersistenceConfigDto | Unset
        if isinstance(_persistence, Unset):
            persistence = UNSET
        else:
            persistence = DominoWorkspaceApiWorkspacePersistenceConfigDto.from_dict(_persistence)

        domino_workspace_web_create_workspace_request = cls(
            name=name,
            environment_id=environment_id,
            hardware_tier_id=hardware_tier_id,
            tools=tools,
            external_volume_mounts=external_volume_mounts,
            environment_revision_spec=environment_revision_spec,
            capacity_type=capacity_type,
            cluster_config=cluster_config,
            compute_cluster_config=compute_cluster_config,
            net_app_volume_ids=net_app_volume_ids,
            override_main_git_repo_ref=override_main_git_repo_ref,
            workspace_reproduction_details=workspace_reproduction_details,
            override_volume_size_gi_b=override_volume_size_gi_b,
            ssh=ssh,
            persistence=persistence,
        )

        domino_workspace_web_create_workspace_request.additional_properties = d
        return domino_workspace_web_create_workspace_request

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
