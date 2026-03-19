from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelEndpointCollaboratorV1")


@_attrs_define
class ModelEndpointCollaboratorV1:
    """
    Attributes:
        name (str | Unset): The name of the entity Example: John Doe.
        organization_id (str | Unset): The organization ID of the entity Example: 62313ce67a0af0281c01a6a5.
        user_id (str | Unset): The user ID of the entity Example: 62313ce67a0af0281c01a6a5.
    """

    name: str | Unset = UNSET
    organization_id: str | Unset = UNSET
    user_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        organization_id = self.organization_id

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        organization_id = d.pop("organizationId", UNSET)

        user_id = d.pop("userId", UNSET)

        model_endpoint_collaborator_v1 = cls(
            name=name,
            organization_id=organization_id,
            user_id=user_id,
        )

        model_endpoint_collaborator_v1.additional_properties = d
        return model_endpoint_collaborator_v1

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
