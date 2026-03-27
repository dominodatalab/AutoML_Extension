from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_common_run_interfaces_new_run_git_ref_dto import DominoCommonRunInterfacesNewRunGitRefDto


T = TypeVar("T", bound="DominoCommonRunInterfacesNewRunDTO")


@_attrs_define
class DominoCommonRunInterfacesNewRunDTO:
    """
    Attributes:
        project_id (str):
        command_to_run (str):
        commit_id (None | str | Unset):
        main_repo_git_ref (DominoCommonRunInterfacesNewRunGitRefDto | Unset):
        hardware_tier_name (None | str | Unset):
        dataset_config (None | str | Unset):
        domino_client_source (None | str | Unset):
    """

    project_id: str
    command_to_run: str
    commit_id: None | str | Unset = UNSET
    main_repo_git_ref: DominoCommonRunInterfacesNewRunGitRefDto | Unset = UNSET
    hardware_tier_name: None | str | Unset = UNSET
    dataset_config: None | str | Unset = UNSET
    domino_client_source: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        command_to_run = self.command_to_run

        commit_id: None | str | Unset
        if isinstance(self.commit_id, Unset):
            commit_id = UNSET
        else:
            commit_id = self.commit_id

        main_repo_git_ref: dict[str, Any] | Unset = UNSET
        if not isinstance(self.main_repo_git_ref, Unset):
            main_repo_git_ref = self.main_repo_git_ref.to_dict()

        hardware_tier_name: None | str | Unset
        if isinstance(self.hardware_tier_name, Unset):
            hardware_tier_name = UNSET
        else:
            hardware_tier_name = self.hardware_tier_name

        dataset_config: None | str | Unset
        if isinstance(self.dataset_config, Unset):
            dataset_config = UNSET
        else:
            dataset_config = self.dataset_config

        domino_client_source: None | str | Unset
        if isinstance(self.domino_client_source, Unset):
            domino_client_source = UNSET
        else:
            domino_client_source = self.domino_client_source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectId": project_id,
                "commandToRun": command_to_run,
            }
        )
        if commit_id is not UNSET:
            field_dict["commitId"] = commit_id
        if main_repo_git_ref is not UNSET:
            field_dict["mainRepoGitRef"] = main_repo_git_ref
        if hardware_tier_name is not UNSET:
            field_dict["hardwareTierName"] = hardware_tier_name
        if dataset_config is not UNSET:
            field_dict["datasetConfig"] = dataset_config
        if domino_client_source is not UNSET:
            field_dict["dominoClientSource"] = domino_client_source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_common_run_interfaces_new_run_git_ref_dto import DominoCommonRunInterfacesNewRunGitRefDto

        d = dict(src_dict)
        project_id = d.pop("projectId")

        command_to_run = d.pop("commandToRun")

        def _parse_commit_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commit_id = _parse_commit_id(d.pop("commitId", UNSET))

        _main_repo_git_ref = d.pop("mainRepoGitRef", UNSET)
        main_repo_git_ref: DominoCommonRunInterfacesNewRunGitRefDto | Unset
        if isinstance(_main_repo_git_ref, Unset):
            main_repo_git_ref = UNSET
        else:
            main_repo_git_ref = DominoCommonRunInterfacesNewRunGitRefDto.from_dict(_main_repo_git_ref)

        def _parse_hardware_tier_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hardware_tier_name = _parse_hardware_tier_name(d.pop("hardwareTierName", UNSET))

        def _parse_dataset_config(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_config = _parse_dataset_config(d.pop("datasetConfig", UNSET))

        def _parse_domino_client_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        domino_client_source = _parse_domino_client_source(d.pop("dominoClientSource", UNSET))

        domino_common_run_interfaces_new_run_dto = cls(
            project_id=project_id,
            command_to_run=command_to_run,
            commit_id=commit_id,
            main_repo_git_ref=main_repo_git_ref,
            hardware_tier_name=hardware_tier_name,
            dataset_config=dataset_config,
            domino_client_source=domino_client_source,
        )

        domino_common_run_interfaces_new_run_dto.additional_properties = d
        return domino_common_run_interfaces_new_run_dto

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
