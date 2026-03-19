from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dataset_rw_grant_v1 import DatasetRwGrantV1
    from ..models.metadata_v1 import MetadataV1


T = TypeVar("T", bound="DatasetRwGrantEnvelopeV1")


@_attrs_define
class DatasetRwGrantEnvelopeV1:
    """
    Attributes:
        grants (list[DatasetRwGrantV1]):
        metadata (MetadataV1):
    """

    grants: list[DatasetRwGrantV1]
    metadata: MetadataV1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grants = []
        for grants_item_data in self.grants:
            grants_item = grants_item_data.to_dict()
            grants.append(grants_item)

        metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "grants": grants,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_rw_grant_v1 import DatasetRwGrantV1
        from ..models.metadata_v1 import MetadataV1

        d = dict(src_dict)
        grants = []
        _grants = d.pop("grants")
        for grants_item_data in _grants:
            grants_item = DatasetRwGrantV1.from_dict(grants_item_data)

            grants.append(grants_item)

        metadata = MetadataV1.from_dict(d.pop("metadata"))

        dataset_rw_grant_envelope_v1 = cls(
            grants=grants,
            metadata=metadata,
        )

        dataset_rw_grant_envelope_v1.additional_properties = d
        return dataset_rw_grant_envelope_v1

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
