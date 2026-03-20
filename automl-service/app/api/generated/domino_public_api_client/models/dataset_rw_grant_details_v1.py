from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dataset_rw_role_v1 import DatasetRwRoleV1

T = TypeVar("T", bound="DatasetRwGrantDetailsV1")


@_attrs_define
class DatasetRwGrantDetailsV1:
    """
    Attributes:
        is_organization (bool): If target id is an organization
        target_id (str): ID of the user within the grant
        target_name (str): Username of user within the grant
        target_role (DatasetRwRoleV1): Role that the user will assume in the dataset. Note that organizations cannot be
            dataset Owners
    """

    is_organization: bool
    target_id: str
    target_name: str
    target_role: DatasetRwRoleV1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_organization = self.is_organization

        target_id = self.target_id

        target_name = self.target_name

        target_role = self.target_role.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isOrganization": is_organization,
                "targetId": target_id,
                "targetName": target_name,
                "targetRole": target_role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_organization = d.pop("isOrganization")

        target_id = d.pop("targetId")

        target_name = d.pop("targetName")

        target_role = DatasetRwRoleV1(d.pop("targetRole"))

        dataset_rw_grant_details_v1 = cls(
            is_organization=is_organization,
            target_id=target_id,
            target_name=target_name,
            target_role=target_role,
        )

        dataset_rw_grant_details_v1.additional_properties = d
        return dataset_rw_grant_details_v1

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
