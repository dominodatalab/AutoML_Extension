from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.provider_repo_visibility_v1 import ProviderRepoVisibilityV1

T = TypeVar("T", bound="DeepCopyGitRepoSpecV1")


@_attrs_define
class DeepCopyGitRepoSpecV1:
    """Data which specifies what the copied repository will look like.

    Attributes:
        new_repo_name (str): The name of the new repository.
        new_repo_owner_name (str): The name of the user who will own the new repository in the git service provider.
        visibility (ProviderRepoVisibilityV1): The visibility of the code repo. Internal can only be used for Github
            Enterprise.
    """

    new_repo_name: str
    new_repo_owner_name: str
    visibility: ProviderRepoVisibilityV1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        new_repo_name = self.new_repo_name

        new_repo_owner_name = self.new_repo_owner_name

        visibility = self.visibility.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "newRepoName": new_repo_name,
                "newRepoOwnerName": new_repo_owner_name,
                "visibility": visibility,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        new_repo_name = d.pop("newRepoName")

        new_repo_owner_name = d.pop("newRepoOwnerName")

        visibility = ProviderRepoVisibilityV1(d.pop("visibility"))

        deep_copy_git_repo_spec_v1 = cls(
            new_repo_name=new_repo_name,
            new_repo_owner_name=new_repo_owner_name,
            visibility=visibility,
        )

        deep_copy_git_repo_spec_v1.additional_properties = d
        return deep_copy_git_repo_spec_v1

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
