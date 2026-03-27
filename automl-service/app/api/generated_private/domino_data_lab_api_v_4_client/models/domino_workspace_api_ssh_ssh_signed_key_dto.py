from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoWorkspaceApiSshSshSignedKeyDto")


@_attrs_define
class DominoWorkspaceApiSshSshSignedKeyDto:
    """
    Attributes:
        signed_key (str):
    """

    signed_key: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        signed_key = self.signed_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "signedKey": signed_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        signed_key = d.pop("signedKey")

        domino_workspace_api_ssh_ssh_signed_key_dto = cls(
            signed_key=signed_key,
        )

        domino_workspace_api_ssh_ssh_signed_key_dto.additional_properties = d
        return domino_workspace_api_ssh_ssh_signed_key_dto

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
