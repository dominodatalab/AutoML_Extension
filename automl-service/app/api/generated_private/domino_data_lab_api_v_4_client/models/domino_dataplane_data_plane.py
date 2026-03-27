from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_dataplane_data_plane_configuration import DominoDataplaneDataPlaneConfiguration
    from ..models.domino_dataplane_data_plane_name import DominoDataplaneDataPlaneName
    from ..models.domino_dataplane_data_plane_status import DominoDataplaneDataPlaneStatus


T = TypeVar("T", bound="DominoDataplaneDataPlane")


@_attrs_define
class DominoDataplaneDataPlane:
    """
    Attributes:
        id (str):
        name (DominoDataplaneDataPlaneName):
        namespace (str):
        configuration (DominoDataplaneDataPlaneConfiguration):
        entity_id (str):
        status (DominoDataplaneDataPlaneStatus):
        is_archived (bool):
        is_locked (bool):
    """

    id: str
    name: DominoDataplaneDataPlaneName
    namespace: str
    configuration: DominoDataplaneDataPlaneConfiguration
    entity_id: str
    status: DominoDataplaneDataPlaneStatus
    is_archived: bool
    is_locked: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name.to_dict()

        namespace = self.namespace

        configuration = self.configuration.to_dict()

        entity_id = self.entity_id

        status = self.status.to_dict()

        is_archived = self.is_archived

        is_locked = self.is_locked

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "namespace": namespace,
                "configuration": configuration,
                "entityId": entity_id,
                "status": status,
                "isArchived": is_archived,
                "isLocked": is_locked,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_dataplane_data_plane_configuration import DominoDataplaneDataPlaneConfiguration
        from ..models.domino_dataplane_data_plane_name import DominoDataplaneDataPlaneName
        from ..models.domino_dataplane_data_plane_status import DominoDataplaneDataPlaneStatus

        d = dict(src_dict)
        id = d.pop("id")

        name = DominoDataplaneDataPlaneName.from_dict(d.pop("name"))

        namespace = d.pop("namespace")

        configuration = DominoDataplaneDataPlaneConfiguration.from_dict(d.pop("configuration"))

        entity_id = d.pop("entityId")

        status = DominoDataplaneDataPlaneStatus.from_dict(d.pop("status"))

        is_archived = d.pop("isArchived")

        is_locked = d.pop("isLocked")

        domino_dataplane_data_plane = cls(
            id=id,
            name=name,
            namespace=namespace,
            configuration=configuration,
            entity_id=entity_id,
            status=status,
            is_archived=is_archived,
            is_locked=is_locked,
        )

        domino_dataplane_data_plane.additional_properties = d
        return domino_dataplane_data_plane

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
