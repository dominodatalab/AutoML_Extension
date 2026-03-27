from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_dataset_api_consumed_snapshot_dto_consumer_type import (
        DominoDatasetApiConsumedSnapshotDtoConsumerType,
    )


T = TypeVar("T", bound="DominoDatasetApiConsumedSnapshotDto")


@_attrs_define
class DominoDatasetApiConsumedSnapshotDto:
    """
    Attributes:
        consumer_type (DominoDatasetApiConsumedSnapshotDtoConsumerType):
        consumer_id (str):
        dataset_id (str):
        dataset_name (str):
        snapshot_id (str):
        snapshot_version (int):
        timestamp (int):
    """

    consumer_type: DominoDatasetApiConsumedSnapshotDtoConsumerType
    consumer_id: str
    dataset_id: str
    dataset_name: str
    snapshot_id: str
    snapshot_version: int
    timestamp: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        consumer_type = self.consumer_type.to_dict()

        consumer_id = self.consumer_id

        dataset_id = self.dataset_id

        dataset_name = self.dataset_name

        snapshot_id = self.snapshot_id

        snapshot_version = self.snapshot_version

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "consumerType": consumer_type,
                "consumerId": consumer_id,
                "datasetId": dataset_id,
                "datasetName": dataset_name,
                "snapshotId": snapshot_id,
                "snapshotVersion": snapshot_version,
                "timestamp": timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_dataset_api_consumed_snapshot_dto_consumer_type import (
            DominoDatasetApiConsumedSnapshotDtoConsumerType,
        )

        d = dict(src_dict)
        consumer_type = DominoDatasetApiConsumedSnapshotDtoConsumerType.from_dict(d.pop("consumerType"))

        consumer_id = d.pop("consumerId")

        dataset_id = d.pop("datasetId")

        dataset_name = d.pop("datasetName")

        snapshot_id = d.pop("snapshotId")

        snapshot_version = d.pop("snapshotVersion")

        timestamp = d.pop("timestamp")

        domino_dataset_api_consumed_snapshot_dto = cls(
            consumer_type=consumer_type,
            consumer_id=consumer_id,
            dataset_id=dataset_id,
            dataset_name=dataset_name,
            snapshot_id=snapshot_id,
            snapshot_version=snapshot_version,
            timestamp=timestamp,
        )

        domino_dataset_api_consumed_snapshot_dto.additional_properties = d
        return domino_dataset_api_consumed_snapshot_dto

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
