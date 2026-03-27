from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_dataplane_data_plane_configuration import DominoDataplaneDataPlaneConfiguration


T = TypeVar("T", bound="DominoDataplaneDataPlaneFormDto")


@_attrs_define
class DominoDataplaneDataPlaneFormDto:
    """
    Attributes:
        name (str):
        namespace (str):
        configuration (DominoDataplaneDataPlaneConfiguration):
    """

    name: str
    namespace: str
    configuration: DominoDataplaneDataPlaneConfiguration
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        namespace = self.namespace

        configuration = self.configuration.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "namespace": namespace,
                "configuration": configuration,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_dataplane_data_plane_configuration import DominoDataplaneDataPlaneConfiguration

        d = dict(src_dict)
        name = d.pop("name")

        namespace = d.pop("namespace")

        configuration = DominoDataplaneDataPlaneConfiguration.from_dict(d.pop("configuration"))

        domino_dataplane_data_plane_form_dto = cls(
            name=name,
            namespace=namespace,
            configuration=configuration,
        )

        domino_dataplane_data_plane_form_dto.additional_properties = d
        return domino_dataplane_data_plane_form_dto

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
