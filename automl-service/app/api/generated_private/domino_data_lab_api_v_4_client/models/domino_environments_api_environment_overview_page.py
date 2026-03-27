from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_environments_api_environment_overview import DominoEnvironmentsApiEnvironmentOverview


T = TypeVar("T", bound="DominoEnvironmentsApiEnvironmentOverviewPage")


@_attrs_define
class DominoEnvironmentsApiEnvironmentOverviewPage:
    """
    Attributes:
        items (list[DominoEnvironmentsApiEnvironmentOverview]):
        total_items (int):
        offset (int):
        limit (int):
    """

    items: list[DominoEnvironmentsApiEnvironmentOverview]
    total_items: int
    offset: int
    limit: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        total_items = self.total_items

        offset = self.offset

        limit = self.limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
                "totalItems": total_items,
                "offset": offset,
                "limit": limit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_environments_api_environment_overview import DominoEnvironmentsApiEnvironmentOverview

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = DominoEnvironmentsApiEnvironmentOverview.from_dict(items_item_data)

            items.append(items_item)

        total_items = d.pop("totalItems")

        offset = d.pop("offset")

        limit = d.pop("limit")

        domino_environments_api_environment_overview_page = cls(
            items=items,
            total_items=total_items,
            offset=offset,
            limit=limit,
        )

        domino_environments_api_environment_overview_page.additional_properties = d
        return domino_environments_api_environment_overview_page

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
