from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.provider_repo_visibility_v1 import ProviderRepoVisibilityV1
from ..models.write_type_v1 import WriteTypeV1
from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateBackingGitCodeSpec")


@_attrs_define
class TemplateBackingGitCodeSpec:
    """
    Attributes:
        credential_id (str):
        repo_name (str):
        repo_owner_name (str):
        visibility (ProviderRepoVisibilityV1 | Unset): The visibility of the code repo. Internal can only be used for
            Github Enterprise.
        write_type (WriteTypeV1 | Unset): The kind of repo to use as the code repo in a template
    """

    credential_id: str
    repo_name: str
    repo_owner_name: str
    visibility: ProviderRepoVisibilityV1 | Unset = UNSET
    write_type: WriteTypeV1 | Unset = UNSET
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
        visibility: ProviderRepoVisibilityV1 | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = ProviderRepoVisibilityV1(_visibility)

        _write_type = d.pop("writeType", UNSET)
        write_type: WriteTypeV1 | Unset
        if isinstance(_write_type, Unset):
            write_type = UNSET
        else:
            write_type = WriteTypeV1(_write_type)

        template_backing_git_code_spec = cls(
            credential_id=credential_id,
            repo_name=repo_name,
            repo_owner_name=repo_owner_name,
            visibility=visibility,
            write_type=write_type,
        )

        template_backing_git_code_spec.additional_properties = d
        return template_backing_git_code_spec

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
