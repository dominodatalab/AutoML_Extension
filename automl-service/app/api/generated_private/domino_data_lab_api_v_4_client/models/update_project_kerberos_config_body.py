from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="UpdateProjectKerberosConfigBody")


@_attrs_define
class UpdateProjectKerberosConfigBody:
    """
    Attributes:
        kerberos_mode (str):
        upfile (File | Unset): The file to upload
        principal (str | Unset):
        keytab_file_name (str | Unset):
    """

    kerberos_mode: str
    upfile: File | Unset = UNSET
    principal: str | Unset = UNSET
    keytab_file_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kerberos_mode = self.kerberos_mode

        upfile: FileTypes | Unset = UNSET
        if not isinstance(self.upfile, Unset):
            upfile = self.upfile.to_tuple()

        principal = self.principal

        keytab_file_name = self.keytab_file_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kerberosMode": kerberos_mode,
            }
        )
        if upfile is not UNSET:
            field_dict["upfile"] = upfile
        if principal is not UNSET:
            field_dict["principal"] = principal
        if keytab_file_name is not UNSET:
            field_dict["keytabFileName"] = keytab_file_name

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("kerberosMode", (None, str(self.kerberos_mode).encode(), "text/plain")))

        if not isinstance(self.upfile, Unset):
            files.append(("upfile", self.upfile.to_tuple()))

        if not isinstance(self.principal, Unset):
            files.append(("principal", (None, str(self.principal).encode(), "text/plain")))

        if not isinstance(self.keytab_file_name, Unset):
            files.append(("keytabFileName", (None, str(self.keytab_file_name).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kerberos_mode = d.pop("kerberosMode")

        _upfile = d.pop("upfile", UNSET)
        upfile: File | Unset
        if isinstance(_upfile, Unset):
            upfile = UNSET
        else:
            upfile = File(payload=BytesIO(_upfile))

        principal = d.pop("principal", UNSET)

        keytab_file_name = d.pop("keytabFileName", UNSET)

        update_project_kerberos_config_body = cls(
            kerberos_mode=kerberos_mode,
            upfile=upfile,
            principal=principal,
            keytab_file_name=keytab_file_name,
        )

        update_project_kerberos_config_body.additional_properties = d
        return update_project_kerberos_config_body

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
