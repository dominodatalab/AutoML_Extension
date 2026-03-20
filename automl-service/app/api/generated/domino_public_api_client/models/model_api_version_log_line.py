from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_api_version_log_tag import ModelApiVersionLogTag


T = TypeVar("T", bound="ModelApiVersionLogLine")


@_attrs_define
class ModelApiVersionLogLine:
    """
    Attributes:
        log (str): The content of the log line.
        stream_type (str): The type of stream the log line is sourced from.
        tags (list[ModelApiVersionLogTag]): The tags of the log line.
        time_nano (float): The time in nanoseconds of the log line.
        timestamp (float): The timestamp of the log line.
    """

    log: str
    stream_type: str
    tags: list[ModelApiVersionLogTag]
    time_nano: float
    timestamp: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        log = self.log

        stream_type = self.stream_type

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.to_dict()
            tags.append(tags_item)

        time_nano = self.time_nano

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "log": log,
                "streamType": stream_type,
                "tags": tags,
                "timeNano": time_nano,
                "timestamp": timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_api_version_log_tag import ModelApiVersionLogTag

        d = dict(src_dict)
        log = d.pop("log")

        stream_type = d.pop("streamType")

        tags = []
        _tags = d.pop("tags")
        for tags_item_data in _tags:
            tags_item = ModelApiVersionLogTag.from_dict(tags_item_data)

            tags.append(tags_item)

        time_nano = d.pop("timeNano")

        timestamp = d.pop("timestamp")

        model_api_version_log_line = cls(
            log=log,
            stream_type=stream_type,
            tags=tags,
            time_nano=time_nano,
            timestamp=timestamp,
        )

        model_api_version_log_line.additional_properties = d
        return model_api_version_log_line

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
