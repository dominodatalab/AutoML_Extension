from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_api_writable_project_mounts_imported_git_mounts import (
        DominoProjectsApiWritableProjectMountsImportedGitMounts,
    )


T = TypeVar("T", bound="DominoProjectsApiWritableProjectMounts")


@_attrs_define
class DominoProjectsApiWritableProjectMounts:
    """
    Attributes:
        imported_git_mounts (DominoProjectsApiWritableProjectMountsImportedGitMounts):
        main_dfs_mount (str):
        main_git_mount (None | str | Unset):
    """

    imported_git_mounts: DominoProjectsApiWritableProjectMountsImportedGitMounts
    main_dfs_mount: str
    main_git_mount: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        imported_git_mounts = self.imported_git_mounts.to_dict()

        main_dfs_mount = self.main_dfs_mount

        main_git_mount: None | str | Unset
        if isinstance(self.main_git_mount, Unset):
            main_git_mount = UNSET
        else:
            main_git_mount = self.main_git_mount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "importedGitMounts": imported_git_mounts,
                "mainDfsMount": main_dfs_mount,
            }
        )
        if main_git_mount is not UNSET:
            field_dict["mainGitMount"] = main_git_mount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_writable_project_mounts_imported_git_mounts import (
            DominoProjectsApiWritableProjectMountsImportedGitMounts,
        )

        d = dict(src_dict)
        imported_git_mounts = DominoProjectsApiWritableProjectMountsImportedGitMounts.from_dict(
            d.pop("importedGitMounts")
        )

        main_dfs_mount = d.pop("mainDfsMount")

        def _parse_main_git_mount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        main_git_mount = _parse_main_git_mount(d.pop("mainGitMount", UNSET))

        domino_projects_api_writable_project_mounts = cls(
            imported_git_mounts=imported_git_mounts,
            main_dfs_mount=main_dfs_mount,
            main_git_mount=main_git_mount,
        )

        domino_projects_api_writable_project_mounts.additional_properties = d
        return domino_projects_api_writable_project_mounts

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
