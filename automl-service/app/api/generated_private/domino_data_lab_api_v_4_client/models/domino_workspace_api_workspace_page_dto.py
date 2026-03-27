from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_workspace_api_workspace_dto import DominoWorkspaceApiWorkspaceDto


T = TypeVar("T", bound="DominoWorkspaceApiWorkspacePageDto")


@_attrs_define
class DominoWorkspaceApiWorkspacePageDto:
    """
    Attributes:
        workspaces (list[DominoWorkspaceApiWorkspaceDto]):
        total_workspace_count (int):
        offset (int):
        limit (int):
    """

    workspaces: list[DominoWorkspaceApiWorkspaceDto]
    total_workspace_count: int
    offset: int
    limit: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workspaces = []
        for workspaces_item_data in self.workspaces:
            workspaces_item = workspaces_item_data.to_dict()
            workspaces.append(workspaces_item)

        total_workspace_count = self.total_workspace_count

        offset = self.offset

        limit = self.limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workspaces": workspaces,
                "totalWorkspaceCount": total_workspace_count,
                "offset": offset,
                "limit": limit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_workspace_api_workspace_dto import DominoWorkspaceApiWorkspaceDto

        d = dict(src_dict)
        workspaces = []
        _workspaces = d.pop("workspaces")
        for workspaces_item_data in _workspaces:
            workspaces_item = DominoWorkspaceApiWorkspaceDto.from_dict(workspaces_item_data)

            workspaces.append(workspaces_item)

        total_workspace_count = d.pop("totalWorkspaceCount")

        offset = d.pop("offset")

        limit = d.pop("limit")

        domino_workspace_api_workspace_page_dto = cls(
            workspaces=workspaces,
            total_workspace_count=total_workspace_count,
            offset=offset,
            limit=limit,
        )

        domino_workspace_api_workspace_page_dto.additional_properties = d
        return domino_workspace_api_workspace_page_dto

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
