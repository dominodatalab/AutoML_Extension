from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoEnvironmentsApiNewEnvironmentRevisionBase")


@_attrs_define
class DominoEnvironmentsApiNewEnvironmentRevisionBase:
    """
    Attributes:
        image (None | str | Unset):
        base_revision_id (None | str | Unset):
        follow_active_revision_of (None | str | Unset):
    """

    image: None | str | Unset = UNSET
    base_revision_id: None | str | Unset = UNSET
    follow_active_revision_of: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image: None | str | Unset
        if isinstance(self.image, Unset):
            image = UNSET
        else:
            image = self.image

        base_revision_id: None | str | Unset
        if isinstance(self.base_revision_id, Unset):
            base_revision_id = UNSET
        else:
            base_revision_id = self.base_revision_id

        follow_active_revision_of: None | str | Unset
        if isinstance(self.follow_active_revision_of, Unset):
            follow_active_revision_of = UNSET
        else:
            follow_active_revision_of = self.follow_active_revision_of

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image is not UNSET:
            field_dict["image"] = image
        if base_revision_id is not UNSET:
            field_dict["baseRevisionId"] = base_revision_id
        if follow_active_revision_of is not UNSET:
            field_dict["followActiveRevisionOf"] = follow_active_revision_of

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_image(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image = _parse_image(d.pop("image", UNSET))

        def _parse_base_revision_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        base_revision_id = _parse_base_revision_id(d.pop("baseRevisionId", UNSET))

        def _parse_follow_active_revision_of(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        follow_active_revision_of = _parse_follow_active_revision_of(d.pop("followActiveRevisionOf", UNSET))

        domino_environments_api_new_environment_revision_base = cls(
            image=image,
            base_revision_id=base_revision_id,
            follow_active_revision_of=follow_active_revision_of,
        )

        domino_environments_api_new_environment_revision_base.additional_properties = d
        return domino_environments_api_new_environment_revision_base

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
