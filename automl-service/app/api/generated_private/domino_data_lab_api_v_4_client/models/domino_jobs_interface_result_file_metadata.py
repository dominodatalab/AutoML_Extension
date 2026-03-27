from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoJobsInterfaceResultFileMetadata")


@_attrs_define
class DominoJobsInterfaceResultFileMetadata:
    """
    Attributes:
        content_id (str):
        filename (str):
        size (int):
        last_modified (int):
        author (str):
    """

    content_id: str
    filename: str
    size: int
    last_modified: int
    author: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_id = self.content_id

        filename = self.filename

        size = self.size

        last_modified = self.last_modified

        author = self.author

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contentId": content_id,
                "filename": filename,
                "size": size,
                "lastModified": last_modified,
                "author": author,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content_id = d.pop("contentId")

        filename = d.pop("filename")

        size = d.pop("size")

        last_modified = d.pop("lastModified")

        author = d.pop("author")

        domino_jobs_interface_result_file_metadata = cls(
            content_id=content_id,
            filename=filename,
            size=size,
            last_modified=last_modified,
            author=author,
        )

        domino_jobs_interface_result_file_metadata.additional_properties = d
        return domino_jobs_interface_result_file_metadata

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
