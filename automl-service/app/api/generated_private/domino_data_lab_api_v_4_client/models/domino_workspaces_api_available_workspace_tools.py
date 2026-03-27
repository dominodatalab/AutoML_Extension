from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_workspaces_api_workspace_definition_dto import DominoWorkspacesApiWorkspaceDefinitionDto


T = TypeVar("T", bound="DominoWorkspacesApiAvailableWorkspaceTools")


@_attrs_define
class DominoWorkspacesApiAvailableWorkspaceTools:
    """
    Attributes:
        workspace_tools (list[DominoWorkspacesApiWorkspaceDefinitionDto]):
    """

    workspace_tools: list[DominoWorkspacesApiWorkspaceDefinitionDto]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workspace_tools = []
        for workspace_tools_item_data in self.workspace_tools:
            workspace_tools_item = workspace_tools_item_data.to_dict()
            workspace_tools.append(workspace_tools_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workspaceTools": workspace_tools,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_workspaces_api_workspace_definition_dto import DominoWorkspacesApiWorkspaceDefinitionDto

        d = dict(src_dict)
        workspace_tools = []
        _workspace_tools = d.pop("workspaceTools")
        for workspace_tools_item_data in _workspace_tools:
            workspace_tools_item = DominoWorkspacesApiWorkspaceDefinitionDto.from_dict(workspace_tools_item_data)

            workspace_tools.append(workspace_tools_item)

        domino_workspaces_api_available_workspace_tools = cls(
            workspace_tools=workspace_tools,
        )

        domino_workspaces_api_available_workspace_tools.additional_properties = d
        return domino_workspaces_api_available_workspace_tools

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
