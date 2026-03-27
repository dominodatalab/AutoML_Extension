from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.domino_nucleus_modelproduct_models_model_product_model_product_type import (
    DominoNucleusModelproductModelsModelProductModelProductType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_common_user_person import DominoCommonUserPerson
    from ..models.domino_nucleus_modelproduct_models_app import DominoNucleusModelproductModelsApp
    from ..models.domino_nucleus_modelproduct_models_permissions_data import (
        DominoNucleusModelproductModelsPermissionsData,
    )
    from ..models.domino_nucleus_modelproduct_models_stats import DominoNucleusModelproductModelsStats


T = TypeVar("T", bound="DominoNucleusModelproductModelsModelProduct")


@_attrs_define
class DominoNucleusModelproductModelsModelProduct:
    """
    Attributes:
        model_product_type (DominoNucleusModelproductModelsModelProductModelProductType):
        project_id (str):
        name (str):
        created (datetime.datetime):
        last_updated (datetime.datetime):
        status (str):
        media (list[str]):
        tags (list[str]):
        stats (DominoNucleusModelproductModelsStats):
        id (str):
        permissions_data (DominoNucleusModelproductModelsPermissionsData): ModelProduct permissions
        description (None | str | Unset):
        entry_point (None | str | Unset):
        vanity_url (None | str | Unset):
        render_i_frame (bool | None | Unset):
        publisher (DominoCommonUserPerson | Unset):
        open_url (None | str | Unset):
        project_url (None | str | Unset):
        app_extension (DominoNucleusModelproductModelsApp | Unset):
        latest_app_instance_id (None | str | Unset):
        running_app_url (None | str | Unset):
        running_commit_id (None | str | Unset):
        environment_id (None | str | Unset):
        hardware_tier_id (None | str | Unset):
        mount_datasets (bool | None | Unset):
        mount_net_app_volumes (bool | None | Unset):
        run_describe_url (None | str | Unset):
        goal_ids (list[str] | None | Unset):
    """

    model_product_type: DominoNucleusModelproductModelsModelProductModelProductType
    project_id: str
    name: str
    created: datetime.datetime
    last_updated: datetime.datetime
    status: str
    media: list[str]
    tags: list[str]
    stats: DominoNucleusModelproductModelsStats
    id: str
    permissions_data: DominoNucleusModelproductModelsPermissionsData
    description: None | str | Unset = UNSET
    entry_point: None | str | Unset = UNSET
    vanity_url: None | str | Unset = UNSET
    render_i_frame: bool | None | Unset = UNSET
    publisher: DominoCommonUserPerson | Unset = UNSET
    open_url: None | str | Unset = UNSET
    project_url: None | str | Unset = UNSET
    app_extension: DominoNucleusModelproductModelsApp | Unset = UNSET
    latest_app_instance_id: None | str | Unset = UNSET
    running_app_url: None | str | Unset = UNSET
    running_commit_id: None | str | Unset = UNSET
    environment_id: None | str | Unset = UNSET
    hardware_tier_id: None | str | Unset = UNSET
    mount_datasets: bool | None | Unset = UNSET
    mount_net_app_volumes: bool | None | Unset = UNSET
    run_describe_url: None | str | Unset = UNSET
    goal_ids: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_product_type = self.model_product_type.value

        project_id = self.project_id

        name = self.name

        created = self.created.isoformat()

        last_updated = self.last_updated.isoformat()

        status = self.status

        media = self.media

        tags = self.tags

        stats = self.stats.to_dict()

        id = self.id

        permissions_data = self.permissions_data.to_dict()

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

        render_i_frame: bool | None | Unset
        if isinstance(self.render_i_frame, Unset):
            render_i_frame = UNSET
        else:
            render_i_frame = self.render_i_frame

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

        app_extension: dict[str, Any] | Unset = UNSET
        if not isinstance(self.app_extension, Unset):
            app_extension = self.app_extension.to_dict()

        latest_app_instance_id: None | str | Unset
        if isinstance(self.latest_app_instance_id, Unset):
            latest_app_instance_id = UNSET
        else:
            latest_app_instance_id = self.latest_app_instance_id

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

        environment_id: None | str | Unset
        if isinstance(self.environment_id, Unset):
            environment_id = UNSET
        else:
            environment_id = self.environment_id

        hardware_tier_id: None | str | Unset
        if isinstance(self.hardware_tier_id, Unset):
            hardware_tier_id = UNSET
        else:
            hardware_tier_id = self.hardware_tier_id

        mount_datasets: bool | None | Unset
        if isinstance(self.mount_datasets, Unset):
            mount_datasets = UNSET
        else:
            mount_datasets = self.mount_datasets

        mount_net_app_volumes: bool | None | Unset
        if isinstance(self.mount_net_app_volumes, Unset):
            mount_net_app_volumes = UNSET
        else:
            mount_net_app_volumes = self.mount_net_app_volumes

        run_describe_url: None | str | Unset
        if isinstance(self.run_describe_url, Unset):
            run_describe_url = UNSET
        else:
            run_describe_url = self.run_describe_url

        goal_ids: list[str] | None | Unset
        if isinstance(self.goal_ids, Unset):
            goal_ids = UNSET
        elif isinstance(self.goal_ids, list):
            goal_ids = self.goal_ids

        else:
            goal_ids = self.goal_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modelProductType": model_product_type,
                "projectId": project_id,
                "name": name,
                "created": created,
                "lastUpdated": last_updated,
                "status": status,
                "media": media,
                "tags": tags,
                "stats": stats,
                "id": id,
                "permissionsData": permissions_data,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if entry_point is not UNSET:
            field_dict["entryPoint"] = entry_point
        if vanity_url is not UNSET:
            field_dict["vanityUrl"] = vanity_url
        if render_i_frame is not UNSET:
            field_dict["renderIFrame"] = render_i_frame
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if open_url is not UNSET:
            field_dict["openUrl"] = open_url
        if project_url is not UNSET:
            field_dict["projectUrl"] = project_url
        if app_extension is not UNSET:
            field_dict["appExtension"] = app_extension
        if latest_app_instance_id is not UNSET:
            field_dict["latestAppInstanceId"] = latest_app_instance_id
        if running_app_url is not UNSET:
            field_dict["runningAppUrl"] = running_app_url
        if running_commit_id is not UNSET:
            field_dict["runningCommitId"] = running_commit_id
        if environment_id is not UNSET:
            field_dict["environmentId"] = environment_id
        if hardware_tier_id is not UNSET:
            field_dict["hardwareTierId"] = hardware_tier_id
        if mount_datasets is not UNSET:
            field_dict["mountDatasets"] = mount_datasets
        if mount_net_app_volumes is not UNSET:
            field_dict["mountNetAppVolumes"] = mount_net_app_volumes
        if run_describe_url is not UNSET:
            field_dict["runDescribeUrl"] = run_describe_url
        if goal_ids is not UNSET:
            field_dict["goalIds"] = goal_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_common_user_person import DominoCommonUserPerson
        from ..models.domino_nucleus_modelproduct_models_app import DominoNucleusModelproductModelsApp
        from ..models.domino_nucleus_modelproduct_models_permissions_data import (
            DominoNucleusModelproductModelsPermissionsData,
        )
        from ..models.domino_nucleus_modelproduct_models_stats import DominoNucleusModelproductModelsStats

        d = dict(src_dict)
        model_product_type = DominoNucleusModelproductModelsModelProductModelProductType(d.pop("modelProductType"))

        project_id = d.pop("projectId")

        name = d.pop("name")

        created = isoparse(d.pop("created"))

        last_updated = isoparse(d.pop("lastUpdated"))

        status = d.pop("status")

        media = cast(list[str], d.pop("media"))

        tags = cast(list[str], d.pop("tags"))

        stats = DominoNucleusModelproductModelsStats.from_dict(d.pop("stats"))

        id = d.pop("id")

        permissions_data = DominoNucleusModelproductModelsPermissionsData.from_dict(d.pop("permissionsData"))

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

        def _parse_render_i_frame(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        render_i_frame = _parse_render_i_frame(d.pop("renderIFrame", UNSET))

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

        _app_extension = d.pop("appExtension", UNSET)
        app_extension: DominoNucleusModelproductModelsApp | Unset
        if isinstance(_app_extension, Unset):
            app_extension = UNSET
        else:
            app_extension = DominoNucleusModelproductModelsApp.from_dict(_app_extension)

        def _parse_latest_app_instance_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latest_app_instance_id = _parse_latest_app_instance_id(d.pop("latestAppInstanceId", UNSET))

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

        def _parse_environment_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        environment_id = _parse_environment_id(d.pop("environmentId", UNSET))

        def _parse_hardware_tier_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hardware_tier_id = _parse_hardware_tier_id(d.pop("hardwareTierId", UNSET))

        def _parse_mount_datasets(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        mount_datasets = _parse_mount_datasets(d.pop("mountDatasets", UNSET))

        def _parse_mount_net_app_volumes(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        mount_net_app_volumes = _parse_mount_net_app_volumes(d.pop("mountNetAppVolumes", UNSET))

        def _parse_run_describe_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        run_describe_url = _parse_run_describe_url(d.pop("runDescribeUrl", UNSET))

        def _parse_goal_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                goal_ids_type_0 = cast(list[str], data)

                return goal_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        goal_ids = _parse_goal_ids(d.pop("goalIds", UNSET))

        domino_nucleus_modelproduct_models_model_product = cls(
            model_product_type=model_product_type,
            project_id=project_id,
            name=name,
            created=created,
            last_updated=last_updated,
            status=status,
            media=media,
            tags=tags,
            stats=stats,
            id=id,
            permissions_data=permissions_data,
            description=description,
            entry_point=entry_point,
            vanity_url=vanity_url,
            render_i_frame=render_i_frame,
            publisher=publisher,
            open_url=open_url,
            project_url=project_url,
            app_extension=app_extension,
            latest_app_instance_id=latest_app_instance_id,
            running_app_url=running_app_url,
            running_commit_id=running_commit_id,
            environment_id=environment_id,
            hardware_tier_id=hardware_tier_id,
            mount_datasets=mount_datasets,
            mount_net_app_volumes=mount_net_app_volumes,
            run_describe_url=run_describe_url,
            goal_ids=goal_ids,
        )

        domino_nucleus_modelproduct_models_model_product.additional_properties = d
        return domino_nucleus_modelproduct_models_model_product

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
