from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoEnvironmentsApiDominoCompatibleTools")


@_attrs_define
class DominoEnvironmentsApiDominoCompatibleTools:
    """
    Attributes:
        workspace_tools (None | str | Unset):
        dockerfile_instructions (None | str | Unset):
    """

    workspace_tools: None | str | Unset = UNSET
    dockerfile_instructions: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workspace_tools: None | str | Unset
        if isinstance(self.workspace_tools, Unset):
            workspace_tools = UNSET
        else:
            workspace_tools = self.workspace_tools

        dockerfile_instructions: None | str | Unset
        if isinstance(self.dockerfile_instructions, Unset):
            dockerfile_instructions = UNSET
        else:
            dockerfile_instructions = self.dockerfile_instructions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if workspace_tools is not UNSET:
            field_dict["workspaceTools"] = workspace_tools
        if dockerfile_instructions is not UNSET:
            field_dict["dockerfileInstructions"] = dockerfile_instructions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_workspace_tools(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        workspace_tools = _parse_workspace_tools(d.pop("workspaceTools", UNSET))

        def _parse_dockerfile_instructions(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dockerfile_instructions = _parse_dockerfile_instructions(d.pop("dockerfileInstructions", UNSET))

        domino_environments_api_domino_compatible_tools = cls(
            workspace_tools=workspace_tools,
            dockerfile_instructions=dockerfile_instructions,
        )

        domino_environments_api_domino_compatible_tools.additional_properties = d
        return domino_environments_api_domino_compatible_tools

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
