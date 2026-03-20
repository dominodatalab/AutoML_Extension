from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.registered_model_version_data_source_details_v1 import RegisteredModelVersionDataSourceDetailsV1
    from ..models.registered_model_version_dataset_details_v1 import RegisteredModelVersionDatasetDetailsV1
    from ..models.registered_model_version_experiment_run_info_v1 import RegisteredModelVersionExperimentRunInfoV1


T = TypeVar("T", bound="RegisteredModelVersionUiDetailsV2")


@_attrs_define
class RegisteredModelVersionUiDetailsV2:
    """
    Attributes:
        model_version_data_sources (list[RegisteredModelVersionDataSourceDetailsV1]):
        model_version_datasets (list[RegisteredModelVersionDatasetDetailsV1]):
        experiment_run_info (RegisteredModelVersionExperimentRunInfoV1 | Unset):
    """

    model_version_data_sources: list[RegisteredModelVersionDataSourceDetailsV1]
    model_version_datasets: list[RegisteredModelVersionDatasetDetailsV1]
    experiment_run_info: RegisteredModelVersionExperimentRunInfoV1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_version_data_sources = []
        for model_version_data_sources_item_data in self.model_version_data_sources:
            model_version_data_sources_item = model_version_data_sources_item_data.to_dict()
            model_version_data_sources.append(model_version_data_sources_item)

        model_version_datasets = []
        for model_version_datasets_item_data in self.model_version_datasets:
            model_version_datasets_item = model_version_datasets_item_data.to_dict()
            model_version_datasets.append(model_version_datasets_item)

        experiment_run_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.experiment_run_info, Unset):
            experiment_run_info = self.experiment_run_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modelVersionDataSources": model_version_data_sources,
                "modelVersionDatasets": model_version_datasets,
            }
        )
        if experiment_run_info is not UNSET:
            field_dict["experimentRunInfo"] = experiment_run_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.registered_model_version_data_source_details_v1 import RegisteredModelVersionDataSourceDetailsV1
        from ..models.registered_model_version_dataset_details_v1 import RegisteredModelVersionDatasetDetailsV1
        from ..models.registered_model_version_experiment_run_info_v1 import RegisteredModelVersionExperimentRunInfoV1

        d = dict(src_dict)
        model_version_data_sources = []
        _model_version_data_sources = d.pop("modelVersionDataSources")
        for model_version_data_sources_item_data in _model_version_data_sources:
            model_version_data_sources_item = RegisteredModelVersionDataSourceDetailsV1.from_dict(
                model_version_data_sources_item_data
            )

            model_version_data_sources.append(model_version_data_sources_item)

        model_version_datasets = []
        _model_version_datasets = d.pop("modelVersionDatasets")
        for model_version_datasets_item_data in _model_version_datasets:
            model_version_datasets_item = RegisteredModelVersionDatasetDetailsV1.from_dict(
                model_version_datasets_item_data
            )

            model_version_datasets.append(model_version_datasets_item)

        _experiment_run_info = d.pop("experimentRunInfo", UNSET)
        experiment_run_info: RegisteredModelVersionExperimentRunInfoV1 | Unset
        if isinstance(_experiment_run_info, Unset):
            experiment_run_info = UNSET
        else:
            experiment_run_info = RegisteredModelVersionExperimentRunInfoV1.from_dict(_experiment_run_info)

        registered_model_version_ui_details_v2 = cls(
            model_version_data_sources=model_version_data_sources,
            model_version_datasets=model_version_datasets,
            experiment_run_info=experiment_run_info,
        )

        registered_model_version_ui_details_v2.additional_properties = d
        return registered_model_version_ui_details_v2

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
