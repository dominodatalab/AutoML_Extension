from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoDatasetrwApiDatasetRwMountInfoDto")


@_attrs_define
class DominoDatasetrwApiDatasetRwMountInfoDto:
    """
    Attributes:
        mount_path (str):
        sub_dir (str):
        volume_name (str):
        driver_type (None | str | Unset):
    """

    mount_path: str
    sub_dir: str
    volume_name: str
    driver_type: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mount_path = self.mount_path

        sub_dir = self.sub_dir

        volume_name = self.volume_name

        driver_type: None | str | Unset
        if isinstance(self.driver_type, Unset):
            driver_type = UNSET
        else:
            driver_type = self.driver_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mountPath": mount_path,
                "subDir": sub_dir,
                "volumeName": volume_name,
            }
        )
        if driver_type is not UNSET:
            field_dict["driverType"] = driver_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mount_path = d.pop("mountPath")

        sub_dir = d.pop("subDir")

        volume_name = d.pop("volumeName")

        def _parse_driver_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        driver_type = _parse_driver_type(d.pop("driverType", UNSET))

        domino_datasetrw_api_dataset_rw_mount_info_dto = cls(
            mount_path=mount_path,
            sub_dir=sub_dir,
            volume_name=volume_name,
            driver_type=driver_type,
        )

        domino_datasetrw_api_dataset_rw_mount_info_dto.additional_properties = d
        return domino_datasetrw_api_dataset_rw_mount_info_dto

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
