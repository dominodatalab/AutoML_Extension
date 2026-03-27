from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoModelmanagerApiSnowflakeExport")


@_attrs_define
class DominoModelmanagerApiSnowflakeExport:
    """
    Attributes:
        snowflake_udf_name (str):
        snowflake_url (str):
        snowflake_username (str):
        snowflake_password (str):
        snowflake_user_role (str):
        snowflake_warehouse_name (str):
        snowflake_database_name (str):
        snowflake_schema_name (str):
        snowflake_stage_name (str):
    """

    snowflake_udf_name: str
    snowflake_url: str
    snowflake_username: str
    snowflake_password: str
    snowflake_user_role: str
    snowflake_warehouse_name: str
    snowflake_database_name: str
    snowflake_schema_name: str
    snowflake_stage_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        snowflake_udf_name = self.snowflake_udf_name

        snowflake_url = self.snowflake_url

        snowflake_username = self.snowflake_username

        snowflake_password = self.snowflake_password

        snowflake_user_role = self.snowflake_user_role

        snowflake_warehouse_name = self.snowflake_warehouse_name

        snowflake_database_name = self.snowflake_database_name

        snowflake_schema_name = self.snowflake_schema_name

        snowflake_stage_name = self.snowflake_stage_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "snowflakeUdfName": snowflake_udf_name,
                "snowflakeUrl": snowflake_url,
                "snowflakeUsername": snowflake_username,
                "snowflakePassword": snowflake_password,
                "snowflakeUserRole": snowflake_user_role,
                "snowflakeWarehouseName": snowflake_warehouse_name,
                "snowflakeDatabaseName": snowflake_database_name,
                "snowflakeSchemaName": snowflake_schema_name,
                "snowflakeStageName": snowflake_stage_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        snowflake_udf_name = d.pop("snowflakeUdfName")

        snowflake_url = d.pop("snowflakeUrl")

        snowflake_username = d.pop("snowflakeUsername")

        snowflake_password = d.pop("snowflakePassword")

        snowflake_user_role = d.pop("snowflakeUserRole")

        snowflake_warehouse_name = d.pop("snowflakeWarehouseName")

        snowflake_database_name = d.pop("snowflakeDatabaseName")

        snowflake_schema_name = d.pop("snowflakeSchemaName")

        snowflake_stage_name = d.pop("snowflakeStageName")

        domino_modelmanager_api_snowflake_export = cls(
            snowflake_udf_name=snowflake_udf_name,
            snowflake_url=snowflake_url,
            snowflake_username=snowflake_username,
            snowflake_password=snowflake_password,
            snowflake_user_role=snowflake_user_role,
            snowflake_warehouse_name=snowflake_warehouse_name,
            snowflake_database_name=snowflake_database_name,
            snowflake_schema_name=snowflake_schema_name,
            snowflake_stage_name=snowflake_stage_name,
        )

        domino_modelmanager_api_snowflake_export.additional_properties = d
        return domino_modelmanager_api_snowflake_export

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
