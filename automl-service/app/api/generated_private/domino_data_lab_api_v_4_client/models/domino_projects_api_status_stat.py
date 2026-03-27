from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_projects_api_status_stat_name import DominoProjectsApiStatusStatName

T = TypeVar("T", bound="DominoProjectsApiStatusStat")


@_attrs_define
class DominoProjectsApiStatusStat:
    """
    Attributes:
        name (DominoProjectsApiStatusStatName):
        project_count (int):
    """

    name: DominoProjectsApiStatusStatName
    project_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name.value

        project_count = self.project_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "projectCount": project_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = DominoProjectsApiStatusStatName(d.pop("name"))

        project_count = d.pop("projectCount")

        domino_projects_api_status_stat = cls(
            name=name,
            project_count=project_count,
        )

        domino_projects_api_status_stat.additional_properties = d
        return domino_projects_api_status_stat

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
