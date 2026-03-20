from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.logs_pagination_v1 import LogsPaginationV1


T = TypeVar("T", bound="LogsEnvelopeV1Metadata")


@_attrs_define
class LogsEnvelopeV1Metadata:
    """
    Attributes:
        notices (list[str]): Notices relating to the request
        pagination (LogsPaginationV1):
        request_id (str): Id used to correlate a request with server actions. Example:
            bbd78579-93c4-45ee-a983-0d5c8da6d5b1.
    """

    notices: list[str]
    pagination: LogsPaginationV1
    request_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        notices = self.notices

        pagination = self.pagination.to_dict()

        request_id = self.request_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "notices": notices,
                "pagination": pagination,
                "requestId": request_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.logs_pagination_v1 import LogsPaginationV1

        d = dict(src_dict)
        notices = cast(list[str], d.pop("notices"))

        pagination = LogsPaginationV1.from_dict(d.pop("pagination"))

        request_id = d.pop("requestId")

        logs_envelope_v1_metadata = cls(
            notices=notices,
            pagination=pagination,
            request_id=request_id,
        )

        logs_envelope_v1_metadata.additional_properties = d
        return logs_envelope_v1_metadata

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
