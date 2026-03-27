from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sync_operation_type import SyncOperationType

T = TypeVar("T", bound="DominoProvenanceApiSyncOperationInfo")


@_attrs_define
class DominoProvenanceApiSyncOperationInfo:
    """
    Attributes:
        sync_operation_id (str):
        sync_operation_type (SyncOperationType): Type of sync operation taking place
    """

    sync_operation_id: str
    sync_operation_type: SyncOperationType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sync_operation_id = self.sync_operation_id

        sync_operation_type = self.sync_operation_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "syncOperationId": sync_operation_id,
                "syncOperationType": sync_operation_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sync_operation_id = d.pop("syncOperationId")

        sync_operation_type = SyncOperationType(d.pop("syncOperationType"))

        domino_provenance_api_sync_operation_info = cls(
            sync_operation_id=sync_operation_id,
            sync_operation_type=sync_operation_type,
        )

        domino_provenance_api_sync_operation_info.additional_properties = d
        return domino_provenance_api_sync_operation_info

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
