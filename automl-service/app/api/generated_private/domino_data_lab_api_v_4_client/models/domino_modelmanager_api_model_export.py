from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_modelmanager_api_model_export_target import DominoModelmanagerApiModelExportTarget
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoModelmanagerApiModelExport")


@_attrs_define
class DominoModelmanagerApiModelExport:
    """
    Attributes:
        id (str):
        model_id (str):
        registry_url_host_name (str):
        target (DominoModelmanagerApiModelExportTarget):
        project_id (str):
        model_name (str):
        model_description (str):
        is_archived (bool):
        created (int):
        latest_successful_version_id (None | str | Unset):
    """

    id: str
    model_id: str
    registry_url_host_name: str
    target: DominoModelmanagerApiModelExportTarget
    project_id: str
    model_name: str
    model_description: str
    is_archived: bool
    created: int
    latest_successful_version_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        model_id = self.model_id

        registry_url_host_name = self.registry_url_host_name

        target = self.target.value

        project_id = self.project_id

        model_name = self.model_name

        model_description = self.model_description

        is_archived = self.is_archived

        created = self.created

        latest_successful_version_id: None | str | Unset
        if isinstance(self.latest_successful_version_id, Unset):
            latest_successful_version_id = UNSET
        else:
            latest_successful_version_id = self.latest_successful_version_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "modelId": model_id,
                "registryUrlHostName": registry_url_host_name,
                "target": target,
                "projectId": project_id,
                "modelName": model_name,
                "modelDescription": model_description,
                "isArchived": is_archived,
                "created": created,
            }
        )
        if latest_successful_version_id is not UNSET:
            field_dict["latestSuccessfulVersionId"] = latest_successful_version_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        model_id = d.pop("modelId")

        registry_url_host_name = d.pop("registryUrlHostName")

        target = DominoModelmanagerApiModelExportTarget(d.pop("target"))

        project_id = d.pop("projectId")

        model_name = d.pop("modelName")

        model_description = d.pop("modelDescription")

        is_archived = d.pop("isArchived")

        created = d.pop("created")

        def _parse_latest_successful_version_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latest_successful_version_id = _parse_latest_successful_version_id(d.pop("latestSuccessfulVersionId", UNSET))

        domino_modelmanager_api_model_export = cls(
            id=id,
            model_id=model_id,
            registry_url_host_name=registry_url_host_name,
            target=target,
            project_id=project_id,
            model_name=model_name,
            model_description=model_description,
            is_archived=is_archived,
            created=created,
            latest_successful_version_id=latest_successful_version_id,
        )

        domino_modelmanager_api_model_export.additional_properties = d
        return domino_modelmanager_api_model_export

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
