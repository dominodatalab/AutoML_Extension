from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.unregistered_models_for_experiment_response_v1_unregistered_models_by_run import (
        UnregisteredModelsForExperimentResponseV1UnregisteredModelsByRun,
    )


T = TypeVar("T", bound="UnregisteredModelsForExperimentResponseV1")


@_attrs_define
class UnregisteredModelsForExperimentResponseV1:
    """
    Attributes:
        unregistered_models_by_run (UnregisteredModelsForExperimentResponseV1UnregisteredModelsByRun): Map from run ID
            to unregistered models for that run Example: {'run-123': [{'id': 'my_model', 'name': 'my_model', 'source':
            'artifact_path'}, {'id': 'another_model', 'name': 'another_model', 'source': 'artifact_path'}, {'id':
            'm-a12b305b76a54a578c3f710c3931411c', 'name': 'my-logged-model', 'source': 'logged_model'}]}.
    """

    unregistered_models_by_run: UnregisteredModelsForExperimentResponseV1UnregisteredModelsByRun
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unregistered_models_by_run = self.unregistered_models_by_run.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unregisteredModelsByRun": unregistered_models_by_run,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unregistered_models_for_experiment_response_v1_unregistered_models_by_run import (
            UnregisteredModelsForExperimentResponseV1UnregisteredModelsByRun,
        )

        d = dict(src_dict)
        unregistered_models_by_run = UnregisteredModelsForExperimentResponseV1UnregisteredModelsByRun.from_dict(
            d.pop("unregisteredModelsByRun")
        )

        unregistered_models_for_experiment_response_v1 = cls(
            unregistered_models_by_run=unregistered_models_by_run,
        )

        unregistered_models_for_experiment_response_v1.additional_properties = d
        return unregistered_models_for_experiment_response_v1

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
