from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_dataplane_data_plane_status_dto_state import DominoDataplaneDataPlaneStatusDtoState
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoDataplaneDataPlaneStatusDto")


@_attrs_define
class DominoDataplaneDataPlaneStatusDto:
    """
    Attributes:
        state (DominoDataplaneDataPlaneStatusDtoState):
        message (str):
        agent_version (str):
        catalog_version (str):
        requires_upgrade (bool):
        supports_upgrade (bool):
        kubernetes_version (None | str | Unset):
        last_heartbeat_timestamp (int | None | Unset):
    """

    state: DominoDataplaneDataPlaneStatusDtoState
    message: str
    agent_version: str
    catalog_version: str
    requires_upgrade: bool
    supports_upgrade: bool
    kubernetes_version: None | str | Unset = UNSET
    last_heartbeat_timestamp: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state.value

        message = self.message

        agent_version = self.agent_version

        catalog_version = self.catalog_version

        requires_upgrade = self.requires_upgrade

        supports_upgrade = self.supports_upgrade

        kubernetes_version: None | str | Unset
        if isinstance(self.kubernetes_version, Unset):
            kubernetes_version = UNSET
        else:
            kubernetes_version = self.kubernetes_version

        last_heartbeat_timestamp: int | None | Unset
        if isinstance(self.last_heartbeat_timestamp, Unset):
            last_heartbeat_timestamp = UNSET
        else:
            last_heartbeat_timestamp = self.last_heartbeat_timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
                "message": message,
                "agentVersion": agent_version,
                "catalogVersion": catalog_version,
                "requiresUpgrade": requires_upgrade,
                "supportsUpgrade": supports_upgrade,
            }
        )
        if kubernetes_version is not UNSET:
            field_dict["kubernetesVersion"] = kubernetes_version
        if last_heartbeat_timestamp is not UNSET:
            field_dict["lastHeartbeatTimestamp"] = last_heartbeat_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        state = DominoDataplaneDataPlaneStatusDtoState(d.pop("state"))

        message = d.pop("message")

        agent_version = d.pop("agentVersion")

        catalog_version = d.pop("catalogVersion")

        requires_upgrade = d.pop("requiresUpgrade")

        supports_upgrade = d.pop("supportsUpgrade")

        def _parse_kubernetes_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kubernetes_version = _parse_kubernetes_version(d.pop("kubernetesVersion", UNSET))

        def _parse_last_heartbeat_timestamp(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_heartbeat_timestamp = _parse_last_heartbeat_timestamp(d.pop("lastHeartbeatTimestamp", UNSET))

        domino_dataplane_data_plane_status_dto = cls(
            state=state,
            message=message,
            agent_version=agent_version,
            catalog_version=catalog_version,
            requires_upgrade=requires_upgrade,
            supports_upgrade=supports_upgrade,
            kubernetes_version=kubernetes_version,
            last_heartbeat_timestamp=last_heartbeat_timestamp,
        )

        domino_dataplane_data_plane_status_dto.additional_properties = d
        return domino_dataplane_data_plane_status_dto

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
