from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoDatasetrwApiDatasetRwStorageInfoDto")


@_attrs_define
class DominoDatasetrwApiDatasetRwStorageInfoDto:
    """
    Attributes:
        name (str):
        data_plane_name (None | str | Unset):
        pvc_name (None | str | Unset):
        is_accessible (bool | None | Unset):
        mount_path (None | str | Unset):
        sub_dir (None | str | Unset):
    """

    name: str
    data_plane_name: None | str | Unset = UNSET
    pvc_name: None | str | Unset = UNSET
    is_accessible: bool | None | Unset = UNSET
    mount_path: None | str | Unset = UNSET
    sub_dir: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        data_plane_name: None | str | Unset
        if isinstance(self.data_plane_name, Unset):
            data_plane_name = UNSET
        else:
            data_plane_name = self.data_plane_name

        pvc_name: None | str | Unset
        if isinstance(self.pvc_name, Unset):
            pvc_name = UNSET
        else:
            pvc_name = self.pvc_name

        is_accessible: bool | None | Unset
        if isinstance(self.is_accessible, Unset):
            is_accessible = UNSET
        else:
            is_accessible = self.is_accessible

        mount_path: None | str | Unset
        if isinstance(self.mount_path, Unset):
            mount_path = UNSET
        else:
            mount_path = self.mount_path

        sub_dir: None | str | Unset
        if isinstance(self.sub_dir, Unset):
            sub_dir = UNSET
        else:
            sub_dir = self.sub_dir

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if data_plane_name is not UNSET:
            field_dict["dataPlaneName"] = data_plane_name
        if pvc_name is not UNSET:
            field_dict["pvcName"] = pvc_name
        if is_accessible is not UNSET:
            field_dict["isAccessible"] = is_accessible
        if mount_path is not UNSET:
            field_dict["mountPath"] = mount_path
        if sub_dir is not UNSET:
            field_dict["subDir"] = sub_dir

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_data_plane_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_plane_name = _parse_data_plane_name(d.pop("dataPlaneName", UNSET))

        def _parse_pvc_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pvc_name = _parse_pvc_name(d.pop("pvcName", UNSET))

        def _parse_is_accessible(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_accessible = _parse_is_accessible(d.pop("isAccessible", UNSET))

        def _parse_mount_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mount_path = _parse_mount_path(d.pop("mountPath", UNSET))

        def _parse_sub_dir(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sub_dir = _parse_sub_dir(d.pop("subDir", UNSET))

        domino_datasetrw_api_dataset_rw_storage_info_dto = cls(
            name=name,
            data_plane_name=data_plane_name,
            pvc_name=pvc_name,
            is_accessible=is_accessible,
            mount_path=mount_path,
            sub_dir=sub_dir,
        )

        domino_datasetrw_api_dataset_rw_storage_info_dto.additional_properties = d
        return domino_datasetrw_api_dataset_rw_storage_info_dto

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
