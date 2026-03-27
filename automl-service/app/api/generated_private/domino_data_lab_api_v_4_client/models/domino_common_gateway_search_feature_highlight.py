from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoCommonGatewaySearchFeatureHighlight")


@_attrs_define
class DominoCommonGatewaySearchFeatureHighlight:
    """
    Attributes:
        feature_name (str):
        highlighted_feature_name (str):
    """

    feature_name: str
    highlighted_feature_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        feature_name = self.feature_name

        highlighted_feature_name = self.highlighted_feature_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "featureName": feature_name,
                "highlightedFeatureName": highlighted_feature_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        feature_name = d.pop("featureName")

        highlighted_feature_name = d.pop("highlightedFeatureName")

        domino_common_gateway_search_feature_highlight = cls(
            feature_name=feature_name,
            highlighted_feature_name=highlighted_feature_name,
        )

        domino_common_gateway_search_feature_highlight.additional_properties = d
        return domino_common_gateway_search_feature_highlight

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
