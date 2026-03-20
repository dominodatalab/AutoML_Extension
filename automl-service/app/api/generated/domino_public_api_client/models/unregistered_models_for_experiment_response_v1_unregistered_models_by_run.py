from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.unregistered_model_v1 import UnregisteredModelV1


T = TypeVar("T", bound="UnregisteredModelsForExperimentResponseV1UnregisteredModelsByRun")


@_attrs_define
class UnregisteredModelsForExperimentResponseV1UnregisteredModelsByRun:
    """Map from run ID to unregistered models for that run

    Example:
        {'run-123': [{'id': 'my_model', 'name': 'my_model', 'source': 'artifact_path'}, {'id': 'another_model', 'name':
            'another_model', 'source': 'artifact_path'}, {'id': 'm-a12b305b76a54a578c3f710c3931411c', 'name': 'my-logged-
            model', 'source': 'logged_model'}]}

    """

    additional_properties: dict[str, list[UnregisteredModelV1]] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = []
            for additional_property_item_data in prop:
                additional_property_item = additional_property_item_data.to_dict()
                field_dict[prop_name].append(additional_property_item)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unregistered_model_v1 import UnregisteredModelV1

        d = dict(src_dict)
        unregistered_models_for_experiment_response_v1_unregistered_models_by_run = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = []
            _additional_property = prop_dict
            for additional_property_item_data in _additional_property:
                additional_property_item = UnregisteredModelV1.from_dict(additional_property_item_data)

                additional_property.append(additional_property_item)

            additional_properties[prop_name] = additional_property

        unregistered_models_for_experiment_response_v1_unregistered_models_by_run.additional_properties = (
            additional_properties
        )
        return unregistered_models_for_experiment_response_v1_unregistered_models_by_run

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> list[UnregisteredModelV1]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: list[UnregisteredModelV1]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
