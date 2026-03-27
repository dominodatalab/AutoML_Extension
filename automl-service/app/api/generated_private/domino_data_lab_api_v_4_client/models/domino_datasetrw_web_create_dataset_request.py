from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_datasetrw_api_dataset_rw_grant import DominoDatasetrwApiDatasetRwGrant


T = TypeVar("T", bound="DominoDatasetrwWebCreateDatasetRequest")


@_attrs_define
class DominoDatasetrwWebCreateDatasetRequest:
    """
    Attributes:
        dataset_name (str):
        project_id (str):
        used_for_model_monitoring (bool):
        description (None | str | Unset):
        grants (list[DominoDatasetrwApiDatasetRwGrant] | None | Unset):
        dataset_storage_id (None | str | Unset):
    """

    dataset_name: str
    project_id: str
    used_for_model_monitoring: bool
    description: None | str | Unset = UNSET
    grants: list[DominoDatasetrwApiDatasetRwGrant] | None | Unset = UNSET
    dataset_storage_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataset_name = self.dataset_name

        project_id = self.project_id

        used_for_model_monitoring = self.used_for_model_monitoring

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        grants: list[dict[str, Any]] | None | Unset
        if isinstance(self.grants, Unset):
            grants = UNSET
        elif isinstance(self.grants, list):
            grants = []
            for grants_type_0_item_data in self.grants:
                grants_type_0_item = grants_type_0_item_data.to_dict()
                grants.append(grants_type_0_item)

        else:
            grants = self.grants

        dataset_storage_id: None | str | Unset
        if isinstance(self.dataset_storage_id, Unset):
            dataset_storage_id = UNSET
        else:
            dataset_storage_id = self.dataset_storage_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "datasetName": dataset_name,
                "projectId": project_id,
                "usedForModelMonitoring": used_for_model_monitoring,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if grants is not UNSET:
            field_dict["grants"] = grants
        if dataset_storage_id is not UNSET:
            field_dict["datasetStorageId"] = dataset_storage_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_datasetrw_api_dataset_rw_grant import DominoDatasetrwApiDatasetRwGrant

        d = dict(src_dict)
        dataset_name = d.pop("datasetName")

        project_id = d.pop("projectId")

        used_for_model_monitoring = d.pop("usedForModelMonitoring")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_grants(data: object) -> list[DominoDatasetrwApiDatasetRwGrant] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                grants_type_0 = []
                _grants_type_0 = data
                for grants_type_0_item_data in _grants_type_0:
                    grants_type_0_item = DominoDatasetrwApiDatasetRwGrant.from_dict(grants_type_0_item_data)

                    grants_type_0.append(grants_type_0_item)

                return grants_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DominoDatasetrwApiDatasetRwGrant] | None | Unset, data)

        grants = _parse_grants(d.pop("grants", UNSET))

        def _parse_dataset_storage_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_storage_id = _parse_dataset_storage_id(d.pop("datasetStorageId", UNSET))

        domino_datasetrw_web_create_dataset_request = cls(
            dataset_name=dataset_name,
            project_id=project_id,
            used_for_model_monitoring=used_for_model_monitoring,
            description=description,
            grants=grants,
            dataset_storage_id=dataset_storage_id,
        )

        domino_datasetrw_web_create_dataset_request.additional_properties = d
        return domino_datasetrw_web_create_dataset_request

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
