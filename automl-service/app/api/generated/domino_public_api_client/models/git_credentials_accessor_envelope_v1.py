from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.git_credentials_accessor_v1 import GitCredentialsAccessorV1
    from ..models.metadata_v1 import MetadataV1


T = TypeVar("T", bound="GitCredentialsAccessorEnvelopeV1")


@_attrs_define
class GitCredentialsAccessorEnvelopeV1:
    """
    Attributes:
        credential (GitCredentialsAccessorV1):
        metadata (MetadataV1):
    """

    credential: GitCredentialsAccessorV1
    metadata: MetadataV1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credential = self.credential.to_dict()

        metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credential": credential,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.git_credentials_accessor_v1 import GitCredentialsAccessorV1
        from ..models.metadata_v1 import MetadataV1

        d = dict(src_dict)
        credential = GitCredentialsAccessorV1.from_dict(d.pop("credential"))

        metadata = MetadataV1.from_dict(d.pop("metadata"))

        git_credentials_accessor_envelope_v1 = cls(
            credential=credential,
            metadata=metadata,
        )

        git_credentials_accessor_envelope_v1.additional_properties = d
        return git_credentials_accessor_envelope_v1

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
