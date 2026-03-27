from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_datasource_api_data_source_data_plane_info import DominoDatasourceApiDataSourceDataPlaneInfo


T = TypeVar("T", bound="DominoDatasourceWebUpdateDataSourceDataPlanesRequest")


@_attrs_define
class DominoDatasourceWebUpdateDataSourceDataPlanesRequest:
    """
    Attributes:
        data_planes (list[DominoDatasourceApiDataSourceDataPlaneInfo]):
    """

    data_planes: list[DominoDatasourceApiDataSourceDataPlaneInfo]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_planes = []
        for data_planes_item_data in self.data_planes:
            data_planes_item = data_planes_item_data.to_dict()
            data_planes.append(data_planes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataPlanes": data_planes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_datasource_api_data_source_data_plane_info import (
            DominoDatasourceApiDataSourceDataPlaneInfo,
        )

        d = dict(src_dict)
        data_planes = []
        _data_planes = d.pop("dataPlanes")
        for data_planes_item_data in _data_planes:
            data_planes_item = DominoDatasourceApiDataSourceDataPlaneInfo.from_dict(data_planes_item_data)

            data_planes.append(data_planes_item)

        domino_datasource_web_update_data_source_data_planes_request = cls(
            data_planes=data_planes,
        )

        domino_datasource_web_update_data_source_data_planes_request.additional_properties = d
        return domino_datasource_web_update_data_source_data_planes_request

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
