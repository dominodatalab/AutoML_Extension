from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpsertAppThumbnailResponse")


@_attrs_define
class UpsertAppThumbnailResponse:
    """
    Attributes:
        created (bool): Whether a new thumbnail document was created (vs replaced)
        etag (str): ETag of the upserted thumbnail
        filename (str | Unset): Original filename of the upserted thumbnail, if provided
        size_bytes (float | Unset): Size of the upserted thumbnail in bytes
    """

    created: bool
    etag: str
    filename: str | Unset = UNSET
    size_bytes: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        etag = self.etag

        filename = self.filename

        size_bytes = self.size_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "etag": etag,
            }
        )
        if filename is not UNSET:
            field_dict["filename"] = filename
        if size_bytes is not UNSET:
            field_dict["sizeBytes"] = size_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created = d.pop("created")

        etag = d.pop("etag")

        filename = d.pop("filename", UNSET)

        size_bytes = d.pop("sizeBytes", UNSET)

        upsert_app_thumbnail_response = cls(
            created=created,
            etag=etag,
            filename=filename,
            size_bytes=size_bytes,
        )

        upsert_app_thumbnail_response.additional_properties = d
        return upsert_app_thumbnail_response

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
