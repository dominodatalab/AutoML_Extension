from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_common_modelproduct_app_code_info_repository_dto import (
        DominoCommonModelproductAppCodeInfoRepositoryDto,
    )


T = TypeVar("T", bound="DominoCommonModelproductAppCodeInfoDto")


@_attrs_define
class DominoCommonModelproductAppCodeInfoDto:
    """
    Attributes:
        imported_git_repos (list[DominoCommonModelproductAppCodeInfoRepositoryDto]):
        main_repo (DominoCommonModelproductAppCodeInfoRepositoryDto | Unset):
    """

    imported_git_repos: list[DominoCommonModelproductAppCodeInfoRepositoryDto]
    main_repo: DominoCommonModelproductAppCodeInfoRepositoryDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        imported_git_repos = []
        for imported_git_repos_item_data in self.imported_git_repos:
            imported_git_repos_item = imported_git_repos_item_data.to_dict()
            imported_git_repos.append(imported_git_repos_item)

        main_repo: dict[str, Any] | Unset = UNSET
        if not isinstance(self.main_repo, Unset):
            main_repo = self.main_repo.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "importedGitRepos": imported_git_repos,
            }
        )
        if main_repo is not UNSET:
            field_dict["mainRepo"] = main_repo

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_common_modelproduct_app_code_info_repository_dto import (
            DominoCommonModelproductAppCodeInfoRepositoryDto,
        )

        d = dict(src_dict)
        imported_git_repos = []
        _imported_git_repos = d.pop("importedGitRepos")
        for imported_git_repos_item_data in _imported_git_repos:
            imported_git_repos_item = DominoCommonModelproductAppCodeInfoRepositoryDto.from_dict(
                imported_git_repos_item_data
            )

            imported_git_repos.append(imported_git_repos_item)

        _main_repo = d.pop("mainRepo", UNSET)
        main_repo: DominoCommonModelproductAppCodeInfoRepositoryDto | Unset
        if isinstance(_main_repo, Unset):
            main_repo = UNSET
        else:
            main_repo = DominoCommonModelproductAppCodeInfoRepositoryDto.from_dict(_main_repo)

        domino_common_modelproduct_app_code_info_dto = cls(
            imported_git_repos=imported_git_repos,
            main_repo=main_repo,
        )

        domino_common_modelproduct_app_code_info_dto.additional_properties = d
        return domino_common_modelproduct_app_code_info_dto

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
