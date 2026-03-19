from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelEndpointEnvironmentUpdateV1")


@_attrs_define
class ModelEndpointEnvironmentUpdateV1:
    """
    Attributes:
        environment_id (str): The environment ID of the endpoint Example: 62313ce67a0af0281c01a6a5.
        revision_id (str | Unset): The ID of the environment revision used to run the endpoint Example:
            62313ce67a0af0281c01a6a5.
    """

    environment_id: str
    revision_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        environment_id = self.environment_id

        revision_id = self.revision_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "environmentId": environment_id,
            }
        )
        if revision_id is not UNSET:
            field_dict["revisionId"] = revision_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        environment_id = d.pop("environmentId")

        revision_id = d.pop("revisionId", UNSET)

        model_endpoint_environment_update_v1 = cls(
            environment_id=environment_id,
            revision_id=revision_id,
        )

        model_endpoint_environment_update_v1.additional_properties = d
        return model_endpoint_environment_update_v1

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
