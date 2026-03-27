from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoLauncherjobApiLauncherJobUploadedFile")


@_attrs_define
class DominoLauncherjobApiLauncherJobUploadedFile:
    """
    Attributes:
        parameter_name (str):
        file_name (str):
        temp_file_base_64_encoding (str):
    """

    parameter_name: str
    file_name: str
    temp_file_base_64_encoding: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parameter_name = self.parameter_name

        file_name = self.file_name

        temp_file_base_64_encoding = self.temp_file_base_64_encoding

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parameterName": parameter_name,
                "fileName": file_name,
                "tempFileBase64Encoding": temp_file_base_64_encoding,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        parameter_name = d.pop("parameterName")

        file_name = d.pop("fileName")

        temp_file_base_64_encoding = d.pop("tempFileBase64Encoding")

        domino_launcherjob_api_launcher_job_uploaded_file = cls(
            parameter_name=parameter_name,
            file_name=file_name,
            temp_file_base_64_encoding=temp_file_base_64_encoding,
        )

        domino_launcherjob_api_launcher_job_uploaded_file.additional_properties = d
        return domino_launcherjob_api_launcher_job_uploaded_file

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
