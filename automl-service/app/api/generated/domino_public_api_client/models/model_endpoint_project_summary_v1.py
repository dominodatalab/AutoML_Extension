from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_endpoint_user_v1 import ModelEndpointUserV1


T = TypeVar("T", bound="ModelEndpointProjectSummaryV1")


@_attrs_define
class ModelEndpointProjectSummaryV1:
    """
    Attributes:
        id (str): Unique identifier for the project Example: 62313ce67a0af0281c01a6a5.
        name (str): Name of the project Example: My Project.
        owner (ModelEndpointUserV1):
    """

    id: str
    name: str
    owner: ModelEndpointUserV1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        owner = self.owner.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "owner": owner,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_endpoint_user_v1 import ModelEndpointUserV1

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        owner = ModelEndpointUserV1.from_dict(d.pop("owner"))

        model_endpoint_project_summary_v1 = cls(
            id=id,
            name=name,
            owner=owner,
        )

        model_endpoint_project_summary_v1.additional_properties = d
        return model_endpoint_project_summary_v1

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
