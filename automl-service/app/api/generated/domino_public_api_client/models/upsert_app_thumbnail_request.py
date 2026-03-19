from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpsertAppThumbnailRequest")


@_attrs_define
class UpsertAppThumbnailRequest:
    """
    Attributes:
        content_base_64 (str): Base64-encoded thumbnail bytes
        content_type (str): MIME type of the thumbnail content (e.g., image/png)
        filename (str | Unset): Original filename of the thumbnail (if provided)
    """

    content_base_64: str
    content_type: str
    filename: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_base_64 = self.content_base_64

        content_type = self.content_type

        filename = self.filename

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contentBase64": content_base_64,
                "contentType": content_type,
            }
        )
        if filename is not UNSET:
            field_dict["filename"] = filename

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content_base_64 = d.pop("contentBase64")

        content_type = d.pop("contentType")

        filename = d.pop("filename", UNSET)

        upsert_app_thumbnail_request = cls(
            content_base_64=content_base_64,
            content_type=content_type,
            filename=filename,
        )

        upsert_app_thumbnail_request.additional_properties = d
        return upsert_app_thumbnail_request

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
