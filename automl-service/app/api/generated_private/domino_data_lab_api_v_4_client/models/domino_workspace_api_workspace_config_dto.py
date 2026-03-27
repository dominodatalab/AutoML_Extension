from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_workspace_api_workspace_config_dto_capacity_type import (
    DominoWorkspaceApiWorkspaceConfigDtoCapacityType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_computecluster_api_compute_cluster_config_response_dto import (
        DominoComputeclusterApiComputeClusterConfigResponseDto,
    )
    from ..models.domino_computecluster_api_spark_cluster_props_dto import DominoComputeclusterApiSparkClusterPropsDto
    from ..models.domino_environments_api_environment_revision_summary import (
        DominoEnvironmentsApiEnvironmentRevisionSummary,
    )
    from ..models.domino_workspace_api_data_plane_dto import DominoWorkspaceApiDataPlaneDto
    from ..models.domino_workspace_api_ssh_config_dto import DominoWorkspaceApiSshConfigDto
    from ..models.domino_workspace_api_workspace_hardware_tier_dto import DominoWorkspaceApiWorkspaceHardwareTierDto
    from ..models.domino_workspace_api_workspace_persistence_config_dto import (
        DominoWorkspaceApiWorkspacePersistenceConfigDto,
    )


T = TypeVar("T", bound="DominoWorkspaceApiWorkspaceConfigDto")


@_attrs_define
class DominoWorkspaceApiWorkspaceConfigDto:
    """
    Attributes:
        environment (DominoEnvironmentsApiEnvironmentRevisionSummary):
        hardware_tier (DominoWorkspaceApiWorkspaceHardwareTierDto):
        tools (list[str]):
        capacity_type (DominoWorkspaceApiWorkspaceConfigDtoCapacityType | Unset):
        cluster_props (DominoComputeclusterApiSparkClusterPropsDto | Unset):
        compute_cluster_response_props (DominoComputeclusterApiComputeClusterConfigResponseDto | Unset):
        ssh (DominoWorkspaceApiSshConfigDto | Unset):
        data_plane (DominoWorkspaceApiDataPlaneDto | Unset):
        persistence (DominoWorkspaceApiWorkspacePersistenceConfigDto | Unset):
    """

    environment: DominoEnvironmentsApiEnvironmentRevisionSummary
    hardware_tier: DominoWorkspaceApiWorkspaceHardwareTierDto
    tools: list[str]
    capacity_type: DominoWorkspaceApiWorkspaceConfigDtoCapacityType | Unset = UNSET
    cluster_props: DominoComputeclusterApiSparkClusterPropsDto | Unset = UNSET
    compute_cluster_response_props: DominoComputeclusterApiComputeClusterConfigResponseDto | Unset = UNSET
    ssh: DominoWorkspaceApiSshConfigDto | Unset = UNSET
    data_plane: DominoWorkspaceApiDataPlaneDto | Unset = UNSET
    persistence: DominoWorkspaceApiWorkspacePersistenceConfigDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        environment = self.environment.to_dict()

        hardware_tier = self.hardware_tier.to_dict()

        tools = self.tools

        capacity_type: str | Unset = UNSET
        if not isinstance(self.capacity_type, Unset):
            capacity_type = self.capacity_type.value

        cluster_props: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cluster_props, Unset):
            cluster_props = self.cluster_props.to_dict()

        compute_cluster_response_props: dict[str, Any] | Unset = UNSET
        if not isinstance(self.compute_cluster_response_props, Unset):
            compute_cluster_response_props = self.compute_cluster_response_props.to_dict()

        ssh: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ssh, Unset):
            ssh = self.ssh.to_dict()

        data_plane: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_plane, Unset):
            data_plane = self.data_plane.to_dict()

        persistence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.persistence, Unset):
            persistence = self.persistence.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "environment": environment,
                "hardwareTier": hardware_tier,
                "tools": tools,
            }
        )
        if capacity_type is not UNSET:
            field_dict["capacityType"] = capacity_type
        if cluster_props is not UNSET:
            field_dict["clusterProps"] = cluster_props
        if compute_cluster_response_props is not UNSET:
            field_dict["computeClusterResponseProps"] = compute_cluster_response_props
        if ssh is not UNSET:
            field_dict["ssh"] = ssh
        if data_plane is not UNSET:
            field_dict["dataPlane"] = data_plane
        if persistence is not UNSET:
            field_dict["persistence"] = persistence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_computecluster_api_compute_cluster_config_response_dto import (
            DominoComputeclusterApiComputeClusterConfigResponseDto,
        )
        from ..models.domino_computecluster_api_spark_cluster_props_dto import (
            DominoComputeclusterApiSparkClusterPropsDto,
        )
        from ..models.domino_environments_api_environment_revision_summary import (
            DominoEnvironmentsApiEnvironmentRevisionSummary,
        )
        from ..models.domino_workspace_api_data_plane_dto import DominoWorkspaceApiDataPlaneDto
        from ..models.domino_workspace_api_ssh_config_dto import DominoWorkspaceApiSshConfigDto
        from ..models.domino_workspace_api_workspace_hardware_tier_dto import DominoWorkspaceApiWorkspaceHardwareTierDto
        from ..models.domino_workspace_api_workspace_persistence_config_dto import (
            DominoWorkspaceApiWorkspacePersistenceConfigDto,
        )

        d = dict(src_dict)
        environment = DominoEnvironmentsApiEnvironmentRevisionSummary.from_dict(d.pop("environment"))

        hardware_tier = DominoWorkspaceApiWorkspaceHardwareTierDto.from_dict(d.pop("hardwareTier"))

        tools = cast(list[str], d.pop("tools"))

        _capacity_type = d.pop("capacityType", UNSET)
        capacity_type: DominoWorkspaceApiWorkspaceConfigDtoCapacityType | Unset
        if isinstance(_capacity_type, Unset):
            capacity_type = UNSET
        else:
            capacity_type = DominoWorkspaceApiWorkspaceConfigDtoCapacityType(_capacity_type)

        _cluster_props = d.pop("clusterProps", UNSET)
        cluster_props: DominoComputeclusterApiSparkClusterPropsDto | Unset
        if isinstance(_cluster_props, Unset):
            cluster_props = UNSET
        else:
            cluster_props = DominoComputeclusterApiSparkClusterPropsDto.from_dict(_cluster_props)

        _compute_cluster_response_props = d.pop("computeClusterResponseProps", UNSET)
        compute_cluster_response_props: DominoComputeclusterApiComputeClusterConfigResponseDto | Unset
        if isinstance(_compute_cluster_response_props, Unset):
            compute_cluster_response_props = UNSET
        else:
            compute_cluster_response_props = DominoComputeclusterApiComputeClusterConfigResponseDto.from_dict(
                _compute_cluster_response_props
            )

        _ssh = d.pop("ssh", UNSET)
        ssh: DominoWorkspaceApiSshConfigDto | Unset
        if isinstance(_ssh, Unset):
            ssh = UNSET
        else:
            ssh = DominoWorkspaceApiSshConfigDto.from_dict(_ssh)

        _data_plane = d.pop("dataPlane", UNSET)
        data_plane: DominoWorkspaceApiDataPlaneDto | Unset
        if isinstance(_data_plane, Unset):
            data_plane = UNSET
        else:
            data_plane = DominoWorkspaceApiDataPlaneDto.from_dict(_data_plane)

        _persistence = d.pop("persistence", UNSET)
        persistence: DominoWorkspaceApiWorkspacePersistenceConfigDto | Unset
        if isinstance(_persistence, Unset):
            persistence = UNSET
        else:
            persistence = DominoWorkspaceApiWorkspacePersistenceConfigDto.from_dict(_persistence)

        domino_workspace_api_workspace_config_dto = cls(
            environment=environment,
            hardware_tier=hardware_tier,
            tools=tools,
            capacity_type=capacity_type,
            cluster_props=cluster_props,
            compute_cluster_response_props=compute_cluster_response_props,
            ssh=ssh,
            data_plane=data_plane,
            persistence=persistence,
        )

        domino_workspace_api_workspace_config_dto.additional_properties = d
        return domino_workspace_api_workspace_config_dto

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
