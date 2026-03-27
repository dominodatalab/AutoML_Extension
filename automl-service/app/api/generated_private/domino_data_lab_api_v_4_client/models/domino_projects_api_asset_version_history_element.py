from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_api_asset_version_info import DominoProjectsApiAssetVersionInfo
    from ..models.domino_projects_api_project_stakeholder import DominoProjectsApiProjectStakeholder


T = TypeVar("T", bound="DominoProjectsApiAssetVersionHistoryElement")


@_attrs_define
class DominoProjectsApiAssetVersionHistoryElement:
    """
    Attributes:
        timestamp (int):
        stakeholder (DominoProjectsApiProjectStakeholder):
        project_id (str):
        project_name (str):
        duration (int | None | Unset):
        asset_version (DominoProjectsApiAssetVersionInfo | Unset):
    """

    timestamp: int
    stakeholder: DominoProjectsApiProjectStakeholder
    project_id: str
    project_name: str
    duration: int | None | Unset = UNSET
    asset_version: DominoProjectsApiAssetVersionInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        stakeholder = self.stakeholder.to_dict()

        project_id = self.project_id

        project_name = self.project_name

        duration: int | None | Unset
        if isinstance(self.duration, Unset):
            duration = UNSET
        else:
            duration = self.duration

        asset_version: dict[str, Any] | Unset = UNSET
        if not isinstance(self.asset_version, Unset):
            asset_version = self.asset_version.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "stakeholder": stakeholder,
                "projectId": project_id,
                "projectName": project_name,
            }
        )
        if duration is not UNSET:
            field_dict["duration"] = duration
        if asset_version is not UNSET:
            field_dict["assetVersion"] = asset_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_asset_version_info import DominoProjectsApiAssetVersionInfo
        from ..models.domino_projects_api_project_stakeholder import DominoProjectsApiProjectStakeholder

        d = dict(src_dict)
        timestamp = d.pop("timestamp")

        stakeholder = DominoProjectsApiProjectStakeholder.from_dict(d.pop("stakeholder"))

        project_id = d.pop("projectId")

        project_name = d.pop("projectName")

        def _parse_duration(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration = _parse_duration(d.pop("duration", UNSET))

        _asset_version = d.pop("assetVersion", UNSET)
        asset_version: DominoProjectsApiAssetVersionInfo | Unset
        if isinstance(_asset_version, Unset):
            asset_version = UNSET
        else:
            asset_version = DominoProjectsApiAssetVersionInfo.from_dict(_asset_version)

        domino_projects_api_asset_version_history_element = cls(
            timestamp=timestamp,
            stakeholder=stakeholder,
            project_id=project_id,
            project_name=project_name,
            duration=duration,
            asset_version=asset_version,
        )

        domino_projects_api_asset_version_history_element.additional_properties = d
        return domino_projects_api_asset_version_history_element

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
