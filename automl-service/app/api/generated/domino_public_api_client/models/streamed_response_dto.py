from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, Unset

if TYPE_CHECKING:
    from ..models.streamed_response_dto_extra_headers import StreamedResponseDTOExtraHeaders


T = TypeVar("T", bound="StreamedResponseDTO")


@_attrs_define
class StreamedResponseDTO:
    """An internal DTO to stream responses. Should not be referenced by public OAS files directly.

    Attributes:
        extra_headers (StreamedResponseDTOExtraHeaders):
        size (int):
        source (File):
        content_type (str | Unset):
    """

    extra_headers: StreamedResponseDTOExtraHeaders
    size: int
    source: File
    content_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extra_headers = self.extra_headers.to_dict()

        size = self.size

        source = self.source.to_tuple()

        content_type = self.content_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "extraHeaders": extra_headers,
                "size": size,
                "source": source,
            }
        )
        if content_type is not UNSET:
            field_dict["contentType"] = content_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.streamed_response_dto_extra_headers import StreamedResponseDTOExtraHeaders

        d = dict(src_dict)
        extra_headers = StreamedResponseDTOExtraHeaders.from_dict(d.pop("extraHeaders"))

        size = d.pop("size")

        source = File(payload=BytesIO(d.pop("source")))

        content_type = d.pop("contentType", UNSET)

        streamed_response_dto = cls(
            extra_headers=extra_headers,
            size=size,
            source=source,
            content_type=content_type,
        )

        streamed_response_dto.additional_properties = d
        return streamed_response_dto

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
