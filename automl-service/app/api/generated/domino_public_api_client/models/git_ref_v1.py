from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GitRefV1")


@_attrs_define
class GitRefV1:
    """
    Attributes:
        ref_type (str): The type of git reference being used. Example: head | commitId | tags | branches.
        value (str | Unset): The value of the git reference. Only necessary for relevant git ref types. Example: my-
            test-branch.
    """

    ref_type: str
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ref_type = self.ref_type

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "refType": ref_type,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ref_type = d.pop("refType")

        value = d.pop("value", UNSET)

        git_ref_v1 = cls(
            ref_type=ref_type,
            value=value,
        )

        git_ref_v1.additional_properties = d
        return git_ref_v1

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
