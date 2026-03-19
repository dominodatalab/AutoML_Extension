from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.git_service_provider_v1 import GitServiceProviderV1
from ..types import UNSET, Unset

T = TypeVar("T", bound="MountedGitRepoV1")


@_attrs_define
class MountedGitRepoV1:
    """
    Attributes:
        id (str): Id of the git repo mounted to the Job. Example: 6231365e7a0af0281c01a69f.
        name (str): Name of the git repo mounted to the Job. Example: MyRepo.
        ref (str):
        service_provider (GitServiceProviderV1): Git service provider
        uri (str): Uri for the repo being mounted. Example: git@github.com:apache/spark.git.
        ending_branch (str | Unset): Branch this git repo ended at. Example: final-branch.
        ending_commit_id (str | Unset): Ending commitId for this git repo. Example:
            dff155c9a736f9cd230eac420e3c1ef3daa0ad7e.
        starting_branch (str | Unset): Branch this git repo started at. Example: init-test-branch.
        starting_commit_id (str | Unset): CommitId the git repo should be mounted at. Example:
            4f2d5c2f54db4fbb16a093d4fb11fdb1fe0794c7.
    """

    id: str
    name: str
    ref: str
    service_provider: GitServiceProviderV1
    uri: str
    ending_branch: str | Unset = UNSET
    ending_commit_id: str | Unset = UNSET
    starting_branch: str | Unset = UNSET
    starting_commit_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        ref = self.ref

        service_provider = self.service_provider.value

        uri = self.uri

        ending_branch = self.ending_branch

        ending_commit_id = self.ending_commit_id

        starting_branch = self.starting_branch

        starting_commit_id = self.starting_commit_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "ref": ref,
                "serviceProvider": service_provider,
                "uri": uri,
            }
        )
        if ending_branch is not UNSET:
            field_dict["endingBranch"] = ending_branch
        if ending_commit_id is not UNSET:
            field_dict["endingCommitId"] = ending_commit_id
        if starting_branch is not UNSET:
            field_dict["startingBranch"] = starting_branch
        if starting_commit_id is not UNSET:
            field_dict["startingCommitId"] = starting_commit_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        ref = d.pop("ref")

        service_provider = GitServiceProviderV1(d.pop("serviceProvider"))

        uri = d.pop("uri")

        ending_branch = d.pop("endingBranch", UNSET)

        ending_commit_id = d.pop("endingCommitId", UNSET)

        starting_branch = d.pop("startingBranch", UNSET)

        starting_commit_id = d.pop("startingCommitId", UNSET)

        mounted_git_repo_v1 = cls(
            id=id,
            name=name,
            ref=ref,
            service_provider=service_provider,
            uri=uri,
            ending_branch=ending_branch,
            ending_commit_id=ending_commit_id,
            starting_branch=starting_branch,
            starting_commit_id=starting_commit_id,
        )

        mounted_git_repo_v1.additional_properties = d
        return mounted_git_repo_v1

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
