from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_common_gateway_search_search_project_details import (
        DominoCommonGatewaySearchSearchProjectDetails,
    )


T = TypeVar("T", bound="DominoCommonGatewaySearchSearchFileDTO")


@_attrs_define
class DominoCommonGatewaySearchSearchFileDTO:
    """
    Attributes:
        project (DominoCommonGatewaySearchSearchProjectDetails):
        code_snippet (None | str | Unset):
    """

    project: DominoCommonGatewaySearchSearchProjectDetails
    code_snippet: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project = self.project.to_dict()

        code_snippet: None | str | Unset
        if isinstance(self.code_snippet, Unset):
            code_snippet = UNSET
        else:
            code_snippet = self.code_snippet

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project": project,
            }
        )
        if code_snippet is not UNSET:
            field_dict["codeSnippet"] = code_snippet

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_common_gateway_search_search_project_details import (
            DominoCommonGatewaySearchSearchProjectDetails,
        )

        d = dict(src_dict)
        project = DominoCommonGatewaySearchSearchProjectDetails.from_dict(d.pop("project"))

        def _parse_code_snippet(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code_snippet = _parse_code_snippet(d.pop("codeSnippet", UNSET))

        domino_common_gateway_search_search_file_dto = cls(
            project=project,
            code_snippet=code_snippet,
        )

        domino_common_gateway_search_search_file_dto.additional_properties = d
        return domino_common_gateway_search_search_file_dto

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
