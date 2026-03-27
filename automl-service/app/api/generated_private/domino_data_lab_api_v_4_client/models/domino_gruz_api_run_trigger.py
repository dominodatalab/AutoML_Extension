from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_gruz_api_raw_run_command import DominoGruzApiRawRunCommand
    from ..models.domino_gruz_api_run_memory_limit import DominoGruzApiRunMemoryLimit


T = TypeVar("T", bound="DominoGruzApiRunTrigger")


@_attrs_define
class DominoGruzApiRunTrigger:
    """
    Attributes:
        command (DominoGruzApiRawRunCommand):
        commit_id (str):
        starting_user_id (None | str | Unset):
        starting_scheduled_run_id (None | str | Unset):
        environment_id (None | str | Unset):
        environment_revision_id (None | str | Unset):
        run_memory_limit (DominoGruzApiRunMemoryLimit | Unset):
    """

    command: DominoGruzApiRawRunCommand
    commit_id: str
    starting_user_id: None | str | Unset = UNSET
    starting_scheduled_run_id: None | str | Unset = UNSET
    environment_id: None | str | Unset = UNSET
    environment_revision_id: None | str | Unset = UNSET
    run_memory_limit: DominoGruzApiRunMemoryLimit | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        command = self.command.to_dict()

        commit_id = self.commit_id

        starting_user_id: None | str | Unset
        if isinstance(self.starting_user_id, Unset):
            starting_user_id = UNSET
        else:
            starting_user_id = self.starting_user_id

        starting_scheduled_run_id: None | str | Unset
        if isinstance(self.starting_scheduled_run_id, Unset):
            starting_scheduled_run_id = UNSET
        else:
            starting_scheduled_run_id = self.starting_scheduled_run_id

        environment_id: None | str | Unset
        if isinstance(self.environment_id, Unset):
            environment_id = UNSET
        else:
            environment_id = self.environment_id

        environment_revision_id: None | str | Unset
        if isinstance(self.environment_revision_id, Unset):
            environment_revision_id = UNSET
        else:
            environment_revision_id = self.environment_revision_id

        run_memory_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.run_memory_limit, Unset):
            run_memory_limit = self.run_memory_limit.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "command": command,
                "commitId": commit_id,
            }
        )
        if starting_user_id is not UNSET:
            field_dict["startingUserId"] = starting_user_id
        if starting_scheduled_run_id is not UNSET:
            field_dict["startingScheduledRunId"] = starting_scheduled_run_id
        if environment_id is not UNSET:
            field_dict["environmentId"] = environment_id
        if environment_revision_id is not UNSET:
            field_dict["environmentRevisionId"] = environment_revision_id
        if run_memory_limit is not UNSET:
            field_dict["runMemoryLimit"] = run_memory_limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_gruz_api_raw_run_command import DominoGruzApiRawRunCommand
        from ..models.domino_gruz_api_run_memory_limit import DominoGruzApiRunMemoryLimit

        d = dict(src_dict)
        command = DominoGruzApiRawRunCommand.from_dict(d.pop("command"))

        commit_id = d.pop("commitId")

        def _parse_starting_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        starting_user_id = _parse_starting_user_id(d.pop("startingUserId", UNSET))

        def _parse_starting_scheduled_run_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        starting_scheduled_run_id = _parse_starting_scheduled_run_id(d.pop("startingScheduledRunId", UNSET))

        def _parse_environment_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        environment_id = _parse_environment_id(d.pop("environmentId", UNSET))

        def _parse_environment_revision_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        environment_revision_id = _parse_environment_revision_id(d.pop("environmentRevisionId", UNSET))

        _run_memory_limit = d.pop("runMemoryLimit", UNSET)
        run_memory_limit: DominoGruzApiRunMemoryLimit | Unset
        if isinstance(_run_memory_limit, Unset):
            run_memory_limit = UNSET
        else:
            run_memory_limit = DominoGruzApiRunMemoryLimit.from_dict(_run_memory_limit)

        domino_gruz_api_run_trigger = cls(
            command=command,
            commit_id=commit_id,
            starting_user_id=starting_user_id,
            starting_scheduled_run_id=starting_scheduled_run_id,
            environment_id=environment_id,
            environment_revision_id=environment_revision_id,
            run_memory_limit=run_memory_limit,
        )

        domino_gruz_api_run_trigger.additional_properties = d
        return domino_gruz_api_run_trigger

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
