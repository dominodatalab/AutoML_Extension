from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_common_gateway_search_feature_view_search_result_dto import (
        DominoCommonGatewaySearchFeatureViewSearchResultDTO,
    )


T = TypeVar("T", bound="DominoCommonGatewaySearchSearchResultGatewayDTO")


@_attrs_define
class DominoCommonGatewaySearchSearchResultGatewayDTO:
    """
    Attributes:
        link (str):
        area (str):
        id (None | str | Unset):
        project_id (None | str | Unset):
        display_text (None | str | Unset):
        owner_id (None | str | Unset):
        path (None | str | Unset):
        feature_view_info (DominoCommonGatewaySearchFeatureViewSearchResultDTO | Unset):
    """

    link: str
    area: str
    id: None | str | Unset = UNSET
    project_id: None | str | Unset = UNSET
    display_text: None | str | Unset = UNSET
    owner_id: None | str | Unset = UNSET
    path: None | str | Unset = UNSET
    feature_view_info: DominoCommonGatewaySearchFeatureViewSearchResultDTO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        link = self.link

        area = self.area

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        display_text: None | str | Unset
        if isinstance(self.display_text, Unset):
            display_text = UNSET
        else:
            display_text = self.display_text

        owner_id: None | str | Unset
        if isinstance(self.owner_id, Unset):
            owner_id = UNSET
        else:
            owner_id = self.owner_id

        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        feature_view_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.feature_view_info, Unset):
            feature_view_info = self.feature_view_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "link": link,
                "area": area,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if display_text is not UNSET:
            field_dict["displayText"] = display_text
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if path is not UNSET:
            field_dict["path"] = path
        if feature_view_info is not UNSET:
            field_dict["featureViewInfo"] = feature_view_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_common_gateway_search_feature_view_search_result_dto import (
            DominoCommonGatewaySearchFeatureViewSearchResultDTO,
        )

        d = dict(src_dict)
        link = d.pop("link")

        area = d.pop("area")

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_project_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_id = _parse_project_id(d.pop("projectId", UNSET))

        def _parse_display_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_text = _parse_display_text(d.pop("displayText", UNSET))

        def _parse_owner_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_id = _parse_owner_id(d.pop("ownerId", UNSET))

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))

        _feature_view_info = d.pop("featureViewInfo", UNSET)
        feature_view_info: DominoCommonGatewaySearchFeatureViewSearchResultDTO | Unset
        if isinstance(_feature_view_info, Unset):
            feature_view_info = UNSET
        else:
            feature_view_info = DominoCommonGatewaySearchFeatureViewSearchResultDTO.from_dict(_feature_view_info)

        domino_common_gateway_search_search_result_gateway_dto = cls(
            link=link,
            area=area,
            id=id,
            project_id=project_id,
            display_text=display_text,
            owner_id=owner_id,
            path=path,
            feature_view_info=feature_view_info,
        )

        domino_common_gateway_search_search_result_gateway_dto.additional_properties = d
        return domino_common_gateway_search_search_result_gateway_dto

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
