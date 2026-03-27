from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoWorkspaceApiWorkspaceExecutionInfoDto")


@_attrs_define
class DominoWorkspaceApiWorkspaceExecutionInfoDto:
    """
    Attributes:
        execution_id (str):
        is_restartable (bool):
        workspace_id (None | str | Unset):
        workspace_session_id (None | str | Unset):
    """

    execution_id: str
    is_restartable: bool
    workspace_id: None | str | Unset = UNSET
    workspace_session_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        execution_id = self.execution_id

        is_restartable = self.is_restartable

        workspace_id: None | str | Unset
        if isinstance(self.workspace_id, Unset):
            workspace_id = UNSET
        else:
            workspace_id = self.workspace_id

        workspace_session_id: None | str | Unset
        if isinstance(self.workspace_session_id, Unset):
            workspace_session_id = UNSET
        else:
            workspace_session_id = self.workspace_session_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "executionId": execution_id,
                "isRestartable": is_restartable,
            }
        )
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id
        if workspace_session_id is not UNSET:
            field_dict["workspaceSessionId"] = workspace_session_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        execution_id = d.pop("executionId")

        is_restartable = d.pop("isRestartable")

        def _parse_workspace_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        workspace_id = _parse_workspace_id(d.pop("workspaceId", UNSET))

        def _parse_workspace_session_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        workspace_session_id = _parse_workspace_session_id(d.pop("workspaceSessionId", UNSET))

        domino_workspace_api_workspace_execution_info_dto = cls(
            execution_id=execution_id,
            is_restartable=is_restartable,
            workspace_id=workspace_id,
            workspace_session_id=workspace_session_id,
        )

        domino_workspace_api_workspace_execution_info_dto.additional_properties = d
        return domino_workspace_api_workspace_execution_info_dto

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
