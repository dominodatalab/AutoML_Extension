from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_filesync_sync_relative_file_path import DominoFilesyncSyncRelativeFilePath
    from ..models.domino_modelmanager_api_model_owner import DominoModelmanagerApiModelOwner


T = TypeVar("T", bound="DominoModelmanagerApiModelVersion")


@_attrs_define
class DominoModelmanagerApiModelVersion:
    """
    Attributes:
        model_version_id (str):
        model_id (str):
        project_id (str):
        commit_id (str):
        exclude_files (list[DominoFilesyncSyncRelativeFilePath]):
        environment_id (str):
        environment_revision_id (str):
        data_plane_id (str):
        created_by (DominoModelmanagerApiModelOwner):
        created (int):
        file (DominoFilesyncSyncRelativeFilePath | Unset):
        function (None | str | Unset):
        registered_model_name (None | str | Unset):
        registered_model_version (int | None | Unset):
        number (int | None | Unset):
    """

    model_version_id: str
    model_id: str
    project_id: str
    commit_id: str
    exclude_files: list[DominoFilesyncSyncRelativeFilePath]
    environment_id: str
    environment_revision_id: str
    data_plane_id: str
    created_by: DominoModelmanagerApiModelOwner
    created: int
    file: DominoFilesyncSyncRelativeFilePath | Unset = UNSET
    function: None | str | Unset = UNSET
    registered_model_name: None | str | Unset = UNSET
    registered_model_version: int | None | Unset = UNSET
    number: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_version_id = self.model_version_id

        model_id = self.model_id

        project_id = self.project_id

        commit_id = self.commit_id

        exclude_files = []
        for exclude_files_item_data in self.exclude_files:
            exclude_files_item = exclude_files_item_data.to_dict()
            exclude_files.append(exclude_files_item)

        environment_id = self.environment_id

        environment_revision_id = self.environment_revision_id

        data_plane_id = self.data_plane_id

        created_by = self.created_by.to_dict()

        created = self.created

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

        number: int | None | Unset
        if isinstance(self.number, Unset):
            number = UNSET
        else:
            number = self.number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modelVersionId": model_version_id,
                "modelId": model_id,
                "projectId": project_id,
                "commitId": commit_id,
                "excludeFiles": exclude_files,
                "environmentId": environment_id,
                "environmentRevisionId": environment_revision_id,
                "dataPlaneId": data_plane_id,
                "createdBy": created_by,
                "created": created,
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
        if number is not UNSET:
            field_dict["number"] = number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_filesync_sync_relative_file_path import DominoFilesyncSyncRelativeFilePath
        from ..models.domino_modelmanager_api_model_owner import DominoModelmanagerApiModelOwner

        d = dict(src_dict)
        model_version_id = d.pop("modelVersionId")

        model_id = d.pop("modelId")

        project_id = d.pop("projectId")

        commit_id = d.pop("commitId")

        exclude_files = []
        _exclude_files = d.pop("excludeFiles")
        for exclude_files_item_data in _exclude_files:
            exclude_files_item = DominoFilesyncSyncRelativeFilePath.from_dict(exclude_files_item_data)

            exclude_files.append(exclude_files_item)

        environment_id = d.pop("environmentId")

        environment_revision_id = d.pop("environmentRevisionId")

        data_plane_id = d.pop("dataPlaneId")

        created_by = DominoModelmanagerApiModelOwner.from_dict(d.pop("createdBy"))

        created = d.pop("created")

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

        def _parse_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        number = _parse_number(d.pop("number", UNSET))

        domino_modelmanager_api_model_version = cls(
            model_version_id=model_version_id,
            model_id=model_id,
            project_id=project_id,
            commit_id=commit_id,
            exclude_files=exclude_files,
            environment_id=environment_id,
            environment_revision_id=environment_revision_id,
            data_plane_id=data_plane_id,
            created_by=created_by,
            created=created,
            file=file,
            function=function,
            registered_model_name=registered_model_name,
            registered_model_version=registered_model_version,
            number=number,
        )

        domino_modelmanager_api_model_version.additional_properties = d
        return domino_modelmanager_api_model_version

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
