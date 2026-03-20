from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.registered_model_tags_v1 import RegisteredModelTagsV1


T = TypeVar("T", bound="NewRegisteredModelV1")


@_attrs_define
class NewRegisteredModelV1:
    """
    Attributes:
        discoverable (bool): Indicates whether this model is publicly discoverable. If true, users who are not project
            members will see this model in search results and can view basic model details.
        experiment_run_id (str): The id of the experiment run to create the version from Example:
            a8ea375c781d4b9c8e58469f0ad738f8.
        model_name (str): The name of the registered model Example: housing_price_predictor.
        description (str | Unset): The description of the registered model Example: This model predicts housing prices.
        tags (RegisteredModelTagsV1 | Unset): A map of key -> value Example: {'key': 'value', 'key2': 'anothervalue'}.
    """

    discoverable: bool
    experiment_run_id: str
    model_name: str
    description: str | Unset = UNSET
    tags: RegisteredModelTagsV1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        discoverable = self.discoverable

        experiment_run_id = self.experiment_run_id

        model_name = self.model_name

        description = self.description

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "discoverable": discoverable,
                "experimentRunId": experiment_run_id,
                "modelName": model_name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.registered_model_tags_v1 import RegisteredModelTagsV1

        d = dict(src_dict)
        discoverable = d.pop("discoverable")

        experiment_run_id = d.pop("experimentRunId")

        model_name = d.pop("modelName")

        description = d.pop("description", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: RegisteredModelTagsV1 | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = RegisteredModelTagsV1.from_dict(_tags)

        new_registered_model_v1 = cls(
            discoverable=discoverable,
            experiment_run_id=experiment_run_id,
            model_name=model_name,
            description=description,
            tags=tags,
        )

        new_registered_model_v1.additional_properties = d
        return new_registered_model_v1

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
