from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.paginated_metadata_v1 import PaginatedMetadataV1
    from ..models.service_account import ServiceAccount


T = TypeVar("T", bound="PaginatedServiceAccountEnvelope")


@_attrs_define
class PaginatedServiceAccountEnvelope:
    """
    Attributes:
        metadata (PaginatedMetadataV1):
        service_accounts (list[ServiceAccount]):
    """

    metadata: PaginatedMetadataV1
    service_accounts: list[ServiceAccount]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metadata = self.metadata.to_dict()

        service_accounts = []
        for service_accounts_item_data in self.service_accounts:
            service_accounts_item = service_accounts_item_data.to_dict()
            service_accounts.append(service_accounts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metadata": metadata,
                "serviceAccounts": service_accounts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paginated_metadata_v1 import PaginatedMetadataV1
        from ..models.service_account import ServiceAccount

        d = dict(src_dict)
        metadata = PaginatedMetadataV1.from_dict(d.pop("metadata"))

        service_accounts = []
        _service_accounts = d.pop("serviceAccounts")
        for service_accounts_item_data in _service_accounts:
            service_accounts_item = ServiceAccount.from_dict(service_accounts_item_data)

            service_accounts.append(service_accounts_item)

        paginated_service_account_envelope = cls(
            metadata=metadata,
            service_accounts=service_accounts,
        )

        paginated_service_account_envelope.additional_properties = d
        return paginated_service_account_envelope

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
