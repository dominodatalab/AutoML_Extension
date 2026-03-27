from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoDatasetrwWebAddTagRequest")


@_attrs_define
class DominoDatasetrwWebAddTagRequest:
    """
    Attributes:
        snapshot_id (str):
        tag (str):
    """

    snapshot_id: str
    tag: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        snapshot_id = self.snapshot_id

        tag = self.tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "snapshotId": snapshot_id,
                "tag": tag,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        snapshot_id = d.pop("snapshotId")

        tag = d.pop("tag")

        domino_datasetrw_web_add_tag_request = cls(
            snapshot_id=snapshot_id,
            tag=tag,
        )

        domino_datasetrw_web_add_tag_request.additional_properties = d
        return domino_datasetrw_web_add_tag_request

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
