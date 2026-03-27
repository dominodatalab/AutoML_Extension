from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_activity_api_project_status import DominoActivityApiProjectStatus


T = TypeVar("T", bound="DominoActivityApiProjectStatusChangeActivityMetaData")


@_attrs_define
class DominoActivityApiProjectStatusChangeActivityMetaData:
    """
    Attributes:
        project_name (str):
        from_status (DominoActivityApiProjectStatus):
        to_status (DominoActivityApiProjectStatus):
    """

    project_name: str
    from_status: DominoActivityApiProjectStatus
    to_status: DominoActivityApiProjectStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_name = self.project_name

        from_status = self.from_status.to_dict()

        to_status = self.to_status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectName": project_name,
                "fromStatus": from_status,
                "toStatus": to_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_activity_api_project_status import DominoActivityApiProjectStatus

        d = dict(src_dict)
        project_name = d.pop("projectName")

        from_status = DominoActivityApiProjectStatus.from_dict(d.pop("fromStatus"))

        to_status = DominoActivityApiProjectStatus.from_dict(d.pop("toStatus"))

        domino_activity_api_project_status_change_activity_meta_data = cls(
            project_name=project_name,
            from_status=from_status,
            to_status=to_status,
        )

        domino_activity_api_project_status_change_activity_meta_data.additional_properties = d
        return domino_activity_api_project_status_change_activity_meta_data

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
