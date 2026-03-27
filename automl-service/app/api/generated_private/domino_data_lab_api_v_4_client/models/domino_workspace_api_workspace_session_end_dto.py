from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_workspace_api_workspace_session_end_dto_exit_status import (
    DominoWorkspaceApiWorkspaceSessionEndDtoExitStatus,
)

T = TypeVar("T", bound="DominoWorkspaceApiWorkspaceSessionEndDto")


@_attrs_define
class DominoWorkspaceApiWorkspaceSessionEndDto:
    """
    Attributes:
        time (int):
        exit_status (DominoWorkspaceApiWorkspaceSessionEndDtoExitStatus):
        repo_dirty (bool):
    """

    time: int
    exit_status: DominoWorkspaceApiWorkspaceSessionEndDtoExitStatus
    repo_dirty: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        exit_status = self.exit_status.value

        repo_dirty = self.repo_dirty

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "time": time,
                "exitStatus": exit_status,
                "repoDirty": repo_dirty,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        time = d.pop("time")

        exit_status = DominoWorkspaceApiWorkspaceSessionEndDtoExitStatus(d.pop("exitStatus"))

        repo_dirty = d.pop("repoDirty")

        domino_workspace_api_workspace_session_end_dto = cls(
            time=time,
            exit_status=exit_status,
            repo_dirty=repo_dirty,
        )

        domino_workspace_api_workspace_session_end_dto.additional_properties = d
        return domino_workspace_api_workspace_session_end_dto

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
