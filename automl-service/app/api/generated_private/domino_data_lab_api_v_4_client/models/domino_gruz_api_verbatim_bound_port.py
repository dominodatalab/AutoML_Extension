from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_gruz_api_ports_range import DominoGruzApiPortsRange


T = TypeVar("T", bound="DominoGruzApiVerbatimBoundPort")


@_attrs_define
class DominoGruzApiVerbatimBoundPort:
    """
    Attributes:
        environment_variable_name (str):
        assign_port_from_range (DominoGruzApiPortsRange | Unset):
        name (None | str | Unset):
        port (int | None | Unset):
    """

    environment_variable_name: str
    assign_port_from_range: DominoGruzApiPortsRange | Unset = UNSET
    name: None | str | Unset = UNSET
    port: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        environment_variable_name = self.environment_variable_name

        assign_port_from_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assign_port_from_range, Unset):
            assign_port_from_range = self.assign_port_from_range.to_dict()

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        port: int | None | Unset
        if isinstance(self.port, Unset):
            port = UNSET
        else:
            port = self.port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "environmentVariableName": environment_variable_name,
            }
        )
        if assign_port_from_range is not UNSET:
            field_dict["assignPortFromRange"] = assign_port_from_range
        if name is not UNSET:
            field_dict["name"] = name
        if port is not UNSET:
            field_dict["port"] = port

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_gruz_api_ports_range import DominoGruzApiPortsRange

        d = dict(src_dict)
        environment_variable_name = d.pop("environmentVariableName")

        _assign_port_from_range = d.pop("assignPortFromRange", UNSET)
        assign_port_from_range: DominoGruzApiPortsRange | Unset
        if isinstance(_assign_port_from_range, Unset):
            assign_port_from_range = UNSET
        else:
            assign_port_from_range = DominoGruzApiPortsRange.from_dict(_assign_port_from_range)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_port(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        port = _parse_port(d.pop("port", UNSET))

        domino_gruz_api_verbatim_bound_port = cls(
            environment_variable_name=environment_variable_name,
            assign_port_from_range=assign_port_from_range,
            name=name,
            port=port,
        )

        domino_gruz_api_verbatim_bound_port.additional_properties = d
        return domino_gruz_api_verbatim_bound_port

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
