from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.paginated_metadata_v1 import PaginatedMetadataV1
    from ..models.snapshot_details_v1 import SnapshotDetailsV1


T = TypeVar("T", bound="PaginatedSnapshotEnvelopeV1")


@_attrs_define
class PaginatedSnapshotEnvelopeV1:
    """
    Attributes:
        metadata (PaginatedMetadataV1):
        snapshots (list[SnapshotDetailsV1]):
    """

    metadata: PaginatedMetadataV1
    snapshots: list[SnapshotDetailsV1]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metadata = self.metadata.to_dict()

        snapshots = []
        for snapshots_item_data in self.snapshots:
            snapshots_item = snapshots_item_data.to_dict()
            snapshots.append(snapshots_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metadata": metadata,
                "snapshots": snapshots,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paginated_metadata_v1 import PaginatedMetadataV1
        from ..models.snapshot_details_v1 import SnapshotDetailsV1

        d = dict(src_dict)
        metadata = PaginatedMetadataV1.from_dict(d.pop("metadata"))

        snapshots = []
        _snapshots = d.pop("snapshots")
        for snapshots_item_data in _snapshots:
            snapshots_item = SnapshotDetailsV1.from_dict(snapshots_item_data)

            snapshots.append(snapshots_item)

        paginated_snapshot_envelope_v1 = cls(
            metadata=metadata,
            snapshots=snapshots,
        )

        paginated_snapshot_envelope_v1.additional_properties = d
        return paginated_snapshot_envelope_v1

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
