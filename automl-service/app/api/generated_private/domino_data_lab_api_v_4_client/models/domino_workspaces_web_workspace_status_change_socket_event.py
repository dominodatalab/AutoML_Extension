from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoWorkspacesWebWorkspaceStatusChangeSocketEvent")


@_attrs_define
class DominoWorkspacesWebWorkspaceStatusChangeSocketEvent:
    """
    Attributes:
        correlation_id (str):
        workspace_id (str):
        project_id (str):
        room (str):
        status (str):
        timestamp (int):
        started_by (None | str | Unset):
    """

    correlation_id: str
    workspace_id: str
    project_id: str
    room: str
    status: str
    timestamp: int
    started_by: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        correlation_id = self.correlation_id

        workspace_id = self.workspace_id

        project_id = self.project_id

        room = self.room

        status = self.status

        timestamp = self.timestamp

        started_by: None | str | Unset
        if isinstance(self.started_by, Unset):
            started_by = UNSET
        else:
            started_by = self.started_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "correlationId": correlation_id,
                "workspaceId": workspace_id,
                "projectId": project_id,
                "room": room,
                "status": status,
                "timestamp": timestamp,
            }
        )
        if started_by is not UNSET:
            field_dict["startedBy"] = started_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        correlation_id = d.pop("correlationId")

        workspace_id = d.pop("workspaceId")

        project_id = d.pop("projectId")

        room = d.pop("room")

        status = d.pop("status")

        timestamp = d.pop("timestamp")

        def _parse_started_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        started_by = _parse_started_by(d.pop("startedBy", UNSET))

        domino_workspaces_web_workspace_status_change_socket_event = cls(
            correlation_id=correlation_id,
            workspace_id=workspace_id,
            project_id=project_id,
            room=room,
            status=status,
            timestamp=timestamp,
            started_by=started_by,
        )

        domino_workspaces_web_workspace_status_change_socket_event.additional_properties = d
        return domino_workspaces_web_workspace_status_change_socket_event

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
