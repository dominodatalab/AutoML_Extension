from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_api_source_type import ModelApiSourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelApiSource")


@_attrs_define
class ModelApiSource:
    """
    Attributes:
        type_ (ModelApiSourceType): The type of source of the Model API.
        exclude_files (list[str] | Unset): The files excluded from the Model API.
        file (str | Unset): The name of the source file of the model served by the Model API.
        function (str | Unset): The function used to call the model served by the Model API.
        registered_model_name (str | Unset): The name of the registered model served by the Model API.
        registered_model_version (int | Unset): The version of the registered model served by the Model API.
    """

    type_: ModelApiSourceType
    exclude_files: list[str] | Unset = UNSET
    file: str | Unset = UNSET
    function: str | Unset = UNSET
    registered_model_name: str | Unset = UNSET
    registered_model_version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        exclude_files: list[str] | Unset = UNSET
        if not isinstance(self.exclude_files, Unset):
            exclude_files = self.exclude_files

        file = self.file

        function = self.function

        registered_model_name = self.registered_model_name

        registered_model_version = self.registered_model_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if exclude_files is not UNSET:
            field_dict["excludeFiles"] = exclude_files
        if file is not UNSET:
            field_dict["file"] = file
        if function is not UNSET:
            field_dict["function"] = function
        if registered_model_name is not UNSET:
            field_dict["registeredModelName"] = registered_model_name
        if registered_model_version is not UNSET:
            field_dict["registeredModelVersion"] = registered_model_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = ModelApiSourceType(d.pop("type"))

        exclude_files = cast(list[str], d.pop("excludeFiles", UNSET))

        file = d.pop("file", UNSET)

        function = d.pop("function", UNSET)

        registered_model_name = d.pop("registeredModelName", UNSET)

        registered_model_version = d.pop("registeredModelVersion", UNSET)

        model_api_source = cls(
            type_=type_,
            exclude_files=exclude_files,
            file=file,
            function=function,
            registered_model_name=registered_model_name,
            registered_model_version=registered_model_version,
        )

        model_api_source.additional_properties = d
        return model_api_source

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
