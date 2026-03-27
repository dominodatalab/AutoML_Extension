from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_dataplane_data_plane_status_state import DominoDataplaneDataPlaneStatusState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_dataplane_data_plane_status_component_versions_type_0 import (
        DominoDataplaneDataPlaneStatusComponentVersionsType0,
    )


T = TypeVar("T", bound="DominoDataplaneDataPlaneStatus")


@_attrs_define
class DominoDataplaneDataPlaneStatus:
    """
    Attributes:
        state (DominoDataplaneDataPlaneStatusState):
        message (str):
        agent_version (str):
        catalog_version (str):
        requires_upgrade (bool):
        supports_upgrade (bool):
        component_versions (DominoDataplaneDataPlaneStatusComponentVersionsType0 | None | Unset):
        last_heartbeat_timestamp (int | None | Unset):
    """

    state: DominoDataplaneDataPlaneStatusState
    message: str
    agent_version: str
    catalog_version: str
    requires_upgrade: bool
    supports_upgrade: bool
    component_versions: DominoDataplaneDataPlaneStatusComponentVersionsType0 | None | Unset = UNSET
    last_heartbeat_timestamp: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.domino_dataplane_data_plane_status_component_versions_type_0 import (
            DominoDataplaneDataPlaneStatusComponentVersionsType0,
        )

        state = self.state.value

        message = self.message

        agent_version = self.agent_version

        catalog_version = self.catalog_version

        requires_upgrade = self.requires_upgrade

        supports_upgrade = self.supports_upgrade

        component_versions: dict[str, Any] | None | Unset
        if isinstance(self.component_versions, Unset):
            component_versions = UNSET
        elif isinstance(self.component_versions, DominoDataplaneDataPlaneStatusComponentVersionsType0):
            component_versions = self.component_versions.to_dict()
        else:
            component_versions = self.component_versions

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
        if component_versions is not UNSET:
            field_dict["componentVersions"] = component_versions
        if last_heartbeat_timestamp is not UNSET:
            field_dict["lastHeartbeatTimestamp"] = last_heartbeat_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_dataplane_data_plane_status_component_versions_type_0 import (
            DominoDataplaneDataPlaneStatusComponentVersionsType0,
        )

        d = dict(src_dict)
        state = DominoDataplaneDataPlaneStatusState(d.pop("state"))

        message = d.pop("message")

        agent_version = d.pop("agentVersion")

        catalog_version = d.pop("catalogVersion")

        requires_upgrade = d.pop("requiresUpgrade")

        supports_upgrade = d.pop("supportsUpgrade")

        def _parse_component_versions(
            data: object,
        ) -> DominoDataplaneDataPlaneStatusComponentVersionsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                component_versions_type_0 = DominoDataplaneDataPlaneStatusComponentVersionsType0.from_dict(data)

                return component_versions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DominoDataplaneDataPlaneStatusComponentVersionsType0 | None | Unset, data)

        component_versions = _parse_component_versions(d.pop("componentVersions", UNSET))

        def _parse_last_heartbeat_timestamp(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_heartbeat_timestamp = _parse_last_heartbeat_timestamp(d.pop("lastHeartbeatTimestamp", UNSET))

        domino_dataplane_data_plane_status = cls(
            state=state,
            message=message,
            agent_version=agent_version,
            catalog_version=catalog_version,
            requires_upgrade=requires_upgrade,
            supports_upgrade=supports_upgrade,
            component_versions=component_versions,
            last_heartbeat_timestamp=last_heartbeat_timestamp,
        )

        domino_dataplane_data_plane_status.additional_properties = d
        return domino_dataplane_data_plane_status

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
