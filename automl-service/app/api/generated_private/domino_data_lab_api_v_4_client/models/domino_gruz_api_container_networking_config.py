from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_gruz_api_custom_hostname_mapping import DominoGruzApiCustomHostnameMapping
    from ..models.domino_gruz_api_executor_hostname_mapping import DominoGruzApiExecutorHostnameMapping
    from ..models.domino_gruz_api_ports_range import DominoGruzApiPortsRange
    from ..models.domino_gruz_api_verbatim_bound_port import DominoGruzApiVerbatimBoundPort


T = TypeVar("T", bound="DominoGruzApiContainerNetworkingConfig")


@_attrs_define
class DominoGruzApiContainerNetworkingConfig:
    """
    Attributes:
        auto_bound_ports (list[int]):
        verbatim_bound_ports (list[DominoGruzApiVerbatimBoundPort]):
        custom_hostname_mappings (list[DominoGruzApiCustomHostnameMapping]):
        http_proxy_port (int | None | Unset):
        allowed_verbatim_ports_range (DominoGruzApiPortsRange | Unset):
        executor_hostname_mapping (DominoGruzApiExecutorHostnameMapping | Unset):
    """

    auto_bound_ports: list[int]
    verbatim_bound_ports: list[DominoGruzApiVerbatimBoundPort]
    custom_hostname_mappings: list[DominoGruzApiCustomHostnameMapping]
    http_proxy_port: int | None | Unset = UNSET
    allowed_verbatim_ports_range: DominoGruzApiPortsRange | Unset = UNSET
    executor_hostname_mapping: DominoGruzApiExecutorHostnameMapping | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_bound_ports = self.auto_bound_ports

        verbatim_bound_ports = []
        for verbatim_bound_ports_item_data in self.verbatim_bound_ports:
            verbatim_bound_ports_item = verbatim_bound_ports_item_data.to_dict()
            verbatim_bound_ports.append(verbatim_bound_ports_item)

        custom_hostname_mappings = []
        for custom_hostname_mappings_item_data in self.custom_hostname_mappings:
            custom_hostname_mappings_item = custom_hostname_mappings_item_data.to_dict()
            custom_hostname_mappings.append(custom_hostname_mappings_item)

        http_proxy_port: int | None | Unset
        if isinstance(self.http_proxy_port, Unset):
            http_proxy_port = UNSET
        else:
            http_proxy_port = self.http_proxy_port

        allowed_verbatim_ports_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.allowed_verbatim_ports_range, Unset):
            allowed_verbatim_ports_range = self.allowed_verbatim_ports_range.to_dict()

        executor_hostname_mapping: dict[str, Any] | Unset = UNSET
        if not isinstance(self.executor_hostname_mapping, Unset):
            executor_hostname_mapping = self.executor_hostname_mapping.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "autoBoundPorts": auto_bound_ports,
                "verbatimBoundPorts": verbatim_bound_ports,
                "customHostnameMappings": custom_hostname_mappings,
            }
        )
        if http_proxy_port is not UNSET:
            field_dict["httpProxyPort"] = http_proxy_port
        if allowed_verbatim_ports_range is not UNSET:
            field_dict["allowedVerbatimPortsRange"] = allowed_verbatim_ports_range
        if executor_hostname_mapping is not UNSET:
            field_dict["executorHostnameMapping"] = executor_hostname_mapping

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_gruz_api_custom_hostname_mapping import DominoGruzApiCustomHostnameMapping
        from ..models.domino_gruz_api_executor_hostname_mapping import DominoGruzApiExecutorHostnameMapping
        from ..models.domino_gruz_api_ports_range import DominoGruzApiPortsRange
        from ..models.domino_gruz_api_verbatim_bound_port import DominoGruzApiVerbatimBoundPort

        d = dict(src_dict)
        auto_bound_ports = cast(list[int], d.pop("autoBoundPorts"))

        verbatim_bound_ports = []
        _verbatim_bound_ports = d.pop("verbatimBoundPorts")
        for verbatim_bound_ports_item_data in _verbatim_bound_ports:
            verbatim_bound_ports_item = DominoGruzApiVerbatimBoundPort.from_dict(verbatim_bound_ports_item_data)

            verbatim_bound_ports.append(verbatim_bound_ports_item)

        custom_hostname_mappings = []
        _custom_hostname_mappings = d.pop("customHostnameMappings")
        for custom_hostname_mappings_item_data in _custom_hostname_mappings:
            custom_hostname_mappings_item = DominoGruzApiCustomHostnameMapping.from_dict(
                custom_hostname_mappings_item_data
            )

            custom_hostname_mappings.append(custom_hostname_mappings_item)

        def _parse_http_proxy_port(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        http_proxy_port = _parse_http_proxy_port(d.pop("httpProxyPort", UNSET))

        _allowed_verbatim_ports_range = d.pop("allowedVerbatimPortsRange", UNSET)
        allowed_verbatim_ports_range: DominoGruzApiPortsRange | Unset
        if isinstance(_allowed_verbatim_ports_range, Unset):
            allowed_verbatim_ports_range = UNSET
        else:
            allowed_verbatim_ports_range = DominoGruzApiPortsRange.from_dict(_allowed_verbatim_ports_range)

        _executor_hostname_mapping = d.pop("executorHostnameMapping", UNSET)
        executor_hostname_mapping: DominoGruzApiExecutorHostnameMapping | Unset
        if isinstance(_executor_hostname_mapping, Unset):
            executor_hostname_mapping = UNSET
        else:
            executor_hostname_mapping = DominoGruzApiExecutorHostnameMapping.from_dict(_executor_hostname_mapping)

        domino_gruz_api_container_networking_config = cls(
            auto_bound_ports=auto_bound_ports,
            verbatim_bound_ports=verbatim_bound_ports,
            custom_hostname_mappings=custom_hostname_mappings,
            http_proxy_port=http_proxy_port,
            allowed_verbatim_ports_range=allowed_verbatim_ports_range,
            executor_hostname_mapping=executor_hostname_mapping,
        )

        domino_gruz_api_container_networking_config.additional_properties = d
        return domino_gruz_api_container_networking_config

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
