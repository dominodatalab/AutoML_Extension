from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoDatasetrwWebUpdateDatasetRwStorageRequest")


@_attrs_define
class DominoDatasetrwWebUpdateDatasetRwStorageRequest:
    """
    Attributes:
        name (None | str | Unset):
        data_plane_id (None | str | Unset):
        is_data_plane_default (bool | None | Unset):
        pvc_name (None | str | Unset):
        mount_path (None | str | Unset):
    """

    name: None | str | Unset = UNSET
    data_plane_id: None | str | Unset = UNSET
    is_data_plane_default: bool | None | Unset = UNSET
    pvc_name: None | str | Unset = UNSET
    mount_path: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        data_plane_id: None | str | Unset
        if isinstance(self.data_plane_id, Unset):
            data_plane_id = UNSET
        else:
            data_plane_id = self.data_plane_id

        is_data_plane_default: bool | None | Unset
        if isinstance(self.is_data_plane_default, Unset):
            is_data_plane_default = UNSET
        else:
            is_data_plane_default = self.is_data_plane_default

        pvc_name: None | str | Unset
        if isinstance(self.pvc_name, Unset):
            pvc_name = UNSET
        else:
            pvc_name = self.pvc_name

        mount_path: None | str | Unset
        if isinstance(self.mount_path, Unset):
            mount_path = UNSET
        else:
            mount_path = self.mount_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if data_plane_id is not UNSET:
            field_dict["dataPlaneId"] = data_plane_id
        if is_data_plane_default is not UNSET:
            field_dict["isDataPlaneDefault"] = is_data_plane_default
        if pvc_name is not UNSET:
            field_dict["pvcName"] = pvc_name
        if mount_path is not UNSET:
            field_dict["mountPath"] = mount_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_data_plane_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_plane_id = _parse_data_plane_id(d.pop("dataPlaneId", UNSET))

        def _parse_is_data_plane_default(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_data_plane_default = _parse_is_data_plane_default(d.pop("isDataPlaneDefault", UNSET))

        def _parse_pvc_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pvc_name = _parse_pvc_name(d.pop("pvcName", UNSET))

        def _parse_mount_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mount_path = _parse_mount_path(d.pop("mountPath", UNSET))

        domino_datasetrw_web_update_dataset_rw_storage_request = cls(
            name=name,
            data_plane_id=data_plane_id,
            is_data_plane_default=is_data_plane_default,
            pvc_name=pvc_name,
            mount_path=mount_path,
        )

        domino_datasetrw_web_update_dataset_rw_storage_request.additional_properties = d
        return domino_datasetrw_web_update_dataset_rw_storage_request

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
