from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.domino_workspace_api_workspace_dto import DominoWorkspaceApiWorkspaceDto


T = TypeVar("T", bound="DominoWorkspaceApiRestartableWorkspaceChangeEvent")


@_attrs_define
class DominoWorkspaceApiRestartableWorkspaceChangeEvent:
    """
    Attributes:
        correlation_id (str):
        room (str):
        timestamp (datetime.datetime):
        workspace (DominoWorkspaceApiWorkspaceDto):
    """

    correlation_id: str
    room: str
    timestamp: datetime.datetime
    workspace: DominoWorkspaceApiWorkspaceDto
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        correlation_id = self.correlation_id

        room = self.room

        timestamp = self.timestamp.isoformat()

        workspace = self.workspace.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "correlationId": correlation_id,
                "room": room,
                "timestamp": timestamp,
                "workspace": workspace,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_workspace_api_workspace_dto import DominoWorkspaceApiWorkspaceDto

        d = dict(src_dict)
        correlation_id = d.pop("correlationId")

        room = d.pop("room")

        timestamp = isoparse(d.pop("timestamp"))

        workspace = DominoWorkspaceApiWorkspaceDto.from_dict(d.pop("workspace"))

        domino_workspace_api_restartable_workspace_change_event = cls(
            correlation_id=correlation_id,
            room=room,
            timestamp=timestamp,
            workspace=workspace,
        )

        domino_workspace_api_restartable_workspace_change_event.additional_properties = d
        return domino_workspace_api_restartable_workspace_change_event

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
