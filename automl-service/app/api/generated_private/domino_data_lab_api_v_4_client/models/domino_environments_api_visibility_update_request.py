from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_environments_api_visibility_update_request_visibility import (
    DominoEnvironmentsApiVisibilityUpdateRequestVisibility,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoEnvironmentsApiVisibilityUpdateRequest")


@_attrs_define
class DominoEnvironmentsApiVisibilityUpdateRequest:
    """
    Attributes:
        visibility (DominoEnvironmentsApiVisibilityUpdateRequestVisibility):
        owner_id (None | str | Unset):
    """

    visibility: DominoEnvironmentsApiVisibilityUpdateRequestVisibility
    owner_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        visibility = self.visibility.value

        owner_id: None | str | Unset
        if isinstance(self.owner_id, Unset):
            owner_id = UNSET
        else:
            owner_id = self.owner_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "visibility": visibility,
            }
        )
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        visibility = DominoEnvironmentsApiVisibilityUpdateRequestVisibility(d.pop("visibility"))

        def _parse_owner_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_id = _parse_owner_id(d.pop("ownerId", UNSET))

        domino_environments_api_visibility_update_request = cls(
            visibility=visibility,
            owner_id=owner_id,
        )

        domino_environments_api_visibility_update_request.additional_properties = d
        return domino_environments_api_visibility_update_request

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
