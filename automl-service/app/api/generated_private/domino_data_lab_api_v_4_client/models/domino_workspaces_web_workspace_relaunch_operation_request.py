from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoWorkspacesWebWorkspaceRelaunchOperationRequest")


@_attrs_define
class DominoWorkspacesWebWorkspaceRelaunchOperationRequest:
    """
    Attributes:
        project_id (str):
        workspace_id (str):
        use_original_input_commit (bool):
    """

    project_id: str
    workspace_id: str
    use_original_input_commit: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        workspace_id = self.workspace_id

        use_original_input_commit = self.use_original_input_commit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectId": project_id,
                "workspaceId": workspace_id,
                "useOriginalInputCommit": use_original_input_commit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = d.pop("projectId")

        workspace_id = d.pop("workspaceId")

        use_original_input_commit = d.pop("useOriginalInputCommit")

        domino_workspaces_web_workspace_relaunch_operation_request = cls(
            project_id=project_id,
            workspace_id=workspace_id,
            use_original_input_commit=use_original_input_commit,
        )

        domino_workspaces_web_workspace_relaunch_operation_request.additional_properties = d
        return domino_workspaces_web_workspace_relaunch_operation_request

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
