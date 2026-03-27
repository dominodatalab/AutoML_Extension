from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoProjectsApiRepositoriesCredentialMappingDTO")


@_attrs_define
class DominoProjectsApiRepositoriesCredentialMappingDTO:
    """
    Attributes:
        user_id (str):
        project_id (str):
        repo_id (str):
        credential_id (None | str | Unset):
    """

    user_id: str
    project_id: str
    repo_id: str
    credential_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        project_id = self.project_id

        repo_id = self.repo_id

        credential_id: None | str | Unset
        if isinstance(self.credential_id, Unset):
            credential_id = UNSET
        else:
            credential_id = self.credential_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "projectId": project_id,
                "repoId": repo_id,
            }
        )
        if credential_id is not UNSET:
            field_dict["credentialId"] = credential_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("userId")

        project_id = d.pop("projectId")

        repo_id = d.pop("repoId")

        def _parse_credential_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        credential_id = _parse_credential_id(d.pop("credentialId", UNSET))

        domino_projects_api_repositories_credential_mapping_dto = cls(
            user_id=user_id,
            project_id=project_id,
            repo_id=repo_id,
            credential_id=credential_id,
        )

        domino_projects_api_repositories_credential_mapping_dto.additional_properties = d
        return domino_projects_api_repositories_credential_mapping_dto

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
