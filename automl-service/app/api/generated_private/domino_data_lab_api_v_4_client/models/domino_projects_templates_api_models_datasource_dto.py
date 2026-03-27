from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoProjectsTemplatesApiModelsDatasourceDto")


@_attrs_define
class DominoProjectsTemplatesApiModelsDatasourceDto:
    """
    Attributes:
        id (str):
        name (str):
        ownername (str):
    """

    id: str
    name: str
    ownername: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        ownername = self.ownername

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "ownername": ownername,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        ownername = d.pop("ownername")

        domino_projects_templates_api_models_datasource_dto = cls(
            id=id,
            name=name,
            ownername=ownername,
        )

        domino_projects_templates_api_models_datasource_dto.additional_properties = d
        return domino_projects_templates_api_models_datasource_dto

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
