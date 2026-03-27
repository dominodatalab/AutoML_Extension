from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_environments_api_environment_run_usage_summary import (
        DominoEnvironmentsApiEnvironmentRunUsageSummary,
    )


T = TypeVar("T", bound="DominoEnvironmentsApiEnvironmentProjectUsageSummary")


@_attrs_define
class DominoEnvironmentsApiEnvironmentProjectUsageSummary:
    """
    Attributes:
        name (str):
        owner_name (str):
        visibility (str):
        latest_runs (list[DominoEnvironmentsApiEnvironmentRunUsageSummary]):
        latest_results_timestamp (datetime.datetime | None | Unset):
    """

    name: str
    owner_name: str
    visibility: str
    latest_runs: list[DominoEnvironmentsApiEnvironmentRunUsageSummary]
    latest_results_timestamp: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        owner_name = self.owner_name

        visibility = self.visibility

        latest_runs = []
        for latest_runs_item_data in self.latest_runs:
            latest_runs_item = latest_runs_item_data.to_dict()
            latest_runs.append(latest_runs_item)

        latest_results_timestamp: None | str | Unset
        if isinstance(self.latest_results_timestamp, Unset):
            latest_results_timestamp = UNSET
        elif isinstance(self.latest_results_timestamp, datetime.datetime):
            latest_results_timestamp = self.latest_results_timestamp.isoformat()
        else:
            latest_results_timestamp = self.latest_results_timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "ownerName": owner_name,
                "visibility": visibility,
                "latestRuns": latest_runs,
            }
        )
        if latest_results_timestamp is not UNSET:
            field_dict["latestResultsTimestamp"] = latest_results_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_environments_api_environment_run_usage_summary import (
            DominoEnvironmentsApiEnvironmentRunUsageSummary,
        )

        d = dict(src_dict)
        name = d.pop("name")

        owner_name = d.pop("ownerName")

        visibility = d.pop("visibility")

        latest_runs = []
        _latest_runs = d.pop("latestRuns")
        for latest_runs_item_data in _latest_runs:
            latest_runs_item = DominoEnvironmentsApiEnvironmentRunUsageSummary.from_dict(latest_runs_item_data)

            latest_runs.append(latest_runs_item)

        def _parse_latest_results_timestamp(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                latest_results_timestamp_type_0 = isoparse(data)

                return latest_results_timestamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        latest_results_timestamp = _parse_latest_results_timestamp(d.pop("latestResultsTimestamp", UNSET))

        domino_environments_api_environment_project_usage_summary = cls(
            name=name,
            owner_name=owner_name,
            visibility=visibility,
            latest_runs=latest_runs,
            latest_results_timestamp=latest_results_timestamp,
        )

        domino_environments_api_environment_project_usage_summary.additional_properties = d
        return domino_environments_api_environment_project_usage_summary

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
