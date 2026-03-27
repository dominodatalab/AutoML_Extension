from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_datasource_model_auth_type import DominoDatasourceModelAuthType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_datasource_model_auth_config_fields import DominoDatasourceModelAuthConfigFields
    from ..models.domino_datasource_model_auth_config_meta import DominoDatasourceModelAuthConfigMeta


T = TypeVar("T", bound="DominoDatasourceModelAuthConfig")


@_attrs_define
class DominoDatasourceModelAuthConfig:
    """
    Attributes:
        fields (DominoDatasourceModelAuthConfigFields):
        meta (DominoDatasourceModelAuthConfigMeta):
        auth_type (DominoDatasourceModelAuthType | Unset):
    """

    fields: DominoDatasourceModelAuthConfigFields
    meta: DominoDatasourceModelAuthConfigMeta
    auth_type: DominoDatasourceModelAuthType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fields = self.fields.to_dict()

        meta = self.meta.to_dict()

        auth_type: str | Unset = UNSET
        if not isinstance(self.auth_type, Unset):
            auth_type = self.auth_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fields": fields,
                "meta": meta,
            }
        )
        if auth_type is not UNSET:
            field_dict["authType"] = auth_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_datasource_model_auth_config_fields import DominoDatasourceModelAuthConfigFields
        from ..models.domino_datasource_model_auth_config_meta import DominoDatasourceModelAuthConfigMeta

        d = dict(src_dict)
        fields = DominoDatasourceModelAuthConfigFields.from_dict(d.pop("fields"))

        meta = DominoDatasourceModelAuthConfigMeta.from_dict(d.pop("meta"))

        _auth_type = d.pop("authType", UNSET)
        auth_type: DominoDatasourceModelAuthType | Unset
        if isinstance(_auth_type, Unset):
            auth_type = UNSET
        else:
            auth_type = DominoDatasourceModelAuthType(_auth_type)

        domino_datasource_model_auth_config = cls(
            fields=fields,
            meta=meta,
            auth_type=auth_type,
        )

        domino_datasource_model_auth_config.additional_properties = d
        return domino_datasource_model_auth_config

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
