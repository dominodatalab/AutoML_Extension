from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_common_models_environment_variable import DominoCommonModelsEnvironmentVariable


T = TypeVar("T", bound="DominoCommonModelsEnvironmentVariables")


@_attrs_define
class DominoCommonModelsEnvironmentVariables:
    """
    Attributes:
        vars_ (list[DominoCommonModelsEnvironmentVariable]):
    """

    vars_: list[DominoCommonModelsEnvironmentVariable]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vars_ = []
        for vars_item_data in self.vars_:
            vars_item = vars_item_data.to_dict()
            vars_.append(vars_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vars": vars_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_common_models_environment_variable import DominoCommonModelsEnvironmentVariable

        d = dict(src_dict)
        vars_ = []
        _vars_ = d.pop("vars")
        for vars_item_data in _vars_:
            vars_item = DominoCommonModelsEnvironmentVariable.from_dict(vars_item_data)

            vars_.append(vars_item)

        domino_common_models_environment_variables = cls(
            vars_=vars_,
        )

        domino_common_models_environment_variables.additional_properties = d
        return domino_common_models_environment_variables

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
