from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_quota_api_quota_action_type import DominoQuotaApiQuotaActionType

T = TypeVar("T", bound="DominoQuotaWebRecordQuotaActionRequest")


@_attrs_define
class DominoQuotaWebRecordQuotaActionRequest:
    """
    Attributes:
        quota_id (str): quota Id
        user_id (str): Id of user for quota
        time_of_action (int): when the action was taken
        action_type (DominoQuotaApiQuotaActionType): type of quota action
    """

    quota_id: str
    user_id: str
    time_of_action: int
    action_type: DominoQuotaApiQuotaActionType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quota_id = self.quota_id

        user_id = self.user_id

        time_of_action = self.time_of_action

        action_type = self.action_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quotaId": quota_id,
                "userId": user_id,
                "timeOfAction": time_of_action,
                "actionType": action_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        quota_id = d.pop("quotaId")

        user_id = d.pop("userId")

        time_of_action = d.pop("timeOfAction")

        action_type = DominoQuotaApiQuotaActionType(d.pop("actionType"))

        domino_quota_web_record_quota_action_request = cls(
            quota_id=quota_id,
            user_id=user_id,
            time_of_action=time_of_action,
            action_type=action_type,
        )

        domino_quota_web_record_quota_action_request.additional_properties = d
        return domino_quota_web_record_quota_action_request

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
