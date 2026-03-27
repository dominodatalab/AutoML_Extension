from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoNucleusDatasetUiCreateSnapshotWithWorkspaceInput")


@_attrs_define
class DominoNucleusDatasetUiCreateSnapshotWithWorkspaceInput:
    """
    Attributes:
        dataset_id (str):
        output_path (str):
        workspace_definition_id (str):
        title (None | str | Unset):
        commit_id (None | str | Unset):
        hardware_tier_id (None | str | Unset):
    """

    dataset_id: str
    output_path: str
    workspace_definition_id: str
    title: None | str | Unset = UNSET
    commit_id: None | str | Unset = UNSET
    hardware_tier_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataset_id = self.dataset_id

        output_path = self.output_path

        workspace_definition_id = self.workspace_definition_id

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        commit_id: None | str | Unset
        if isinstance(self.commit_id, Unset):
            commit_id = UNSET
        else:
            commit_id = self.commit_id

        hardware_tier_id: None | str | Unset
        if isinstance(self.hardware_tier_id, Unset):
            hardware_tier_id = UNSET
        else:
            hardware_tier_id = self.hardware_tier_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "datasetId": dataset_id,
                "outputPath": output_path,
                "workspaceDefinitionId": workspace_definition_id,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if commit_id is not UNSET:
            field_dict["commitId"] = commit_id
        if hardware_tier_id is not UNSET:
            field_dict["hardwareTierId"] = hardware_tier_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dataset_id = d.pop("datasetId")

        output_path = d.pop("outputPath")

        workspace_definition_id = d.pop("workspaceDefinitionId")

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_commit_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commit_id = _parse_commit_id(d.pop("commitId", UNSET))

        def _parse_hardware_tier_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hardware_tier_id = _parse_hardware_tier_id(d.pop("hardwareTierId", UNSET))

        domino_nucleus_dataset_ui_create_snapshot_with_workspace_input = cls(
            dataset_id=dataset_id,
            output_path=output_path,
            workspace_definition_id=workspace_definition_id,
            title=title,
            commit_id=commit_id,
            hardware_tier_id=hardware_tier_id,
        )

        domino_nucleus_dataset_ui_create_snapshot_with_workspace_input.additional_properties = d
        return domino_nucleus_dataset_ui_create_snapshot_with_workspace_input

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
