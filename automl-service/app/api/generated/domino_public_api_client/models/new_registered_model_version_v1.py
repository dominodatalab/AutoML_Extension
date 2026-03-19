from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NewRegisteredModelVersionV1")


@_attrs_define
class NewRegisteredModelVersionV1:
    """
    Attributes:
        artifact (str): The artifact of the run to create the version from Example: LogisticRegression.
        description (str): The description of the registered model version Example: Logistic regression model version 2.
        experiment_run_id (str): The id of the experiment run to create the version from Example:
            a8ea375c781d4b9c8e58469f0ad738f8.
    """

    artifact: str
    description: str
    experiment_run_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        artifact = self.artifact

        description = self.description

        experiment_run_id = self.experiment_run_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "artifact": artifact,
                "description": description,
                "experimentRunId": experiment_run_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        artifact = d.pop("artifact")

        description = d.pop("description")

        experiment_run_id = d.pop("experimentRunId")

        new_registered_model_version_v1 = cls(
            artifact=artifact,
            description=description,
            experiment_run_id=experiment_run_id,
        )

        new_registered_model_version_v1.additional_properties = d
        return new_registered_model_version_v1

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
