from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_projects_api_asset_portfolio_element_asset_type import (
    DominoProjectsApiAssetPortfolioElementAssetType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_api_asset_usage_values import DominoProjectsApiAssetUsageValues
    from ..models.domino_projects_api_asset_version_history_element import DominoProjectsApiAssetVersionHistoryElement
    from ..models.domino_projects_api_asset_view_stats import DominoProjectsApiAssetViewStats
    from ..models.domino_projects_api_project_stakeholder import DominoProjectsApiProjectStakeholder


T = TypeVar("T", bound="DominoProjectsApiAssetPortfolioElement")


@_attrs_define
class DominoProjectsApiAssetPortfolioElement:
    """
    Attributes:
        asset_id (str):
        asset_name (str):
        asset_type (DominoProjectsApiAssetPortfolioElementAssetType):
        project_id (str):
        project_name (str):
        project_owner (DominoProjectsApiProjectStakeholder):
        last_updated_at (int | None | Unset):
        owner (DominoProjectsApiProjectStakeholder | Unset):
        version_history (list[DominoProjectsApiAssetVersionHistoryElement] | None | Unset):
        status (None | str | Unset):
        usage (list[DominoProjectsApiAssetUsageValues] | None | Unset):
        metadata (DominoProjectsApiAssetViewStats | Unset):
    """

    asset_id: str
    asset_name: str
    asset_type: DominoProjectsApiAssetPortfolioElementAssetType
    project_id: str
    project_name: str
    project_owner: DominoProjectsApiProjectStakeholder
    last_updated_at: int | None | Unset = UNSET
    owner: DominoProjectsApiProjectStakeholder | Unset = UNSET
    version_history: list[DominoProjectsApiAssetVersionHistoryElement] | None | Unset = UNSET
    status: None | str | Unset = UNSET
    usage: list[DominoProjectsApiAssetUsageValues] | None | Unset = UNSET
    metadata: DominoProjectsApiAssetViewStats | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        asset_name = self.asset_name

        asset_type = self.asset_type.value

        project_id = self.project_id

        project_name = self.project_name

        project_owner = self.project_owner.to_dict()

        last_updated_at: int | None | Unset
        if isinstance(self.last_updated_at, Unset):
            last_updated_at = UNSET
        else:
            last_updated_at = self.last_updated_at

        owner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        version_history: list[dict[str, Any]] | None | Unset
        if isinstance(self.version_history, Unset):
            version_history = UNSET
        elif isinstance(self.version_history, list):
            version_history = []
            for version_history_type_0_item_data in self.version_history:
                version_history_type_0_item = version_history_type_0_item_data.to_dict()
                version_history.append(version_history_type_0_item)

        else:
            version_history = self.version_history

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        usage: list[dict[str, Any]] | None | Unset
        if isinstance(self.usage, Unset):
            usage = UNSET
        elif isinstance(self.usage, list):
            usage = []
            for usage_type_0_item_data in self.usage:
                usage_type_0_item = usage_type_0_item_data.to_dict()
                usage.append(usage_type_0_item)

        else:
            usage = self.usage

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assetId": asset_id,
                "assetName": asset_name,
                "assetType": asset_type,
                "projectId": project_id,
                "projectName": project_name,
                "projectOwner": project_owner,
            }
        )
        if last_updated_at is not UNSET:
            field_dict["lastUpdatedAt"] = last_updated_at
        if owner is not UNSET:
            field_dict["owner"] = owner
        if version_history is not UNSET:
            field_dict["versionHistory"] = version_history
        if status is not UNSET:
            field_dict["status"] = status
        if usage is not UNSET:
            field_dict["usage"] = usage
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_asset_usage_values import DominoProjectsApiAssetUsageValues
        from ..models.domino_projects_api_asset_version_history_element import (
            DominoProjectsApiAssetVersionHistoryElement,
        )
        from ..models.domino_projects_api_asset_view_stats import DominoProjectsApiAssetViewStats
        from ..models.domino_projects_api_project_stakeholder import DominoProjectsApiProjectStakeholder

        d = dict(src_dict)
        asset_id = d.pop("assetId")

        asset_name = d.pop("assetName")

        asset_type = DominoProjectsApiAssetPortfolioElementAssetType(d.pop("assetType"))

        project_id = d.pop("projectId")

        project_name = d.pop("projectName")

        project_owner = DominoProjectsApiProjectStakeholder.from_dict(d.pop("projectOwner"))

        def _parse_last_updated_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_updated_at = _parse_last_updated_at(d.pop("lastUpdatedAt", UNSET))

        _owner = d.pop("owner", UNSET)
        owner: DominoProjectsApiProjectStakeholder | Unset
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = DominoProjectsApiProjectStakeholder.from_dict(_owner)

        def _parse_version_history(data: object) -> list[DominoProjectsApiAssetVersionHistoryElement] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                version_history_type_0 = []
                _version_history_type_0 = data
                for version_history_type_0_item_data in _version_history_type_0:
                    version_history_type_0_item = DominoProjectsApiAssetVersionHistoryElement.from_dict(
                        version_history_type_0_item_data
                    )

                    version_history_type_0.append(version_history_type_0_item)

                return version_history_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DominoProjectsApiAssetVersionHistoryElement] | None | Unset, data)

        version_history = _parse_version_history(d.pop("versionHistory", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_usage(data: object) -> list[DominoProjectsApiAssetUsageValues] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                usage_type_0 = []
                _usage_type_0 = data
                for usage_type_0_item_data in _usage_type_0:
                    usage_type_0_item = DominoProjectsApiAssetUsageValues.from_dict(usage_type_0_item_data)

                    usage_type_0.append(usage_type_0_item)

                return usage_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DominoProjectsApiAssetUsageValues] | None | Unset, data)

        usage = _parse_usage(d.pop("usage", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: DominoProjectsApiAssetViewStats | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = DominoProjectsApiAssetViewStats.from_dict(_metadata)

        domino_projects_api_asset_portfolio_element = cls(
            asset_id=asset_id,
            asset_name=asset_name,
            asset_type=asset_type,
            project_id=project_id,
            project_name=project_name,
            project_owner=project_owner,
            last_updated_at=last_updated_at,
            owner=owner,
            version_history=version_history,
            status=status,
            usage=usage,
            metadata=metadata,
        )

        domino_projects_api_asset_portfolio_element.additional_properties = d
        return domino_projects_api_asset_portfolio_element

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
