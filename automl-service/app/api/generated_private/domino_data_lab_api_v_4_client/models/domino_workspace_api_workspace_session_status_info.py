from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="DominoWorkspaceApiWorkspaceSessionStatusInfo")


@_attrs_define
class DominoWorkspaceApiWorkspaceSessionStatusInfo:
    """
    Attributes:
        raw_execution_display_status (str):
        raw_execution_display_status_updated_at (datetime.datetime):
        is_loading (bool):
        is_running (bool):
        is_stoppable (bool):
        is_completing (bool):
        is_failed (bool):
        is_successful (bool):
        is_completed (bool):
    """

    raw_execution_display_status: str
    raw_execution_display_status_updated_at: datetime.datetime
    is_loading: bool
    is_running: bool
    is_stoppable: bool
    is_completing: bool
    is_failed: bool
    is_successful: bool
    is_completed: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        raw_execution_display_status = self.raw_execution_display_status

        raw_execution_display_status_updated_at = self.raw_execution_display_status_updated_at.isoformat()

        is_loading = self.is_loading

        is_running = self.is_running

        is_stoppable = self.is_stoppable

        is_completing = self.is_completing

        is_failed = self.is_failed

        is_successful = self.is_successful

        is_completed = self.is_completed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rawExecutionDisplayStatus": raw_execution_display_status,
                "rawExecutionDisplayStatusUpdatedAt": raw_execution_display_status_updated_at,
                "isLoading": is_loading,
                "isRunning": is_running,
                "isStoppable": is_stoppable,
                "isCompleting": is_completing,
                "isFailed": is_failed,
                "isSuccessful": is_successful,
                "isCompleted": is_completed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        raw_execution_display_status = d.pop("rawExecutionDisplayStatus")

        raw_execution_display_status_updated_at = isoparse(d.pop("rawExecutionDisplayStatusUpdatedAt"))

        is_loading = d.pop("isLoading")

        is_running = d.pop("isRunning")

        is_stoppable = d.pop("isStoppable")

        is_completing = d.pop("isCompleting")

        is_failed = d.pop("isFailed")

        is_successful = d.pop("isSuccessful")

        is_completed = d.pop("isCompleted")

        domino_workspace_api_workspace_session_status_info = cls(
            raw_execution_display_status=raw_execution_display_status,
            raw_execution_display_status_updated_at=raw_execution_display_status_updated_at,
            is_loading=is_loading,
            is_running=is_running,
            is_stoppable=is_stoppable,
            is_completing=is_completing,
            is_failed=is_failed,
            is_successful=is_successful,
            is_completed=is_completed,
        )

        domino_workspace_api_workspace_session_status_info.additional_properties = d
        return domino_workspace_api_workspace_session_status_info

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
