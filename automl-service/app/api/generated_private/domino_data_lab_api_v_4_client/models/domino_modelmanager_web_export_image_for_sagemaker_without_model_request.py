from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoModelmanagerWebExportImageForSagemakerWithoutModelRequest")


@_attrs_define
class DominoModelmanagerWebExportImageForSagemakerWithoutModelRequest:
    """
    Attributes:
        registry_url (str):
        repository (str):
        export_name (str):
        user_id (str):
        project_id (str):
        file (str):
        function (str):
        environment_id (str):
        tag (None | str | Unset):
        username (None | str | Unset):
        password (None | str | Unset):
        export_description (None | str | Unset):
    """

    registry_url: str
    repository: str
    export_name: str
    user_id: str
    project_id: str
    file: str
    function: str
    environment_id: str
    tag: None | str | Unset = UNSET
    username: None | str | Unset = UNSET
    password: None | str | Unset = UNSET
    export_description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        registry_url = self.registry_url

        repository = self.repository

        export_name = self.export_name

        user_id = self.user_id

        project_id = self.project_id

        file = self.file

        function = self.function

        environment_id = self.environment_id

        tag: None | str | Unset
        if isinstance(self.tag, Unset):
            tag = UNSET
        else:
            tag = self.tag

        username: None | str | Unset
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        export_description: None | str | Unset
        if isinstance(self.export_description, Unset):
            export_description = UNSET
        else:
            export_description = self.export_description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "registryUrl": registry_url,
                "repository": repository,
                "exportName": export_name,
                "userId": user_id,
                "projectId": project_id,
                "file": file,
                "function": function,
                "environmentId": environment_id,
            }
        )
        if tag is not UNSET:
            field_dict["tag"] = tag
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if export_description is not UNSET:
            field_dict["exportDescription"] = export_description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        registry_url = d.pop("registryUrl")

        repository = d.pop("repository")

        export_name = d.pop("exportName")

        user_id = d.pop("userId")

        project_id = d.pop("projectId")

        file = d.pop("file")

        function = d.pop("function")

        environment_id = d.pop("environmentId")

        def _parse_tag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tag = _parse_tag(d.pop("tag", UNSET))

        def _parse_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        username = _parse_username(d.pop("username", UNSET))

        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))

        def _parse_export_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        export_description = _parse_export_description(d.pop("exportDescription", UNSET))

        domino_modelmanager_web_export_image_for_sagemaker_without_model_request = cls(
            registry_url=registry_url,
            repository=repository,
            export_name=export_name,
            user_id=user_id,
            project_id=project_id,
            file=file,
            function=function,
            environment_id=environment_id,
            tag=tag,
            username=username,
            password=password,
            export_description=export_description,
        )

        domino_modelmanager_web_export_image_for_sagemaker_without_model_request.additional_properties = d
        return domino_modelmanager_web_export_image_for_sagemaker_without_model_request

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
