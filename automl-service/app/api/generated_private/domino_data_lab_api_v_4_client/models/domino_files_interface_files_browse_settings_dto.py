from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoFilesInterfaceFilesBrowseSettingsDto")


@_attrs_define
class DominoFilesInterfaceFilesBrowseSettingsDto:
    """
    Attributes:
        allow_folder_downloads (bool):
        max_upload_files_count (int):
        max_upload_file_size_in_megabytes (int):
        restricted_file_types (str):
    """

    allow_folder_downloads: bool
    max_upload_files_count: int
    max_upload_file_size_in_megabytes: int
    restricted_file_types: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_folder_downloads = self.allow_folder_downloads

        max_upload_files_count = self.max_upload_files_count

        max_upload_file_size_in_megabytes = self.max_upload_file_size_in_megabytes

        restricted_file_types = self.restricted_file_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowFolderDownloads": allow_folder_downloads,
                "maxUploadFilesCount": max_upload_files_count,
                "maxUploadFileSizeInMegabytes": max_upload_file_size_in_megabytes,
                "restrictedFileTypes": restricted_file_types,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_folder_downloads = d.pop("allowFolderDownloads")

        max_upload_files_count = d.pop("maxUploadFilesCount")

        max_upload_file_size_in_megabytes = d.pop("maxUploadFileSizeInMegabytes")

        restricted_file_types = d.pop("restrictedFileTypes")

        domino_files_interface_files_browse_settings_dto = cls(
            allow_folder_downloads=allow_folder_downloads,
            max_upload_files_count=max_upload_files_count,
            max_upload_file_size_in_megabytes=max_upload_file_size_in_megabytes,
            restricted_file_types=restricted_file_types,
        )

        domino_files_interface_files_browse_settings_dto.additional_properties = d
        return domino_files_interface_files_browse_settings_dto

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
