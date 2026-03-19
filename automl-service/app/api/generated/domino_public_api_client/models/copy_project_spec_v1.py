from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.project_visibility_v1 import ProjectVisibilityV1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.billing_tag_v1 import BillingTagV1
    from ..models.git_code_repo_spec_v1 import GitCodeRepoSpecV1


T = TypeVar("T", bound="CopyProjectSpecV1")


@_attrs_define
class CopyProjectSpecV1:
    """
    Attributes:
        copy_datasets (bool): Whether to copy the Project's Datasets or not
        billing_tag (BillingTagV1 | Unset): Billing Tag to assign to projects for cost aggregation
        copy_net_app_volumes (bool | Unset): Whether to copy the Project's NetApp Volumes or not
        git_code_repo_spec (GitCodeRepoSpecV1 | Unset): Details needed in order to copy the code repository of a Git-
            backed project.
        imported_git_repos_credential_id (str | Unset): The Domino ID of the PAT credential, which will be used to
            access the Imported Git Repos on the new project.
        name (str | Unset): The name of the new Domino Project.
        owner_id (str | Unset): The Domino ID of owner of the copied project.
        visibility (ProjectVisibilityV1 | Unset): Project visibility
    """

    copy_datasets: bool
    billing_tag: BillingTagV1 | Unset = UNSET
    copy_net_app_volumes: bool | Unset = UNSET
    git_code_repo_spec: GitCodeRepoSpecV1 | Unset = UNSET
    imported_git_repos_credential_id: str | Unset = UNSET
    name: str | Unset = UNSET
    owner_id: str | Unset = UNSET
    visibility: ProjectVisibilityV1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        copy_datasets = self.copy_datasets

        billing_tag: dict[str, Any] | Unset = UNSET
        if not isinstance(self.billing_tag, Unset):
            billing_tag = self.billing_tag.to_dict()

        copy_net_app_volumes = self.copy_net_app_volumes

        git_code_repo_spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.git_code_repo_spec, Unset):
            git_code_repo_spec = self.git_code_repo_spec.to_dict()

        imported_git_repos_credential_id = self.imported_git_repos_credential_id

        name = self.name

        owner_id = self.owner_id

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "copyDatasets": copy_datasets,
            }
        )
        if billing_tag is not UNSET:
            field_dict["billingTag"] = billing_tag
        if copy_net_app_volumes is not UNSET:
            field_dict["copyNetAppVolumes"] = copy_net_app_volumes
        if git_code_repo_spec is not UNSET:
            field_dict["gitCodeRepoSpec"] = git_code_repo_spec
        if imported_git_repos_credential_id is not UNSET:
            field_dict["importedGitReposCredentialId"] = imported_git_repos_credential_id
        if name is not UNSET:
            field_dict["name"] = name
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.billing_tag_v1 import BillingTagV1
        from ..models.git_code_repo_spec_v1 import GitCodeRepoSpecV1

        d = dict(src_dict)
        copy_datasets = d.pop("copyDatasets")

        _billing_tag = d.pop("billingTag", UNSET)
        billing_tag: BillingTagV1 | Unset
        if isinstance(_billing_tag, Unset):
            billing_tag = UNSET
        else:
            billing_tag = BillingTagV1.from_dict(_billing_tag)

        copy_net_app_volumes = d.pop("copyNetAppVolumes", UNSET)

        _git_code_repo_spec = d.pop("gitCodeRepoSpec", UNSET)
        git_code_repo_spec: GitCodeRepoSpecV1 | Unset
        if isinstance(_git_code_repo_spec, Unset):
            git_code_repo_spec = UNSET
        else:
            git_code_repo_spec = GitCodeRepoSpecV1.from_dict(_git_code_repo_spec)

        imported_git_repos_credential_id = d.pop("importedGitReposCredentialId", UNSET)

        name = d.pop("name", UNSET)

        owner_id = d.pop("ownerId", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: ProjectVisibilityV1 | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = ProjectVisibilityV1(_visibility)

        copy_project_spec_v1 = cls(
            copy_datasets=copy_datasets,
            billing_tag=billing_tag,
            copy_net_app_volumes=copy_net_app_volumes,
            git_code_repo_spec=git_code_repo_spec,
            imported_git_repos_credential_id=imported_git_repos_credential_id,
            name=name,
            owner_id=owner_id,
            visibility=visibility,
        )

        copy_project_spec_v1.additional_properties = d
        return copy_project_spec_v1

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
