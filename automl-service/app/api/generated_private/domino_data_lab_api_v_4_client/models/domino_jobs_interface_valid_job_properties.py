from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_datasetrw_api_dataset_snapshot_ref_dto import DominoDatasetrwApiDatasetSnapshotRefDto
    from ..models.domino_jobs_interface_environment_with_revisions import DominoJobsInterfaceEnvironmentWithRevisions
    from ..models.domino_jobs_interface_external_volume_mount_ref_dto import (
        DominoJobsInterfaceExternalVolumeMountRefDto,
    )
    from ..models.domino_jobs_interface_hardware_tier_ref import DominoJobsInterfaceHardwareTierRef
    from ..models.domino_projects_api_repositories_reference_dto import DominoProjectsApiRepositoriesReferenceDTO


T = TypeVar("T", bound="DominoJobsInterfaceValidJobProperties")


@_attrs_define
class DominoJobsInterfaceValidJobProperties:
    """
    Attributes:
        hardware_tiers (list[DominoJobsInterfaceHardwareTierRef]):
        dataset_snapshots (list[DominoDatasetrwApiDatasetSnapshotRefDto]):
        environments (list[DominoJobsInterfaceEnvironmentWithRevisions]):
        external_volume_mounts (list[DominoJobsInterfaceExternalVolumeMountRefDto]):
        main_repo_git_refs (list[DominoProjectsApiRepositoriesReferenceDTO] | None | Unset):
    """

    hardware_tiers: list[DominoJobsInterfaceHardwareTierRef]
    dataset_snapshots: list[DominoDatasetrwApiDatasetSnapshotRefDto]
    environments: list[DominoJobsInterfaceEnvironmentWithRevisions]
    external_volume_mounts: list[DominoJobsInterfaceExternalVolumeMountRefDto]
    main_repo_git_refs: list[DominoProjectsApiRepositoriesReferenceDTO] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hardware_tiers = []
        for hardware_tiers_item_data in self.hardware_tiers:
            hardware_tiers_item = hardware_tiers_item_data.to_dict()
            hardware_tiers.append(hardware_tiers_item)

        dataset_snapshots = []
        for dataset_snapshots_item_data in self.dataset_snapshots:
            dataset_snapshots_item = dataset_snapshots_item_data.to_dict()
            dataset_snapshots.append(dataset_snapshots_item)

        environments = []
        for environments_item_data in self.environments:
            environments_item = environments_item_data.to_dict()
            environments.append(environments_item)

        external_volume_mounts = []
        for external_volume_mounts_item_data in self.external_volume_mounts:
            external_volume_mounts_item = external_volume_mounts_item_data.to_dict()
            external_volume_mounts.append(external_volume_mounts_item)

        main_repo_git_refs: list[dict[str, Any]] | None | Unset
        if isinstance(self.main_repo_git_refs, Unset):
            main_repo_git_refs = UNSET
        elif isinstance(self.main_repo_git_refs, list):
            main_repo_git_refs = []
            for main_repo_git_refs_type_0_item_data in self.main_repo_git_refs:
                main_repo_git_refs_type_0_item = main_repo_git_refs_type_0_item_data.to_dict()
                main_repo_git_refs.append(main_repo_git_refs_type_0_item)

        else:
            main_repo_git_refs = self.main_repo_git_refs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hardwareTiers": hardware_tiers,
                "datasetSnapshots": dataset_snapshots,
                "environments": environments,
                "externalVolumeMounts": external_volume_mounts,
            }
        )
        if main_repo_git_refs is not UNSET:
            field_dict["mainRepoGitRefs"] = main_repo_git_refs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_datasetrw_api_dataset_snapshot_ref_dto import DominoDatasetrwApiDatasetSnapshotRefDto
        from ..models.domino_jobs_interface_environment_with_revisions import (
            DominoJobsInterfaceEnvironmentWithRevisions,
        )
        from ..models.domino_jobs_interface_external_volume_mount_ref_dto import (
            DominoJobsInterfaceExternalVolumeMountRefDto,
        )
        from ..models.domino_jobs_interface_hardware_tier_ref import DominoJobsInterfaceHardwareTierRef
        from ..models.domino_projects_api_repositories_reference_dto import DominoProjectsApiRepositoriesReferenceDTO

        d = dict(src_dict)
        hardware_tiers = []
        _hardware_tiers = d.pop("hardwareTiers")
        for hardware_tiers_item_data in _hardware_tiers:
            hardware_tiers_item = DominoJobsInterfaceHardwareTierRef.from_dict(hardware_tiers_item_data)

            hardware_tiers.append(hardware_tiers_item)

        dataset_snapshots = []
        _dataset_snapshots = d.pop("datasetSnapshots")
        for dataset_snapshots_item_data in _dataset_snapshots:
            dataset_snapshots_item = DominoDatasetrwApiDatasetSnapshotRefDto.from_dict(dataset_snapshots_item_data)

            dataset_snapshots.append(dataset_snapshots_item)

        environments = []
        _environments = d.pop("environments")
        for environments_item_data in _environments:
            environments_item = DominoJobsInterfaceEnvironmentWithRevisions.from_dict(environments_item_data)

            environments.append(environments_item)

        external_volume_mounts = []
        _external_volume_mounts = d.pop("externalVolumeMounts")
        for external_volume_mounts_item_data in _external_volume_mounts:
            external_volume_mounts_item = DominoJobsInterfaceExternalVolumeMountRefDto.from_dict(
                external_volume_mounts_item_data
            )

            external_volume_mounts.append(external_volume_mounts_item)

        def _parse_main_repo_git_refs(data: object) -> list[DominoProjectsApiRepositoriesReferenceDTO] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                main_repo_git_refs_type_0 = []
                _main_repo_git_refs_type_0 = data
                for main_repo_git_refs_type_0_item_data in _main_repo_git_refs_type_0:
                    main_repo_git_refs_type_0_item = DominoProjectsApiRepositoriesReferenceDTO.from_dict(
                        main_repo_git_refs_type_0_item_data
                    )

                    main_repo_git_refs_type_0.append(main_repo_git_refs_type_0_item)

                return main_repo_git_refs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DominoProjectsApiRepositoriesReferenceDTO] | None | Unset, data)

        main_repo_git_refs = _parse_main_repo_git_refs(d.pop("mainRepoGitRefs", UNSET))

        domino_jobs_interface_valid_job_properties = cls(
            hardware_tiers=hardware_tiers,
            dataset_snapshots=dataset_snapshots,
            environments=environments,
            external_volume_mounts=external_volume_mounts,
            main_repo_git_refs=main_repo_git_refs,
        )

        domino_jobs_interface_valid_job_properties.additional_properties = d
        return domino_jobs_interface_valid_job_properties

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
