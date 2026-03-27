from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_api_copied_git_repo_metadata import DominoProjectsApiCopiedGitRepoMetadata
    from ..models.domino_projects_api_import_git_files_spec import DominoProjectsApiImportGitFilesSpec
    from ..models.domino_projects_api_linked_git_repo_metadata import DominoProjectsApiLinkedGitRepoMetadata


T = TypeVar("T", bound="DominoProjectsApiCopyGitRequest")


@_attrs_define
class DominoProjectsApiCopyGitRequest:
    """
    Attributes:
        credential_id (str):
        imported_git_repos_credential_id (None | str | Unset):
        link_spec (DominoProjectsApiLinkedGitRepoMetadata | Unset):
        copy_spec (DominoProjectsApiCopiedGitRepoMetadata | Unset):
        import_spec (DominoProjectsApiImportGitFilesSpec | Unset):
    """

    credential_id: str
    imported_git_repos_credential_id: None | str | Unset = UNSET
    link_spec: DominoProjectsApiLinkedGitRepoMetadata | Unset = UNSET
    copy_spec: DominoProjectsApiCopiedGitRepoMetadata | Unset = UNSET
    import_spec: DominoProjectsApiImportGitFilesSpec | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credential_id = self.credential_id

        imported_git_repos_credential_id: None | str | Unset
        if isinstance(self.imported_git_repos_credential_id, Unset):
            imported_git_repos_credential_id = UNSET
        else:
            imported_git_repos_credential_id = self.imported_git_repos_credential_id

        link_spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.link_spec, Unset):
            link_spec = self.link_spec.to_dict()

        copy_spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.copy_spec, Unset):
            copy_spec = self.copy_spec.to_dict()

        import_spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.import_spec, Unset):
            import_spec = self.import_spec.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credentialId": credential_id,
            }
        )
        if imported_git_repos_credential_id is not UNSET:
            field_dict["importedGitReposCredentialId"] = imported_git_repos_credential_id
        if link_spec is not UNSET:
            field_dict["linkSpec"] = link_spec
        if copy_spec is not UNSET:
            field_dict["copySpec"] = copy_spec
        if import_spec is not UNSET:
            field_dict["importSpec"] = import_spec

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_copied_git_repo_metadata import DominoProjectsApiCopiedGitRepoMetadata
        from ..models.domino_projects_api_import_git_files_spec import DominoProjectsApiImportGitFilesSpec
        from ..models.domino_projects_api_linked_git_repo_metadata import DominoProjectsApiLinkedGitRepoMetadata

        d = dict(src_dict)
        credential_id = d.pop("credentialId")

        def _parse_imported_git_repos_credential_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        imported_git_repos_credential_id = _parse_imported_git_repos_credential_id(
            d.pop("importedGitReposCredentialId", UNSET)
        )

        _link_spec = d.pop("linkSpec", UNSET)
        link_spec: DominoProjectsApiLinkedGitRepoMetadata | Unset
        if isinstance(_link_spec, Unset):
            link_spec = UNSET
        else:
            link_spec = DominoProjectsApiLinkedGitRepoMetadata.from_dict(_link_spec)

        _copy_spec = d.pop("copySpec", UNSET)
        copy_spec: DominoProjectsApiCopiedGitRepoMetadata | Unset
        if isinstance(_copy_spec, Unset):
            copy_spec = UNSET
        else:
            copy_spec = DominoProjectsApiCopiedGitRepoMetadata.from_dict(_copy_spec)

        _import_spec = d.pop("importSpec", UNSET)
        import_spec: DominoProjectsApiImportGitFilesSpec | Unset
        if isinstance(_import_spec, Unset):
            import_spec = UNSET
        else:
            import_spec = DominoProjectsApiImportGitFilesSpec.from_dict(_import_spec)

        domino_projects_api_copy_git_request = cls(
            credential_id=credential_id,
            imported_git_repos_credential_id=imported_git_repos_credential_id,
            link_spec=link_spec,
            copy_spec=copy_spec,
            import_spec=import_spec,
        )

        domino_projects_api_copy_git_request.additional_properties = d
        return domino_projects_api_copy_git_request

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
