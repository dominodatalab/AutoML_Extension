from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_modelmanager_api_model_build_build_status import DominoModelmanagerApiModelBuildBuildStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoModelmanagerApiModelBuild")


@_attrs_define
class DominoModelmanagerApiModelBuild:
    """
    Attributes:
        model_id (str):
        name (str):
        environment_id (str):
        project_id (str):
        project_name (str):
        build_status (DominoModelmanagerApiModelBuildBuildStatus):
        model_version_id (str):
        model_version_number (int):
        description (None | str | Unset):
    """

    model_id: str
    name: str
    environment_id: str
    project_id: str
    project_name: str
    build_status: DominoModelmanagerApiModelBuildBuildStatus
    model_version_id: str
    model_version_number: int
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_id = self.model_id

        name = self.name

        environment_id = self.environment_id

        project_id = self.project_id

        project_name = self.project_name

        build_status = self.build_status.value

        model_version_id = self.model_version_id

        model_version_number = self.model_version_number

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modelId": model_id,
                "name": name,
                "environmentId": environment_id,
                "projectId": project_id,
                "projectName": project_name,
                "buildStatus": build_status,
                "modelVersionId": model_version_id,
                "modelVersionNumber": model_version_number,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model_id = d.pop("modelId")

        name = d.pop("name")

        environment_id = d.pop("environmentId")

        project_id = d.pop("projectId")

        project_name = d.pop("projectName")

        build_status = DominoModelmanagerApiModelBuildBuildStatus(d.pop("buildStatus"))

        model_version_id = d.pop("modelVersionId")

        model_version_number = d.pop("modelVersionNumber")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        domino_modelmanager_api_model_build = cls(
            model_id=model_id,
            name=name,
            environment_id=environment_id,
            project_id=project_id,
            project_name=project_name,
            build_status=build_status,
            model_version_id=model_version_id,
            model_version_number=model_version_number,
            description=description,
        )

        domino_modelmanager_api_model_build.additional_properties = d
        return domino_modelmanager_api_model_build

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
