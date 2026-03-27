from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_admin_usermanagement_api_aggregate_user_activity_report_role_based_counts import (
        DominoAdminUsermanagementApiAggregateUserActivityReportRoleBasedCounts,
    )


T = TypeVar("T", bound="DominoAdminUsermanagementApiAggregateUserActivityReport")


@_attrs_define
class DominoAdminUsermanagementApiAggregateUserActivityReport:
    """
    Attributes:
        enabled_users (int):
        practitioners (int):
        results_consumers (int):
        license_quota (int):
        recent_usage_days (int):
        hide_license_type (bool):
        role_based_counts (DominoAdminUsermanagementApiAggregateUserActivityReportRoleBasedCounts):
        report_end_date (None | str | Unset):
    """

    enabled_users: int
    practitioners: int
    results_consumers: int
    license_quota: int
    recent_usage_days: int
    hide_license_type: bool
    role_based_counts: DominoAdminUsermanagementApiAggregateUserActivityReportRoleBasedCounts
    report_end_date: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled_users = self.enabled_users

        practitioners = self.practitioners

        results_consumers = self.results_consumers

        license_quota = self.license_quota

        recent_usage_days = self.recent_usage_days

        hide_license_type = self.hide_license_type

        role_based_counts = self.role_based_counts.to_dict()

        report_end_date: None | str | Unset
        if isinstance(self.report_end_date, Unset):
            report_end_date = UNSET
        else:
            report_end_date = self.report_end_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabledUsers": enabled_users,
                "practitioners": practitioners,
                "resultsConsumers": results_consumers,
                "licenseQuota": license_quota,
                "recentUsageDays": recent_usage_days,
                "hideLicenseType": hide_license_type,
                "roleBasedCounts": role_based_counts,
            }
        )
        if report_end_date is not UNSET:
            field_dict["reportEndDate"] = report_end_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_admin_usermanagement_api_aggregate_user_activity_report_role_based_counts import (
            DominoAdminUsermanagementApiAggregateUserActivityReportRoleBasedCounts,
        )

        d = dict(src_dict)
        enabled_users = d.pop("enabledUsers")

        practitioners = d.pop("practitioners")

        results_consumers = d.pop("resultsConsumers")

        license_quota = d.pop("licenseQuota")

        recent_usage_days = d.pop("recentUsageDays")

        hide_license_type = d.pop("hideLicenseType")

        role_based_counts = DominoAdminUsermanagementApiAggregateUserActivityReportRoleBasedCounts.from_dict(
            d.pop("roleBasedCounts")
        )

        def _parse_report_end_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        report_end_date = _parse_report_end_date(d.pop("reportEndDate", UNSET))

        domino_admin_usermanagement_api_aggregate_user_activity_report = cls(
            enabled_users=enabled_users,
            practitioners=practitioners,
            results_consumers=results_consumers,
            license_quota=license_quota,
            recent_usage_days=recent_usage_days,
            hide_license_type=hide_license_type,
            role_based_counts=role_based_counts,
            report_end_date=report_end_date,
        )

        domino_admin_usermanagement_api_aggregate_user_activity_report.additional_properties = d
        return domino_admin_usermanagement_api_aggregate_user_activity_report

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
