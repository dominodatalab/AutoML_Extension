from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.paginated_metadata_v1 import PaginatedMetadataV1
    from ..models.user_v1 import UserV1


T = TypeVar("T", bound="PaginatedUserEnvelopeV1")


@_attrs_define
class PaginatedUserEnvelopeV1:
    """
    Attributes:
        metadata (PaginatedMetadataV1):
        users (list[UserV1]):
    """

    metadata: PaginatedMetadataV1
    users: list[UserV1]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metadata = self.metadata.to_dict()

        users = []
        for users_item_data in self.users:
            users_item = users_item_data.to_dict()
            users.append(users_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metadata": metadata,
                "users": users,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paginated_metadata_v1 import PaginatedMetadataV1
        from ..models.user_v1 import UserV1

        d = dict(src_dict)
        metadata = PaginatedMetadataV1.from_dict(d.pop("metadata"))

        users = []
        _users = d.pop("users")
        for users_item_data in _users:
            users_item = UserV1.from_dict(users_item_data)

            users.append(users_item)

        paginated_user_envelope_v1 = cls(
            metadata=metadata,
            users=users,
        )

        paginated_user_envelope_v1.additional_properties = d
        return paginated_user_envelope_v1

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
