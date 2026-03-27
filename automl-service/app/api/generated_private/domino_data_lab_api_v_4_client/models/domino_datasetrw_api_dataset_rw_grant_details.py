from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_datasetrw_api_dataset_rw_grant_details_target_role import (
    DominoDatasetrwApiDatasetRwGrantDetailsTargetRole,
)

T = TypeVar("T", bound="DominoDatasetrwApiDatasetRwGrantDetails")


@_attrs_define
class DominoDatasetrwApiDatasetRwGrantDetails:
    """
    Attributes:
        target_id (str):
        target_name (str):
        target_role (DominoDatasetrwApiDatasetRwGrantDetailsTargetRole):
        is_organization (bool):
    """

    target_id: str
    target_name: str
    target_role: DominoDatasetrwApiDatasetRwGrantDetailsTargetRole
    is_organization: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_id = self.target_id

        target_name = self.target_name

        target_role = self.target_role.value

        is_organization = self.is_organization

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "targetId": target_id,
                "targetName": target_name,
                "targetRole": target_role,
                "isOrganization": is_organization,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_id = d.pop("targetId")

        target_name = d.pop("targetName")

        target_role = DominoDatasetrwApiDatasetRwGrantDetailsTargetRole(d.pop("targetRole"))

        is_organization = d.pop("isOrganization")

        domino_datasetrw_api_dataset_rw_grant_details = cls(
            target_id=target_id,
            target_name=target_name,
            target_role=target_role,
            is_organization=is_organization,
        )

        domino_datasetrw_api_dataset_rw_grant_details.additional_properties = d
        return domino_datasetrw_api_dataset_rw_grant_details

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
