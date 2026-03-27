from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_projects_api_project_portfolio_meta_data_project_status_type import (
    DominoProjectsApiProjectPortfolioMetaDataProjectStatusType,
)

T = TypeVar("T", bound="DominoProjectsApiProjectPortfolioMetaData")


@_attrs_define
class DominoProjectsApiProjectPortfolioMetaData:
    """
    Attributes:
        project_status_type (DominoProjectsApiProjectPortfolioMetaDataProjectStatusType):
    """

    project_status_type: DominoProjectsApiProjectPortfolioMetaDataProjectStatusType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_status_type = self.project_status_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectStatusType": project_status_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_status_type = DominoProjectsApiProjectPortfolioMetaDataProjectStatusType(d.pop("projectStatusType"))

        domino_projects_api_project_portfolio_meta_data = cls(
            project_status_type=project_status_type,
        )

        domino_projects_api_project_portfolio_meta_data.additional_properties = d
        return domino_projects_api_project_portfolio_meta_data

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
