from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReferenceCopyGitRepoSpecV1")


@_attrs_define
class ReferenceCopyGitRepoSpecV1:
    """Specifies the git service provider repository to use as the code repository in the new Domino project.

    Attributes:
        main_repo_url (str): The cloneable url for the git service provider repository. Must be a http(s) schema url.
    """

    main_repo_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        main_repo_url = self.main_repo_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mainRepoUrl": main_repo_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        main_repo_url = d.pop("mainRepoUrl")

        reference_copy_git_repo_spec_v1 = cls(
            main_repo_url=main_repo_url,
        )

        reference_copy_git_repo_spec_v1.additional_properties = d
        return reference_copy_git_repo_spec_v1

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
