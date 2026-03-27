from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoCommonUserReasonForChangeDTO")


@_attrs_define
class DominoCommonUserReasonForChangeDTO:
    """
    Attributes:
        reason_for_change_id (str):
        user_id (str):
        action (str):
        reason (str):
        comment (None | str | Unset):
        project_id (None | str | Unset):
        entity_ids (list[str] | None | Unset):
    """

    reason_for_change_id: str
    user_id: str
    action: str
    reason: str
    comment: None | str | Unset = UNSET
    project_id: None | str | Unset = UNSET
    entity_ids: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reason_for_change_id = self.reason_for_change_id

        user_id = self.user_id

        action = self.action

        reason = self.reason

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        entity_ids: list[str] | None | Unset
        if isinstance(self.entity_ids, Unset):
            entity_ids = UNSET
        elif isinstance(self.entity_ids, list):
            entity_ids = self.entity_ids

        else:
            entity_ids = self.entity_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reasonForChangeId": reason_for_change_id,
                "userId": user_id,
                "action": action,
                "reason": reason,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if entity_ids is not UNSET:
            field_dict["entityIds"] = entity_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reason_for_change_id = d.pop("reasonForChangeId")

        user_id = d.pop("userId")

        action = d.pop("action")

        reason = d.pop("reason")

        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))

        def _parse_project_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_id = _parse_project_id(d.pop("projectId", UNSET))

        def _parse_entity_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                entity_ids_type_0 = cast(list[str], data)

                return entity_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        entity_ids = _parse_entity_ids(d.pop("entityIds", UNSET))

        domino_common_user_reason_for_change_dto = cls(
            reason_for_change_id=reason_for_change_id,
            user_id=user_id,
            action=action,
            reason=reason,
            comment=comment,
            project_id=project_id,
            entity_ids=entity_ids,
        )

        domino_common_user_reason_for_change_dto.additional_properties = d
        return domino_common_user_reason_for_change_dto

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
