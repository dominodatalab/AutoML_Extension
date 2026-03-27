from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_modelmanager_api_model_export import DominoModelmanagerApiModelExport


T = TypeVar("T", bound="DominoModelmanagerApiResponsesModelExportsApiResponse")


@_attrs_define
class DominoModelmanagerApiResponsesModelExportsApiResponse:
    """
    Attributes:
        current_item_count (int):
        items_per_page (int):
        start_index (int):
        total_items (int):
        items (list[DominoModelmanagerApiModelExport]):
    """

    current_item_count: int
    items_per_page: int
    start_index: int
    total_items: int
    items: list[DominoModelmanagerApiModelExport]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_item_count = self.current_item_count

        items_per_page = self.items_per_page

        start_index = self.start_index

        total_items = self.total_items

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currentItemCount": current_item_count,
                "itemsPerPage": items_per_page,
                "startIndex": start_index,
                "totalItems": total_items,
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_modelmanager_api_model_export import DominoModelmanagerApiModelExport

        d = dict(src_dict)
        current_item_count = d.pop("currentItemCount")

        items_per_page = d.pop("itemsPerPage")

        start_index = d.pop("startIndex")

        total_items = d.pop("totalItems")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = DominoModelmanagerApiModelExport.from_dict(items_item_data)

            items.append(items_item)

        domino_modelmanager_api_responses_model_exports_api_response = cls(
            current_item_count=current_item_count,
            items_per_page=items_per_page,
            start_index=start_index,
            total_items=total_items,
            items=items,
        )

        domino_modelmanager_api_responses_model_exports_api_response.additional_properties = d
        return domino_modelmanager_api_responses_model_exports_api_response

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
