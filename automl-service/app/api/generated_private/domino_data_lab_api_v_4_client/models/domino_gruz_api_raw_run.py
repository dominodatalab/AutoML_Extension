from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_gruz_api_run_meta import DominoGruzApiRunMeta
    from ..models.domino_gruz_api_run_output import DominoGruzApiRunOutput
    from ..models.domino_gruz_api_run_trigger import DominoGruzApiRunTrigger


T = TypeVar("T", bound="DominoGruzApiRawRun")


@_attrs_define
class DominoGruzApiRawRun:
    """
    Attributes:
        id (str):
        project_id (str):
        status (str):
        trigger (DominoGruzApiRunTrigger):
        meta (DominoGruzApiRunMeta):
        output (DominoGruzApiRunOutput):
    """

    id: str
    project_id: str
    status: str
    trigger: DominoGruzApiRunTrigger
    meta: DominoGruzApiRunMeta
    output: DominoGruzApiRunOutput
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        project_id = self.project_id

        status = self.status

        trigger = self.trigger.to_dict()

        meta = self.meta.to_dict()

        output = self.output.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "projectId": project_id,
                "status": status,
                "trigger": trigger,
                "meta": meta,
                "output": output,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_gruz_api_run_meta import DominoGruzApiRunMeta
        from ..models.domino_gruz_api_run_output import DominoGruzApiRunOutput
        from ..models.domino_gruz_api_run_trigger import DominoGruzApiRunTrigger

        d = dict(src_dict)
        id = d.pop("id")

        project_id = d.pop("projectId")

        status = d.pop("status")

        trigger = DominoGruzApiRunTrigger.from_dict(d.pop("trigger"))

        meta = DominoGruzApiRunMeta.from_dict(d.pop("meta"))

        output = DominoGruzApiRunOutput.from_dict(d.pop("output"))

        domino_gruz_api_raw_run = cls(
            id=id,
            project_id=project_id,
            status=status,
            trigger=trigger,
            meta=meta,
            output=output,
        )

        domino_gruz_api_raw_run.additional_properties = d
        return domino_gruz_api_raw_run

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
