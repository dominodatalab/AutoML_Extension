from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_scheduledjob_api_updated_scheduled_job_dto_capacity_type import (
    DominoScheduledjobApiUpdatedScheduledJobDTOCapacityType,
)
from ..models.domino_scheduledjob_api_updated_scheduled_job_dto_environment_revision_spec_type_0 import (
    DominoScheduledjobApiUpdatedScheduledJobDTOEnvironmentRevisionSpecType0,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_api_repositories_reference_dto import DominoProjectsApiRepositoriesReferenceDTO
    from ..models.domino_scheduledjob_api_compute_cluster_config_spec_dto import (
        DominoScheduledjobApiComputeClusterConfigSpecDto,
    )
    from ..models.domino_scheduledjob_api_edit_cron_schedule_dto import DominoScheduledjobApiEditCronScheduleDTO
    from ..models.domino_scheduledjob_api_updated_scheduled_job_dto_environment_revision_spec_type_1 import (
        DominoScheduledjobApiUpdatedScheduledJobDTOEnvironmentRevisionSpecType1,
    )
    from ..models.domino_scheduledjob_api_updated_scheduled_job_dto_volume_specification_override_type_0 import (
        DominoScheduledjobApiUpdatedScheduledJobDTOVolumeSpecificationOverrideType0,
    )


T = TypeVar("T", bound="DominoScheduledjobApiUpdatedScheduledJobDTO")


@_attrs_define
class DominoScheduledjobApiUpdatedScheduledJobDTO:
    """
    Attributes:
        title (str):
        command (str):
        schedule (DominoScheduledjobApiEditCronScheduleDTO):
        timezone_id (str):
        is_paused (bool):
        allow_concurrent_execution (bool):
        hardware_tier_identifier (str):
        environment_revision_spec (DominoScheduledjobApiUpdatedScheduledJobDTOEnvironmentRevisionSpecType0 |
            DominoScheduledjobApiUpdatedScheduledJobDTOEnvironmentRevisionSpecType1):
        scheduled_by_user_id (str):
        notify_on_complete_email_addresses (list[str]):
        publish_model_id (None | str | Unset):
        capacity_type (DominoScheduledjobApiUpdatedScheduledJobDTOCapacityType | Unset):
        override_environment_id (None | str | Unset):
        dataset_config (None | str | Unset):
        compute_cluster_properties (DominoScheduledjobApiComputeClusterConfigSpecDto | Unset):
        volume_specification_override (DominoScheduledjobApiUpdatedScheduledJobDTOVolumeSpecificationOverrideType0 |
            None | Unset):
        external_volume_mounts (list[str] | None | Unset):
        net_app_volume_ids (list[str] | None | Unset):
        main_repo_git_ref (DominoProjectsApiRepositoriesReferenceDTO | Unset):
        snapshot_datasets_on_completion (bool | None | Unset):
        snapshot_net_app_volumes_on_completion (bool | None | Unset):
    """

    title: str
    command: str
    schedule: DominoScheduledjobApiEditCronScheduleDTO
    timezone_id: str
    is_paused: bool
    allow_concurrent_execution: bool
    hardware_tier_identifier: str
    environment_revision_spec: (
        DominoScheduledjobApiUpdatedScheduledJobDTOEnvironmentRevisionSpecType0
        | DominoScheduledjobApiUpdatedScheduledJobDTOEnvironmentRevisionSpecType1
    )
    scheduled_by_user_id: str
    notify_on_complete_email_addresses: list[str]
    publish_model_id: None | str | Unset = UNSET
    capacity_type: DominoScheduledjobApiUpdatedScheduledJobDTOCapacityType | Unset = UNSET
    override_environment_id: None | str | Unset = UNSET
    dataset_config: None | str | Unset = UNSET
    compute_cluster_properties: DominoScheduledjobApiComputeClusterConfigSpecDto | Unset = UNSET
    volume_specification_override: (
        DominoScheduledjobApiUpdatedScheduledJobDTOVolumeSpecificationOverrideType0 | None | Unset
    ) = UNSET
    external_volume_mounts: list[str] | None | Unset = UNSET
    net_app_volume_ids: list[str] | None | Unset = UNSET
    main_repo_git_ref: DominoProjectsApiRepositoriesReferenceDTO | Unset = UNSET
    snapshot_datasets_on_completion: bool | None | Unset = UNSET
    snapshot_net_app_volumes_on_completion: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.domino_scheduledjob_api_updated_scheduled_job_dto_volume_specification_override_type_0 import (
            DominoScheduledjobApiUpdatedScheduledJobDTOVolumeSpecificationOverrideType0,
        )

        title = self.title

        command = self.command

        schedule = self.schedule.to_dict()

        timezone_id = self.timezone_id

        is_paused = self.is_paused

        allow_concurrent_execution = self.allow_concurrent_execution

        hardware_tier_identifier = self.hardware_tier_identifier

        environment_revision_spec: dict[str, Any] | str
        if isinstance(
            self.environment_revision_spec, DominoScheduledjobApiUpdatedScheduledJobDTOEnvironmentRevisionSpecType0
        ):
            environment_revision_spec = self.environment_revision_spec.value
        else:
            environment_revision_spec = self.environment_revision_spec.to_dict()

        scheduled_by_user_id = self.scheduled_by_user_id

        notify_on_complete_email_addresses = self.notify_on_complete_email_addresses

        publish_model_id: None | str | Unset
        if isinstance(self.publish_model_id, Unset):
            publish_model_id = UNSET
        else:
            publish_model_id = self.publish_model_id

        capacity_type: str | Unset = UNSET
        if not isinstance(self.capacity_type, Unset):
            capacity_type = self.capacity_type.value

        override_environment_id: None | str | Unset
        if isinstance(self.override_environment_id, Unset):
            override_environment_id = UNSET
        else:
            override_environment_id = self.override_environment_id

        dataset_config: None | str | Unset
        if isinstance(self.dataset_config, Unset):
            dataset_config = UNSET
        else:
            dataset_config = self.dataset_config

        compute_cluster_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.compute_cluster_properties, Unset):
            compute_cluster_properties = self.compute_cluster_properties.to_dict()

        volume_specification_override: dict[str, Any] | None | Unset
        if isinstance(self.volume_specification_override, Unset):
            volume_specification_override = UNSET
        elif isinstance(
            self.volume_specification_override,
            DominoScheduledjobApiUpdatedScheduledJobDTOVolumeSpecificationOverrideType0,
        ):
            volume_specification_override = self.volume_specification_override.to_dict()
        else:
            volume_specification_override = self.volume_specification_override

        external_volume_mounts: list[str] | None | Unset
        if isinstance(self.external_volume_mounts, Unset):
            external_volume_mounts = UNSET
        elif isinstance(self.external_volume_mounts, list):
            external_volume_mounts = self.external_volume_mounts

        else:
            external_volume_mounts = self.external_volume_mounts

        net_app_volume_ids: list[str] | None | Unset
        if isinstance(self.net_app_volume_ids, Unset):
            net_app_volume_ids = UNSET
        elif isinstance(self.net_app_volume_ids, list):
            net_app_volume_ids = self.net_app_volume_ids

        else:
            net_app_volume_ids = self.net_app_volume_ids

        main_repo_git_ref: dict[str, Any] | Unset = UNSET
        if not isinstance(self.main_repo_git_ref, Unset):
            main_repo_git_ref = self.main_repo_git_ref.to_dict()

        snapshot_datasets_on_completion: bool | None | Unset
        if isinstance(self.snapshot_datasets_on_completion, Unset):
            snapshot_datasets_on_completion = UNSET
        else:
            snapshot_datasets_on_completion = self.snapshot_datasets_on_completion

        snapshot_net_app_volumes_on_completion: bool | None | Unset
        if isinstance(self.snapshot_net_app_volumes_on_completion, Unset):
            snapshot_net_app_volumes_on_completion = UNSET
        else:
            snapshot_net_app_volumes_on_completion = self.snapshot_net_app_volumes_on_completion

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "command": command,
                "schedule": schedule,
                "timezoneId": timezone_id,
                "isPaused": is_paused,
                "allowConcurrentExecution": allow_concurrent_execution,
                "hardwareTierIdentifier": hardware_tier_identifier,
                "environmentRevisionSpec": environment_revision_spec,
                "scheduledByUserId": scheduled_by_user_id,
                "notifyOnCompleteEmailAddresses": notify_on_complete_email_addresses,
            }
        )
        if publish_model_id is not UNSET:
            field_dict["publishModelId"] = publish_model_id
        if capacity_type is not UNSET:
            field_dict["capacityType"] = capacity_type
        if override_environment_id is not UNSET:
            field_dict["overrideEnvironmentId"] = override_environment_id
        if dataset_config is not UNSET:
            field_dict["datasetConfig"] = dataset_config
        if compute_cluster_properties is not UNSET:
            field_dict["computeClusterProperties"] = compute_cluster_properties
        if volume_specification_override is not UNSET:
            field_dict["volumeSpecificationOverride"] = volume_specification_override
        if external_volume_mounts is not UNSET:
            field_dict["externalVolumeMounts"] = external_volume_mounts
        if net_app_volume_ids is not UNSET:
            field_dict["netAppVolumeIds"] = net_app_volume_ids
        if main_repo_git_ref is not UNSET:
            field_dict["mainRepoGitRef"] = main_repo_git_ref
        if snapshot_datasets_on_completion is not UNSET:
            field_dict["snapshotDatasetsOnCompletion"] = snapshot_datasets_on_completion
        if snapshot_net_app_volumes_on_completion is not UNSET:
            field_dict["snapshotNetAppVolumesOnCompletion"] = snapshot_net_app_volumes_on_completion

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_repositories_reference_dto import DominoProjectsApiRepositoriesReferenceDTO
        from ..models.domino_scheduledjob_api_compute_cluster_config_spec_dto import (
            DominoScheduledjobApiComputeClusterConfigSpecDto,
        )
        from ..models.domino_scheduledjob_api_edit_cron_schedule_dto import DominoScheduledjobApiEditCronScheduleDTO
        from ..models.domino_scheduledjob_api_updated_scheduled_job_dto_environment_revision_spec_type_1 import (
            DominoScheduledjobApiUpdatedScheduledJobDTOEnvironmentRevisionSpecType1,
        )
        from ..models.domino_scheduledjob_api_updated_scheduled_job_dto_volume_specification_override_type_0 import (
            DominoScheduledjobApiUpdatedScheduledJobDTOVolumeSpecificationOverrideType0,
        )

        d = dict(src_dict)
        title = d.pop("title")

        command = d.pop("command")

        schedule = DominoScheduledjobApiEditCronScheduleDTO.from_dict(d.pop("schedule"))

        timezone_id = d.pop("timezoneId")

        is_paused = d.pop("isPaused")

        allow_concurrent_execution = d.pop("allowConcurrentExecution")

        hardware_tier_identifier = d.pop("hardwareTierIdentifier")

        def _parse_environment_revision_spec(
            data: object,
        ) -> (
            DominoScheduledjobApiUpdatedScheduledJobDTOEnvironmentRevisionSpecType0
            | DominoScheduledjobApiUpdatedScheduledJobDTOEnvironmentRevisionSpecType1
        ):
            try:
                if not isinstance(data, str):
                    raise TypeError()
                environment_revision_spec_type_0 = (
                    DominoScheduledjobApiUpdatedScheduledJobDTOEnvironmentRevisionSpecType0(data)
                )

                return environment_revision_spec_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            environment_revision_spec_type_1 = (
                DominoScheduledjobApiUpdatedScheduledJobDTOEnvironmentRevisionSpecType1.from_dict(data)
            )

            return environment_revision_spec_type_1

        environment_revision_spec = _parse_environment_revision_spec(d.pop("environmentRevisionSpec"))

        scheduled_by_user_id = d.pop("scheduledByUserId")

        notify_on_complete_email_addresses = cast(list[str], d.pop("notifyOnCompleteEmailAddresses"))

        def _parse_publish_model_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        publish_model_id = _parse_publish_model_id(d.pop("publishModelId", UNSET))

        _capacity_type = d.pop("capacityType", UNSET)
        capacity_type: DominoScheduledjobApiUpdatedScheduledJobDTOCapacityType | Unset
        if isinstance(_capacity_type, Unset):
            capacity_type = UNSET
        else:
            capacity_type = DominoScheduledjobApiUpdatedScheduledJobDTOCapacityType(_capacity_type)

        def _parse_override_environment_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        override_environment_id = _parse_override_environment_id(d.pop("overrideEnvironmentId", UNSET))

        def _parse_dataset_config(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_config = _parse_dataset_config(d.pop("datasetConfig", UNSET))

        _compute_cluster_properties = d.pop("computeClusterProperties", UNSET)
        compute_cluster_properties: DominoScheduledjobApiComputeClusterConfigSpecDto | Unset
        if isinstance(_compute_cluster_properties, Unset):
            compute_cluster_properties = UNSET
        else:
            compute_cluster_properties = DominoScheduledjobApiComputeClusterConfigSpecDto.from_dict(
                _compute_cluster_properties
            )

        def _parse_volume_specification_override(
            data: object,
        ) -> DominoScheduledjobApiUpdatedScheduledJobDTOVolumeSpecificationOverrideType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                volume_specification_override_type_0 = (
                    DominoScheduledjobApiUpdatedScheduledJobDTOVolumeSpecificationOverrideType0.from_dict(data)
                )

                return volume_specification_override_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                DominoScheduledjobApiUpdatedScheduledJobDTOVolumeSpecificationOverrideType0 | None | Unset, data
            )

        volume_specification_override = _parse_volume_specification_override(
            d.pop("volumeSpecificationOverride", UNSET)
        )

        def _parse_external_volume_mounts(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                external_volume_mounts_type_0 = cast(list[str], data)

                return external_volume_mounts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        external_volume_mounts = _parse_external_volume_mounts(d.pop("externalVolumeMounts", UNSET))

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

        _main_repo_git_ref = d.pop("mainRepoGitRef", UNSET)
        main_repo_git_ref: DominoProjectsApiRepositoriesReferenceDTO | Unset
        if isinstance(_main_repo_git_ref, Unset):
            main_repo_git_ref = UNSET
        else:
            main_repo_git_ref = DominoProjectsApiRepositoriesReferenceDTO.from_dict(_main_repo_git_ref)

        def _parse_snapshot_datasets_on_completion(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        snapshot_datasets_on_completion = _parse_snapshot_datasets_on_completion(
            d.pop("snapshotDatasetsOnCompletion", UNSET)
        )

        def _parse_snapshot_net_app_volumes_on_completion(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        snapshot_net_app_volumes_on_completion = _parse_snapshot_net_app_volumes_on_completion(
            d.pop("snapshotNetAppVolumesOnCompletion", UNSET)
        )

        domino_scheduledjob_api_updated_scheduled_job_dto = cls(
            title=title,
            command=command,
            schedule=schedule,
            timezone_id=timezone_id,
            is_paused=is_paused,
            allow_concurrent_execution=allow_concurrent_execution,
            hardware_tier_identifier=hardware_tier_identifier,
            environment_revision_spec=environment_revision_spec,
            scheduled_by_user_id=scheduled_by_user_id,
            notify_on_complete_email_addresses=notify_on_complete_email_addresses,
            publish_model_id=publish_model_id,
            capacity_type=capacity_type,
            override_environment_id=override_environment_id,
            dataset_config=dataset_config,
            compute_cluster_properties=compute_cluster_properties,
            volume_specification_override=volume_specification_override,
            external_volume_mounts=external_volume_mounts,
            net_app_volume_ids=net_app_volume_ids,
            main_repo_git_ref=main_repo_git_ref,
            snapshot_datasets_on_completion=snapshot_datasets_on_completion,
            snapshot_net_app_volumes_on_completion=snapshot_net_app_volumes_on_completion,
        )

        domino_scheduledjob_api_updated_scheduled_job_dto.additional_properties = d
        return domino_scheduledjob_api_updated_scheduled_job_dto

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
