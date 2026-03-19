from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TokenPaginatedMetadataV1")


@_attrs_define
class TokenPaginatedMetadataV1:
    """
    Attributes:
        notices (list[str]): Notices relating to the request
        request_id (str):
        next_page_token (str | Unset): Pagination token to request the next page of objects
    """

    notices: list[str]
    request_id: str
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        notices = self.notices

        request_id = self.request_id

        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "notices": notices,
                "requestId": request_id,
            }
        )
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        notices = cast(list[str], d.pop("notices"))

        request_id = d.pop("requestId")

        next_page_token = d.pop("nextPageToken", UNSET)

        token_paginated_metadata_v1 = cls(
            notices=notices,
            request_id=request_id,
            next_page_token=next_page_token,
        )

        token_paginated_metadata_v1.additional_properties = d
        return token_paginated_metadata_v1

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
