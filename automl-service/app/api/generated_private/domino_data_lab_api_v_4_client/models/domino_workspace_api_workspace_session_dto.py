from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_workspace_api_data_mount_specification_dto import DominoWorkspaceApiDataMountSpecificationDto
    from ..models.domino_workspace_api_net_app_volume_mount_specification_dto import (
        DominoWorkspaceApiNetAppVolumeMountSpecificationDto,
    )
    from ..models.domino_workspace_api_queued_workspace_history_details import (
        DominoWorkspaceApiQueuedWorkspaceHistoryDetails,
    )
    from ..models.domino_workspace_api_workspace_config_dto import DominoWorkspaceApiWorkspaceConfigDto
    from ..models.domino_workspace_api_workspace_dataset_mount_dto import DominoWorkspaceApiWorkspaceDatasetMountDto
    from ..models.domino_workspace_api_workspace_disk_usage_dto import DominoWorkspaceApiWorkspaceDiskUsageDto
    from ..models.domino_workspace_api_workspace_session_end_dto import DominoWorkspaceApiWorkspaceSessionEndDto
    from ..models.domino_workspace_api_workspace_session_start_dto import DominoWorkspaceApiWorkspaceSessionStartDto
    from ..models.domino_workspace_api_workspace_session_status_info import DominoWorkspaceApiWorkspaceSessionStatusInfo


T = TypeVar("T", bound="DominoWorkspaceApiWorkspaceSessionDto")


@_attrs_define
class DominoWorkspaceApiWorkspaceSessionDto:
    """
    Attributes:
        id (str):
        execution_id (str):
        config (DominoWorkspaceApiWorkspaceConfigDto):
        dataset_mounts (list[DominoWorkspaceApiWorkspaceDatasetMountDto]):
        external_volume_mounts (list[DominoWorkspaceApiDataMountSpecificationDto]):
        net_app_volume_mounts (list[DominoWorkspaceApiNetAppVolumeMountSpecificationDto]):
        queued_workspace_history_details (DominoWorkspaceApiQueuedWorkspaceHistoryDetails):
        start (DominoWorkspaceApiWorkspaceSessionStartDto | Unset):
        end (DominoWorkspaceApiWorkspaceSessionEndDto | Unset):
        session_status_info (DominoWorkspaceApiWorkspaceSessionStatusInfo | Unset):
        disk_usage (DominoWorkspaceApiWorkspaceDiskUsageDto | Unset):
    """

    id: str
    execution_id: str
    config: DominoWorkspaceApiWorkspaceConfigDto
    dataset_mounts: list[DominoWorkspaceApiWorkspaceDatasetMountDto]
    external_volume_mounts: list[DominoWorkspaceApiDataMountSpecificationDto]
    net_app_volume_mounts: list[DominoWorkspaceApiNetAppVolumeMountSpecificationDto]
    queued_workspace_history_details: DominoWorkspaceApiQueuedWorkspaceHistoryDetails
    start: DominoWorkspaceApiWorkspaceSessionStartDto | Unset = UNSET
    end: DominoWorkspaceApiWorkspaceSessionEndDto | Unset = UNSET
    session_status_info: DominoWorkspaceApiWorkspaceSessionStatusInfo | Unset = UNSET
    disk_usage: DominoWorkspaceApiWorkspaceDiskUsageDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        execution_id = self.execution_id

        config = self.config.to_dict()

        dataset_mounts = []
        for dataset_mounts_item_data in self.dataset_mounts:
            dataset_mounts_item = dataset_mounts_item_data.to_dict()
            dataset_mounts.append(dataset_mounts_item)

        external_volume_mounts = []
        for external_volume_mounts_item_data in self.external_volume_mounts:
            external_volume_mounts_item = external_volume_mounts_item_data.to_dict()
            external_volume_mounts.append(external_volume_mounts_item)

        net_app_volume_mounts = []
        for net_app_volume_mounts_item_data in self.net_app_volume_mounts:
            net_app_volume_mounts_item = net_app_volume_mounts_item_data.to_dict()
            net_app_volume_mounts.append(net_app_volume_mounts_item)

        queued_workspace_history_details = self.queued_workspace_history_details.to_dict()

        start: dict[str, Any] | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.to_dict()

        end: dict[str, Any] | Unset = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.to_dict()

        session_status_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.session_status_info, Unset):
            session_status_info = self.session_status_info.to_dict()

        disk_usage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.disk_usage, Unset):
            disk_usage = self.disk_usage.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "executionId": execution_id,
                "config": config,
                "datasetMounts": dataset_mounts,
                "externalVolumeMounts": external_volume_mounts,
                "netAppVolumeMounts": net_app_volume_mounts,
                "queuedWorkspaceHistoryDetails": queued_workspace_history_details,
            }
        )
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if session_status_info is not UNSET:
            field_dict["sessionStatusInfo"] = session_status_info
        if disk_usage is not UNSET:
            field_dict["diskUsage"] = disk_usage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_workspace_api_data_mount_specification_dto import (
            DominoWorkspaceApiDataMountSpecificationDto,
        )
        from ..models.domino_workspace_api_net_app_volume_mount_specification_dto import (
            DominoWorkspaceApiNetAppVolumeMountSpecificationDto,
        )
        from ..models.domino_workspace_api_queued_workspace_history_details import (
            DominoWorkspaceApiQueuedWorkspaceHistoryDetails,
        )
        from ..models.domino_workspace_api_workspace_config_dto import DominoWorkspaceApiWorkspaceConfigDto
        from ..models.domino_workspace_api_workspace_dataset_mount_dto import DominoWorkspaceApiWorkspaceDatasetMountDto
        from ..models.domino_workspace_api_workspace_disk_usage_dto import DominoWorkspaceApiWorkspaceDiskUsageDto
        from ..models.domino_workspace_api_workspace_session_end_dto import DominoWorkspaceApiWorkspaceSessionEndDto
        from ..models.domino_workspace_api_workspace_session_start_dto import DominoWorkspaceApiWorkspaceSessionStartDto
        from ..models.domino_workspace_api_workspace_session_status_info import (
            DominoWorkspaceApiWorkspaceSessionStatusInfo,
        )

        d = dict(src_dict)
        id = d.pop("id")

        execution_id = d.pop("executionId")

        config = DominoWorkspaceApiWorkspaceConfigDto.from_dict(d.pop("config"))

        dataset_mounts = []
        _dataset_mounts = d.pop("datasetMounts")
        for dataset_mounts_item_data in _dataset_mounts:
            dataset_mounts_item = DominoWorkspaceApiWorkspaceDatasetMountDto.from_dict(dataset_mounts_item_data)

            dataset_mounts.append(dataset_mounts_item)

        external_volume_mounts = []
        _external_volume_mounts = d.pop("externalVolumeMounts")
        for external_volume_mounts_item_data in _external_volume_mounts:
            external_volume_mounts_item = DominoWorkspaceApiDataMountSpecificationDto.from_dict(
                external_volume_mounts_item_data
            )

            external_volume_mounts.append(external_volume_mounts_item)

        net_app_volume_mounts = []
        _net_app_volume_mounts = d.pop("netAppVolumeMounts")
        for net_app_volume_mounts_item_data in _net_app_volume_mounts:
            net_app_volume_mounts_item = DominoWorkspaceApiNetAppVolumeMountSpecificationDto.from_dict(
                net_app_volume_mounts_item_data
            )

            net_app_volume_mounts.append(net_app_volume_mounts_item)

        queued_workspace_history_details = DominoWorkspaceApiQueuedWorkspaceHistoryDetails.from_dict(
            d.pop("queuedWorkspaceHistoryDetails")
        )

        _start = d.pop("start", UNSET)
        start: DominoWorkspaceApiWorkspaceSessionStartDto | Unset
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = DominoWorkspaceApiWorkspaceSessionStartDto.from_dict(_start)

        _end = d.pop("end", UNSET)
        end: DominoWorkspaceApiWorkspaceSessionEndDto | Unset
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = DominoWorkspaceApiWorkspaceSessionEndDto.from_dict(_end)

        _session_status_info = d.pop("sessionStatusInfo", UNSET)
        session_status_info: DominoWorkspaceApiWorkspaceSessionStatusInfo | Unset
        if isinstance(_session_status_info, Unset):
            session_status_info = UNSET
        else:
            session_status_info = DominoWorkspaceApiWorkspaceSessionStatusInfo.from_dict(_session_status_info)

        _disk_usage = d.pop("diskUsage", UNSET)
        disk_usage: DominoWorkspaceApiWorkspaceDiskUsageDto | Unset
        if isinstance(_disk_usage, Unset):
            disk_usage = UNSET
        else:
            disk_usage = DominoWorkspaceApiWorkspaceDiskUsageDto.from_dict(_disk_usage)

        domino_workspace_api_workspace_session_dto = cls(
            id=id,
            execution_id=execution_id,
            config=config,
            dataset_mounts=dataset_mounts,
            external_volume_mounts=external_volume_mounts,
            net_app_volume_mounts=net_app_volume_mounts,
            queued_workspace_history_details=queued_workspace_history_details,
            start=start,
            end=end,
            session_status_info=session_status_info,
            disk_usage=disk_usage,
        )

        domino_workspace_api_workspace_session_dto.additional_properties = d
        return domino_workspace_api_workspace_session_dto

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
