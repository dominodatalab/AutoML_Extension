from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_workspace_web_update_workspace_request_capacity_type import (
    DominoWorkspaceWebUpdateWorkspaceRequestCapacityType,
)
from ..models.domino_workspace_web_update_workspace_request_environment_revision_spec_type_0 import (
    DominoWorkspaceWebUpdateWorkspaceRequestEnvironmentRevisionSpecType0,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_hardwaretier_api_hardware_tier_identifier import DominoHardwaretierApiHardwareTierIdentifier
    from ..models.domino_workspace_api_compute_cluster_config_dto import DominoWorkspaceApiComputeClusterConfigDto
    from ..models.domino_workspace_api_ssh_config_dto import DominoWorkspaceApiSshConfigDto
    from ..models.domino_workspace_api_workspace_cluster_config_dto import DominoWorkspaceApiWorkspaceClusterConfigDto
    from ..models.domino_workspace_api_workspace_persistence_config_dto import (
        DominoWorkspaceApiWorkspacePersistenceConfigDto,
    )
    from ..models.domino_workspace_web_update_workspace_request_environment_revision_spec_type_1 import (
        DominoWorkspaceWebUpdateWorkspaceRequestEnvironmentRevisionSpecType1,
    )


T = TypeVar("T", bound="DominoWorkspaceWebUpdateWorkspaceRequest")


@_attrs_define
class DominoWorkspaceWebUpdateWorkspaceRequest:
    """
    Attributes:
        name (str):
        environment_id (str):
        hardware_tier_id (DominoHardwaretierApiHardwareTierIdentifier):
        tools (list[str]):
        environment_revision_spec (DominoWorkspaceWebUpdateWorkspaceRequestEnvironmentRevisionSpecType0 |
            DominoWorkspaceWebUpdateWorkspaceRequestEnvironmentRevisionSpecType1 | None | Unset):
        capacity_type (DominoWorkspaceWebUpdateWorkspaceRequestCapacityType | Unset):
        cluster_config (DominoWorkspaceApiWorkspaceClusterConfigDto | Unset):
        compute_cluster_config (DominoWorkspaceApiComputeClusterConfigDto | Unset):
        ssh (DominoWorkspaceApiSshConfigDto | Unset):
        persistence (DominoWorkspaceApiWorkspacePersistenceConfigDto | Unset):
    """

    name: str
    environment_id: str
    hardware_tier_id: DominoHardwaretierApiHardwareTierIdentifier
    tools: list[str]
    environment_revision_spec: (
        DominoWorkspaceWebUpdateWorkspaceRequestEnvironmentRevisionSpecType0
        | DominoWorkspaceWebUpdateWorkspaceRequestEnvironmentRevisionSpecType1
        | None
        | Unset
    ) = UNSET
    capacity_type: DominoWorkspaceWebUpdateWorkspaceRequestCapacityType | Unset = UNSET
    cluster_config: DominoWorkspaceApiWorkspaceClusterConfigDto | Unset = UNSET
    compute_cluster_config: DominoWorkspaceApiComputeClusterConfigDto | Unset = UNSET
    ssh: DominoWorkspaceApiSshConfigDto | Unset = UNSET
    persistence: DominoWorkspaceApiWorkspacePersistenceConfigDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.domino_workspace_web_update_workspace_request_environment_revision_spec_type_1 import (
            DominoWorkspaceWebUpdateWorkspaceRequestEnvironmentRevisionSpecType1,
        )

        name = self.name

        environment_id = self.environment_id

        hardware_tier_id = self.hardware_tier_id.to_dict()

        tools = self.tools

        environment_revision_spec: dict[str, Any] | None | str | Unset
        if isinstance(self.environment_revision_spec, Unset):
            environment_revision_spec = UNSET
        elif isinstance(
            self.environment_revision_spec, DominoWorkspaceWebUpdateWorkspaceRequestEnvironmentRevisionSpecType0
        ):
            environment_revision_spec = self.environment_revision_spec.value
        elif isinstance(
            self.environment_revision_spec, DominoWorkspaceWebUpdateWorkspaceRequestEnvironmentRevisionSpecType1
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
        from ..models.domino_workspace_api_compute_cluster_config_dto import DominoWorkspaceApiComputeClusterConfigDto
        from ..models.domino_workspace_api_ssh_config_dto import DominoWorkspaceApiSshConfigDto
        from ..models.domino_workspace_api_workspace_cluster_config_dto import (
            DominoWorkspaceApiWorkspaceClusterConfigDto,
        )
        from ..models.domino_workspace_api_workspace_persistence_config_dto import (
            DominoWorkspaceApiWorkspacePersistenceConfigDto,
        )
        from ..models.domino_workspace_web_update_workspace_request_environment_revision_spec_type_1 import (
            DominoWorkspaceWebUpdateWorkspaceRequestEnvironmentRevisionSpecType1,
        )

        d = dict(src_dict)
        name = d.pop("name")

        environment_id = d.pop("environmentId")

        hardware_tier_id = DominoHardwaretierApiHardwareTierIdentifier.from_dict(d.pop("hardwareTierId"))

        tools = cast(list[str], d.pop("tools"))

        def _parse_environment_revision_spec(
            data: object,
        ) -> (
            DominoWorkspaceWebUpdateWorkspaceRequestEnvironmentRevisionSpecType0
            | DominoWorkspaceWebUpdateWorkspaceRequestEnvironmentRevisionSpecType1
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
                environment_revision_spec_type_0 = DominoWorkspaceWebUpdateWorkspaceRequestEnvironmentRevisionSpecType0(
                    data
                )

                return environment_revision_spec_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                environment_revision_spec_type_1 = (
                    DominoWorkspaceWebUpdateWorkspaceRequestEnvironmentRevisionSpecType1.from_dict(data)
                )

                return environment_revision_spec_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                DominoWorkspaceWebUpdateWorkspaceRequestEnvironmentRevisionSpecType0
                | DominoWorkspaceWebUpdateWorkspaceRequestEnvironmentRevisionSpecType1
                | None
                | Unset,
                data,
            )

        environment_revision_spec = _parse_environment_revision_spec(d.pop("environmentRevisionSpec", UNSET))

        _capacity_type = d.pop("capacityType", UNSET)
        capacity_type: DominoWorkspaceWebUpdateWorkspaceRequestCapacityType | Unset
        if isinstance(_capacity_type, Unset):
            capacity_type = UNSET
        else:
            capacity_type = DominoWorkspaceWebUpdateWorkspaceRequestCapacityType(_capacity_type)

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

        domino_workspace_web_update_workspace_request = cls(
            name=name,
            environment_id=environment_id,
            hardware_tier_id=hardware_tier_id,
            tools=tools,
            environment_revision_spec=environment_revision_spec,
            capacity_type=capacity_type,
            cluster_config=cluster_config,
            compute_cluster_config=compute_cluster_config,
            ssh=ssh,
            persistence=persistence,
        )

        domino_workspace_web_update_workspace_request.additional_properties = d
        return domino_workspace_web_update_workspace_request

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
