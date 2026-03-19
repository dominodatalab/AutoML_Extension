from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.repo_status_status import RepoStatusStatus

T = TypeVar("T", bound="RepoStatus")


@_attrs_define
class RepoStatus:
    """
    Attributes:
        full_repo_url (str): Complete repository base URL without snapshot (e.g., "http://ppm-server:4499/cran")
        message (str): Success message or error details
        repo_name (str): Repository name (e.g., "cran", "bioconductor", "pypi")
        status (RepoStatusStatus): Status of the repository query
    """

    full_repo_url: str
    message: str
    repo_name: str
    status: RepoStatusStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        full_repo_url = self.full_repo_url

        message = self.message

        repo_name = self.repo_name

        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fullRepoUrl": full_repo_url,
                "message": message,
                "repoName": repo_name,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        full_repo_url = d.pop("fullRepoUrl")

        message = d.pop("message")

        repo_name = d.pop("repoName")

        status = RepoStatusStatus(d.pop("status"))

        repo_status = cls(
            full_repo_url=full_repo_url,
            message=message,
            repo_name=repo_name,
            status=status,
        )

        repo_status.additional_properties = d
        return repo_status

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
