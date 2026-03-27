from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoEnvironmentsApiEnvironmentPatch")


@_attrs_define
class DominoEnvironmentsApiEnvironmentPatch:
    """
    Attributes:
        assign_latest_revision_as_active (bool | None | Unset):
    """

    assign_latest_revision_as_active: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assign_latest_revision_as_active: bool | None | Unset
        if isinstance(self.assign_latest_revision_as_active, Unset):
            assign_latest_revision_as_active = UNSET
        else:
            assign_latest_revision_as_active = self.assign_latest_revision_as_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assign_latest_revision_as_active is not UNSET:
            field_dict["assignLatestRevisionAsActive"] = assign_latest_revision_as_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_assign_latest_revision_as_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        assign_latest_revision_as_active = _parse_assign_latest_revision_as_active(
            d.pop("assignLatestRevisionAsActive", UNSET)
        )

        domino_environments_api_environment_patch = cls(
            assign_latest_revision_as_active=assign_latest_revision_as_active,
        )

        domino_environments_api_environment_patch.additional_properties = d
        return domino_environments_api_environment_patch

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
