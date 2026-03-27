from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_workspace_api_workspace_admin_page_table_row import (
        DominoWorkspaceApiWorkspaceAdminPageTableRow,
    )


T = TypeVar("T", bound="DominoWorkspaceApiWorkspaceAdminPageDataDto")


@_attrs_define
class DominoWorkspaceApiWorkspaceAdminPageDataDto:
    """
    Attributes:
        offset (int):
        limit (int):
        total_entries (int):
        table_rows (list[DominoWorkspaceApiWorkspaceAdminPageTableRow]):
    """

    offset: int
    limit: int
    total_entries: int
    table_rows: list[DominoWorkspaceApiWorkspaceAdminPageTableRow]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offset = self.offset

        limit = self.limit

        total_entries = self.total_entries

        table_rows = []
        for table_rows_item_data in self.table_rows:
            table_rows_item = table_rows_item_data.to_dict()
            table_rows.append(table_rows_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "offset": offset,
                "limit": limit,
                "totalEntries": total_entries,
                "tableRows": table_rows,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_workspace_api_workspace_admin_page_table_row import (
            DominoWorkspaceApiWorkspaceAdminPageTableRow,
        )

        d = dict(src_dict)
        offset = d.pop("offset")

        limit = d.pop("limit")

        total_entries = d.pop("totalEntries")

        table_rows = []
        _table_rows = d.pop("tableRows")
        for table_rows_item_data in _table_rows:
            table_rows_item = DominoWorkspaceApiWorkspaceAdminPageTableRow.from_dict(table_rows_item_data)

            table_rows.append(table_rows_item)

        domino_workspace_api_workspace_admin_page_data_dto = cls(
            offset=offset,
            limit=limit,
            total_entries=total_entries,
            table_rows=table_rows,
        )

        domino_workspace_api_workspace_admin_page_data_dto.additional_properties = d
        return domino_workspace_api_workspace_admin_page_data_dto

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
