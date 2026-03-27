from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_api_project_env_var_version import DominoProjectsApiProjectEnvVarVersion


T = TypeVar("T", bound="DominoProvenanceApiProvenanceEnvironmentVariablesMap")


@_attrs_define
class DominoProvenanceApiProvenanceEnvironmentVariablesMap:
    """
    Attributes:
        project_env_var_blob_keys (list[str]):
        project_var_versions (list[DominoProjectsApiProjectEnvVarVersion]):
        user_env_var_blob_key (None | str | Unset):
        user_var_version (int | None | Unset):
    """

    project_env_var_blob_keys: list[str]
    project_var_versions: list[DominoProjectsApiProjectEnvVarVersion]
    user_env_var_blob_key: None | str | Unset = UNSET
    user_var_version: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_env_var_blob_keys = self.project_env_var_blob_keys

        project_var_versions = []
        for project_var_versions_item_data in self.project_var_versions:
            project_var_versions_item = project_var_versions_item_data.to_dict()
            project_var_versions.append(project_var_versions_item)

        user_env_var_blob_key: None | str | Unset
        if isinstance(self.user_env_var_blob_key, Unset):
            user_env_var_blob_key = UNSET
        else:
            user_env_var_blob_key = self.user_env_var_blob_key

        user_var_version: int | None | Unset
        if isinstance(self.user_var_version, Unset):
            user_var_version = UNSET
        else:
            user_var_version = self.user_var_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectEnvVarBlobKeys": project_env_var_blob_keys,
                "projectVarVersions": project_var_versions,
            }
        )
        if user_env_var_blob_key is not UNSET:
            field_dict["userEnvVarBlobKey"] = user_env_var_blob_key
        if user_var_version is not UNSET:
            field_dict["userVarVersion"] = user_var_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_project_env_var_version import DominoProjectsApiProjectEnvVarVersion

        d = dict(src_dict)
        project_env_var_blob_keys = cast(list[str], d.pop("projectEnvVarBlobKeys"))

        project_var_versions = []
        _project_var_versions = d.pop("projectVarVersions")
        for project_var_versions_item_data in _project_var_versions:
            project_var_versions_item = DominoProjectsApiProjectEnvVarVersion.from_dict(project_var_versions_item_data)

            project_var_versions.append(project_var_versions_item)

        def _parse_user_env_var_blob_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_env_var_blob_key = _parse_user_env_var_blob_key(d.pop("userEnvVarBlobKey", UNSET))

        def _parse_user_var_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user_var_version = _parse_user_var_version(d.pop("userVarVersion", UNSET))

        domino_provenance_api_provenance_environment_variables_map = cls(
            project_env_var_blob_keys=project_env_var_blob_keys,
            project_var_versions=project_var_versions,
            user_env_var_blob_key=user_env_var_blob_key,
            user_var_version=user_var_version,
        )

        domino_provenance_api_provenance_environment_variables_map.additional_properties = d
        return domino_provenance_api_provenance_environment_variables_map

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
