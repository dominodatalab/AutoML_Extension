from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.build_log_tag_v1 import BuildLogTagV1


T = TypeVar("T", bound="BuildLogLineV1")


@_attrs_define
class BuildLogLineV1:
    """
    Attributes:
        log (str | Unset):
        stream_type (str | Unset):
        tags (list[BuildLogTagV1] | Unset):
        time_nano (int | Unset):
        timestamp (int | Unset):
    """

    log: str | Unset = UNSET
    stream_type: str | Unset = UNSET
    tags: list[BuildLogTagV1] | Unset = UNSET
    time_nano: int | Unset = UNSET
    timestamp: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        log = self.log

        stream_type = self.stream_type

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        time_nano = self.time_nano

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if log is not UNSET:
            field_dict["log"] = log
        if stream_type is not UNSET:
            field_dict["streamType"] = stream_type
        if tags is not UNSET:
            field_dict["tags"] = tags
        if time_nano is not UNSET:
            field_dict["timeNano"] = time_nano
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.build_log_tag_v1 import BuildLogTagV1

        d = dict(src_dict)
        log = d.pop("log", UNSET)

        stream_type = d.pop("streamType", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: list[BuildLogTagV1] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = BuildLogTagV1.from_dict(tags_item_data)

                tags.append(tags_item)

        time_nano = d.pop("timeNano", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        build_log_line_v1 = cls(
            log=log,
            stream_type=stream_type,
            tags=tags,
            time_nano=time_nano,
            timestamp=timestamp,
        )

        build_log_line_v1.additional_properties = d
        return build_log_line_v1

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
