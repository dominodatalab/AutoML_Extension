from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AthenaBillingConfigsV1")


@_attrs_define
class AthenaBillingConfigsV1:
    """
    Attributes:
        athena_bucket_name (str):
        athena_database (str):
        athena_region (str):
        athena_table (str):
        project_id (str):
        service_key_name (str):
        service_key_secret (str):
    """

    athena_bucket_name: str
    athena_database: str
    athena_region: str
    athena_table: str
    project_id: str
    service_key_name: str
    service_key_secret: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        athena_bucket_name = self.athena_bucket_name

        athena_database = self.athena_database

        athena_region = self.athena_region

        athena_table = self.athena_table

        project_id = self.project_id

        service_key_name = self.service_key_name

        service_key_secret = self.service_key_secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "athenaBucketName": athena_bucket_name,
                "athenaDatabase": athena_database,
                "athenaRegion": athena_region,
                "athenaTable": athena_table,
                "projectID": project_id,
                "serviceKeyName": service_key_name,
                "serviceKeySecret": service_key_secret,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        athena_bucket_name = d.pop("athenaBucketName")

        athena_database = d.pop("athenaDatabase")

        athena_region = d.pop("athenaRegion")

        athena_table = d.pop("athenaTable")

        project_id = d.pop("projectID")

        service_key_name = d.pop("serviceKeyName")

        service_key_secret = d.pop("serviceKeySecret")

        athena_billing_configs_v1 = cls(
            athena_bucket_name=athena_bucket_name,
            athena_database=athena_database,
            athena_region=athena_region,
            athena_table=athena_table,
            project_id=project_id,
            service_key_name=service_key_name,
            service_key_secret=service_key_secret,
        )

        athena_billing_configs_v1.additional_properties = d
        return athena_billing_configs_v1

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
