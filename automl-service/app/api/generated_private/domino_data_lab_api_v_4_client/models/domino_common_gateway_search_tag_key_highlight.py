from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoCommonGatewaySearchTagKeyHighlight")


@_attrs_define
class DominoCommonGatewaySearchTagKeyHighlight:
    """
    Attributes:
        tag_key (str):
        highlighted_tag_key (str):
    """

    tag_key: str
    highlighted_tag_key: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tag_key = self.tag_key

        highlighted_tag_key = self.highlighted_tag_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tagKey": tag_key,
                "highlightedTagKey": highlighted_tag_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tag_key = d.pop("tagKey")

        highlighted_tag_key = d.pop("highlightedTagKey")

        domino_common_gateway_search_tag_key_highlight = cls(
            tag_key=tag_key,
            highlighted_tag_key=highlighted_tag_key,
        )

        domino_common_gateway_search_tag_key_highlight.additional_properties = d
        return domino_common_gateway_search_tag_key_highlight

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
