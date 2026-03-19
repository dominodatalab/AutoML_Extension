from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.paginated_metadata_v1 import PaginatedMetadataV1
    from ..models.service_account_token_details import ServiceAccountTokenDetails


T = TypeVar("T", bound="PaginatedServiceAccountTokenEnvelope")


@_attrs_define
class PaginatedServiceAccountTokenEnvelope:
    """
    Attributes:
        metadata (PaginatedMetadataV1):
        tokens (list[ServiceAccountTokenDetails]):
    """

    metadata: PaginatedMetadataV1
    tokens: list[ServiceAccountTokenDetails]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metadata = self.metadata.to_dict()

        tokens = []
        for tokens_item_data in self.tokens:
            tokens_item = tokens_item_data.to_dict()
            tokens.append(tokens_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metadata": metadata,
                "tokens": tokens,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paginated_metadata_v1 import PaginatedMetadataV1
        from ..models.service_account_token_details import ServiceAccountTokenDetails

        d = dict(src_dict)
        metadata = PaginatedMetadataV1.from_dict(d.pop("metadata"))

        tokens = []
        _tokens = d.pop("tokens")
        for tokens_item_data in _tokens:
            tokens_item = ServiceAccountTokenDetails.from_dict(tokens_item_data)

            tokens.append(tokens_item)

        paginated_service_account_token_envelope = cls(
            metadata=metadata,
            tokens=tokens,
        )

        paginated_service_account_token_envelope.additional_properties = d
        return paginated_service_account_token_envelope

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
