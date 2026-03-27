from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoCommonGatewaySearchEntityHighlight")


@_attrs_define
class DominoCommonGatewaySearchEntityHighlight:
    """
    Attributes:
        entity_name (str):
        highlighted_entity_name (str):
    """

    entity_name: str
    highlighted_entity_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entity_name = self.entity_name

        highlighted_entity_name = self.highlighted_entity_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entityName": entity_name,
                "highlightedEntityName": highlighted_entity_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entity_name = d.pop("entityName")

        highlighted_entity_name = d.pop("highlightedEntityName")

        domino_common_gateway_search_entity_highlight = cls(
            entity_name=entity_name,
            highlighted_entity_name=highlighted_entity_name,
        )

        domino_common_gateway_search_entity_highlight.additional_properties = d
        return domino_common_gateway_search_entity_highlight

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
