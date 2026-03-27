from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoAdminUsermanagementApiBriefUserUsageReport")


@_attrs_define
class DominoAdminUsermanagementApiBriefUserUsageReport:
    """
    Attributes:
        user_id (str):
        practitioner_workloads_total (int):
        runs_total (int):
        runs_recent (int):
        projects_total (int):
        projects_recent (int):
        license_type (str):
        most_recent_activity (None | str | Unset):
    """

    user_id: str
    practitioner_workloads_total: int
    runs_total: int
    runs_recent: int
    projects_total: int
    projects_recent: int
    license_type: str
    most_recent_activity: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        practitioner_workloads_total = self.practitioner_workloads_total

        runs_total = self.runs_total

        runs_recent = self.runs_recent

        projects_total = self.projects_total

        projects_recent = self.projects_recent

        license_type = self.license_type

        most_recent_activity: None | str | Unset
        if isinstance(self.most_recent_activity, Unset):
            most_recent_activity = UNSET
        else:
            most_recent_activity = self.most_recent_activity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "practitionerWorkloadsTotal": practitioner_workloads_total,
                "runsTotal": runs_total,
                "runsRecent": runs_recent,
                "projectsTotal": projects_total,
                "projectsRecent": projects_recent,
                "licenseType": license_type,
            }
        )
        if most_recent_activity is not UNSET:
            field_dict["mostRecentActivity"] = most_recent_activity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("userId")

        practitioner_workloads_total = d.pop("practitionerWorkloadsTotal")

        runs_total = d.pop("runsTotal")

        runs_recent = d.pop("runsRecent")

        projects_total = d.pop("projectsTotal")

        projects_recent = d.pop("projectsRecent")

        license_type = d.pop("licenseType")

        def _parse_most_recent_activity(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        most_recent_activity = _parse_most_recent_activity(d.pop("mostRecentActivity", UNSET))

        domino_admin_usermanagement_api_brief_user_usage_report = cls(
            user_id=user_id,
            practitioner_workloads_total=practitioner_workloads_total,
            runs_total=runs_total,
            runs_recent=runs_recent,
            projects_total=projects_total,
            projects_recent=projects_recent,
            license_type=license_type,
            most_recent_activity=most_recent_activity,
        )

        domino_admin_usermanagement_api_brief_user_usage_report.additional_properties = d
        return domino_admin_usermanagement_api_brief_user_usage_report

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
