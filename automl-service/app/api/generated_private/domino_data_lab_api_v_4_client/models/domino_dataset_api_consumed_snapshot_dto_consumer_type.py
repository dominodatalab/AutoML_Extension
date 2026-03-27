from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_dataset_api_consumed_snapshot_dto_consumer_type_entry_name import (
    DominoDatasetApiConsumedSnapshotDtoConsumerTypeEntryName,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoDatasetApiConsumedSnapshotDtoConsumerType")


@_attrs_define
class DominoDatasetApiConsumedSnapshotDtoConsumerType:
    """
    Attributes:
        entry_name (DominoDatasetApiConsumedSnapshotDtoConsumerTypeEntryName | Unset):
    """

    entry_name: DominoDatasetApiConsumedSnapshotDtoConsumerTypeEntryName | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entry_name: str | Unset = UNSET
        if not isinstance(self.entry_name, Unset):
            entry_name = self.entry_name.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entry_name is not UNSET:
            field_dict["entryName"] = entry_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _entry_name = d.pop("entryName", UNSET)
        entry_name: DominoDatasetApiConsumedSnapshotDtoConsumerTypeEntryName | Unset
        if isinstance(_entry_name, Unset):
            entry_name = UNSET
        else:
            entry_name = DominoDatasetApiConsumedSnapshotDtoConsumerTypeEntryName(_entry_name)

        domino_dataset_api_consumed_snapshot_dto_consumer_type = cls(
            entry_name=entry_name,
        )

        domino_dataset_api_consumed_snapshot_dto_consumer_type.additional_properties = d
        return domino_dataset_api_consumed_snapshot_dto_consumer_type

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
