from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_api_repositories_reference_dto import DominoProjectsApiRepositoriesReferenceDTO


T = TypeVar("T", bound="DominoNucleusModelproductModelsStartParams")


@_attrs_define
class DominoNucleusModelproductModelsStartParams:
    """
    Attributes:
        commit_id (None | str | Unset):
        main_repo_git_ref (DominoProjectsApiRepositoriesReferenceDTO | Unset):
        environment_id (None | str | Unset):
        hardware_tier_id (None | str | Unset):
        dataset_config_name (None | str | Unset):
        external_volume_mount_ids (list[str] | None | Unset):
        net_app_volume_ids (list[str] | None | Unset):
        bundle_id (None | str | Unset):
    """

    commit_id: None | str | Unset = UNSET
    main_repo_git_ref: DominoProjectsApiRepositoriesReferenceDTO | Unset = UNSET
    environment_id: None | str | Unset = UNSET
    hardware_tier_id: None | str | Unset = UNSET
    dataset_config_name: None | str | Unset = UNSET
    external_volume_mount_ids: list[str] | None | Unset = UNSET
    net_app_volume_ids: list[str] | None | Unset = UNSET
    bundle_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        commit_id: None | str | Unset
        if isinstance(self.commit_id, Unset):
            commit_id = UNSET
        else:
            commit_id = self.commit_id

        main_repo_git_ref: dict[str, Any] | Unset = UNSET
        if not isinstance(self.main_repo_git_ref, Unset):
            main_repo_git_ref = self.main_repo_git_ref.to_dict()

        environment_id: None | str | Unset
        if isinstance(self.environment_id, Unset):
            environment_id = UNSET
        else:
            environment_id = self.environment_id

        hardware_tier_id: None | str | Unset
        if isinstance(self.hardware_tier_id, Unset):
            hardware_tier_id = UNSET
        else:
            hardware_tier_id = self.hardware_tier_id

        dataset_config_name: None | str | Unset
        if isinstance(self.dataset_config_name, Unset):
            dataset_config_name = UNSET
        else:
            dataset_config_name = self.dataset_config_name

        external_volume_mount_ids: list[str] | None | Unset
        if isinstance(self.external_volume_mount_ids, Unset):
            external_volume_mount_ids = UNSET
        elif isinstance(self.external_volume_mount_ids, list):
            external_volume_mount_ids = self.external_volume_mount_ids

        else:
            external_volume_mount_ids = self.external_volume_mount_ids

        net_app_volume_ids: list[str] | None | Unset
        if isinstance(self.net_app_volume_ids, Unset):
            net_app_volume_ids = UNSET
        elif isinstance(self.net_app_volume_ids, list):
            net_app_volume_ids = self.net_app_volume_ids

        else:
            net_app_volume_ids = self.net_app_volume_ids

        bundle_id: None | str | Unset
        if isinstance(self.bundle_id, Unset):
            bundle_id = UNSET
        else:
            bundle_id = self.bundle_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if commit_id is not UNSET:
            field_dict["commitId"] = commit_id
        if main_repo_git_ref is not UNSET:
            field_dict["mainRepoGitRef"] = main_repo_git_ref
        if environment_id is not UNSET:
            field_dict["environmentId"] = environment_id
        if hardware_tier_id is not UNSET:
            field_dict["hardwareTierId"] = hardware_tier_id
        if dataset_config_name is not UNSET:
            field_dict["datasetConfigName"] = dataset_config_name
        if external_volume_mount_ids is not UNSET:
            field_dict["externalVolumeMountIds"] = external_volume_mount_ids
        if net_app_volume_ids is not UNSET:
            field_dict["netAppVolumeIds"] = net_app_volume_ids
        if bundle_id is not UNSET:
            field_dict["bundleId"] = bundle_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_repositories_reference_dto import DominoProjectsApiRepositoriesReferenceDTO

        d = dict(src_dict)

        def _parse_commit_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commit_id = _parse_commit_id(d.pop("commitId", UNSET))

        _main_repo_git_ref = d.pop("mainRepoGitRef", UNSET)
        main_repo_git_ref: DominoProjectsApiRepositoriesReferenceDTO | Unset
        if isinstance(_main_repo_git_ref, Unset):
            main_repo_git_ref = UNSET
        else:
            main_repo_git_ref = DominoProjectsApiRepositoriesReferenceDTO.from_dict(_main_repo_git_ref)

        def _parse_environment_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        environment_id = _parse_environment_id(d.pop("environmentId", UNSET))

        def _parse_hardware_tier_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hardware_tier_id = _parse_hardware_tier_id(d.pop("hardwareTierId", UNSET))

        def _parse_dataset_config_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_config_name = _parse_dataset_config_name(d.pop("datasetConfigName", UNSET))

        def _parse_external_volume_mount_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                external_volume_mount_ids_type_0 = cast(list[str], data)

                return external_volume_mount_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        external_volume_mount_ids = _parse_external_volume_mount_ids(d.pop("externalVolumeMountIds", UNSET))

        def _parse_net_app_volume_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                net_app_volume_ids_type_0 = cast(list[str], data)

                return net_app_volume_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        net_app_volume_ids = _parse_net_app_volume_ids(d.pop("netAppVolumeIds", UNSET))

        def _parse_bundle_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bundle_id = _parse_bundle_id(d.pop("bundleId", UNSET))

        domino_nucleus_modelproduct_models_start_params = cls(
            commit_id=commit_id,
            main_repo_git_ref=main_repo_git_ref,
            environment_id=environment_id,
            hardware_tier_id=hardware_tier_id,
            dataset_config_name=dataset_config_name,
            external_volume_mount_ids=external_volume_mount_ids,
            net_app_volume_ids=net_app_volume_ids,
            bundle_id=bundle_id,
        )

        domino_nucleus_modelproduct_models_start_params.additional_properties = d
        return domino_nucleus_modelproduct_models_start_params

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
