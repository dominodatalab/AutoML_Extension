from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoProjectManagementApiPmOAuth1AConfiguration")


@_attrs_define
class DominoProjectManagementApiPmOAuth1AConfiguration:
    """
    Attributes:
        application_url (str):
        application_name (str):
        application_type (str):
        create_incoming_link (bool):
        in_coming_consumer_key (str):
        in_coming_consumer_name (str):
        public_key (None | str | Unset):
    """

    application_url: str
    application_name: str
    application_type: str
    create_incoming_link: bool
    in_coming_consumer_key: str
    in_coming_consumer_name: str
    public_key: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application_url = self.application_url

        application_name = self.application_name

        application_type = self.application_type

        create_incoming_link = self.create_incoming_link

        in_coming_consumer_key = self.in_coming_consumer_key

        in_coming_consumer_name = self.in_coming_consumer_name

        public_key: None | str | Unset
        if isinstance(self.public_key, Unset):
            public_key = UNSET
        else:
            public_key = self.public_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "applicationUrl": application_url,
                "applicationName": application_name,
                "applicationType": application_type,
                "createIncomingLink": create_incoming_link,
                "inComingConsumerKey": in_coming_consumer_key,
                "inComingConsumerName": in_coming_consumer_name,
            }
        )
        if public_key is not UNSET:
            field_dict["publicKey"] = public_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        application_url = d.pop("applicationUrl")

        application_name = d.pop("applicationName")

        application_type = d.pop("applicationType")

        create_incoming_link = d.pop("createIncomingLink")

        in_coming_consumer_key = d.pop("inComingConsumerKey")

        in_coming_consumer_name = d.pop("inComingConsumerName")

        def _parse_public_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_key = _parse_public_key(d.pop("publicKey", UNSET))

        domino_project_management_api_pm_o_auth_1a_configuration = cls(
            application_url=application_url,
            application_name=application_name,
            application_type=application_type,
            create_incoming_link=create_incoming_link,
            in_coming_consumer_key=in_coming_consumer_key,
            in_coming_consumer_name=in_coming_consumer_name,
            public_key=public_key,
        )

        domino_project_management_api_pm_o_auth_1a_configuration.additional_properties = d
        return domino_project_management_api_pm_o_auth_1a_configuration

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
