from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_datasource_api_data_source_accessed_info_data_source_type import (
    DominoDatasourceApiDataSourceAccessedInfoDataSourceType,
)

T = TypeVar("T", bound="DominoDatasourceApiDataSourceAccessedInfo")


@_attrs_define
class DominoDatasourceApiDataSourceAccessedInfo:
    """
    Attributes:
        data_source_id (str):
        data_source_name (str):
        data_source_type (DominoDatasourceApiDataSourceAccessedInfoDataSourceType):
        owner_name (str):
    """

    data_source_id: str
    data_source_name: str
    data_source_type: DominoDatasourceApiDataSourceAccessedInfoDataSourceType
    owner_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_source_id = self.data_source_id

        data_source_name = self.data_source_name

        data_source_type = self.data_source_type.value

        owner_name = self.owner_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataSourceId": data_source_id,
                "dataSourceName": data_source_name,
                "dataSourceType": data_source_type,
                "ownerName": owner_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data_source_id = d.pop("dataSourceId")

        data_source_name = d.pop("dataSourceName")

        data_source_type = DominoDatasourceApiDataSourceAccessedInfoDataSourceType(d.pop("dataSourceType"))

        owner_name = d.pop("ownerName")

        domino_datasource_api_data_source_accessed_info = cls(
            data_source_id=data_source_id,
            data_source_name=data_source_name,
            data_source_type=data_source_type,
            owner_name=owner_name,
        )

        domino_datasource_api_data_source_accessed_info.additional_properties = d
        return domino_datasource_api_data_source_accessed_info

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
