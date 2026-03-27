from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_workspace_api_restartable_workspace_change_event import (
        DominoWorkspaceApiRestartableWorkspaceChangeEvent,
    )


T = TypeVar("T", bound="DominoWorkspaceWebWorkspaceEvents")


@_attrs_define
class DominoWorkspaceWebWorkspaceEvents:
    """
    Attributes:
        change_event (DominoWorkspaceApiRestartableWorkspaceChangeEvent):
    """

    change_event: DominoWorkspaceApiRestartableWorkspaceChangeEvent
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        change_event = self.change_event.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "changeEvent": change_event,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_workspace_api_restartable_workspace_change_event import (
            DominoWorkspaceApiRestartableWorkspaceChangeEvent,
        )

        d = dict(src_dict)
        change_event = DominoWorkspaceApiRestartableWorkspaceChangeEvent.from_dict(d.pop("changeEvent"))

        domino_workspace_web_workspace_events = cls(
            change_event=change_event,
        )

        domino_workspace_web_workspace_events.additional_properties = d
        return domino_workspace_web_workspace_events

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
