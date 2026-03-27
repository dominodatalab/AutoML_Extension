from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_server_projects_api_project_gateway_overview_allowed_operations_item import (
    DominoServerProjectsApiProjectGatewayOverviewAllowedOperationsItem,
)
from ..models.domino_server_projects_api_project_gateway_overview_requesting_user_role import (
    DominoServerProjectsApiProjectGatewayOverviewRequestingUserRole,
)
from ..models.domino_server_projects_api_project_gateway_overview_visibility import (
    DominoServerProjectsApiProjectGatewayOverviewVisibility,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_api_project_template_details import DominoProjectsApiProjectTemplateDetails
    from ..models.domino_repoman_domain_git_repository import DominoRepomanDomainGitRepository
    from ..models.domino_server_projects_api_main_repository_details import DominoServerProjectsApiMainRepositoryDetails
    from ..models.domino_server_projects_api_owner import DominoServerProjectsApiOwner
    from ..models.domino_server_projects_api_project_gateway_executing_runs_by_type import (
        DominoServerProjectsApiProjectGatewayExecutingRunsByType,
    )
    from ..models.domino_server_projects_api_project_gateway_overview_details import (
        DominoServerProjectsApiProjectGatewayOverviewDetails,
    )
    from ..models.domino_server_projects_api_project_gateway_tag import DominoServerProjectsApiProjectGatewayTag
    from ..models.domino_server_projects_api_project_status import DominoServerProjectsApiProjectStatus


T = TypeVar("T", bound="DominoServerProjectsApiProjectGatewayOverview")


@_attrs_define
class DominoServerProjectsApiProjectGatewayOverview:
    """Project Overview entity returned by the API gateway

    Attributes:
        owner (DominoServerProjectsApiOwner):
        visibility (DominoServerProjectsApiProjectGatewayOverviewVisibility):
        hardware_tier_name (str):
        description (str):
        hardware_tier_id (str):
        requesting_user_role (DominoServerProjectsApiProjectGatewayOverviewRequestingUserRole):
        total_run_time (str): sum of run times of all executions in the project, in ISO8601 duration format including
            only seconds and milliseconds
        tags (list[DominoServerProjectsApiProjectGatewayTag]):
        num_comments (int):
        runs_count_by_type (list[DominoServerProjectsApiProjectGatewayExecutingRunsByType]):
        allowed_operations (list[DominoServerProjectsApiProjectGatewayOverviewAllowedOperationsItem]):
        environment_name (str):
        name (str):
        id (str):
        stage_id (str):
        status (DominoServerProjectsApiProjectStatus):
        template_details (DominoProjectsApiProjectTemplateDetails | Unset):
        last_status_change_in_millis (int | None | Unset):
        last_stage_change_in_millis (int | None | Unset):
        main_repository (DominoServerProjectsApiMainRepositoryDetails | Unset):
        enabled_git_repositories (list[DominoRepomanDomainGitRepository] | Unset):
        details (DominoServerProjectsApiProjectGatewayOverviewDetails | Unset):
    """

    owner: DominoServerProjectsApiOwner
    visibility: DominoServerProjectsApiProjectGatewayOverviewVisibility
    hardware_tier_name: str
    description: str
    hardware_tier_id: str
    requesting_user_role: DominoServerProjectsApiProjectGatewayOverviewRequestingUserRole
    total_run_time: str
    tags: list[DominoServerProjectsApiProjectGatewayTag]
    num_comments: int
    runs_count_by_type: list[DominoServerProjectsApiProjectGatewayExecutingRunsByType]
    allowed_operations: list[DominoServerProjectsApiProjectGatewayOverviewAllowedOperationsItem]
    environment_name: str
    name: str
    id: str
    stage_id: str
    status: DominoServerProjectsApiProjectStatus
    template_details: DominoProjectsApiProjectTemplateDetails | Unset = UNSET
    last_status_change_in_millis: int | None | Unset = UNSET
    last_stage_change_in_millis: int | None | Unset = UNSET
    main_repository: DominoServerProjectsApiMainRepositoryDetails | Unset = UNSET
    enabled_git_repositories: list[DominoRepomanDomainGitRepository] | Unset = UNSET
    details: DominoServerProjectsApiProjectGatewayOverviewDetails | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        owner = self.owner.to_dict()

        visibility = self.visibility.value

        hardware_tier_name = self.hardware_tier_name

        description = self.description

        hardware_tier_id = self.hardware_tier_id

        requesting_user_role = self.requesting_user_role.value

        total_run_time = self.total_run_time

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.to_dict()
            tags.append(tags_item)

        num_comments = self.num_comments

        runs_count_by_type = []
        for runs_count_by_type_item_data in self.runs_count_by_type:
            runs_count_by_type_item = runs_count_by_type_item_data.to_dict()
            runs_count_by_type.append(runs_count_by_type_item)

        allowed_operations = []
        for allowed_operations_item_data in self.allowed_operations:
            allowed_operations_item = allowed_operations_item_data.value
            allowed_operations.append(allowed_operations_item)

        environment_name = self.environment_name

        name = self.name

        id = self.id

        stage_id = self.stage_id

        status = self.status.to_dict()

        template_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template_details, Unset):
            template_details = self.template_details.to_dict()

        last_status_change_in_millis: int | None | Unset
        if isinstance(self.last_status_change_in_millis, Unset):
            last_status_change_in_millis = UNSET
        else:
            last_status_change_in_millis = self.last_status_change_in_millis

        last_stage_change_in_millis: int | None | Unset
        if isinstance(self.last_stage_change_in_millis, Unset):
            last_stage_change_in_millis = UNSET
        else:
            last_stage_change_in_millis = self.last_stage_change_in_millis

        main_repository: dict[str, Any] | Unset = UNSET
        if not isinstance(self.main_repository, Unset):
            main_repository = self.main_repository.to_dict()

        enabled_git_repositories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.enabled_git_repositories, Unset):
            enabled_git_repositories = []
            for enabled_git_repositories_item_data in self.enabled_git_repositories:
                enabled_git_repositories_item = enabled_git_repositories_item_data.to_dict()
                enabled_git_repositories.append(enabled_git_repositories_item)

        details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "owner": owner,
                "visibility": visibility,
                "hardwareTierName": hardware_tier_name,
                "description": description,
                "hardwareTierId": hardware_tier_id,
                "requestingUserRole": requesting_user_role,
                "totalRunTime": total_run_time,
                "tags": tags,
                "numComments": num_comments,
                "runsCountByType": runs_count_by_type,
                "allowedOperations": allowed_operations,
                "environmentName": environment_name,
                "name": name,
                "id": id,
                "stageId": stage_id,
                "status": status,
            }
        )
        if template_details is not UNSET:
            field_dict["templateDetails"] = template_details
        if last_status_change_in_millis is not UNSET:
            field_dict["lastStatusChangeInMillis"] = last_status_change_in_millis
        if last_stage_change_in_millis is not UNSET:
            field_dict["lastStageChangeInMillis"] = last_stage_change_in_millis
        if main_repository is not UNSET:
            field_dict["mainRepository"] = main_repository
        if enabled_git_repositories is not UNSET:
            field_dict["enabledGitRepositories"] = enabled_git_repositories
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_project_template_details import DominoProjectsApiProjectTemplateDetails
        from ..models.domino_repoman_domain_git_repository import DominoRepomanDomainGitRepository
        from ..models.domino_server_projects_api_main_repository_details import (
            DominoServerProjectsApiMainRepositoryDetails,
        )
        from ..models.domino_server_projects_api_owner import DominoServerProjectsApiOwner
        from ..models.domino_server_projects_api_project_gateway_executing_runs_by_type import (
            DominoServerProjectsApiProjectGatewayExecutingRunsByType,
        )
        from ..models.domino_server_projects_api_project_gateway_overview_details import (
            DominoServerProjectsApiProjectGatewayOverviewDetails,
        )
        from ..models.domino_server_projects_api_project_gateway_tag import DominoServerProjectsApiProjectGatewayTag
        from ..models.domino_server_projects_api_project_status import DominoServerProjectsApiProjectStatus

        d = dict(src_dict)
        owner = DominoServerProjectsApiOwner.from_dict(d.pop("owner"))

        visibility = DominoServerProjectsApiProjectGatewayOverviewVisibility(d.pop("visibility"))

        hardware_tier_name = d.pop("hardwareTierName")

        description = d.pop("description")

        hardware_tier_id = d.pop("hardwareTierId")

        requesting_user_role = DominoServerProjectsApiProjectGatewayOverviewRequestingUserRole(
            d.pop("requestingUserRole")
        )

        total_run_time = d.pop("totalRunTime")

        tags = []
        _tags = d.pop("tags")
        for tags_item_data in _tags:
            tags_item = DominoServerProjectsApiProjectGatewayTag.from_dict(tags_item_data)

            tags.append(tags_item)

        num_comments = d.pop("numComments")

        runs_count_by_type = []
        _runs_count_by_type = d.pop("runsCountByType")
        for runs_count_by_type_item_data in _runs_count_by_type:
            runs_count_by_type_item = DominoServerProjectsApiProjectGatewayExecutingRunsByType.from_dict(
                runs_count_by_type_item_data
            )

            runs_count_by_type.append(runs_count_by_type_item)

        allowed_operations = []
        _allowed_operations = d.pop("allowedOperations")
        for allowed_operations_item_data in _allowed_operations:
            allowed_operations_item = DominoServerProjectsApiProjectGatewayOverviewAllowedOperationsItem(
                allowed_operations_item_data
            )

            allowed_operations.append(allowed_operations_item)

        environment_name = d.pop("environmentName")

        name = d.pop("name")

        id = d.pop("id")

        stage_id = d.pop("stageId")

        status = DominoServerProjectsApiProjectStatus.from_dict(d.pop("status"))

        _template_details = d.pop("templateDetails", UNSET)
        template_details: DominoProjectsApiProjectTemplateDetails | Unset
        if isinstance(_template_details, Unset):
            template_details = UNSET
        else:
            template_details = DominoProjectsApiProjectTemplateDetails.from_dict(_template_details)

        def _parse_last_status_change_in_millis(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_status_change_in_millis = _parse_last_status_change_in_millis(d.pop("lastStatusChangeInMillis", UNSET))

        def _parse_last_stage_change_in_millis(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_stage_change_in_millis = _parse_last_stage_change_in_millis(d.pop("lastStageChangeInMillis", UNSET))

        _main_repository = d.pop("mainRepository", UNSET)
        main_repository: DominoServerProjectsApiMainRepositoryDetails | Unset
        if isinstance(_main_repository, Unset):
            main_repository = UNSET
        else:
            main_repository = DominoServerProjectsApiMainRepositoryDetails.from_dict(_main_repository)

        _enabled_git_repositories = d.pop("enabledGitRepositories", UNSET)
        enabled_git_repositories: list[DominoRepomanDomainGitRepository] | Unset = UNSET
        if _enabled_git_repositories is not UNSET:
            enabled_git_repositories = []
            for enabled_git_repositories_item_data in _enabled_git_repositories:
                enabled_git_repositories_item = DominoRepomanDomainGitRepository.from_dict(
                    enabled_git_repositories_item_data
                )

                enabled_git_repositories.append(enabled_git_repositories_item)

        _details = d.pop("details", UNSET)
        details: DominoServerProjectsApiProjectGatewayOverviewDetails | Unset
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = DominoServerProjectsApiProjectGatewayOverviewDetails.from_dict(_details)

        domino_server_projects_api_project_gateway_overview = cls(
            owner=owner,
            visibility=visibility,
            hardware_tier_name=hardware_tier_name,
            description=description,
            hardware_tier_id=hardware_tier_id,
            requesting_user_role=requesting_user_role,
            total_run_time=total_run_time,
            tags=tags,
            num_comments=num_comments,
            runs_count_by_type=runs_count_by_type,
            allowed_operations=allowed_operations,
            environment_name=environment_name,
            name=name,
            id=id,
            stage_id=stage_id,
            status=status,
            template_details=template_details,
            last_status_change_in_millis=last_status_change_in_millis,
            last_stage_change_in_millis=last_stage_change_in_millis,
            main_repository=main_repository,
            enabled_git_repositories=enabled_git_repositories,
            details=details,
        )

        domino_server_projects_api_project_gateway_overview.additional_properties = d
        return domino_server_projects_api_project_gateway_overview

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
