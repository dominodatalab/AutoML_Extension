from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_common_gateway_search_search_project_details import (
        DominoCommonGatewaySearchSearchProjectDetails,
    )


T = TypeVar("T", bound="DominoCommonGatewaySearchSearchCommentDTO")


@_attrs_define
class DominoCommonGatewaySearchSearchCommentDTO:
    """
    Attributes:
        project (DominoCommonGatewaySearchSearchProjectDetails):
        context_description (str):
        offset (int):
    """

    project: DominoCommonGatewaySearchSearchProjectDetails
    context_description: str
    offset: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project = self.project.to_dict()

        context_description = self.context_description

        offset = self.offset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project": project,
                "contextDescription": context_description,
                "offset": offset,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_common_gateway_search_search_project_details import (
            DominoCommonGatewaySearchSearchProjectDetails,
        )

        d = dict(src_dict)
        project = DominoCommonGatewaySearchSearchProjectDetails.from_dict(d.pop("project"))

        context_description = d.pop("contextDescription")

        offset = d.pop("offset")

        domino_common_gateway_search_search_comment_dto = cls(
            project=project,
            context_description=context_description,
            offset=offset,
        )

        domino_common_gateway_search_search_comment_dto.additional_properties = d
        return domino_common_gateway_search_search_comment_dto

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
