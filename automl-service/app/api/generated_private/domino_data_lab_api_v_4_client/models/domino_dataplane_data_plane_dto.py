from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_dataplane_data_plane_configuration import DominoDataplaneDataPlaneConfiguration
    from ..models.domino_dataplane_data_plane_status_dto import DominoDataplaneDataPlaneStatusDto


T = TypeVar("T", bound="DominoDataplaneDataPlaneDto")


@_attrs_define
class DominoDataplaneDataPlaneDto:
    """
    Attributes:
        id (str):
        name (str):
        namespace (str):
        is_local (bool):
        configuration (DominoDataplaneDataPlaneConfiguration):
        status (DominoDataplaneDataPlaneStatusDto):
        is_healthy (bool):
        is_archived (bool):
        is_file_sync_disabled (bool):
        is_locked (bool):
    """

    id: str
    name: str
    namespace: str
    is_local: bool
    configuration: DominoDataplaneDataPlaneConfiguration
    status: DominoDataplaneDataPlaneStatusDto
    is_healthy: bool
    is_archived: bool
    is_file_sync_disabled: bool
    is_locked: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        namespace = self.namespace

        is_local = self.is_local

        configuration = self.configuration.to_dict()

        status = self.status.to_dict()

        is_healthy = self.is_healthy

        is_archived = self.is_archived

        is_file_sync_disabled = self.is_file_sync_disabled

        is_locked = self.is_locked

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "namespace": namespace,
                "isLocal": is_local,
                "configuration": configuration,
                "status": status,
                "isHealthy": is_healthy,
                "isArchived": is_archived,
                "isFileSyncDisabled": is_file_sync_disabled,
                "isLocked": is_locked,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_dataplane_data_plane_configuration import DominoDataplaneDataPlaneConfiguration
        from ..models.domino_dataplane_data_plane_status_dto import DominoDataplaneDataPlaneStatusDto

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        namespace = d.pop("namespace")

        is_local = d.pop("isLocal")

        configuration = DominoDataplaneDataPlaneConfiguration.from_dict(d.pop("configuration"))

        status = DominoDataplaneDataPlaneStatusDto.from_dict(d.pop("status"))

        is_healthy = d.pop("isHealthy")

        is_archived = d.pop("isArchived")

        is_file_sync_disabled = d.pop("isFileSyncDisabled")

        is_locked = d.pop("isLocked")

        domino_dataplane_data_plane_dto = cls(
            id=id,
            name=name,
            namespace=namespace,
            is_local=is_local,
            configuration=configuration,
            status=status,
            is_healthy=is_healthy,
            is_archived=is_archived,
            is_file_sync_disabled=is_file_sync_disabled,
            is_locked=is_locked,
        )

        domino_dataplane_data_plane_dto.additional_properties = d
        return domino_dataplane_data_plane_dto

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
