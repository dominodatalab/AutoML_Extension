from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_workspaces_api_execution_checkpoint_status_checkpoint import (
    DominoWorkspacesApiExecutionCheckpointStatusCheckpoint,
)
from ..models.domino_workspaces_api_execution_checkpoint_status_status import (
    DominoWorkspacesApiExecutionCheckpointStatusStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoWorkspacesApiExecutionCheckpointStatus")


@_attrs_define
class DominoWorkspacesApiExecutionCheckpointStatus:
    """
    Attributes:
        checkpoint (DominoWorkspacesApiExecutionCheckpointStatusCheckpoint):
        status (DominoWorkspacesApiExecutionCheckpointStatusStatus):
        message (None | str | Unset):
    """

    checkpoint: DominoWorkspacesApiExecutionCheckpointStatusCheckpoint
    status: DominoWorkspacesApiExecutionCheckpointStatusStatus
    message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        checkpoint = self.checkpoint.value

        status = self.status.value

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "checkpoint": checkpoint,
                "status": status,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        checkpoint = DominoWorkspacesApiExecutionCheckpointStatusCheckpoint(d.pop("checkpoint"))

        status = DominoWorkspacesApiExecutionCheckpointStatusStatus(d.pop("status"))

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        domino_workspaces_api_execution_checkpoint_status = cls(
            checkpoint=checkpoint,
            status=status,
            message=message,
        )

        domino_workspaces_api_execution_checkpoint_status.additional_properties = d
        return domino_workspaces_api_execution_checkpoint_status

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
