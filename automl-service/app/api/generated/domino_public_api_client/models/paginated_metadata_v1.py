from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PaginatedMetadataV1")


@_attrs_define
class PaginatedMetadataV1:
    """
    Attributes:
        notices (list[str]): Notices relating to the request
        request_id (str):
        limit (int): Max number of objects returned
        offset (int): Number of object skipped forward from start of objects
        total_count (int | Unset): Total number of available objects
    """

    notices: list[str]
    request_id: str
    limit: int
    offset: int
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        notices = self.notices

        request_id = self.request_id

        limit = self.limit

        offset = self.offset

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "notices": notices,
                "requestId": request_id,
                "limit": limit,
                "offset": offset,
            }
        )
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        notices = cast(list[str], d.pop("notices"))

        request_id = d.pop("requestId")

        limit = d.pop("limit")

        offset = d.pop("offset")

        total_count = d.pop("totalCount", UNSET)

        paginated_metadata_v1 = cls(
            notices=notices,
            request_id=request_id,
            limit=limit,
            offset=offset,
            total_count=total_count,
        )

        paginated_metadata_v1.additional_properties = d
        return paginated_metadata_v1

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
