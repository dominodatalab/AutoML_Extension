from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.run_type import RunType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RunUtilization")


@_attrs_define
class RunUtilization:
    """Statistics on a specific run

    Attributes:
        id (str | Unset): Id of a run
        project_id (str | Unset): Id of a oproject the run belongs to
        project_identity (str | Unset): human-readable project identifier
        starting_user_id (str | Unset): Id of a user who started the run
        starting_user_full_name (str | Unset): Full name of a user who started the run
        run_type (RunType | Unset): What is the type of the run
        hardware_tier_id (str | Unset): Hardware tier which was used for these runs
        start_date_time (str | Unset): Date when the run was started in the ISO-8601 format
        queue_duration_in_seconds (float | Unset): How long the run spent in the queue before running (in seconds)
        run_duration_in_seconds (float | Unset): How long the run was running (in seconds)
        estimated_cost (float | Unset): The estimated cost of the run
    """

    id: str | Unset = UNSET
    project_id: str | Unset = UNSET
    project_identity: str | Unset = UNSET
    starting_user_id: str | Unset = UNSET
    starting_user_full_name: str | Unset = UNSET
    run_type: RunType | Unset = UNSET
    hardware_tier_id: str | Unset = UNSET
    start_date_time: str | Unset = UNSET
    queue_duration_in_seconds: float | Unset = UNSET
    run_duration_in_seconds: float | Unset = UNSET
    estimated_cost: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        project_id = self.project_id

        project_identity = self.project_identity

        starting_user_id = self.starting_user_id

        starting_user_full_name = self.starting_user_full_name

        run_type: str | Unset = UNSET
        if not isinstance(self.run_type, Unset):
            run_type = self.run_type.value

        hardware_tier_id = self.hardware_tier_id

        start_date_time = self.start_date_time

        queue_duration_in_seconds = self.queue_duration_in_seconds

        run_duration_in_seconds = self.run_duration_in_seconds

        estimated_cost = self.estimated_cost

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if project_identity is not UNSET:
            field_dict["projectIdentity"] = project_identity
        if starting_user_id is not UNSET:
            field_dict["startingUserId"] = starting_user_id
        if starting_user_full_name is not UNSET:
            field_dict["startingUserFullName"] = starting_user_full_name
        if run_type is not UNSET:
            field_dict["runType"] = run_type
        if hardware_tier_id is not UNSET:
            field_dict["hardwareTierId"] = hardware_tier_id
        if start_date_time is not UNSET:
            field_dict["startDateTime"] = start_date_time
        if queue_duration_in_seconds is not UNSET:
            field_dict["queueDurationInSeconds"] = queue_duration_in_seconds
        if run_duration_in_seconds is not UNSET:
            field_dict["runDurationInSeconds"] = run_duration_in_seconds
        if estimated_cost is not UNSET:
            field_dict["estimatedCost"] = estimated_cost

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        project_id = d.pop("projectId", UNSET)

        project_identity = d.pop("projectIdentity", UNSET)

        starting_user_id = d.pop("startingUserId", UNSET)

        starting_user_full_name = d.pop("startingUserFullName", UNSET)

        _run_type = d.pop("runType", UNSET)
        run_type: RunType | Unset
        if isinstance(_run_type, Unset):
            run_type = UNSET
        else:
            run_type = RunType(_run_type)

        hardware_tier_id = d.pop("hardwareTierId", UNSET)

        start_date_time = d.pop("startDateTime", UNSET)

        queue_duration_in_seconds = d.pop("queueDurationInSeconds", UNSET)

        run_duration_in_seconds = d.pop("runDurationInSeconds", UNSET)

        estimated_cost = d.pop("estimatedCost", UNSET)

        run_utilization = cls(
            id=id,
            project_id=project_id,
            project_identity=project_identity,
            starting_user_id=starting_user_id,
            starting_user_full_name=starting_user_full_name,
            run_type=run_type,
            hardware_tier_id=hardware_tier_id,
            start_date_time=start_date_time,
            queue_duration_in_seconds=queue_duration_in_seconds,
            run_duration_in_seconds=run_duration_in_seconds,
            estimated_cost=estimated_cost,
        )

        run_utilization.additional_properties = d
        return run_utilization

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
