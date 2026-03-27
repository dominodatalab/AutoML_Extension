from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_datasetrw_api_task_update import DominoDatasetrwApiTaskUpdate


T = TypeVar("T", bound="DominoDatasetrwWebFiletaskUpdateRequest")


@_attrs_define
class DominoDatasetrwWebFiletaskUpdateRequest:
    """
    Attributes:
        id (str):
        update (DominoDatasetrwApiTaskUpdate):
        key (str):
        task_type (str):
        status (str):
        error_msg (str):
    """

    id: str
    update: DominoDatasetrwApiTaskUpdate
    key: str
    task_type: str
    status: str
    error_msg: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        update = self.update.to_dict()

        key = self.key

        task_type = self.task_type

        status = self.status

        error_msg = self.error_msg

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "update": update,
                "key": key,
                "taskType": task_type,
                "status": status,
                "errorMsg": error_msg,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_datasetrw_api_task_update import DominoDatasetrwApiTaskUpdate

        d = dict(src_dict)
        id = d.pop("id")

        update = DominoDatasetrwApiTaskUpdate.from_dict(d.pop("update"))

        key = d.pop("key")

        task_type = d.pop("taskType")

        status = d.pop("status")

        error_msg = d.pop("errorMsg")

        domino_datasetrw_web_filetask_update_request = cls(
            id=id,
            update=update,
            key=key,
            task_type=task_type,
            status=status,
            error_msg=error_msg,
        )

        domino_datasetrw_web_filetask_update_request.additional_properties = d
        return domino_datasetrw_web_filetask_update_request

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
