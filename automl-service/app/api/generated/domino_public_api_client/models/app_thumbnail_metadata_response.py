from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppThumbnailMetadataResponse")


@_attrs_define
class AppThumbnailMetadataResponse:
    """
    Attributes:
        content_type (str):
        etag (str):
        size_bytes (float):
        updated_at (float):
        filename (str | Unset):
    """

    content_type: str
    etag: str
    size_bytes: float
    updated_at: float
    filename: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_type = self.content_type

        etag = self.etag

        size_bytes = self.size_bytes

        updated_at = self.updated_at

        filename = self.filename

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contentType": content_type,
                "etag": etag,
                "sizeBytes": size_bytes,
                "updatedAt": updated_at,
            }
        )
        if filename is not UNSET:
            field_dict["filename"] = filename

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content_type = d.pop("contentType")

        etag = d.pop("etag")

        size_bytes = d.pop("sizeBytes")

        updated_at = d.pop("updatedAt")

        filename = d.pop("filename", UNSET)

        app_thumbnail_metadata_response = cls(
            content_type=content_type,
            etag=etag,
            size_bytes=size_bytes,
            updated_at=updated_at,
            filename=filename,
        )

        app_thumbnail_metadata_response.additional_properties = d
        return app_thumbnail_metadata_response

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
