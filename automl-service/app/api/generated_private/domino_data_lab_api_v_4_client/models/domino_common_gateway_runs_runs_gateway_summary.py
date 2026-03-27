from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_common_gateway_runs_compute_cluster_details import DominoCommonGatewayRunsComputeClusterDetails


T = TypeVar("T", bound="DominoCommonGatewayRunsRunsGatewaySummary")


@_attrs_define
class DominoCommonGatewayRunsRunsGatewaySummary:
    """
    Attributes:
        batch_id (str):
        run_id (str):
        title (str):
        command (str):
        status (str):
        run_type (str):
        user_name (str):
        user_id (str):
        project_owner_name (str):
        project_owner_id (str):
        project_name (str):
        project_id (str):
        run_duration_sec (float):
        hardware_tier (str):
        hardware_tier_cost_currency (str):
        hardware_tier_cost_amount (float):
        queued_time (datetime.datetime):
        total_cost_currency (str):
        total_cost_amount (float):
        start_time (datetime.datetime | None | Unset):
        end_time (datetime.datetime | None | Unset):
        compute_cluster_details (DominoCommonGatewayRunsComputeClusterDetails | Unset):
        disk_usage_gi_b (float | None | Unset):
        disk_usage_percent (float | None | Unset):
    """

    batch_id: str
    run_id: str
    title: str
    command: str
    status: str
    run_type: str
    user_name: str
    user_id: str
    project_owner_name: str
    project_owner_id: str
    project_name: str
    project_id: str
    run_duration_sec: float
    hardware_tier: str
    hardware_tier_cost_currency: str
    hardware_tier_cost_amount: float
    queued_time: datetime.datetime
    total_cost_currency: str
    total_cost_amount: float
    start_time: datetime.datetime | None | Unset = UNSET
    end_time: datetime.datetime | None | Unset = UNSET
    compute_cluster_details: DominoCommonGatewayRunsComputeClusterDetails | Unset = UNSET
    disk_usage_gi_b: float | None | Unset = UNSET
    disk_usage_percent: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        batch_id = self.batch_id

        run_id = self.run_id

        title = self.title

        command = self.command

        status = self.status

        run_type = self.run_type

        user_name = self.user_name

        user_id = self.user_id

        project_owner_name = self.project_owner_name

        project_owner_id = self.project_owner_id

        project_name = self.project_name

        project_id = self.project_id

        run_duration_sec = self.run_duration_sec

        hardware_tier = self.hardware_tier

        hardware_tier_cost_currency = self.hardware_tier_cost_currency

        hardware_tier_cost_amount = self.hardware_tier_cost_amount

        queued_time = self.queued_time.isoformat()

        total_cost_currency = self.total_cost_currency

        total_cost_amount = self.total_cost_amount

        start_time: None | str | Unset
        if isinstance(self.start_time, Unset):
            start_time = UNSET
        elif isinstance(self.start_time, datetime.datetime):
            start_time = self.start_time.isoformat()
        else:
            start_time = self.start_time

        end_time: None | str | Unset
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        elif isinstance(self.end_time, datetime.datetime):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

        compute_cluster_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.compute_cluster_details, Unset):
            compute_cluster_details = self.compute_cluster_details.to_dict()

        disk_usage_gi_b: float | None | Unset
        if isinstance(self.disk_usage_gi_b, Unset):
            disk_usage_gi_b = UNSET
        else:
            disk_usage_gi_b = self.disk_usage_gi_b

        disk_usage_percent: float | None | Unset
        if isinstance(self.disk_usage_percent, Unset):
            disk_usage_percent = UNSET
        else:
            disk_usage_percent = self.disk_usage_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "batchId": batch_id,
                "runId": run_id,
                "title": title,
                "command": command,
                "status": status,
                "runType": run_type,
                "userName": user_name,
                "userId": user_id,
                "projectOwnerName": project_owner_name,
                "projectOwnerId": project_owner_id,
                "projectName": project_name,
                "projectId": project_id,
                "runDurationSec": run_duration_sec,
                "hardwareTier": hardware_tier,
                "hardwareTierCostCurrency": hardware_tier_cost_currency,
                "hardwareTierCostAmount": hardware_tier_cost_amount,
                "queuedTime": queued_time,
                "totalCostCurrency": total_cost_currency,
                "totalCostAmount": total_cost_amount,
            }
        )
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if compute_cluster_details is not UNSET:
            field_dict["computeClusterDetails"] = compute_cluster_details
        if disk_usage_gi_b is not UNSET:
            field_dict["diskUsageGiB"] = disk_usage_gi_b
        if disk_usage_percent is not UNSET:
            field_dict["diskUsagePercent"] = disk_usage_percent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_common_gateway_runs_compute_cluster_details import (
            DominoCommonGatewayRunsComputeClusterDetails,
        )

        d = dict(src_dict)
        batch_id = d.pop("batchId")

        run_id = d.pop("runId")

        title = d.pop("title")

        command = d.pop("command")

        status = d.pop("status")

        run_type = d.pop("runType")

        user_name = d.pop("userName")

        user_id = d.pop("userId")

        project_owner_name = d.pop("projectOwnerName")

        project_owner_id = d.pop("projectOwnerId")

        project_name = d.pop("projectName")

        project_id = d.pop("projectId")

        run_duration_sec = d.pop("runDurationSec")

        hardware_tier = d.pop("hardwareTier")

        hardware_tier_cost_currency = d.pop("hardwareTierCostCurrency")

        hardware_tier_cost_amount = d.pop("hardwareTierCostAmount")

        queued_time = isoparse(d.pop("queuedTime"))

        total_cost_currency = d.pop("totalCostCurrency")

        total_cost_amount = d.pop("totalCostAmount")

        def _parse_start_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_time_type_0 = isoparse(data)

                return start_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_time = _parse_start_time(d.pop("startTime", UNSET))

        def _parse_end_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_time_type_0 = isoparse(data)

                return end_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_time = _parse_end_time(d.pop("endTime", UNSET))

        _compute_cluster_details = d.pop("computeClusterDetails", UNSET)
        compute_cluster_details: DominoCommonGatewayRunsComputeClusterDetails | Unset
        if isinstance(_compute_cluster_details, Unset):
            compute_cluster_details = UNSET
        else:
            compute_cluster_details = DominoCommonGatewayRunsComputeClusterDetails.from_dict(_compute_cluster_details)

        def _parse_disk_usage_gi_b(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        disk_usage_gi_b = _parse_disk_usage_gi_b(d.pop("diskUsageGiB", UNSET))

        def _parse_disk_usage_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        disk_usage_percent = _parse_disk_usage_percent(d.pop("diskUsagePercent", UNSET))

        domino_common_gateway_runs_runs_gateway_summary = cls(
            batch_id=batch_id,
            run_id=run_id,
            title=title,
            command=command,
            status=status,
            run_type=run_type,
            user_name=user_name,
            user_id=user_id,
            project_owner_name=project_owner_name,
            project_owner_id=project_owner_id,
            project_name=project_name,
            project_id=project_id,
            run_duration_sec=run_duration_sec,
            hardware_tier=hardware_tier,
            hardware_tier_cost_currency=hardware_tier_cost_currency,
            hardware_tier_cost_amount=hardware_tier_cost_amount,
            queued_time=queued_time,
            total_cost_currency=total_cost_currency,
            total_cost_amount=total_cost_amount,
            start_time=start_time,
            end_time=end_time,
            compute_cluster_details=compute_cluster_details,
            disk_usage_gi_b=disk_usage_gi_b,
            disk_usage_percent=disk_usage_percent,
        )

        domino_common_gateway_runs_runs_gateway_summary.additional_properties = d
        return domino_common_gateway_runs_runs_gateway_summary

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
