from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoCommonRunInterfacesNewRunGitRefDto")


@_attrs_define
class DominoCommonRunInterfacesNewRunGitRefDto:
    """
    Attributes:
        ref_type (str):
        ref_value (None | str | Unset):
    """

    ref_type: str
    ref_value: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ref_type = self.ref_type

        ref_value: None | str | Unset
        if isinstance(self.ref_value, Unset):
            ref_value = UNSET
        else:
            ref_value = self.ref_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "refType": ref_type,
            }
        )
        if ref_value is not UNSET:
            field_dict["refValue"] = ref_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ref_type = d.pop("refType")

        def _parse_ref_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ref_value = _parse_ref_value(d.pop("refValue", UNSET))

        domino_common_run_interfaces_new_run_git_ref_dto = cls(
            ref_type=ref_type,
            ref_value=ref_value,
        )

        domino_common_run_interfaces_new_run_git_ref_dto.additional_properties = d
        return domino_common_run_interfaces_new_run_git_ref_dto

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
