from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.unregistered_model_v1_source import UnregisteredModelV1Source

T = TypeVar("T", bound="UnregisteredModelV1")


@_attrs_define
class UnregisteredModelV1:
    """
    Attributes:
        id (str): Artifact path (for MLflow 2) or logged model ID (for MLflow 3) Example: my_model.
        name (str): Artifact path name or logged model name Example: my_model.
        source (UnregisteredModelV1Source): Source of the unregistered model (artifact path from run or logged model)
            Example: artifact_path.
    """

    id: str
    name: str
    source: UnregisteredModelV1Source
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        source = self.source.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "source": source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        source = UnregisteredModelV1Source(d.pop("source"))

        unregistered_model_v1 = cls(
            id=id,
            name=name,
            source=source,
        )

        unregistered_model_v1.additional_properties = d
        return unregistered_model_v1

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
