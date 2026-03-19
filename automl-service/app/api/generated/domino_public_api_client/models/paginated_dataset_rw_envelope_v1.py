from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dataset_rw_details_v1 import DatasetRwDetailsV1
    from ..models.paginated_metadata_v1 import PaginatedMetadataV1


T = TypeVar("T", bound="PaginatedDatasetRwEnvelopeV1")


@_attrs_define
class PaginatedDatasetRwEnvelopeV1:
    """
    Attributes:
        datasets (list[DatasetRwDetailsV1]):
        metadata (PaginatedMetadataV1):
    """

    datasets: list[DatasetRwDetailsV1]
    metadata: PaginatedMetadataV1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        datasets = []
        for datasets_item_data in self.datasets:
            datasets_item = datasets_item_data.to_dict()
            datasets.append(datasets_item)

        metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "datasets": datasets,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_rw_details_v1 import DatasetRwDetailsV1
        from ..models.paginated_metadata_v1 import PaginatedMetadataV1

        d = dict(src_dict)
        datasets = []
        _datasets = d.pop("datasets")
        for datasets_item_data in _datasets:
            datasets_item = DatasetRwDetailsV1.from_dict(datasets_item_data)

            datasets.append(datasets_item)

        metadata = PaginatedMetadataV1.from_dict(d.pop("metadata"))

        paginated_dataset_rw_envelope_v1 = cls(
            datasets=datasets,
            metadata=metadata,
        )

        paginated_dataset_rw_envelope_v1.additional_properties = d
        return paginated_dataset_rw_envelope_v1

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
