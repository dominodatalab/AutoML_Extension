from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_workspace_web_reproduce_workspace_request_workspace_reproduction_type import (
    DominoWorkspaceWebReproduceWorkspaceRequestWorkspaceReproductionType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_hardwaretier_api_hardware_tier_identifier import DominoHardwaretierApiHardwareTierIdentifier
    from ..models.domino_workspace_api_ssh_config_dto import DominoWorkspaceApiSshConfigDto
    from ..models.domino_workspace_api_workspace_persistence_config_dto import (
        DominoWorkspaceApiWorkspacePersistenceConfigDto,
    )


T = TypeVar("T", bound="DominoWorkspaceWebReproduceWorkspaceRequest")


@_attrs_define
class DominoWorkspaceWebReproduceWorkspaceRequest:
    """
    Attributes:
        name (str):
        provenance_checkpoint_id (str):
        hardware_tier_id (DominoHardwaretierApiHardwareTierIdentifier):
        branch_name (str):
        workspace_reproduction_type (DominoWorkspaceWebReproduceWorkspaceRequestWorkspaceReproductionType):
        ssh (DominoWorkspaceApiSshConfigDto | Unset):
        persistence (DominoWorkspaceApiWorkspacePersistenceConfigDto | Unset):
    """

    name: str
    provenance_checkpoint_id: str
    hardware_tier_id: DominoHardwaretierApiHardwareTierIdentifier
    branch_name: str
    workspace_reproduction_type: DominoWorkspaceWebReproduceWorkspaceRequestWorkspaceReproductionType
    ssh: DominoWorkspaceApiSshConfigDto | Unset = UNSET
    persistence: DominoWorkspaceApiWorkspacePersistenceConfigDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        provenance_checkpoint_id = self.provenance_checkpoint_id

        hardware_tier_id = self.hardware_tier_id.to_dict()

        branch_name = self.branch_name

        workspace_reproduction_type = self.workspace_reproduction_type.value

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
                "provenanceCheckpointId": provenance_checkpoint_id,
                "hardwareTierId": hardware_tier_id,
                "branchName": branch_name,
                "workspaceReproductionType": workspace_reproduction_type,
            }
        )
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
        from ..models.domino_workspace_api_ssh_config_dto import DominoWorkspaceApiSshConfigDto
        from ..models.domino_workspace_api_workspace_persistence_config_dto import (
            DominoWorkspaceApiWorkspacePersistenceConfigDto,
        )

        d = dict(src_dict)
        name = d.pop("name")

        provenance_checkpoint_id = d.pop("provenanceCheckpointId")

        hardware_tier_id = DominoHardwaretierApiHardwareTierIdentifier.from_dict(d.pop("hardwareTierId"))

        branch_name = d.pop("branchName")

        workspace_reproduction_type = DominoWorkspaceWebReproduceWorkspaceRequestWorkspaceReproductionType(
            d.pop("workspaceReproductionType")
        )

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

        domino_workspace_web_reproduce_workspace_request = cls(
            name=name,
            provenance_checkpoint_id=provenance_checkpoint_id,
            hardware_tier_id=hardware_tier_id,
            branch_name=branch_name,
            workspace_reproduction_type=workspace_reproduction_type,
            ssh=ssh,
            persistence=persistence,
        )

        domino_workspace_web_reproduce_workspace_request.additional_properties = d
        return domino_workspace_web_reproduce_workspace_request

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
