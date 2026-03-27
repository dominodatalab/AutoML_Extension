from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoAdminInterfaceGovernanceSCESettings")


@_attrs_define
class DominoAdminInterfaceGovernanceSCESettings:
    """
    Attributes:
        bundle (None | str | Unset):
        policy (None | str | Unset):
    """

    bundle: None | str | Unset = UNSET
    policy: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bundle: None | str | Unset
        if isinstance(self.bundle, Unset):
            bundle = UNSET
        else:
            bundle = self.bundle

        policy: None | str | Unset
        if isinstance(self.policy, Unset):
            policy = UNSET
        else:
            policy = self.policy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bundle is not UNSET:
            field_dict["bundle"] = bundle
        if policy is not UNSET:
            field_dict["policy"] = policy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_bundle(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bundle = _parse_bundle(d.pop("bundle", UNSET))

        def _parse_policy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        policy = _parse_policy(d.pop("policy", UNSET))

        domino_admin_interface_governance_sce_settings = cls(
            bundle=bundle,
            policy=policy,
        )

        domino_admin_interface_governance_sce_settings.additional_properties = d
        return domino_admin_interface_governance_sce_settings

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
