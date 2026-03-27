from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_common_gateway_search_search_page_result_gateway_dto import (
        DominoCommonGatewaySearchSearchPageResultGatewayDTO,
    )


T = TypeVar("T", bound="DominoCommonGatewaySearchSearchPageGatewayDTO")


@_attrs_define
class DominoCommonGatewaySearchSearchPageGatewayDTO:
    """
    Attributes:
        results (list[DominoCommonGatewaySearchSearchPageResultGatewayDTO]):
        has_more_results (bool):
    """

    results: list[DominoCommonGatewaySearchSearchPageResultGatewayDTO]
    has_more_results: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        has_more_results = self.has_more_results

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "hasMoreResults": has_more_results,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_common_gateway_search_search_page_result_gateway_dto import (
            DominoCommonGatewaySearchSearchPageResultGatewayDTO,
        )

        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = DominoCommonGatewaySearchSearchPageResultGatewayDTO.from_dict(results_item_data)

            results.append(results_item)

        has_more_results = d.pop("hasMoreResults")

        domino_common_gateway_search_search_page_gateway_dto = cls(
            results=results,
            has_more_results=has_more_results,
        )

        domino_common_gateway_search_search_page_gateway_dto.additional_properties = d
        return domino_common_gateway_search_search_page_gateway_dto

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
