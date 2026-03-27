from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="UploadFileBody")


@_attrs_define
class UploadFileBody:
    """
    Attributes:
        upfile (File | Unset): The file to upload
    """

    upfile: File | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        upfile: FileTypes | Unset = UNSET
        if not isinstance(self.upfile, Unset):
            upfile = self.upfile.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if upfile is not UNSET:
            field_dict["upfile"] = upfile

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.upfile, Unset):
            files.append(("upfile", self.upfile.to_tuple()))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _upfile = d.pop("upfile", UNSET)
        upfile: File | Unset
        if isinstance(_upfile, Unset):
            upfile = UNSET
        else:
            upfile = File(payload=BytesIO(_upfile))

        upload_file_body = cls(
            upfile=upfile,
        )

        upload_file_body.additional_properties = d
        return upload_file_body

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
