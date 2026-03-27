from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_datasource_model_auth_type import DominoDatasourceModelAuthType
from ..models.domino_datasource_model_connector_group import DominoDatasourceModelConnectorGroup
from ..models.domino_datasource_model_connector_type import DominoDatasourceModelConnectorType
from ..models.domino_datasource_model_datasource_type import DominoDatasourceModelDatasourceType
from ..models.domino_datasource_model_engine_type import DominoDatasourceModelEngineType
from ..models.domino_datasource_model_storage_type import DominoDatasourceModelStorageType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_datasource_model_datasource_config_fields import DominoDatasourceModelDatasourceConfigFields


T = TypeVar("T", bound="DominoDatasourceModelDatasourceConfig")


@_attrs_define
class DominoDatasourceModelDatasourceConfig:
    """
    Attributes:
        auth_types (list[DominoDatasourceModelAuthType]):
        fields (DominoDatasourceModelDatasourceConfigFields):
        datasource_type (DominoDatasourceModelDatasourceType):
        engine_type (DominoDatasourceModelEngineType | Unset):
        connector_group (DominoDatasourceModelConnectorGroup | Unset):
        connector_type (DominoDatasourceModelConnectorType | Unset):
        storage_type (DominoDatasourceModelStorageType | Unset):
    """

    auth_types: list[DominoDatasourceModelAuthType]
    fields: DominoDatasourceModelDatasourceConfigFields
    datasource_type: DominoDatasourceModelDatasourceType
    engine_type: DominoDatasourceModelEngineType | Unset = UNSET
    connector_group: DominoDatasourceModelConnectorGroup | Unset = UNSET
    connector_type: DominoDatasourceModelConnectorType | Unset = UNSET
    storage_type: DominoDatasourceModelStorageType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_types = []
        for auth_types_item_data in self.auth_types:
            auth_types_item = auth_types_item_data.value
            auth_types.append(auth_types_item)

        fields = self.fields.to_dict()

        datasource_type = self.datasource_type.value

        engine_type: str | Unset = UNSET
        if not isinstance(self.engine_type, Unset):
            engine_type = self.engine_type.value

        connector_group: str | Unset = UNSET
        if not isinstance(self.connector_group, Unset):
            connector_group = self.connector_group.value

        connector_type: str | Unset = UNSET
        if not isinstance(self.connector_type, Unset):
            connector_type = self.connector_type.value

        storage_type: str | Unset = UNSET
        if not isinstance(self.storage_type, Unset):
            storage_type = self.storage_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authTypes": auth_types,
                "fields": fields,
                "datasourceType": datasource_type,
            }
        )
        if engine_type is not UNSET:
            field_dict["engineType"] = engine_type
        if connector_group is not UNSET:
            field_dict["connectorGroup"] = connector_group
        if connector_type is not UNSET:
            field_dict["connectorType"] = connector_type
        if storage_type is not UNSET:
            field_dict["storageType"] = storage_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_datasource_model_datasource_config_fields import (
            DominoDatasourceModelDatasourceConfigFields,
        )

        d = dict(src_dict)
        auth_types = []
        _auth_types = d.pop("authTypes")
        for auth_types_item_data in _auth_types:
            auth_types_item = DominoDatasourceModelAuthType(auth_types_item_data)

            auth_types.append(auth_types_item)

        fields = DominoDatasourceModelDatasourceConfigFields.from_dict(d.pop("fields"))

        datasource_type = DominoDatasourceModelDatasourceType(d.pop("datasourceType"))

        _engine_type = d.pop("engineType", UNSET)
        engine_type: DominoDatasourceModelEngineType | Unset
        if isinstance(_engine_type, Unset):
            engine_type = UNSET
        else:
            engine_type = DominoDatasourceModelEngineType(_engine_type)

        _connector_group = d.pop("connectorGroup", UNSET)
        connector_group: DominoDatasourceModelConnectorGroup | Unset
        if isinstance(_connector_group, Unset):
            connector_group = UNSET
        else:
            connector_group = DominoDatasourceModelConnectorGroup(_connector_group)

        _connector_type = d.pop("connectorType", UNSET)
        connector_type: DominoDatasourceModelConnectorType | Unset
        if isinstance(_connector_type, Unset):
            connector_type = UNSET
        else:
            connector_type = DominoDatasourceModelConnectorType(_connector_type)

        _storage_type = d.pop("storageType", UNSET)
        storage_type: DominoDatasourceModelStorageType | Unset
        if isinstance(_storage_type, Unset):
            storage_type = UNSET
        else:
            storage_type = DominoDatasourceModelStorageType(_storage_type)

        domino_datasource_model_datasource_config = cls(
            auth_types=auth_types,
            fields=fields,
            datasource_type=datasource_type,
            engine_type=engine_type,
            connector_group=connector_group,
            connector_type=connector_type,
            storage_type=storage_type,
        )

        domino_datasource_model_datasource_config.additional_properties = d
        return domino_datasource_model_datasource_config

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
