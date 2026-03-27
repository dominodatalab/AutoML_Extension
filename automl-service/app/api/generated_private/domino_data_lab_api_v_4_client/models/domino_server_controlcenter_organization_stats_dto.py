from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_server_controlcenter_money_dto import DominoServerControlcenterMoneyDTO


T = TypeVar("T", bound="DominoServerControlcenterOrganizationStatsDTO")


@_attrs_define
class DominoServerControlcenterOrganizationStatsDTO:
    """
    Attributes:
        id (str):
        full_name (str):
        total_compute_time_in_millis (int):
        total_compute_spend (DominoServerControlcenterMoneyDTO):
        number_of_runs (int):
        number_of_projects_with_runs (int):
    """

    id: str
    full_name: str
    total_compute_time_in_millis: int
    total_compute_spend: DominoServerControlcenterMoneyDTO
    number_of_runs: int
    number_of_projects_with_runs: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        full_name = self.full_name

        total_compute_time_in_millis = self.total_compute_time_in_millis

        total_compute_spend = self.total_compute_spend.to_dict()

        number_of_runs = self.number_of_runs

        number_of_projects_with_runs = self.number_of_projects_with_runs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "fullName": full_name,
                "totalComputeTimeInMillis": total_compute_time_in_millis,
                "totalComputeSpend": total_compute_spend,
                "numberOfRuns": number_of_runs,
                "numberOfProjectsWithRuns": number_of_projects_with_runs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_server_controlcenter_money_dto import DominoServerControlcenterMoneyDTO

        d = dict(src_dict)
        id = d.pop("id")

        full_name = d.pop("fullName")

        total_compute_time_in_millis = d.pop("totalComputeTimeInMillis")

        total_compute_spend = DominoServerControlcenterMoneyDTO.from_dict(d.pop("totalComputeSpend"))

        number_of_runs = d.pop("numberOfRuns")

        number_of_projects_with_runs = d.pop("numberOfProjectsWithRuns")

        domino_server_controlcenter_organization_stats_dto = cls(
            id=id,
            full_name=full_name,
            total_compute_time_in_millis=total_compute_time_in_millis,
            total_compute_spend=total_compute_spend,
            number_of_runs=number_of_runs,
            number_of_projects_with_runs=number_of_projects_with_runs,
        )

        domino_server_controlcenter_organization_stats_dto.additional_properties = d
        return domino_server_controlcenter_organization_stats_dto

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
