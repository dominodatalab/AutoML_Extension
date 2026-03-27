from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoCommonGatewaySearchTagValueHighlight")


@_attrs_define
class DominoCommonGatewaySearchTagValueHighlight:
    """
    Attributes:
        tag_value (str):
        highlighted_tag_value (str):
    """

    tag_value: str
    highlighted_tag_value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tag_value = self.tag_value

        highlighted_tag_value = self.highlighted_tag_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tagValue": tag_value,
                "highlightedTagValue": highlighted_tag_value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tag_value = d.pop("tagValue")

        highlighted_tag_value = d.pop("highlightedTagValue")

        domino_common_gateway_search_tag_value_highlight = cls(
            tag_value=tag_value,
            highlighted_tag_value=highlighted_tag_value,
        )

        domino_common_gateway_search_tag_value_highlight.additional_properties = d
        return domino_common_gateway_search_tag_value_highlight

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
