from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoRegisteredModelsApiMlflowModelSourceV1")


@_attrs_define
class DominoRegisteredModelsApiMlflowModelSourceV1:
    """
    Attributes:
        experiment_run_id (str): Experiment run ID Example: a8ea375c781d4b9c8e58469f0ad738f8.
        artifact_path (str | Unset): Path to the model artifact within the experiment run Example: models/my_model.
        logged_model_id (str | Unset): Logged model entity ID Example: m-c7847529147945e78b8622f11f0d3c0f.
    """

    experiment_run_id: str
    artifact_path: str | Unset = UNSET
    logged_model_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        experiment_run_id = self.experiment_run_id

        artifact_path = self.artifact_path

        logged_model_id = self.logged_model_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "experimentRunId": experiment_run_id,
            }
        )
        if artifact_path is not UNSET:
            field_dict["artifactPath"] = artifact_path
        if logged_model_id is not UNSET:
            field_dict["loggedModelId"] = logged_model_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        experiment_run_id = d.pop("experimentRunId")

        artifact_path = d.pop("artifactPath", UNSET)

        logged_model_id = d.pop("loggedModelId", UNSET)

        domino_registered_models_api_mlflow_model_source_v1 = cls(
            experiment_run_id=experiment_run_id,
            artifact_path=artifact_path,
            logged_model_id=logged_model_id,
        )

        domino_registered_models_api_mlflow_model_source_v1.additional_properties = d
        return domino_registered_models_api_mlflow_model_source_v1

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
