from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.domino_server_projects_api_project_gateway_summary_project_type import (
    DominoServerProjectsApiProjectGatewaySummaryProjectType,
)
from ..models.domino_server_projects_api_project_gateway_summary_relationship import (
    DominoServerProjectsApiProjectGatewaySummaryRelationship,
)
from ..models.domino_server_projects_api_project_gateway_summary_service_provider import (
    DominoServerProjectsApiProjectGatewaySummaryServiceProvider,
)
from ..models.domino_server_projects_api_project_gateway_summary_visibility import (
    DominoServerProjectsApiProjectGatewaySummaryVisibility,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_server_projects_api_project_gateway_run_count_for_type import (
        DominoServerProjectsApiProjectGatewayRunCountForType,
    )
    from ..models.domino_server_projects_api_project_gateway_summary_details import (
        DominoServerProjectsApiProjectGatewaySummaryDetails,
    )
    from ..models.domino_server_projects_api_project_gateway_tag import DominoServerProjectsApiProjectGatewayTag
    from ..models.domino_server_projects_api_project_status import DominoServerProjectsApiProjectStatus


T = TypeVar("T", bound="DominoServerProjectsApiProjectGatewaySummary")


@_attrs_define
class DominoServerProjectsApiProjectGatewaySummary:
    """
    Attributes:
        id (str):
        name (str):
        owner_id (str):
        owner_name (str):
        description (str):
        visibility (DominoServerProjectsApiProjectGatewaySummaryVisibility):
        tags (list[DominoServerProjectsApiProjectGatewayTag]):
        run_counts (list[DominoServerProjectsApiProjectGatewayRunCountForType]):
        relationship (DominoServerProjectsApiProjectGatewaySummaryRelationship):
        project_type (DominoServerProjectsApiProjectGatewaySummaryProjectType):
        stage_id (str):
        status (DominoServerProjectsApiProjectStatus):
        details (DominoServerProjectsApiProjectGatewaySummaryDetails):
        latest_result_timestamp (datetime.datetime | None | Unset):
        latest_result_run_id (None | str | Unset):
        main_git_repository_uri (None | str | Unset):
        service_provider (DominoServerProjectsApiProjectGatewaySummaryServiceProvider | Unset):
        is_pinned (bool | None | Unset):
    """

    id: str
    name: str
    owner_id: str
    owner_name: str
    description: str
    visibility: DominoServerProjectsApiProjectGatewaySummaryVisibility
    tags: list[DominoServerProjectsApiProjectGatewayTag]
    run_counts: list[DominoServerProjectsApiProjectGatewayRunCountForType]
    relationship: DominoServerProjectsApiProjectGatewaySummaryRelationship
    project_type: DominoServerProjectsApiProjectGatewaySummaryProjectType
    stage_id: str
    status: DominoServerProjectsApiProjectStatus
    details: DominoServerProjectsApiProjectGatewaySummaryDetails
    latest_result_timestamp: datetime.datetime | None | Unset = UNSET
    latest_result_run_id: None | str | Unset = UNSET
    main_git_repository_uri: None | str | Unset = UNSET
    service_provider: DominoServerProjectsApiProjectGatewaySummaryServiceProvider | Unset = UNSET
    is_pinned: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        owner_id = self.owner_id

        owner_name = self.owner_name

        description = self.description

        visibility = self.visibility.value

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.to_dict()
            tags.append(tags_item)

        run_counts = []
        for run_counts_item_data in self.run_counts:
            run_counts_item = run_counts_item_data.to_dict()
            run_counts.append(run_counts_item)

        relationship = self.relationship.value

        project_type = self.project_type.value

        stage_id = self.stage_id

        status = self.status.to_dict()

        details = self.details.to_dict()

        latest_result_timestamp: None | str | Unset
        if isinstance(self.latest_result_timestamp, Unset):
            latest_result_timestamp = UNSET
        elif isinstance(self.latest_result_timestamp, datetime.datetime):
            latest_result_timestamp = self.latest_result_timestamp.isoformat()
        else:
            latest_result_timestamp = self.latest_result_timestamp

        latest_result_run_id: None | str | Unset
        if isinstance(self.latest_result_run_id, Unset):
            latest_result_run_id = UNSET
        else:
            latest_result_run_id = self.latest_result_run_id

        main_git_repository_uri: None | str | Unset
        if isinstance(self.main_git_repository_uri, Unset):
            main_git_repository_uri = UNSET
        else:
            main_git_repository_uri = self.main_git_repository_uri

        service_provider: str | Unset = UNSET
        if not isinstance(self.service_provider, Unset):
            service_provider = self.service_provider.value

        is_pinned: bool | None | Unset
        if isinstance(self.is_pinned, Unset):
            is_pinned = UNSET
        else:
            is_pinned = self.is_pinned

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "ownerId": owner_id,
                "ownerName": owner_name,
                "description": description,
                "visibility": visibility,
                "tags": tags,
                "runCounts": run_counts,
                "relationship": relationship,
                "projectType": project_type,
                "stageId": stage_id,
                "status": status,
                "details": details,
            }
        )
        if latest_result_timestamp is not UNSET:
            field_dict["latestResultTimestamp"] = latest_result_timestamp
        if latest_result_run_id is not UNSET:
            field_dict["latestResultRunId"] = latest_result_run_id
        if main_git_repository_uri is not UNSET:
            field_dict["mainGitRepositoryUri"] = main_git_repository_uri
        if service_provider is not UNSET:
            field_dict["serviceProvider"] = service_provider
        if is_pinned is not UNSET:
            field_dict["isPinned"] = is_pinned

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_server_projects_api_project_gateway_run_count_for_type import (
            DominoServerProjectsApiProjectGatewayRunCountForType,
        )
        from ..models.domino_server_projects_api_project_gateway_summary_details import (
            DominoServerProjectsApiProjectGatewaySummaryDetails,
        )
        from ..models.domino_server_projects_api_project_gateway_tag import DominoServerProjectsApiProjectGatewayTag
        from ..models.domino_server_projects_api_project_status import DominoServerProjectsApiProjectStatus

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        owner_id = d.pop("ownerId")

        owner_name = d.pop("ownerName")

        description = d.pop("description")

        visibility = DominoServerProjectsApiProjectGatewaySummaryVisibility(d.pop("visibility"))

        tags = []
        _tags = d.pop("tags")
        for tags_item_data in _tags:
            tags_item = DominoServerProjectsApiProjectGatewayTag.from_dict(tags_item_data)

            tags.append(tags_item)

        run_counts = []
        _run_counts = d.pop("runCounts")
        for run_counts_item_data in _run_counts:
            run_counts_item = DominoServerProjectsApiProjectGatewayRunCountForType.from_dict(run_counts_item_data)

            run_counts.append(run_counts_item)

        relationship = DominoServerProjectsApiProjectGatewaySummaryRelationship(d.pop("relationship"))

        project_type = DominoServerProjectsApiProjectGatewaySummaryProjectType(d.pop("projectType"))

        stage_id = d.pop("stageId")

        status = DominoServerProjectsApiProjectStatus.from_dict(d.pop("status"))

        details = DominoServerProjectsApiProjectGatewaySummaryDetails.from_dict(d.pop("details"))

        def _parse_latest_result_timestamp(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                latest_result_timestamp_type_0 = isoparse(data)

                return latest_result_timestamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        latest_result_timestamp = _parse_latest_result_timestamp(d.pop("latestResultTimestamp", UNSET))

        def _parse_latest_result_run_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latest_result_run_id = _parse_latest_result_run_id(d.pop("latestResultRunId", UNSET))

        def _parse_main_git_repository_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        main_git_repository_uri = _parse_main_git_repository_uri(d.pop("mainGitRepositoryUri", UNSET))

        _service_provider = d.pop("serviceProvider", UNSET)
        service_provider: DominoServerProjectsApiProjectGatewaySummaryServiceProvider | Unset
        if isinstance(_service_provider, Unset):
            service_provider = UNSET
        else:
            service_provider = DominoServerProjectsApiProjectGatewaySummaryServiceProvider(_service_provider)

        def _parse_is_pinned(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_pinned = _parse_is_pinned(d.pop("isPinned", UNSET))

        domino_server_projects_api_project_gateway_summary = cls(
            id=id,
            name=name,
            owner_id=owner_id,
            owner_name=owner_name,
            description=description,
            visibility=visibility,
            tags=tags,
            run_counts=run_counts,
            relationship=relationship,
            project_type=project_type,
            stage_id=stage_id,
            status=status,
            details=details,
            latest_result_timestamp=latest_result_timestamp,
            latest_result_run_id=latest_result_run_id,
            main_git_repository_uri=main_git_repository_uri,
            service_provider=service_provider,
            is_pinned=is_pinned,
        )

        domino_server_projects_api_project_gateway_summary.additional_properties = d
        return domino_server_projects_api_project_gateway_summary

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
