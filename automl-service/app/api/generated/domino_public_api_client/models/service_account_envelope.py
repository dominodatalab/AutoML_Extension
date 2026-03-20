from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.metadata_v1 import MetadataV1
    from ..models.service_account import ServiceAccount


T = TypeVar("T", bound="ServiceAccountEnvelope")


@_attrs_define
class ServiceAccountEnvelope:
    """
    Attributes:
        metadata (MetadataV1):
        service_account (ServiceAccount):
    """

    metadata: MetadataV1
    service_account: ServiceAccount
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metadata = self.metadata.to_dict()

        service_account = self.service_account.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metadata": metadata,
                "serviceAccount": service_account,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata_v1 import MetadataV1
        from ..models.service_account import ServiceAccount

        d = dict(src_dict)
        metadata = MetadataV1.from_dict(d.pop("metadata"))

        service_account = ServiceAccount.from_dict(d.pop("serviceAccount"))

        service_account_envelope = cls(
            metadata=metadata,
            service_account=service_account,
        )

        service_account_envelope.additional_properties = d
        return service_account_envelope

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
