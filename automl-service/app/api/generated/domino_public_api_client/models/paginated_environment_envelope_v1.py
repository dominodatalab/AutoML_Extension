from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.environment_v1 import EnvironmentV1
    from ..models.paginated_metadata_v1 import PaginatedMetadataV1


T = TypeVar("T", bound="PaginatedEnvironmentEnvelopeV1")


@_attrs_define
class PaginatedEnvironmentEnvelopeV1:
    """
    Attributes:
        environments (list[EnvironmentV1]):
        metadata (PaginatedMetadataV1):
    """

    environments: list[EnvironmentV1]
    metadata: PaginatedMetadataV1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        environments = []
        for environments_item_data in self.environments:
            environments_item = environments_item_data.to_dict()
            environments.append(environments_item)

        metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "environments": environments,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.environment_v1 import EnvironmentV1
        from ..models.paginated_metadata_v1 import PaginatedMetadataV1

        d = dict(src_dict)
        environments = []
        _environments = d.pop("environments")
        for environments_item_data in _environments:
            environments_item = EnvironmentV1.from_dict(environments_item_data)

            environments.append(environments_item)

        metadata = PaginatedMetadataV1.from_dict(d.pop("metadata"))

        paginated_environment_envelope_v1 = cls(
            environments=environments,
            metadata=metadata,
        )

        paginated_environment_envelope_v1.additional_properties = d
        return paginated_environment_envelope_v1

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
