from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_common_gateway_search_feature_view_search_result_dto_tags import (
        DominoCommonGatewaySearchFeatureViewSearchResultDTOTags,
    )
    from ..models.domino_common_gateway_search_fuzzy_highlight_info import DominoCommonGatewaySearchFuzzyHighlightInfo


T = TypeVar("T", bound="DominoCommonGatewaySearchFeatureViewSearchResultDTO")


@_attrs_define
class DominoCommonGatewaySearchFeatureViewSearchResultDTO:
    """
    Attributes:
        feature_view_id (str):
        highlight_info (DominoCommonGatewaySearchFuzzyHighlightInfo):
        feature_view_name (str):
        description (str):
        entities (list[str]):
        features (list[str]):
        tags (DominoCommonGatewaySearchFeatureViewSearchResultDTOTags):
        author (str):
        last_updated (int):
        created (int):
        project_ids (list[str]):
    """

    feature_view_id: str
    highlight_info: DominoCommonGatewaySearchFuzzyHighlightInfo
    feature_view_name: str
    description: str
    entities: list[str]
    features: list[str]
    tags: DominoCommonGatewaySearchFeatureViewSearchResultDTOTags
    author: str
    last_updated: int
    created: int
    project_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        feature_view_id = self.feature_view_id

        highlight_info = self.highlight_info.to_dict()

        feature_view_name = self.feature_view_name

        description = self.description

        entities = self.entities

        features = self.features

        tags = self.tags.to_dict()

        author = self.author

        last_updated = self.last_updated

        created = self.created

        project_ids = self.project_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "featureViewId": feature_view_id,
                "highlightInfo": highlight_info,
                "featureViewName": feature_view_name,
                "description": description,
                "entities": entities,
                "features": features,
                "tags": tags,
                "author": author,
                "lastUpdated": last_updated,
                "created": created,
                "projectIds": project_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_common_gateway_search_feature_view_search_result_dto_tags import (
            DominoCommonGatewaySearchFeatureViewSearchResultDTOTags,
        )
        from ..models.domino_common_gateway_search_fuzzy_highlight_info import (
            DominoCommonGatewaySearchFuzzyHighlightInfo,
        )

        d = dict(src_dict)
        feature_view_id = d.pop("featureViewId")

        highlight_info = DominoCommonGatewaySearchFuzzyHighlightInfo.from_dict(d.pop("highlightInfo"))

        feature_view_name = d.pop("featureViewName")

        description = d.pop("description")

        entities = cast(list[str], d.pop("entities"))

        features = cast(list[str], d.pop("features"))

        tags = DominoCommonGatewaySearchFeatureViewSearchResultDTOTags.from_dict(d.pop("tags"))

        author = d.pop("author")

        last_updated = d.pop("lastUpdated")

        created = d.pop("created")

        project_ids = cast(list[str], d.pop("projectIds"))

        domino_common_gateway_search_feature_view_search_result_dto = cls(
            feature_view_id=feature_view_id,
            highlight_info=highlight_info,
            feature_view_name=feature_view_name,
            description=description,
            entities=entities,
            features=features,
            tags=tags,
            author=author,
            last_updated=last_updated,
            created=created,
            project_ids=project_ids,
        )

        domino_common_gateway_search_feature_view_search_result_dto.additional_properties = d
        return domino_common_gateway_search_feature_view_search_result_dto

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
