from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoDatasourceApiDataSourceDataPlaneInfo")


@_attrs_define
class DominoDatasourceApiDataSourceDataPlaneInfo:
    """
    Attributes:
        data_plane_id (str):
    """

    data_plane_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_plane_id = self.data_plane_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataPlaneId": data_plane_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data_plane_id = d.pop("dataPlaneId")

        domino_datasource_api_data_source_data_plane_info = cls(
            data_plane_id=data_plane_id,
        )

        domino_datasource_api_data_source_data_plane_info.additional_properties = d
        return domino_datasource_api_data_source_data_plane_info

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
