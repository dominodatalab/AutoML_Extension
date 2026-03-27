from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoDatasetrwApiDatasetRwSnapshotFileMetadataDto")


@_attrs_define
class DominoDatasetrwApiDatasetRwSnapshotFileMetadataDto:
    """
    Attributes:
        exceeds_size_limit (bool | None | Unset):
        file_size (int | None | Unset):
        last_modified (int | None | Unset):
        mime_type (None | str | Unset):
        name (None | str | Unset):
        preview_uri (None | str | Unset):
        uri (None | str | Unset):
    """

    exceeds_size_limit: bool | None | Unset = UNSET
    file_size: int | None | Unset = UNSET
    last_modified: int | None | Unset = UNSET
    mime_type: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    preview_uri: None | str | Unset = UNSET
    uri: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exceeds_size_limit: bool | None | Unset
        if isinstance(self.exceeds_size_limit, Unset):
            exceeds_size_limit = UNSET
        else:
            exceeds_size_limit = self.exceeds_size_limit

        file_size: int | None | Unset
        if isinstance(self.file_size, Unset):
            file_size = UNSET
        else:
            file_size = self.file_size

        last_modified: int | None | Unset
        if isinstance(self.last_modified, Unset):
            last_modified = UNSET
        else:
            last_modified = self.last_modified

        mime_type: None | str | Unset
        if isinstance(self.mime_type, Unset):
            mime_type = UNSET
        else:
            mime_type = self.mime_type

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        preview_uri: None | str | Unset
        if isinstance(self.preview_uri, Unset):
            preview_uri = UNSET
        else:
            preview_uri = self.preview_uri

        uri: None | str | Unset
        if isinstance(self.uri, Unset):
            uri = UNSET
        else:
            uri = self.uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exceeds_size_limit is not UNSET:
            field_dict["exceedsSizeLimit"] = exceeds_size_limit
        if file_size is not UNSET:
            field_dict["fileSize"] = file_size
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if name is not UNSET:
            field_dict["name"] = name
        if preview_uri is not UNSET:
            field_dict["previewUri"] = preview_uri
        if uri is not UNSET:
            field_dict["uri"] = uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_exceeds_size_limit(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        exceeds_size_limit = _parse_exceeds_size_limit(d.pop("exceedsSizeLimit", UNSET))

        def _parse_file_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        file_size = _parse_file_size(d.pop("fileSize", UNSET))

        def _parse_last_modified(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_modified = _parse_last_modified(d.pop("lastModified", UNSET))

        def _parse_mime_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mime_type = _parse_mime_type(d.pop("mimeType", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_preview_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preview_uri = _parse_preview_uri(d.pop("previewUri", UNSET))

        def _parse_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        uri = _parse_uri(d.pop("uri", UNSET))

        domino_datasetrw_api_dataset_rw_snapshot_file_metadata_dto = cls(
            exceeds_size_limit=exceeds_size_limit,
            file_size=file_size,
            last_modified=last_modified,
            mime_type=mime_type,
            name=name,
            preview_uri=preview_uri,
            uri=uri,
        )

        domino_datasetrw_api_dataset_rw_snapshot_file_metadata_dto.additional_properties = d
        return domino_datasetrw_api_dataset_rw_snapshot_file_metadata_dto

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
