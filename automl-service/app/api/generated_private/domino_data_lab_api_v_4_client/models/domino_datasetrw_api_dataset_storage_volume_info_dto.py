from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoDatasetrwApiDatasetStorageVolumeInfoDto")


@_attrs_define
class DominoDatasetrwApiDatasetStorageVolumeInfoDto:
    """
    Attributes:
        pvc_name (str):
        data_plane_id (str):
        data_plane_name (str):
        volume_type (str):
    """

    pvc_name: str
    data_plane_id: str
    data_plane_name: str
    volume_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pvc_name = self.pvc_name

        data_plane_id = self.data_plane_id

        data_plane_name = self.data_plane_name

        volume_type = self.volume_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pvcName": pvc_name,
                "dataPlaneId": data_plane_id,
                "dataPlaneName": data_plane_name,
                "volumeType": volume_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pvc_name = d.pop("pvcName")

        data_plane_id = d.pop("dataPlaneId")

        data_plane_name = d.pop("dataPlaneName")

        volume_type = d.pop("volumeType")

        domino_datasetrw_api_dataset_storage_volume_info_dto = cls(
            pvc_name=pvc_name,
            data_plane_id=data_plane_id,
            data_plane_name=data_plane_name,
            volume_type=volume_type,
        )

        domino_datasetrw_api_dataset_storage_volume_info_dto.additional_properties = d
        return domino_datasetrw_api_dataset_storage_volume_info_dto

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
