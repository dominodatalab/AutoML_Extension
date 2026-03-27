from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoProjectsApiProjectKerberosConfig")


@_attrs_define
class DominoProjectsApiProjectKerberosConfig:
    """
    Attributes:
        kerberos_mode (str):
        principal (None | str | Unset):
        keytab_file_name (None | str | Unset):
    """

    kerberos_mode: str
    principal: None | str | Unset = UNSET
    keytab_file_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kerberos_mode = self.kerberos_mode

        principal: None | str | Unset
        if isinstance(self.principal, Unset):
            principal = UNSET
        else:
            principal = self.principal

        keytab_file_name: None | str | Unset
        if isinstance(self.keytab_file_name, Unset):
            keytab_file_name = UNSET
        else:
            keytab_file_name = self.keytab_file_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kerberosMode": kerberos_mode,
            }
        )
        if principal is not UNSET:
            field_dict["principal"] = principal
        if keytab_file_name is not UNSET:
            field_dict["keytabFileName"] = keytab_file_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kerberos_mode = d.pop("kerberosMode")

        def _parse_principal(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        principal = _parse_principal(d.pop("principal", UNSET))

        def _parse_keytab_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        keytab_file_name = _parse_keytab_file_name(d.pop("keytabFileName", UNSET))

        domino_projects_api_project_kerberos_config = cls(
            kerberos_mode=kerberos_mode,
            principal=principal,
            keytab_file_name=keytab_file_name,
        )

        domino_projects_api_project_kerberos_config.additional_properties = d
        return domino_projects_api_project_kerberos_config

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
