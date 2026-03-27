from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_workspaces_web_workspace_status_change_socket_event import (
        DominoWorkspacesWebWorkspaceStatusChangeSocketEvent,
    )
    from ..models.domino_workspaces_web_workspaces_usage_socket_event import (
        DominoWorkspacesWebWorkspacesUsageSocketEvent,
    )


T = TypeVar("T", bound="DominoWorkspacesWebWorkspaceEvents")


@_attrs_define
class DominoWorkspacesWebWorkspaceEvents:
    """
    Attributes:
        workspaces_usage (DominoWorkspacesWebWorkspacesUsageSocketEvent):
        workspace_status_change_event (DominoWorkspacesWebWorkspaceStatusChangeSocketEvent):
    """

    workspaces_usage: DominoWorkspacesWebWorkspacesUsageSocketEvent
    workspace_status_change_event: DominoWorkspacesWebWorkspaceStatusChangeSocketEvent
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workspaces_usage = self.workspaces_usage.to_dict()

        workspace_status_change_event = self.workspace_status_change_event.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workspacesUsage": workspaces_usage,
                "workspaceStatusChangeEvent": workspace_status_change_event,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_workspaces_web_workspace_status_change_socket_event import (
            DominoWorkspacesWebWorkspaceStatusChangeSocketEvent,
        )
        from ..models.domino_workspaces_web_workspaces_usage_socket_event import (
            DominoWorkspacesWebWorkspacesUsageSocketEvent,
        )

        d = dict(src_dict)
        workspaces_usage = DominoWorkspacesWebWorkspacesUsageSocketEvent.from_dict(d.pop("workspacesUsage"))

        workspace_status_change_event = DominoWorkspacesWebWorkspaceStatusChangeSocketEvent.from_dict(
            d.pop("workspaceStatusChangeEvent")
        )

        domino_workspaces_web_workspace_events = cls(
            workspaces_usage=workspaces_usage,
            workspace_status_change_event=workspace_status_change_event,
        )

        domino_workspaces_web_workspace_events.additional_properties = d
        return domino_workspaces_web_workspace_events

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
