from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_filesync_sync_relative_file_path import DominoFilesyncSyncRelativeFilePath


T = TypeVar("T", bound="DominoModelmanagerApiModelVersionSummary")


@_attrs_define
class DominoModelmanagerApiModelVersionSummary:
    """
    Attributes:
        id (str):
        file (DominoFilesyncSyncRelativeFilePath | Unset):
        function (None | str | Unset):
        registered_model_name (None | str | Unset):
        registered_model_version (int | None | Unset):
    """

    id: str
    file: DominoFilesyncSyncRelativeFilePath | Unset = UNSET
    function: None | str | Unset = UNSET
    registered_model_name: None | str | Unset = UNSET
    registered_model_version: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        file: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_dict()

        function: None | str | Unset
        if isinstance(self.function, Unset):
            function = UNSET
        else:
            function = self.function

        registered_model_name: None | str | Unset
        if isinstance(self.registered_model_name, Unset):
            registered_model_name = UNSET
        else:
            registered_model_name = self.registered_model_name

        registered_model_version: int | None | Unset
        if isinstance(self.registered_model_version, Unset):
            registered_model_version = UNSET
        else:
            registered_model_version = self.registered_model_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
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
        from ..models.domino_filesync_sync_relative_file_path import DominoFilesyncSyncRelativeFilePath

        d = dict(src_dict)
        id = d.pop("id")

        _file = d.pop("file", UNSET)
        file: DominoFilesyncSyncRelativeFilePath | Unset
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = DominoFilesyncSyncRelativeFilePath.from_dict(_file)

        def _parse_function(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        function = _parse_function(d.pop("function", UNSET))

        def _parse_registered_model_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registered_model_name = _parse_registered_model_name(d.pop("registeredModelName", UNSET))

        def _parse_registered_model_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        registered_model_version = _parse_registered_model_version(d.pop("registeredModelVersion", UNSET))

        domino_modelmanager_api_model_version_summary = cls(
            id=id,
            file=file,
            function=function,
            registered_model_name=registered_model_name,
            registered_model_version=registered_model_version,
        )

        domino_modelmanager_api_model_version_summary.additional_properties = d
        return domino_modelmanager_api_model_version_summary

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
