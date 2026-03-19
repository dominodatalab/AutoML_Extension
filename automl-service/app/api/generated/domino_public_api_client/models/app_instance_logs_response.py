from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.app_instance_logs_response_log_content_item import AppInstanceLogsResponseLogContentItem
    from ..models.app_instance_logs_response_pagination import AppInstanceLogsResponsePagination


T = TypeVar("T", bound="AppInstanceLogsResponse")


@_attrs_define
class AppInstanceLogsResponse:
    """
    Attributes:
        is_complete (bool):
        log_content (list[AppInstanceLogsResponseLogContentItem]):
        pagination (AppInstanceLogsResponsePagination):
    """

    is_complete: bool
    log_content: list[AppInstanceLogsResponseLogContentItem]
    pagination: AppInstanceLogsResponsePagination
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_complete = self.is_complete

        log_content = []
        for log_content_item_data in self.log_content:
            log_content_item = log_content_item_data.to_dict()
            log_content.append(log_content_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isComplete": is_complete,
                "logContent": log_content,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_instance_logs_response_log_content_item import AppInstanceLogsResponseLogContentItem
        from ..models.app_instance_logs_response_pagination import AppInstanceLogsResponsePagination

        d = dict(src_dict)
        is_complete = d.pop("isComplete")

        log_content = []
        _log_content = d.pop("logContent")
        for log_content_item_data in _log_content:
            log_content_item = AppInstanceLogsResponseLogContentItem.from_dict(log_content_item_data)

            log_content.append(log_content_item)

        pagination = AppInstanceLogsResponsePagination.from_dict(d.pop("pagination"))

        app_instance_logs_response = cls(
            is_complete=is_complete,
            log_content=log_content,
            pagination=pagination,
        )

        app_instance_logs_response.additional_properties = d
        return app_instance_logs_response

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
