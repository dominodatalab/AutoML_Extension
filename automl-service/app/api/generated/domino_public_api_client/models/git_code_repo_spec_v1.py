from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deep_copy_git_repo_spec_v1 import DeepCopyGitRepoSpecV1
    from ..models.import_files_repo_target_v1 import ImportFilesRepoTargetV1
    from ..models.reference_copy_git_repo_spec_v1 import ReferenceCopyGitRepoSpecV1


T = TypeVar("T", bound="GitCodeRepoSpecV1")


@_attrs_define
class GitCodeRepoSpecV1:
    """Details needed in order to copy the code repository of a Git-backed project.

    Attributes:
        credential_id (str): The Domino ID of the PAT credential, which will be used to copy and/or read from the code
            repository on the new project.
        deep_copy (DeepCopyGitRepoSpecV1 | Unset): Data which specifies what the copied repository will look like.
        import_files_target (ImportFilesRepoTargetV1 | Unset): Specifies what git repository to import the source
            project files into
        reference_copy (ReferenceCopyGitRepoSpecV1 | Unset): Specifies the git service provider repository to use as the
            code repository in the new Domino project.
    """

    credential_id: str
    deep_copy: DeepCopyGitRepoSpecV1 | Unset = UNSET
    import_files_target: ImportFilesRepoTargetV1 | Unset = UNSET
    reference_copy: ReferenceCopyGitRepoSpecV1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credential_id = self.credential_id

        deep_copy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deep_copy, Unset):
            deep_copy = self.deep_copy.to_dict()

        import_files_target: dict[str, Any] | Unset = UNSET
        if not isinstance(self.import_files_target, Unset):
            import_files_target = self.import_files_target.to_dict()

        reference_copy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reference_copy, Unset):
            reference_copy = self.reference_copy.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credentialId": credential_id,
            }
        )
        if deep_copy is not UNSET:
            field_dict["deepCopy"] = deep_copy
        if import_files_target is not UNSET:
            field_dict["importFilesTarget"] = import_files_target
        if reference_copy is not UNSET:
            field_dict["referenceCopy"] = reference_copy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.deep_copy_git_repo_spec_v1 import DeepCopyGitRepoSpecV1
        from ..models.import_files_repo_target_v1 import ImportFilesRepoTargetV1
        from ..models.reference_copy_git_repo_spec_v1 import ReferenceCopyGitRepoSpecV1

        d = dict(src_dict)
        credential_id = d.pop("credentialId")

        _deep_copy = d.pop("deepCopy", UNSET)
        deep_copy: DeepCopyGitRepoSpecV1 | Unset
        if isinstance(_deep_copy, Unset):
            deep_copy = UNSET
        else:
            deep_copy = DeepCopyGitRepoSpecV1.from_dict(_deep_copy)

        _import_files_target = d.pop("importFilesTarget", UNSET)
        import_files_target: ImportFilesRepoTargetV1 | Unset
        if isinstance(_import_files_target, Unset):
            import_files_target = UNSET
        else:
            import_files_target = ImportFilesRepoTargetV1.from_dict(_import_files_target)

        _reference_copy = d.pop("referenceCopy", UNSET)
        reference_copy: ReferenceCopyGitRepoSpecV1 | Unset
        if isinstance(_reference_copy, Unset):
            reference_copy = UNSET
        else:
            reference_copy = ReferenceCopyGitRepoSpecV1.from_dict(_reference_copy)

        git_code_repo_spec_v1 = cls(
            credential_id=credential_id,
            deep_copy=deep_copy,
            import_files_target=import_files_target,
            reference_copy=reference_copy,
        )

        git_code_repo_spec_v1.additional_properties = d
        return git_code_repo_spec_v1

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
