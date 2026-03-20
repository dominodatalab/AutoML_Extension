from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dataset_rw_role_v1 import DatasetRwRoleV1

T = TypeVar("T", bound="DatasetRwGrantV1")


@_attrs_define
class DatasetRwGrantV1:
    """
    Attributes:
        target_id (str): ID of the user within the grant
        target_role (DatasetRwRoleV1): Role that the user will assume in the dataset. Note that organizations cannot be
            dataset Owners
    """

    target_id: str
    target_role: DatasetRwRoleV1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_id = self.target_id

        target_role = self.target_role.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "targetId": target_id,
                "targetRole": target_role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_id = d.pop("targetId")

        target_role = DatasetRwRoleV1(d.pop("targetRole"))

        dataset_rw_grant_v1 = cls(
            target_id=target_id,
            target_role=target_role,
        )

        dataset_rw_grant_v1.additional_properties = d
        return dataset_rw_grant_v1

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
