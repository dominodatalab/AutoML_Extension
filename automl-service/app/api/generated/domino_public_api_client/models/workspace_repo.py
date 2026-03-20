from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WorkspaceRepo")


@_attrs_define
class WorkspaceRepo:
    """
    Attributes:
        base_url (str): PPM server base URL
        current_snapshot (str): Snapshot date or "latest"
        full_url (str): Complete repository URL with snapshot
        repo_name (str): Repository name (e.g., "cran", "bioconductor")
    """

    base_url: str
    current_snapshot: str
    full_url: str
    repo_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_url = self.base_url

        current_snapshot = self.current_snapshot

        full_url = self.full_url

        repo_name = self.repo_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "baseUrl": base_url,
                "currentSnapshot": current_snapshot,
                "fullUrl": full_url,
                "repoName": repo_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base_url = d.pop("baseUrl")

        current_snapshot = d.pop("currentSnapshot")

        full_url = d.pop("fullUrl")

        repo_name = d.pop("repoName")

        workspace_repo = cls(
            base_url=base_url,
            current_snapshot=current_snapshot,
            full_url=full_url,
            repo_name=repo_name,
        )

        workspace_repo.additional_properties = d
        return workspace_repo

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
