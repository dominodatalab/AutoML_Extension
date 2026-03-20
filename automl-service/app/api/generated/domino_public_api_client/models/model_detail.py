from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_detail_source import ModelDetailSource


T = TypeVar("T", bound="ModelDetail")


@_attrs_define
class ModelDetail:
    """
    Attributes:
        environment_id (str): The id of the Domino environment.
        environment_name (str): The name of the Domino environment.
        name (str):  Example: XYZ Model.
        project_id (str): The id of the Domino project the source belongs to.
        source (ModelDetailSource): Model Deployment Model Detail Source
    """

    environment_id: str
    environment_name: str
    name: str
    project_id: str
    source: ModelDetailSource
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        environment_id = self.environment_id

        environment_name = self.environment_name

        name = self.name

        project_id = self.project_id

        source = self.source.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "environmentId": environment_id,
                "environmentName": environment_name,
                "name": name,
                "projectId": project_id,
                "source": source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_detail_source import ModelDetailSource

        d = dict(src_dict)
        environment_id = d.pop("environmentId")

        environment_name = d.pop("environmentName")

        name = d.pop("name")

        project_id = d.pop("projectId")

        source = ModelDetailSource.from_dict(d.pop("source"))

        model_detail = cls(
            environment_id=environment_id,
            environment_name=environment_name,
            name=name,
            project_id=project_id,
            source=source,
        )

        model_detail.additional_properties = d
        return model_detail

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
