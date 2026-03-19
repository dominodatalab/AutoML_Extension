from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.paginated_metadata_v1 import PaginatedMetadataV1
    from ..models.registered_model_version_overview_v2 import RegisteredModelVersionOverviewV2


T = TypeVar("T", bound="PaginatedRegisteredModelVersionOverviewEnvelopeV2")


@_attrs_define
class PaginatedRegisteredModelVersionOverviewEnvelopeV2:
    """
    Attributes:
        items (list[RegisteredModelVersionOverviewV2]):
        metadata (PaginatedMetadataV1):
    """

    items: list[RegisteredModelVersionOverviewV2]
    metadata: PaginatedMetadataV1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paginated_metadata_v1 import PaginatedMetadataV1
        from ..models.registered_model_version_overview_v2 import RegisteredModelVersionOverviewV2

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = RegisteredModelVersionOverviewV2.from_dict(items_item_data)

            items.append(items_item)

        metadata = PaginatedMetadataV1.from_dict(d.pop("metadata"))

        paginated_registered_model_version_overview_envelope_v2 = cls(
            items=items,
            metadata=metadata,
        )

        paginated_registered_model_version_overview_envelope_v2.additional_properties = d
        return paginated_registered_model_version_overview_envelope_v2

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
