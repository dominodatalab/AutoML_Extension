from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_workspace_api_ssh_valid_principal_dto import DominoWorkspaceApiSshValidPrincipalDto


T = TypeVar("T", bound="DominoWorkspaceApiSshSshSignatureRequestDto")


@_attrs_define
class DominoWorkspaceApiSshSshSignatureRequestDto:
    """
    Attributes:
        public_key (str):
        valid_principals (list[DominoWorkspaceApiSshValidPrincipalDto]):
    """

    public_key: str
    valid_principals: list[DominoWorkspaceApiSshValidPrincipalDto]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        public_key = self.public_key

        valid_principals = []
        for valid_principals_item_data in self.valid_principals:
            valid_principals_item = valid_principals_item_data.to_dict()
            valid_principals.append(valid_principals_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "publicKey": public_key,
                "validPrincipals": valid_principals,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_workspace_api_ssh_valid_principal_dto import DominoWorkspaceApiSshValidPrincipalDto

        d = dict(src_dict)
        public_key = d.pop("publicKey")

        valid_principals = []
        _valid_principals = d.pop("validPrincipals")
        for valid_principals_item_data in _valid_principals:
            valid_principals_item = DominoWorkspaceApiSshValidPrincipalDto.from_dict(valid_principals_item_data)

            valid_principals.append(valid_principals_item)

        domino_workspace_api_ssh_ssh_signature_request_dto = cls(
            public_key=public_key,
            valid_principals=valid_principals,
        )

        domino_workspace_api_ssh_ssh_signature_request_dto.additional_properties = d
        return domino_workspace_api_ssh_ssh_signature_request_dto

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
