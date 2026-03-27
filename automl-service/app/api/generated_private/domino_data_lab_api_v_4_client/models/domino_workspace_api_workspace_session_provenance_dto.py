from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_provenance_api_provenance_checkpoint_dto import DominoProvenanceApiProvenanceCheckpointDto


T = TypeVar("T", bound="DominoWorkspaceApiWorkspaceSessionProvenanceDto")


@_attrs_define
class DominoWorkspaceApiWorkspaceSessionProvenanceDto:
    """
    Attributes:
        workspace_session_id (str):
        provenance_checkpoints (list[DominoProvenanceApiProvenanceCheckpointDto]):
    """

    workspace_session_id: str
    provenance_checkpoints: list[DominoProvenanceApiProvenanceCheckpointDto]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workspace_session_id = self.workspace_session_id

        provenance_checkpoints = []
        for provenance_checkpoints_item_data in self.provenance_checkpoints:
            provenance_checkpoints_item = provenance_checkpoints_item_data.to_dict()
            provenance_checkpoints.append(provenance_checkpoints_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workspaceSessionId": workspace_session_id,
                "provenanceCheckpoints": provenance_checkpoints,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_provenance_api_provenance_checkpoint_dto import DominoProvenanceApiProvenanceCheckpointDto

        d = dict(src_dict)
        workspace_session_id = d.pop("workspaceSessionId")

        provenance_checkpoints = []
        _provenance_checkpoints = d.pop("provenanceCheckpoints")
        for provenance_checkpoints_item_data in _provenance_checkpoints:
            provenance_checkpoints_item = DominoProvenanceApiProvenanceCheckpointDto.from_dict(
                provenance_checkpoints_item_data
            )

            provenance_checkpoints.append(provenance_checkpoints_item)

        domino_workspace_api_workspace_session_provenance_dto = cls(
            workspace_session_id=workspace_session_id,
            provenance_checkpoints=provenance_checkpoints,
        )

        domino_workspace_api_workspace_session_provenance_dto.additional_properties = d
        return domino_workspace_api_workspace_session_provenance_dto

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
