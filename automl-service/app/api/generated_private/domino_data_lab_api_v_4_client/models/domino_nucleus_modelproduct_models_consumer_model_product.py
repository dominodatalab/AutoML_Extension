from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.domino_nucleus_modelproduct_models_consumer_model_product_app_access_status import (
    DominoNucleusModelproductModelsConsumerModelProductAppAccessStatus,
)
from ..models.domino_nucleus_modelproduct_models_consumer_model_product_model_product_type import (
    DominoNucleusModelproductModelsConsumerModelProductModelProductType,
)
from ..models.domino_nucleus_modelproduct_models_consumer_model_product_visibility import (
    DominoNucleusModelproductModelsConsumerModelProductVisibility,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_common_modelproduct_notification_recipient import DominoCommonModelproductNotificationRecipient
    from ..models.domino_common_user_person import DominoCommonUserPerson
    from ..models.domino_nucleus_modelproduct_models_stats import DominoNucleusModelproductModelsStats


T = TypeVar("T", bound="DominoNucleusModelproductModelsConsumerModelProduct")


@_attrs_define
class DominoNucleusModelproductModelsConsumerModelProduct:
    """
    Attributes:
        model_product_type (DominoNucleusModelproductModelsConsumerModelProductModelProductType):
        name (str):
        render_i_frame (bool):
        notification_recipients (list[DominoCommonModelproductNotificationRecipient]):
        last_updated (datetime.datetime):
        status (str):
        media (list[str]):
        project_id (str):
        stats (DominoNucleusModelproductModelsStats):
        id (str):
        visibility (DominoNucleusModelproductModelsConsumerModelProductVisibility):
        app_access_status (DominoNucleusModelproductModelsConsumerModelProductAppAccessStatus):
        description (None | str | Unset):
        entry_point (None | str | Unset):
        vanity_url (None | str | Unset):
        publisher (DominoCommonUserPerson | Unset):
        open_url (None | str | Unset):
        project_url (None | str | Unset):
        running_app_url (None | str | Unset):
        running_commit_id (None | str | Unset):
    """

    model_product_type: DominoNucleusModelproductModelsConsumerModelProductModelProductType
    name: str
    render_i_frame: bool
    notification_recipients: list[DominoCommonModelproductNotificationRecipient]
    last_updated: datetime.datetime
    status: str
    media: list[str]
    project_id: str
    stats: DominoNucleusModelproductModelsStats
    id: str
    visibility: DominoNucleusModelproductModelsConsumerModelProductVisibility
    app_access_status: DominoNucleusModelproductModelsConsumerModelProductAppAccessStatus
    description: None | str | Unset = UNSET
    entry_point: None | str | Unset = UNSET
    vanity_url: None | str | Unset = UNSET
    publisher: DominoCommonUserPerson | Unset = UNSET
    open_url: None | str | Unset = UNSET
    project_url: None | str | Unset = UNSET
    running_app_url: None | str | Unset = UNSET
    running_commit_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_product_type = self.model_product_type.value

        name = self.name

        render_i_frame = self.render_i_frame

        notification_recipients = []
        for notification_recipients_item_data in self.notification_recipients:
            notification_recipients_item = notification_recipients_item_data.to_dict()
            notification_recipients.append(notification_recipients_item)

        last_updated = self.last_updated.isoformat()

        status = self.status

        media = self.media

        project_id = self.project_id

        stats = self.stats.to_dict()

        id = self.id

        visibility = self.visibility.value

        app_access_status = self.app_access_status.value

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        entry_point: None | str | Unset
        if isinstance(self.entry_point, Unset):
            entry_point = UNSET
        else:
            entry_point = self.entry_point

        vanity_url: None | str | Unset
        if isinstance(self.vanity_url, Unset):
            vanity_url = UNSET
        else:
            vanity_url = self.vanity_url

        publisher: dict[str, Any] | Unset = UNSET
        if not isinstance(self.publisher, Unset):
            publisher = self.publisher.to_dict()

        open_url: None | str | Unset
        if isinstance(self.open_url, Unset):
            open_url = UNSET
        else:
            open_url = self.open_url

        project_url: None | str | Unset
        if isinstance(self.project_url, Unset):
            project_url = UNSET
        else:
            project_url = self.project_url

        running_app_url: None | str | Unset
        if isinstance(self.running_app_url, Unset):
            running_app_url = UNSET
        else:
            running_app_url = self.running_app_url

        running_commit_id: None | str | Unset
        if isinstance(self.running_commit_id, Unset):
            running_commit_id = UNSET
        else:
            running_commit_id = self.running_commit_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modelProductType": model_product_type,
                "name": name,
                "renderIFrame": render_i_frame,
                "notificationRecipients": notification_recipients,
                "lastUpdated": last_updated,
                "status": status,
                "media": media,
                "projectId": project_id,
                "stats": stats,
                "id": id,
                "visibility": visibility,
                "appAccessStatus": app_access_status,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if entry_point is not UNSET:
            field_dict["entryPoint"] = entry_point
        if vanity_url is not UNSET:
            field_dict["vanityUrl"] = vanity_url
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if open_url is not UNSET:
            field_dict["openUrl"] = open_url
        if project_url is not UNSET:
            field_dict["projectUrl"] = project_url
        if running_app_url is not UNSET:
            field_dict["runningAppUrl"] = running_app_url
        if running_commit_id is not UNSET:
            field_dict["runningCommitId"] = running_commit_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_common_modelproduct_notification_recipient import (
            DominoCommonModelproductNotificationRecipient,
        )
        from ..models.domino_common_user_person import DominoCommonUserPerson
        from ..models.domino_nucleus_modelproduct_models_stats import DominoNucleusModelproductModelsStats

        d = dict(src_dict)
        model_product_type = DominoNucleusModelproductModelsConsumerModelProductModelProductType(
            d.pop("modelProductType")
        )

        name = d.pop("name")

        render_i_frame = d.pop("renderIFrame")

        notification_recipients = []
        _notification_recipients = d.pop("notificationRecipients")
        for notification_recipients_item_data in _notification_recipients:
            notification_recipients_item = DominoCommonModelproductNotificationRecipient.from_dict(
                notification_recipients_item_data
            )

            notification_recipients.append(notification_recipients_item)

        last_updated = isoparse(d.pop("lastUpdated"))

        status = d.pop("status")

        media = cast(list[str], d.pop("media"))

        project_id = d.pop("projectId")

        stats = DominoNucleusModelproductModelsStats.from_dict(d.pop("stats"))

        id = d.pop("id")

        visibility = DominoNucleusModelproductModelsConsumerModelProductVisibility(d.pop("visibility"))

        app_access_status = DominoNucleusModelproductModelsConsumerModelProductAppAccessStatus(d.pop("appAccessStatus"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_entry_point(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        entry_point = _parse_entry_point(d.pop("entryPoint", UNSET))

        def _parse_vanity_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vanity_url = _parse_vanity_url(d.pop("vanityUrl", UNSET))

        _publisher = d.pop("publisher", UNSET)
        publisher: DominoCommonUserPerson | Unset
        if isinstance(_publisher, Unset):
            publisher = UNSET
        else:
            publisher = DominoCommonUserPerson.from_dict(_publisher)

        def _parse_open_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        open_url = _parse_open_url(d.pop("openUrl", UNSET))

        def _parse_project_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_url = _parse_project_url(d.pop("projectUrl", UNSET))

        def _parse_running_app_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        running_app_url = _parse_running_app_url(d.pop("runningAppUrl", UNSET))

        def _parse_running_commit_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        running_commit_id = _parse_running_commit_id(d.pop("runningCommitId", UNSET))

        domino_nucleus_modelproduct_models_consumer_model_product = cls(
            model_product_type=model_product_type,
            name=name,
            render_i_frame=render_i_frame,
            notification_recipients=notification_recipients,
            last_updated=last_updated,
            status=status,
            media=media,
            project_id=project_id,
            stats=stats,
            id=id,
            visibility=visibility,
            app_access_status=app_access_status,
            description=description,
            entry_point=entry_point,
            vanity_url=vanity_url,
            publisher=publisher,
            open_url=open_url,
            project_url=project_url,
            running_app_url=running_app_url,
            running_commit_id=running_commit_id,
        )

        domino_nucleus_modelproduct_models_consumer_model_product.additional_properties = d
        return domino_nucleus_modelproduct_models_consumer_model_product

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
