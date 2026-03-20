from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_endpoint_v1 import ModelEndpointV1
    from ..models.model_endpoint_version_v1 import ModelEndpointVersionV1


T = TypeVar("T", bound="ModelEndpointVersionPatchResultV1")


@_attrs_define
class ModelEndpointVersionPatchResultV1:
    """The result of patch an endpoint version

    Attributes:
        endpoint (ModelEndpointV1):
        version (ModelEndpointVersionV1):
    """

    endpoint: ModelEndpointV1
    version: ModelEndpointVersionV1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        endpoint = self.endpoint.to_dict()

        version = self.version.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endpoint": endpoint,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_endpoint_v1 import ModelEndpointV1
        from ..models.model_endpoint_version_v1 import ModelEndpointVersionV1

        d = dict(src_dict)
        endpoint = ModelEndpointV1.from_dict(d.pop("endpoint"))

        version = ModelEndpointVersionV1.from_dict(d.pop("version"))

        model_endpoint_version_patch_result_v1 = cls(
            endpoint=endpoint,
            version=version,
        )

        model_endpoint_version_patch_result_v1.additional_properties = d
        return model_endpoint_version_patch_result_v1

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
