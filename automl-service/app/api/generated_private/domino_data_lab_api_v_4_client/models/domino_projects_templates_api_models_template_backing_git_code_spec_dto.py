from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_projects_templates_api_models_template_backing_git_code_spec_dto_visibility import (
    DominoProjectsTemplatesApiModelsTemplateBackingGitCodeSpecDtoVisibility,
)
from ..models.domino_projects_templates_api_models_template_backing_git_code_spec_dto_write_type import (
    DominoProjectsTemplatesApiModelsTemplateBackingGitCodeSpecDtoWriteType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoProjectsTemplatesApiModelsTemplateBackingGitCodeSpecDto")


@_attrs_define
class DominoProjectsTemplatesApiModelsTemplateBackingGitCodeSpecDto:
    """
    Attributes:
        credential_id (str):
        repo_name (str):
        repo_owner_name (str):
        visibility (DominoProjectsTemplatesApiModelsTemplateBackingGitCodeSpecDtoVisibility | Unset):
        write_type (DominoProjectsTemplatesApiModelsTemplateBackingGitCodeSpecDtoWriteType | Unset):
    """

    credential_id: str
    repo_name: str
    repo_owner_name: str
    visibility: DominoProjectsTemplatesApiModelsTemplateBackingGitCodeSpecDtoVisibility | Unset = UNSET
    write_type: DominoProjectsTemplatesApiModelsTemplateBackingGitCodeSpecDtoWriteType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credential_id = self.credential_id

        repo_name = self.repo_name

        repo_owner_name = self.repo_owner_name

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        write_type: str | Unset = UNSET
        if not isinstance(self.write_type, Unset):
            write_type = self.write_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credentialId": credential_id,
                "repoName": repo_name,
                "repoOwnerName": repo_owner_name,
            }
        )
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if write_type is not UNSET:
            field_dict["writeType"] = write_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        credential_id = d.pop("credentialId")

        repo_name = d.pop("repoName")

        repo_owner_name = d.pop("repoOwnerName")

        _visibility = d.pop("visibility", UNSET)
        visibility: DominoProjectsTemplatesApiModelsTemplateBackingGitCodeSpecDtoVisibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = DominoProjectsTemplatesApiModelsTemplateBackingGitCodeSpecDtoVisibility(_visibility)

        _write_type = d.pop("writeType", UNSET)
        write_type: DominoProjectsTemplatesApiModelsTemplateBackingGitCodeSpecDtoWriteType | Unset
        if isinstance(_write_type, Unset):
            write_type = UNSET
        else:
            write_type = DominoProjectsTemplatesApiModelsTemplateBackingGitCodeSpecDtoWriteType(_write_type)

        domino_projects_templates_api_models_template_backing_git_code_spec_dto = cls(
            credential_id=credential_id,
            repo_name=repo_name,
            repo_owner_name=repo_owner_name,
            visibility=visibility,
            write_type=write_type,
        )

        domino_projects_templates_api_models_template_backing_git_code_spec_dto.additional_properties = d
        return domino_projects_templates_api_models_template_backing_git_code_spec_dto

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
