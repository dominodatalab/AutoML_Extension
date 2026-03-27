from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.domino_scheduledjob_api_scheduled_job_dto_capacity_type import (
    DominoScheduledjobApiScheduledJobDtoCapacityType,
)
from ..models.domino_scheduledjob_api_scheduled_job_dto_environment_revision_spec_type_0 import (
    DominoScheduledjobApiScheduledJobDtoEnvironmentRevisionSpecType0,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_api_repositories_reference_dto import DominoProjectsApiRepositoriesReferenceDTO
    from ..models.domino_scheduledjob_api_compute_cluster_config_spec_dto import (
        DominoScheduledjobApiComputeClusterConfigSpecDto,
    )
    from ..models.domino_scheduledjob_api_cron_schedule_dto import DominoScheduledjobApiCronScheduleDTO
    from ..models.domino_scheduledjob_api_data_config_dto import DominoScheduledjobApiDataConfigDto
    from ..models.domino_scheduledjob_api_scheduled_job_dto_environment_revision_spec_type_1 import (
        DominoScheduledjobApiScheduledJobDtoEnvironmentRevisionSpecType1,
    )
    from ..models.domino_scheduledjob_api_scheduled_job_dto_volume_specification_override_type_0 import (
        DominoScheduledjobApiScheduledJobDtoVolumeSpecificationOverrideType0,
    )


T = TypeVar("T", bound="DominoScheduledjobApiScheduledJobDto")


@_attrs_define
class DominoScheduledjobApiScheduledJobDto:
    """
    Attributes:
        id (str):
        created (datetime.datetime):
        project_id (str):
        title (str):
        command (str):
        schedule (DominoScheduledjobApiCronScheduleDTO):
        timezone_id (str):
        is_paused (bool):
        allow_concurrent_execution (bool):
        hardware_tier_identifier (str):
        hardware_tier_name (str):
        environment_revision_spec (DominoScheduledjobApiScheduledJobDtoEnvironmentRevisionSpecType0 |
            DominoScheduledjobApiScheduledJobDtoEnvironmentRevisionSpecType1):
        scheduled_by_user_id (str):
        scheduled_by_user_name (str):
        notify_on_complete_email_addresses (list[str]):
        data_config (DominoScheduledjobApiDataConfigDto):
        publish_model_id (None | str | Unset):
        capacity_type (DominoScheduledjobApiScheduledJobDtoCapacityType | Unset):
        override_environment_id (None | str | Unset):
        compute_cluster_properties (DominoScheduledjobApiComputeClusterConfigSpecDto | Unset):
        volume_specification_override (DominoScheduledjobApiScheduledJobDtoVolumeSpecificationOverrideType0 | None |
            Unset):
        main_repo_git_ref (DominoProjectsApiRepositoriesReferenceDTO | Unset):
    """

    id: str
    created: datetime.datetime
    project_id: str
    title: str
    command: str
    schedule: DominoScheduledjobApiCronScheduleDTO
    timezone_id: str
    is_paused: bool
    allow_concurrent_execution: bool
    hardware_tier_identifier: str
    hardware_tier_name: str
    environment_revision_spec: (
        DominoScheduledjobApiScheduledJobDtoEnvironmentRevisionSpecType0
        | DominoScheduledjobApiScheduledJobDtoEnvironmentRevisionSpecType1
    )
    scheduled_by_user_id: str
    scheduled_by_user_name: str
    notify_on_complete_email_addresses: list[str]
    data_config: DominoScheduledjobApiDataConfigDto
    publish_model_id: None | str | Unset = UNSET
    capacity_type: DominoScheduledjobApiScheduledJobDtoCapacityType | Unset = UNSET
    override_environment_id: None | str | Unset = UNSET
    compute_cluster_properties: DominoScheduledjobApiComputeClusterConfigSpecDto | Unset = UNSET
    volume_specification_override: (
        DominoScheduledjobApiScheduledJobDtoVolumeSpecificationOverrideType0 | None | Unset
    ) = UNSET
    main_repo_git_ref: DominoProjectsApiRepositoriesReferenceDTO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.domino_scheduledjob_api_scheduled_job_dto_volume_specification_override_type_0 import (
            DominoScheduledjobApiScheduledJobDtoVolumeSpecificationOverrideType0,
        )

        id = self.id

        created = self.created.isoformat()

        project_id = self.project_id

        title = self.title

        command = self.command

        schedule = self.schedule.to_dict()

        timezone_id = self.timezone_id

        is_paused = self.is_paused

        allow_concurrent_execution = self.allow_concurrent_execution

        hardware_tier_identifier = self.hardware_tier_identifier

        hardware_tier_name = self.hardware_tier_name

        environment_revision_spec: dict[str, Any] | str
        if isinstance(self.environment_revision_spec, DominoScheduledjobApiScheduledJobDtoEnvironmentRevisionSpecType0):
            environment_revision_spec = self.environment_revision_spec.value
        else:
            environment_revision_spec = self.environment_revision_spec.to_dict()

        scheduled_by_user_id = self.scheduled_by_user_id

        scheduled_by_user_name = self.scheduled_by_user_name

        notify_on_complete_email_addresses = self.notify_on_complete_email_addresses

        data_config = self.data_config.to_dict()

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

        compute_cluster_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.compute_cluster_properties, Unset):
            compute_cluster_properties = self.compute_cluster_properties.to_dict()

        volume_specification_override: dict[str, Any] | None | Unset
        if isinstance(self.volume_specification_override, Unset):
            volume_specification_override = UNSET
        elif isinstance(
            self.volume_specification_override, DominoScheduledjobApiScheduledJobDtoVolumeSpecificationOverrideType0
        ):
            volume_specification_override = self.volume_specification_override.to_dict()
        else:
            volume_specification_override = self.volume_specification_override

        main_repo_git_ref: dict[str, Any] | Unset = UNSET
        if not isinstance(self.main_repo_git_ref, Unset):
            main_repo_git_ref = self.main_repo_git_ref.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created": created,
                "projectId": project_id,
                "title": title,
                "command": command,
                "schedule": schedule,
                "timezoneId": timezone_id,
                "isPaused": is_paused,
                "allowConcurrentExecution": allow_concurrent_execution,
                "hardwareTierIdentifier": hardware_tier_identifier,
                "hardwareTierName": hardware_tier_name,
                "environmentRevisionSpec": environment_revision_spec,
                "scheduledByUserId": scheduled_by_user_id,
                "scheduledByUserName": scheduled_by_user_name,
                "notifyOnCompleteEmailAddresses": notify_on_complete_email_addresses,
                "dataConfig": data_config,
            }
        )
        if publish_model_id is not UNSET:
            field_dict["publishModelId"] = publish_model_id
        if capacity_type is not UNSET:
            field_dict["capacityType"] = capacity_type
        if override_environment_id is not UNSET:
            field_dict["overrideEnvironmentId"] = override_environment_id
        if compute_cluster_properties is not UNSET:
            field_dict["computeClusterProperties"] = compute_cluster_properties
        if volume_specification_override is not UNSET:
            field_dict["volumeSpecificationOverride"] = volume_specification_override
        if main_repo_git_ref is not UNSET:
            field_dict["mainRepoGitRef"] = main_repo_git_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_repositories_reference_dto import DominoProjectsApiRepositoriesReferenceDTO
        from ..models.domino_scheduledjob_api_compute_cluster_config_spec_dto import (
            DominoScheduledjobApiComputeClusterConfigSpecDto,
        )
        from ..models.domino_scheduledjob_api_cron_schedule_dto import DominoScheduledjobApiCronScheduleDTO
        from ..models.domino_scheduledjob_api_data_config_dto import DominoScheduledjobApiDataConfigDto
        from ..models.domino_scheduledjob_api_scheduled_job_dto_environment_revision_spec_type_1 import (
            DominoScheduledjobApiScheduledJobDtoEnvironmentRevisionSpecType1,
        )
        from ..models.domino_scheduledjob_api_scheduled_job_dto_volume_specification_override_type_0 import (
            DominoScheduledjobApiScheduledJobDtoVolumeSpecificationOverrideType0,
        )

        d = dict(src_dict)
        id = d.pop("id")

        created = isoparse(d.pop("created"))

        project_id = d.pop("projectId")

        title = d.pop("title")

        command = d.pop("command")

        schedule = DominoScheduledjobApiCronScheduleDTO.from_dict(d.pop("schedule"))

        timezone_id = d.pop("timezoneId")

        is_paused = d.pop("isPaused")

        allow_concurrent_execution = d.pop("allowConcurrentExecution")

        hardware_tier_identifier = d.pop("hardwareTierIdentifier")

        hardware_tier_name = d.pop("hardwareTierName")

        def _parse_environment_revision_spec(
            data: object,
        ) -> (
            DominoScheduledjobApiScheduledJobDtoEnvironmentRevisionSpecType0
            | DominoScheduledjobApiScheduledJobDtoEnvironmentRevisionSpecType1
        ):
            try:
                if not isinstance(data, str):
                    raise TypeError()
                environment_revision_spec_type_0 = DominoScheduledjobApiScheduledJobDtoEnvironmentRevisionSpecType0(
                    data
                )

                return environment_revision_spec_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            environment_revision_spec_type_1 = (
                DominoScheduledjobApiScheduledJobDtoEnvironmentRevisionSpecType1.from_dict(data)
            )

            return environment_revision_spec_type_1

        environment_revision_spec = _parse_environment_revision_spec(d.pop("environmentRevisionSpec"))

        scheduled_by_user_id = d.pop("scheduledByUserId")

        scheduled_by_user_name = d.pop("scheduledByUserName")

        notify_on_complete_email_addresses = cast(list[str], d.pop("notifyOnCompleteEmailAddresses"))

        data_config = DominoScheduledjobApiDataConfigDto.from_dict(d.pop("dataConfig"))

        def _parse_publish_model_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        publish_model_id = _parse_publish_model_id(d.pop("publishModelId", UNSET))

        _capacity_type = d.pop("capacityType", UNSET)
        capacity_type: DominoScheduledjobApiScheduledJobDtoCapacityType | Unset
        if isinstance(_capacity_type, Unset):
            capacity_type = UNSET
        else:
            capacity_type = DominoScheduledjobApiScheduledJobDtoCapacityType(_capacity_type)

        def _parse_override_environment_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        override_environment_id = _parse_override_environment_id(d.pop("overrideEnvironmentId", UNSET))

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
        ) -> DominoScheduledjobApiScheduledJobDtoVolumeSpecificationOverrideType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                volume_specification_override_type_0 = (
                    DominoScheduledjobApiScheduledJobDtoVolumeSpecificationOverrideType0.from_dict(data)
                )

                return volume_specification_override_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DominoScheduledjobApiScheduledJobDtoVolumeSpecificationOverrideType0 | None | Unset, data)

        volume_specification_override = _parse_volume_specification_override(
            d.pop("volumeSpecificationOverride", UNSET)
        )

        _main_repo_git_ref = d.pop("mainRepoGitRef", UNSET)
        main_repo_git_ref: DominoProjectsApiRepositoriesReferenceDTO | Unset
        if isinstance(_main_repo_git_ref, Unset):
            main_repo_git_ref = UNSET
        else:
            main_repo_git_ref = DominoProjectsApiRepositoriesReferenceDTO.from_dict(_main_repo_git_ref)

        domino_scheduledjob_api_scheduled_job_dto = cls(
            id=id,
            created=created,
            project_id=project_id,
            title=title,
            command=command,
            schedule=schedule,
            timezone_id=timezone_id,
            is_paused=is_paused,
            allow_concurrent_execution=allow_concurrent_execution,
            hardware_tier_identifier=hardware_tier_identifier,
            hardware_tier_name=hardware_tier_name,
            environment_revision_spec=environment_revision_spec,
            scheduled_by_user_id=scheduled_by_user_id,
            scheduled_by_user_name=scheduled_by_user_name,
            notify_on_complete_email_addresses=notify_on_complete_email_addresses,
            data_config=data_config,
            publish_model_id=publish_model_id,
            capacity_type=capacity_type,
            override_environment_id=override_environment_id,
            compute_cluster_properties=compute_cluster_properties,
            volume_specification_override=volume_specification_override,
            main_repo_git_ref=main_repo_git_ref,
        )

        domino_scheduledjob_api_scheduled_job_dto.additional_properties = d
        return domino_scheduledjob_api_scheduled_job_dto

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
