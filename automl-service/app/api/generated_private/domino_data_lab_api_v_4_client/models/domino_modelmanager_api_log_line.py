from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_modelmanager_api_log_tag import DominoModelmanagerApiLogTag


T = TypeVar("T", bound="DominoModelmanagerApiLogLine")


@_attrs_define
class DominoModelmanagerApiLogLine:
    """
    Attributes:
        timestamp (int):
        time_nano (int):
        log (str):
        stream_type (str):
        tags (list[DominoModelmanagerApiLogTag]):
    """

    timestamp: int
    time_nano: int
    log: str
    stream_type: str
    tags: list[DominoModelmanagerApiLogTag]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        time_nano = self.time_nano

        log = self.log

        stream_type = self.stream_type

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.to_dict()
            tags.append(tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "timeNano": time_nano,
                "log": log,
                "streamType": stream_type,
                "tags": tags,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_modelmanager_api_log_tag import DominoModelmanagerApiLogTag

        d = dict(src_dict)
        timestamp = d.pop("timestamp")

        time_nano = d.pop("timeNano")

        log = d.pop("log")

        stream_type = d.pop("streamType")

        tags = []
        _tags = d.pop("tags")
        for tags_item_data in _tags:
            tags_item = DominoModelmanagerApiLogTag.from_dict(tags_item_data)

            tags.append(tags_item)

        domino_modelmanager_api_log_line = cls(
            timestamp=timestamp,
            time_nano=time_nano,
            log=log,
            stream_type=stream_type,
            tags=tags,
        )

        domino_modelmanager_api_log_line.additional_properties = d
        return domino_modelmanager_api_log_line

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
