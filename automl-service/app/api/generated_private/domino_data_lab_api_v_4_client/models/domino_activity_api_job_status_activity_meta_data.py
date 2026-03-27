from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoActivityApiJobStatusActivityMetaData")


@_attrs_define
class DominoActivityApiJobStatusActivityMetaData:
    """
    Attributes:
        title (str):
        number (int):
        status (str):
        is_scheduled (bool):
        current_status (str):
        comment_count (int):
    """

    title: str
    number: int
    status: str
    is_scheduled: bool
    current_status: str
    comment_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        number = self.number

        status = self.status

        is_scheduled = self.is_scheduled

        current_status = self.current_status

        comment_count = self.comment_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "number": number,
                "status": status,
                "isScheduled": is_scheduled,
                "currentStatus": current_status,
                "commentCount": comment_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        number = d.pop("number")

        status = d.pop("status")

        is_scheduled = d.pop("isScheduled")

        current_status = d.pop("currentStatus")

        comment_count = d.pop("commentCount")

        domino_activity_api_job_status_activity_meta_data = cls(
            title=title,
            number=number,
            status=status,
            is_scheduled=is_scheduled,
            current_status=current_status,
            comment_count=comment_count,
        )

        domino_activity_api_job_status_activity_meta_data.additional_properties = d
        return domino_activity_api_job_status_activity_meta_data

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
