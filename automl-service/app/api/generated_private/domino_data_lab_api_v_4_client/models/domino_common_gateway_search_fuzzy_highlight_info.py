from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_common_gateway_search_entity_highlight import DominoCommonGatewaySearchEntityHighlight
    from ..models.domino_common_gateway_search_feature_highlight import DominoCommonGatewaySearchFeatureHighlight
    from ..models.domino_common_gateway_search_tag_key_highlight import DominoCommonGatewaySearchTagKeyHighlight
    from ..models.domino_common_gateway_search_tag_value_highlight import DominoCommonGatewaySearchTagValueHighlight


T = TypeVar("T", bound="DominoCommonGatewaySearchFuzzyHighlightInfo")


@_attrs_define
class DominoCommonGatewaySearchFuzzyHighlightInfo:
    """
    Attributes:
        maybe_highlighted_feature_view_name (str):
        maybe_highlighted_description (str):
        highlighted_entities (list[DominoCommonGatewaySearchEntityHighlight]):
        highlighted_features (list[DominoCommonGatewaySearchFeatureHighlight]):
        highlighted_tag_keys (list[DominoCommonGatewaySearchTagKeyHighlight]):
        highlighted_tag_values (list[DominoCommonGatewaySearchTagValueHighlight]):
        maybe_highlighted_model_author (str):
    """

    maybe_highlighted_feature_view_name: str
    maybe_highlighted_description: str
    highlighted_entities: list[DominoCommonGatewaySearchEntityHighlight]
    highlighted_features: list[DominoCommonGatewaySearchFeatureHighlight]
    highlighted_tag_keys: list[DominoCommonGatewaySearchTagKeyHighlight]
    highlighted_tag_values: list[DominoCommonGatewaySearchTagValueHighlight]
    maybe_highlighted_model_author: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        maybe_highlighted_feature_view_name = self.maybe_highlighted_feature_view_name

        maybe_highlighted_description = self.maybe_highlighted_description

        highlighted_entities = []
        for highlighted_entities_item_data in self.highlighted_entities:
            highlighted_entities_item = highlighted_entities_item_data.to_dict()
            highlighted_entities.append(highlighted_entities_item)

        highlighted_features = []
        for highlighted_features_item_data in self.highlighted_features:
            highlighted_features_item = highlighted_features_item_data.to_dict()
            highlighted_features.append(highlighted_features_item)

        highlighted_tag_keys = []
        for highlighted_tag_keys_item_data in self.highlighted_tag_keys:
            highlighted_tag_keys_item = highlighted_tag_keys_item_data.to_dict()
            highlighted_tag_keys.append(highlighted_tag_keys_item)

        highlighted_tag_values = []
        for highlighted_tag_values_item_data in self.highlighted_tag_values:
            highlighted_tag_values_item = highlighted_tag_values_item_data.to_dict()
            highlighted_tag_values.append(highlighted_tag_values_item)

        maybe_highlighted_model_author = self.maybe_highlighted_model_author

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "maybeHighlightedFeatureViewName": maybe_highlighted_feature_view_name,
                "maybeHighlightedDescription": maybe_highlighted_description,
                "highlightedEntities": highlighted_entities,
                "highlightedFeatures": highlighted_features,
                "highlightedTagKeys": highlighted_tag_keys,
                "highlightedTagValues": highlighted_tag_values,
                "maybeHighlightedModelAuthor": maybe_highlighted_model_author,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_common_gateway_search_entity_highlight import DominoCommonGatewaySearchEntityHighlight
        from ..models.domino_common_gateway_search_feature_highlight import DominoCommonGatewaySearchFeatureHighlight
        from ..models.domino_common_gateway_search_tag_key_highlight import DominoCommonGatewaySearchTagKeyHighlight
        from ..models.domino_common_gateway_search_tag_value_highlight import DominoCommonGatewaySearchTagValueHighlight

        d = dict(src_dict)
        maybe_highlighted_feature_view_name = d.pop("maybeHighlightedFeatureViewName")

        maybe_highlighted_description = d.pop("maybeHighlightedDescription")

        highlighted_entities = []
        _highlighted_entities = d.pop("highlightedEntities")
        for highlighted_entities_item_data in _highlighted_entities:
            highlighted_entities_item = DominoCommonGatewaySearchEntityHighlight.from_dict(
                highlighted_entities_item_data
            )

            highlighted_entities.append(highlighted_entities_item)

        highlighted_features = []
        _highlighted_features = d.pop("highlightedFeatures")
        for highlighted_features_item_data in _highlighted_features:
            highlighted_features_item = DominoCommonGatewaySearchFeatureHighlight.from_dict(
                highlighted_features_item_data
            )

            highlighted_features.append(highlighted_features_item)

        highlighted_tag_keys = []
        _highlighted_tag_keys = d.pop("highlightedTagKeys")
        for highlighted_tag_keys_item_data in _highlighted_tag_keys:
            highlighted_tag_keys_item = DominoCommonGatewaySearchTagKeyHighlight.from_dict(
                highlighted_tag_keys_item_data
            )

            highlighted_tag_keys.append(highlighted_tag_keys_item)

        highlighted_tag_values = []
        _highlighted_tag_values = d.pop("highlightedTagValues")
        for highlighted_tag_values_item_data in _highlighted_tag_values:
            highlighted_tag_values_item = DominoCommonGatewaySearchTagValueHighlight.from_dict(
                highlighted_tag_values_item_data
            )

            highlighted_tag_values.append(highlighted_tag_values_item)

        maybe_highlighted_model_author = d.pop("maybeHighlightedModelAuthor")

        domino_common_gateway_search_fuzzy_highlight_info = cls(
            maybe_highlighted_feature_view_name=maybe_highlighted_feature_view_name,
            maybe_highlighted_description=maybe_highlighted_description,
            highlighted_entities=highlighted_entities,
            highlighted_features=highlighted_features,
            highlighted_tag_keys=highlighted_tag_keys,
            highlighted_tag_values=highlighted_tag_values,
            maybe_highlighted_model_author=maybe_highlighted_model_author,
        )

        domino_common_gateway_search_fuzzy_highlight_info.additional_properties = d
        return domino_common_gateway_search_fuzzy_highlight_info

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
