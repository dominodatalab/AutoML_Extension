from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.data_source_envelope_v1 import DataSourceEnvelopeV1
    from ..models.paginated_metadata_v1 import PaginatedMetadataV1


T = TypeVar("T", bound="PaginatedDataSourceEnvelopeV1")


@_attrs_define
class PaginatedDataSourceEnvelopeV1:
    """
    Attributes:
        data_sources (list[DataSourceEnvelopeV1]):
        metadata (PaginatedMetadataV1):
    """

    data_sources: list[DataSourceEnvelopeV1]
    metadata: PaginatedMetadataV1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_sources = []
        for data_sources_item_data in self.data_sources:
            data_sources_item = data_sources_item_data.to_dict()
            data_sources.append(data_sources_item)

        metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataSources": data_sources,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_source_envelope_v1 import DataSourceEnvelopeV1
        from ..models.paginated_metadata_v1 import PaginatedMetadataV1

        d = dict(src_dict)
        data_sources = []
        _data_sources = d.pop("dataSources")
        for data_sources_item_data in _data_sources:
            data_sources_item = DataSourceEnvelopeV1.from_dict(data_sources_item_data)

            data_sources.append(data_sources_item)

        metadata = PaginatedMetadataV1.from_dict(d.pop("metadata"))

        paginated_data_source_envelope_v1 = cls(
            data_sources=data_sources,
            metadata=metadata,
        )

        paginated_data_source_envelope_v1.additional_properties = d
        return paginated_data_source_envelope_v1

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
