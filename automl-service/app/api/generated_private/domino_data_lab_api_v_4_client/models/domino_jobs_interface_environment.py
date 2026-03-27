from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_jobs_interface_environment_environment_revision_spec_type_0 import (
    DominoJobsInterfaceEnvironmentEnvironmentRevisionSpecType0,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_jobs_interface_environment_environment_revision_spec_type_1 import (
        DominoJobsInterfaceEnvironmentEnvironmentRevisionSpecType1,
    )


T = TypeVar("T", bound="DominoJobsInterfaceEnvironment")


@_attrs_define
class DominoJobsInterfaceEnvironment:
    """
    Attributes:
        environment_id (str):
        environment_name (str):
        environment_revision_spec (DominoJobsInterfaceEnvironmentEnvironmentRevisionSpecType0 |
            DominoJobsInterfaceEnvironmentEnvironmentRevisionSpecType1):
        environment_revision_id (None | str | Unset):
        revision_number (int | None | Unset):
    """

    environment_id: str
    environment_name: str
    environment_revision_spec: (
        DominoJobsInterfaceEnvironmentEnvironmentRevisionSpecType0
        | DominoJobsInterfaceEnvironmentEnvironmentRevisionSpecType1
    )
    environment_revision_id: None | str | Unset = UNSET
    revision_number: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        environment_id = self.environment_id

        environment_name = self.environment_name

        environment_revision_spec: dict[str, Any] | str
        if isinstance(self.environment_revision_spec, DominoJobsInterfaceEnvironmentEnvironmentRevisionSpecType0):
            environment_revision_spec = self.environment_revision_spec.value
        else:
            environment_revision_spec = self.environment_revision_spec.to_dict()

        environment_revision_id: None | str | Unset
        if isinstance(self.environment_revision_id, Unset):
            environment_revision_id = UNSET
        else:
            environment_revision_id = self.environment_revision_id

        revision_number: int | None | Unset
        if isinstance(self.revision_number, Unset):
            revision_number = UNSET
        else:
            revision_number = self.revision_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "environmentId": environment_id,
                "environmentName": environment_name,
                "environmentRevisionSpec": environment_revision_spec,
            }
        )
        if environment_revision_id is not UNSET:
            field_dict["environmentRevisionId"] = environment_revision_id
        if revision_number is not UNSET:
            field_dict["revisionNumber"] = revision_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_jobs_interface_environment_environment_revision_spec_type_1 import (
            DominoJobsInterfaceEnvironmentEnvironmentRevisionSpecType1,
        )

        d = dict(src_dict)
        environment_id = d.pop("environmentId")

        environment_name = d.pop("environmentName")

        def _parse_environment_revision_spec(
            data: object,
        ) -> (
            DominoJobsInterfaceEnvironmentEnvironmentRevisionSpecType0
            | DominoJobsInterfaceEnvironmentEnvironmentRevisionSpecType1
        ):
            try:
                if not isinstance(data, str):
                    raise TypeError()
                environment_revision_spec_type_0 = DominoJobsInterfaceEnvironmentEnvironmentRevisionSpecType0(data)

                return environment_revision_spec_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            environment_revision_spec_type_1 = DominoJobsInterfaceEnvironmentEnvironmentRevisionSpecType1.from_dict(
                data
            )

            return environment_revision_spec_type_1

        environment_revision_spec = _parse_environment_revision_spec(d.pop("environmentRevisionSpec"))

        def _parse_environment_revision_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        environment_revision_id = _parse_environment_revision_id(d.pop("environmentRevisionId", UNSET))

        def _parse_revision_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        revision_number = _parse_revision_number(d.pop("revisionNumber", UNSET))

        domino_jobs_interface_environment = cls(
            environment_id=environment_id,
            environment_name=environment_name,
            environment_revision_spec=environment_revision_spec,
            environment_revision_id=environment_revision_id,
            revision_number=revision_number,
        )

        domino_jobs_interface_environment.additional_properties = d
        return domino_jobs_interface_environment

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
