from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dataset_rw_grant_details_v1 import DatasetRwGrantDetailsV1
    from ..models.metadata_v1 import MetadataV1


T = TypeVar("T", bound="DatasetRwGrantDetailsEnvelopeV1")


@_attrs_define
class DatasetRwGrantDetailsEnvelopeV1:
    """
    Attributes:
        grant_details (list[DatasetRwGrantDetailsV1]):
        metadata (MetadataV1):
    """

    grant_details: list[DatasetRwGrantDetailsV1]
    metadata: MetadataV1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grant_details = []
        for grant_details_item_data in self.grant_details:
            grant_details_item = grant_details_item_data.to_dict()
            grant_details.append(grant_details_item)

        metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "grantDetails": grant_details,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_rw_grant_details_v1 import DatasetRwGrantDetailsV1
        from ..models.metadata_v1 import MetadataV1

        d = dict(src_dict)
        grant_details = []
        _grant_details = d.pop("grantDetails")
        for grant_details_item_data in _grant_details:
            grant_details_item = DatasetRwGrantDetailsV1.from_dict(grant_details_item_data)

            grant_details.append(grant_details_item)

        metadata = MetadataV1.from_dict(d.pop("metadata"))

        dataset_rw_grant_details_envelope_v1 = cls(
            grant_details=grant_details,
            metadata=metadata,
        )

        dataset_rw_grant_details_envelope_v1.additional_properties = d
        return dataset_rw_grant_details_envelope_v1

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
